// blog-ის დეტალების ჩვენება
document.addEventListener("DOMContentLoaded", () => {
    const blogId = localStorage.getItem("selectedBlogId");
    if (!blogId) return;

    fetch("https://683c01c428a0b0f2fdc5eb8b.mockapi.io/blogs")
        .then((res) => res.json())
        .then((data) => {
            const blog = data.find(item => item.id == blogId);
            if (!blog) return;

            const blogDetailsContainer = document.getElementById("blog_details_container");
            blogDetailsContainer.innerHTML = `
            <div class="details">
                <img src="${blog.img}" alt="${blog.title}">
                <div class="blog-info">
                    <h1>${blog.title}</h1>
                    <p>${blog.description}</p>
                </div>
            </div>`
        })
        .catch(err => console.error("დეტალების შეცდომა:", err));
})