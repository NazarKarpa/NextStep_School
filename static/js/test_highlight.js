document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('[data-test-id]').forEach(function(testBlock) {

        const correctId = testBlock.dataset.correctId;
        const chosenId  = testBlock.dataset.chosenId;

        if (!chosenId) return;

        testBlock.querySelectorAll('[data-option-id]').forEach(function(option) {
            const optionId = option.dataset.optionId;

            if (optionId === correctId) {
                option.classList.add('option-correct');
            }

            if (optionId === chosenId && chosenId !== correctId) {
                option.classList.add('option-wrong');
            }
        });
    });
});
