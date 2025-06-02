const jobsContainer = document.getElementById("jobs-container");
const paginationContainer = document.getElementById("pagination");
const jobPerPage = 6;
let allJobs = [];
let currentPage = 1;

// სერვერიდან მონაცემების მიღება
async function fetchJobs() {
    try {
        const response = await fetch('https://683c01c428a0b0f2fdc5eb8b.mockapi.io/Open-positions');
        const data = await response.json();
        allJobs = data;
        renderJobs(currentPage);
        renderPagination();
    } catch (error) {
        console.log(error);
    }
}

// მიღებული მონაცემების დამუშავება (ეკრანზე გამოტანა)
function renderJobs(page) {
    jobsContainer.innerHTML = "";
    const startIndex = (page - 1) * jobPerPage;
    const endIndex = startIndex + jobPerPage;
    const currentJobs = allJobs.slice(startIndex, endIndex);  //slice - აბრუნებს ამოჭრილ ელემენტებს
    currentJobs.forEach(job => {
        const card = document.createElement("div");
        card.classList.add("col-md-4", "mb-4");
        card.innerHTML = `
        <div class="card h-100">
            <div class="card-body">
                <h5 class="card-title">${job.name}</h5>
                <p class="card-text">🏠 ${job.type}</p>
                <p class="card-text">📍 ${job.location}</p>
                <a href="#" class="btn btn-primary">View Job</a>
            </div>
        </div>`
        jobsContainer.appendChild(card);
    })
}

// Pagination
function renderPagination() {
    paginationContainer.innerHTML = '';
    const totalPage = Math.ceil(allJobs.length / jobPerPage); // ceil - დამრგვალება

    for (let i = 1; i <= totalPage; i++) {
        const listItem = document.createElement("li");
        listItem.classList.add("page-item");

        if (i === currentPage) {
            listItem.classList.add("active");
        }

        const link = document.createElement("a");
        link.classList.add("page-link");
        link.href = "#";
        link.textContent = i;
        link.addEventListener("click", () => {
            currentPage = i;
            renderJobs(currentPage);
            const activeItem = paginationContainer.querySelector(".page-item.active");
            if (activeItem) {
                activeItem.classList.remove("active");
            }
            listItem.classList.add("active");
        })
        listItem.appendChild(link);
        paginationContainer.appendChild(listItem);
    }
}

fetchJobs();