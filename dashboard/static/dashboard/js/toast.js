document.addEventListener("DOMContentLoaded", () => {

    const toastMessages = document.querySelectorAll(".toast-message");

    toastMessages.forEach((toast) => {

        const closeButton = toast.querySelector(".toast-close");

        // Close notification when close button is clicked
        if (closeButton) {
            closeButton.addEventListener("click", () => {
                dismissToast(toast);
            });
        }

        // Automatically dismiss after 5 seconds
        setTimeout(() => {
            dismissToast(toast);
        }, 5000);

    });

    // Reusable dismiss function
    function dismissToast(toast) {

        if (!toast || toast.classList.contains("toast-hiding")) {
            return;
        }

        toast.classList.add("toast-hiding");

        setTimeout(() => {
            toast.remove();

            // Remove container if no notifications remain
            const container = document.querySelector(".toast-container");

            if (container && container.children.length === 0) {
                container.remove();
            }

        }, 300);

    }

});
