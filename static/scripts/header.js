document.addEventListener('DOMContentLoaded', function () {
    // Dark Mode Toggle
    const toggle = document.getElementById("themeToggle");
    if (toggle) {
        toggle.addEventListener('click', function () {
            document.body.classList.toggle('dark');
            toggle.innerHTML = document.body.classList.contains('dark')
                ? '<i class="fa-solid fa-sun fa-lg" style="color: #ffffff;"></i>'
                : '<i class="fa-solid fa-moon fa-lg" style="color: #ffffff;"></i>';
        });
    }

    // Burger Menu
    const burger = document.getElementById('burger');
    const menu = document.getElementById('menu');
    if (burger && menu) {
        burger.addEventListener('click', function () {
            menu.classList.toggle("active");
        });
    }

    // Header scroll effect
    const header = document.querySelector('header');
    if (header) {
        window.addEventListener('scroll', function () {
            if (window.scrollY > 1) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        });
    }
});
