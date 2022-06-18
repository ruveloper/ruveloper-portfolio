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

// * reCaptcha Callback Function
function onSubmitFormContact(token) {
    document.getElementById("contact-form").submit();
}

/**
 * Init Scripts Function
 */
function InitScripts() {
    "use strict";

    /* * ---- Typing animation ---- */
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


    /* * -------- Navbar Config -------- */
    const navbarEl = document.getElementById('navbar')
    const navbarTriggerEl = document.getElementById('navbar-mobile-menu')
    const navbarTargetEl = document.getElementById('navbar-menu')
    /* Init state */
    navbarTargetEl.classList.add('hidden')
    navbarEl.classList.add('bg-transparent')
    navbarEl.classList.remove('bg-gray-800', 'bg-opacity-40', 'backdrop-filter', 'backdrop-blur-lg', 'drop-shadow-lg')

    /* Navbar change color on scroll */
    window.addEventListener('scroll', () => {
        if (window.scrollY > 70) {
            navbarEl.classList.remove('bg-transparent',)
            navbarEl.classList.add('bg-gray-800', 'bg-opacity-40', 'backdrop-filter', 'backdrop-blur-lg', 'drop-shadow-lg')
            return null;
        }
        navbarEl.classList.add('bg-transparent',)
        navbarEl.classList.remove('bg-gray-800', 'bg-opacity-40', 'backdrop-filter', 'backdrop-blur-lg', 'drop-shadow-lg')
    })

    // * --------------- INIT FLOWBITE COMPONENTS ---------------
    // * ---- Navbar ----
    const navbarOptions = {
        triggerEl: navbarTriggerEl,
        onExpand: () => {
            navbarEl.classList.remove('bg-transparent',)
            navbarEl.classList.add('bg-gray-800', 'bg-opacity-30', 'backdrop-filter', 'backdrop-blur-lg', 'drop-shadow-lg')
        },
        onCollapse: () => {
            navbarEl.classList.add('bg-transparent',)
            navbarEl.classList.remove('bg-gray-800', 'bg-opacity-30', 'backdrop-filter', 'backdrop-blur-lg', 'drop-shadow-lg')
        }
    };
    // * Component declaration
    const navbarCollapse = new Collapse(navbarTargetEl, navbarOptions);

    // * Tooltips
    const tooltipsEls = document.querySelectorAll('[data-tooltip-target]')
    tooltipsEls.forEach((tooltipEl ) => {
        const targetEl = document.getElementById(tooltipEl.dataset.tooltipTarget)
        new Tooltip(targetEl, tooltipEl);
    })

    // * ---- Language Selector ----
    const langSelectorTriggerEl = document.getElementById("langSelectorDropdownButton")
    const langSelectorTargetEl = document.getElementById("langSelectorDropdownMenu")
    // * Component declaration
    const langSelectorDropdown = new Dropdown(langSelectorTargetEl, langSelectorTriggerEl);

    // * ---- Tech Stack ----
    const techStackEl = document.getElementById('techStack')
    if (techStackEl) {
        const tabEls = techStackEl.querySelectorAll('button[role="tab"]')
        let tabListEls = [] // Flowbite require
        Array.from(tabEls).forEach((tabEl) => {
            const targetId = tabEl.getAttribute('data-tabs-target')
            tabListEls.push({
                id: tabEl.id,
                triggerEl: tabEl,
                targetEl: document.querySelector(targetId)
            })
        })
        // * Component declaration
        const techStackTabs = new Tabs(tabListEls);
    }

    // * ---- Modal Contact Success ----
    const modalContactSuccessEl = document.getElementById('modal-contact-success')
    if (modalContactSuccessEl) {
        const closeModalContactBtnEls = document.getElementsByClassName('close-modal')
        // * Component declaration
        const modalContact = new Modal(modalContactSuccessEl)
        // Add hide events to buttons
        Array.from(closeModalContactBtnEls).forEach(btn => {
            btn.addEventListener('click', (event) => modalContact.hide())
        })
        // * Show modal if url success and update
        const url = window.location.pathname
        const regexSuccess = /success.*/i
        if (regexSuccess.test(url)) {
            modalContact.show()
            window.history.replaceState({}, '', url.replace(regexSuccess, ''))
        }
    }


}

/**
 * Execute Init Scripts on load
 */
InitScripts();

/* * ---- Reload Scripts ----*/
function reloadHeadSourceScripts(scriptEl) {
    scriptEl.remove()
    let scriptTag = document.createElement("script")
    scriptTag.src = scriptEl.src
    scriptTag.setAttribute("data-script-reload", "active")
    document.head.appendChild(scriptTag)
}

/**
 * Barba config
 */
(function BarbaConfig() {
    "use strict";

    /* * ---- Barba  INIT ---- */
    barba.init({
        transitions: [{
            name: 'opacity-transition',
            leave(data) {
                return gsap.to(data.current.container, {
                    opacity: 0,
                    y: 70,
                    duration: 0.3,
                });
            },
            enter(data) {
                return gsap.from(data.next.container, {
                    opacity: 0,
                    y: 70,
                    duration: 0.3,
                });
            }
        }]
    });


    /* * ---- Barba HOOKS ---- */
    barba.hooks.beforeLeave((data) => {
        /* On leave, scroll to TOP*/
        scrollToIdWithDelay('main', 0)
    });
    barba.hooks.enter((data) => {
        /* * -------- Update Navbar ---------- */
        let currentNavbarMenuEl = document.getElementById('navbar')
        const nextHTML = new DOMParser().parseFromString(data.next.html, 'text/html')
        const nextNavbarMenuEl = nextHTML.getElementById('navbar')
        currentNavbarMenuEl.innerHTML = nextNavbarMenuEl.innerHTML
    });
    barba.hooks.after((data) => {
        /* * -------- RELOAD JAVASCRIPTS ELEMENTS ---------- */
        // Reload InitScripts
        InitScripts();

        // Reload source scripts in head tagged with data-script-reload="true"
        const taggedScriptEls = document.head.querySelectorAll('script[data-script-reload="active"]')
        Array.from(taggedScriptEls).forEach((scriptEl) => reloadHeadSourceScripts(scriptEl))

        // Reload inline scripts from fetched container
        const containerScriptEls = data.next.container.getElementsByTagName('script')
        Array.from(containerScriptEls).forEach((scriptEl) => eval(scriptEl.innerHTML))
    });

})();
