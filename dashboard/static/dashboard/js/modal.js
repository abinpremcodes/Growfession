
document.addEventListener("DOMContentLoaded", () => {

    // Reusable setup for a confirmation modal
    function setupDeleteModal(config) {

        const modal = document.getElementById(config.modalId);

        if (!modal) return;

        const modalDialog = modal.querySelector(".delete-modal");
        const cancelButton = document.getElementById(config.cancelId);
        const confirmButton = document.getElementById(config.confirmId);
        const modalMessage = config.messageId
            ? document.getElementById(config.messageId)
            : null;

        if (!modalDialog || !cancelButton || !confirmButton) return;

        let selectedForm = null;
        let previousFocus = null;

        function openModal(form) {

            selectedForm = form;
            previousFocus = document.activeElement;

            if (modalMessage && config.getMessage) {
                modalMessage.textContent = config.getMessage(form);
            }

            modal.hidden = false;
            modal.classList.add("active");
            modal.setAttribute("aria-hidden", "false");

            document.body.classList.add("modal-open");

            confirmButton.disabled = false;
            confirmButton.textContent = config.confirmText;

            cancelButton.focus();
        }

        function closeModal() {

            modal.hidden = true;
            modal.classList.remove("active");
            modal.setAttribute("aria-hidden", "true");

            document.body.classList.remove("modal-open");

            selectedForm = null;

            if (previousFocus && typeof previousFocus.focus === "function") {
                previousFocus.focus();
            }

            previousFocus = null;
        }

        // Handle delete buttons used by Projects and Tasks
        if (config.triggerSelector) {

            document.addEventListener("click", (event) => {

                const button = event.target.closest(config.triggerSelector);

                if (!button) return;

                const form = button.closest(config.formSelector);

                if (!form) return;

                event.preventDefault();
                openModal(form);

            });
        }

        // Handle form submissions used by Learning Goals
        if (config.submitSelector) {

            document.addEventListener("submit", (event) => {

                const form = event.target;

                if (!(form instanceof HTMLFormElement)) return;

                if (!form.matches(config.submitSelector)) return;

                event.preventDefault();
                openModal(form);

            });
        }

        // Cancel deletion
        cancelButton.addEventListener("click", closeModal);

        // Confirm deletion
        confirmButton.addEventListener("click", () => {

            if (!selectedForm) return;

            const formToSubmit = selectedForm;

            confirmButton.disabled = true;
            confirmButton.textContent = "Deleting...";

            HTMLFormElement.prototype.submit.call(formToSubmit);

        });

        // Close when clicking outside the dialog
        modal.addEventListener("click", (event) => {

            if (event.target === modal) {
                closeModal();
            }

        });

        // Close using Escape
        document.addEventListener("keydown", (event) => {

            if (!modal.hidden && event.key === "Escape") {
                closeModal();
            }

        });
    }


    // Projects and Tasks
    setupDeleteModal({
        modalId: "deleteModal",
        cancelId: "cancelDelete",
        confirmId: "confirmDelete",
        triggerSelector: ".delete-project-trigger, .delete-task-trigger",
        formSelector: "form.delete-project-form",
        confirmText: "Yes, Delete"
    });


    // Learning Goals
    setupDeleteModal({
        modalId: "deleteGoalModal",
        cancelId: "cancelGoalDelete",
        confirmId: "confirmGoalDelete",
        messageId: "deleteModalMessage",
        submitSelector: "form.delete-goal-form",
        confirmText: "Delete Goal",

        getMessage: (form) => {

            const goalTitle = form.dataset.goalTitle;

            return goalTitle
                ? `Are you sure you want to delete "${goalTitle}"? This action cannot be undone.`
                : "Are you sure you want to delete this learning goal? This action cannot be undone.";

        }
    });

});
