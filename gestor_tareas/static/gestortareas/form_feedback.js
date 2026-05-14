document.addEventListener("DOMContentLoaded", function () {
    const forms = document.querySelectorAll(".js-submit-once");

    forms.forEach(function (form) {
        form.addEventListener("submit", function () {
            const submitButtons = form.querySelectorAll('button[type="submit"], input[type="submit"]');

            submitButtons.forEach(function (btn) {
                const loadingText = btn.dataset.loadingText || "Procesando...";
                btn.disabled = true;
                btn.classList.add("is-submitting");
                btn.innerHTML = loadingText;
            });
        });
    });
});