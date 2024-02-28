document.addEventListener("DOMContentLoaded", () => {
    // Get all elements with the class 'modal-footer' and loop through them
    const modalFooters = document.querySelectorAll('.modal-footer');
    modalFooters.forEach(modalFooter => {
        // Get the input element and buttons within each modal footer
        const quantityInput = modalFooter.querySelector('.quantity-input');
        const plusBtn = modalFooter.querySelector('.plus-btn');
        const minusBtn = modalFooter.querySelector('.minus-btn');

        // Add event listeners to the plus and minus buttons
        plusBtn.addEventListener('click', () => {
            quantityInput.value = parseInt(quantityInput.value) + 1;
        });

        minusBtn.addEventListener('click', () => {
            const currentValue = parseInt(quantityInput.value);
            if (currentValue > 1) {
                quantityInput.value = currentValue - 1;
            }
        });
    });
});