document.addEventListener("DOMContentLoaded", function () {
    const toasts = document.querySelectorAll(".toast");

    toasts.forEach(function (toast) {
        const closeBtn = toast.querySelector(".toast-close");

        const closeToast = function () {
            toast.classList.add("toast-hide");
            setTimeout(function () {
                toast.remove();
            }, 180);
        };

        if (closeBtn) {
            closeBtn.addEventListener("click", closeToast);
        }

        setTimeout(closeToast, 4000);
    });
});