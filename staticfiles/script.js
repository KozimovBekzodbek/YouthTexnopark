document.addEventListener("DOMContentLoaded", () => {

    let all = document.querySelectorAll("body > *:not(script)")
    const opener = document.querySelector(".opener")
    const closer = document.querySelector(".times")
    const resNav = document.querySelector("#navbar .navbar-content ul")
    const lists = document.querySelectorAll("#navbar .navbar-content ul a")

    // responsive navbar
    opener.addEventListener("click", () => {
        if (!resNav.classList.contains("tr-0")) {
            resNav.classList.add("tr-0");
        }
    })
    closer.addEventListener("click", () => {
        if (resNav.classList.contains("tr-0")) {
            resNav.classList.remove("tr-0");
        }
    })
    lists.forEach(list => {
        list.addEventListener("click", () => {
            if (resNav.classList.contains("tr-0")) {
                resNav.classList.remove("tr-0");
            }
        })
    })


    // all.forEach(all => {
    //     if (all.classList.contains("light")) {
    //         all.classList.remove("light")
    //         all.classList.add("dark")
    //         console.log(all)
    //     }
    //     else {
    //         all.classList.add("light")
    //         all.classList.remove("dark")

    //     }
    // })


    let mode = document.querySelector(".mode i")

    mode.addEventListener("click", () => {
        let root = document.querySelector(":root")

        if (mode.classList.contains("lni-sun")) {
            mode.classList.add("lni-night")
            mode.classList.remove("lni-sun")
            root.style.setProperty("--color-body", "#0F1214")
            root.style.setProperty("--color-text", "#fff")
            root.style.setProperty("--color-text-04", "#ffffff40")
            root.style.setProperty("--color-body-2", "#0F1214")

        } else {
            mode.classList.remove("lni-night")
            mode.classList.add("lni-sun")
            root.style.setProperty("--color-body", "#fff")
            root.style.setProperty("--color-text", "#0F1214")
            root.style.setProperty("--color-text-04", "#0F121440")
            root.style.setProperty("--color-body-2", "#E8EAEE")
        }




        // console.log(root.style.getPropertyValue("--color-body"))
    })




    // swiper 1
    let swiper = new Swiper(".mySwiper", {
        effect: "coverflow",
        grabCursor: true,
        centeredSlides: true,
        loop: true,
        slidesPerView: "1.2",
        autoplay: {
            delay: 4000,
            disableOnInteraction: false,
        },
        coverflowEffect: {
            rotate: 50,
            stretch: 0,
            depth: 200,
            modifier: 1,
            slideShadows: true,
        },
        pagination: {
            el: ".swiper-pagination",
            clickable: true,
        },
        breakpoints: {
            640: {
                slidesPerView: 1.5,
                spaceBetween: 20,
            },
            768: {
                slidesPerView: 2,
                spaceBetween: 40,
            },
            1200: {
                slidesPerView: 2.9,
                spaceBetween: 40,
            },

        },
    });
    // swiper 2
    let swiper2 = new Swiper(".mySwiper2", {
        slidesPerView: 1.1,
        spaceBetween: 10,
        loop: true,
        autoplay: {
            delay: 5000,
            disableOnInteraction: false,
        },
        breakpoints: {
            400: {
                slidesPerView: 1.6,
                spaceBetween: 10,
            },
            576: {
                slidesPerView: 2.2,
                spaceBetween: 10,
            },
            768: {
                slidesPerView: 3.3,
                spaceBetween: 10,
            },
            1200: {
                slidesPerView: 3.1,
                spaceBetween: 10,
            },

        },

    });

})