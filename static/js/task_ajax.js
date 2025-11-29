document.addEventListener("DOMContentLoaded", () => {

    document.querySelectorAll(".test-form").forEach(form => {

        form.addEventListener("submit", async function (e) {
            e.preventDefault();

            const testId = this.dataset.testId;
            const answerInput = this.querySelector("input[name='answers']:checked");
            const csrf = this.querySelector("[name=csrfmiddlewaretoken]").value;

            if (!answerInput) return;

            const formData = new URLSearchParams();
            formData.append("test_question_id", testId);
            formData.append("answers", answerInput.value);

            const response = await fetch(window.location.href, {
                method: "POST",
                headers: {
                    "X-CSRFToken": csrf,
                    "X-Requested-With": "XMLHttpRequest"
                },
                body: formData
            });

            const data = await response.json();

            const labels = this.querySelectorAll("label");

            labels.forEach(label => {
                const id = Number(label.getAttribute("for").replace("option-", ""));

                label.classList.remove("btn-success", "btn-danger", "btn-outline-primary");

                if (id === data.correct_id) {
                    label.classList.add("btn-success");
                } else if (id === data.chosen_id) {
                    label.classList.add("btn-danger");
                } else {
                    label.classList.add("btn-outline-primary");
                }
            });

            const resultDiv = this.parentElement.querySelector(".test-result");
            resultDiv.innerHTML = data.correct ? "Правильно! 🎉" : "Неправильно 😔";
        });
    });
});
