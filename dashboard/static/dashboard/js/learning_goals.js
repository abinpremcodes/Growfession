
document.addEventListener("DOMContentLoaded", () => {

    const modal = document.getElementById("deleteGoalModal");
    const modalDialog = modal?.querySelector(".delete-modal");
    const modalMessage = document.getElementById("deleteModalMessage");

    const cancelButton = document.getElementById("cancelGoalDelete");
    const confirmButton = document.getElementById("confirmGoalDelete");

    if (
        !modal ||
        !modalDialog ||
        !modalMessage ||
        !cancelButton ||
        !confirmButton
    ) {
        return;
    }

    let selectedForm = null;
    let previousFocus = null;

    // Open the confirmation modal
    function openModal(form) {

        selectedForm = form;
        previousFocus = document.activeElement;

        const goalTitle = form.dataset.goalTitle;

        modalMessage.textContent = goalTitle
            ? `Are you sure you want to delete "${goalTitle}"? This action cannot be undone.`
            : "Are you sure you want to delete this learning goal? This action cannot be undone.";

        modal.hidden = false;
        modal.classList.add("active");
        modal.setAttribute("aria-hidden", "false");

        document.body.classList.add("modal-open");

        confirmButton.disabled = false;
        confirmButton.textContent = "Delete Goal";

        cancelButton.focus();
    }

    // Close the confirmation modal
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

    // Intercept only Learning Goal delete forms
    document.addEventListener("submit", (event) => {

        const form = event.target;

        if (!(form instanceof HTMLFormElement)) {
            return;
        }

        if (!form.matches("form.delete-goal-form")) {
            return;
        }

        event.preventDefault();

        openModal(form);

    });

    // Cancel deletion
    cancelButton.addEventListener("click", closeModal);

    // Confirm deletion
    confirmButton.addEventListener("click", () => {

        if (!selectedForm) {
            return;
        }

        const formToSubmit = selectedForm;

        confirmButton.disabled = true;
        confirmButton.textContent = "Deleting...";

        HTMLFormElement.prototype.submit.call(formToSubmit);

    });

    // Close when clicking outside the modal
    modal.addEventListener("click", (event) => {

        if (event.target === modal) {
            closeModal();
        }

    });

    // Close when pressing Escape
    document.addEventListener("keydown", (event) => {

        if (!modal.hidden && event.key === "Escape") {
            closeModal();
        }

    });

});
