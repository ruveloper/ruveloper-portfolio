/**
 * Init Functions
 */
(function () {
    "use strict";

    /* ---- Typing animation ---- */
    const typed = document.querySelector('.typed')
    if (typed) {
        let typed_strings = typed.getAttribute('data-typed-items')
        typed_strings = typed_strings.split(',')
        new Typed('.typed', {
            strings: typed_strings,
            loop: true,
            typeSpeed: 50,
            backSpeed: 20,
            backDelay: 2000
        });
    }


    /* -------- Navbar State Colors -------- */
    /* Navbar change color on scroll */
    const navbarEl = document.getElementById('navbar')
    window.addEventListener('scroll', () => {
        if (window.scrollY > 140) {
            navbarEl.classList.remove('bg-gray-300')
            navbarEl.classList.add('bg-gray-800')
            return null;
        }
        navbarEl.classList.add('bg-gray-300')
        navbarEl.classList.remove('bg-gray-800')
    })
    /* Mobile Navbar change color on expand menu */
    const navbarTargetEl = document.getElementById('navbar-menu')
    const navbarTriggerEl = document.getElementById('navbar-mobile-menu')
    // Callback functions
    const options = {
        triggerEl: navbarTriggerEl,
        onExpand: () => {
            navbarEl.classList.remove('bg-gray-300')
            navbarEl.classList.add('bg-gray-800')
        },
        onCollapse: () => {
            navbarEl.classList.add('bg-gray-300')
            navbarEl.classList.remove('bg-gray-800')
        }
    };
    const collapse = new Collapse(navbarTargetEl, options);


})();

/**
 * Helper Functions
 */
function scrollToIdWithDelay(id, delay) {
    setTimeout(
        function () {
            document.getElementById(id).scrollIntoView({
                behavior: "smooth",
                block: "center"
            });
        }, delay);
}