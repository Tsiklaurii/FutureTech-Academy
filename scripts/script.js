function loadContent(id, file) {
    fetch(file)
        .then((res) => res.text())
        .then((html) => {
            document.getElementById(id).innerHTML = html;

            // Dark Mode Logic
            if (id === "header") {
                const toggle = document.getElementById("themeToggle");
                toggle.addEventListener('click', function () {
                    document.body.classList.toggle('dark');
                    toggle.innerHTML = document.body.classList.contains('dark')
                        ? '<i class="fa-solid fa-sun fa-lg" style="color: #ffffff;"></i>'
                        : '<i class="fa-solid fa-moon fa-lg" style="color: #ffffff;"></i>';
                })
            }

            // Burger Menu
            if (id === "header") {
                const burger = document.getElementById('burger');
                const menu = document.getElementById('menu');

                burger.addEventListener('click', function () {
                    menu.classList.toggle("active");
                })
            }
        })
}
loadContent('header', 'header.html');
loadContent('footer', 'footer.html');

window.addEventListener('scroll', function () {
    const header = document.querySelector('header');
    if (window.scrollY > 1) {
        header.classList.add('scrolled');
    } else {
        header.classList.remove('scrolled');
    }
});
