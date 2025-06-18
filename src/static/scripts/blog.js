fetch('https://683c01c428a0b0f2fdc5eb8b.mockapi.io/blogs')
    .then((res) => res.json())
    .then((data) => {
        const blogsContainer = document.getElementById("blogs-container");

        data.forEach(blog => {
            const card = document.createElement("div");
            card.className = "blog-card";
            card.innerHTML = `
                <div class="blogs-image-container">
                    <img alt='${blog.title}' src='${blog.img}'/>
                </div>
                <p>${blog.title}</p>`
            blogsContainer.appendChild(card);

            // ბლოგის id-ის შენახვა დეტალების სანახავად
            card.addEventListener("click", () => {
                localStorage.setItem("selectedBlogId", blog.id);
                window.location.href = "/blogdetails";
            })
        });
    })
    .catch(err => console.error("შეცდომა:", err));
