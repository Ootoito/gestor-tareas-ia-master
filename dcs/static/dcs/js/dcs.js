document.addEventListener("DOMContentLoaded", () => {

    // =========================================================
    // MENÚ RESPONSIVE
    // =========================================================

    const toggle = document.querySelector(".nav-toggle");
    const navLinks = document.querySelector(".nav-links");

    if (toggle && navLinks) {

        toggle.addEventListener("click", () => {

            const opened = navLinks.classList.toggle("open");

            toggle.setAttribute(
                "aria-expanded",
                opened ? "true" : "false"
            );

        });

    }


    // =========================================================
    // ROTADOR DE NOTICIAS
    // =========================================================

    const newsItems = document.querySelectorAll(".news-item");

    if (newsItems.length > 0) {

        let current = 0;

        const previousButton =
            document.getElementById("news-prev");

        const nextButton =
            document.getElementById("news-next");

        const counter =
            document.getElementById("news-counter");


        function showNews(index) {

            newsItems.forEach((item) => {
                item.classList.remove("active");
            });

            current =
                (index + newsItems.length) %
                newsItems.length;

            newsItems[current].classList.add("active");

            if (counter) {
                counter.textContent =
                    `${current + 1} / ${newsItems.length}`;
            }

        }


        if (previousButton) {

            previousButton.addEventListener(
                "click",
                () => showNews(current - 1)
            );

        }


        if (nextButton) {

            nextButton.addEventListener(
                "click",
                () => showNews(current + 1)
            );

        }


        setInterval(() => {

            showNews(current + 1);

        }, 9000);

    }

});