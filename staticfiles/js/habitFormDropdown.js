const createHabitBtn = document.getElementById("createHabitBtn");
const habitForm = document.getElementById("habitForm");
const habitFormCancelBtn = document.getElementById("habitFormCancelBtn");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

if (
  createHabitBtn === null ||
  habitForm === null ||
  habitFormCancelBtn === null
) {
  // elements not found on page
} else {
  createHabitBtn.addEventListener("click", () => {
    habitForm.style.display = "block";
    createHabitBtn.style.display = "none";
  });

  habitFormCancelBtn.addEventListener("click", () => {
    // clear habitForm and set display to none
    habitForm.reset();
    habitForm.style.display = "none";
    createHabitBtn.style.display = "inline-block";
  });
}

console.log("length",deleteButtons.length);

/**
 * Modified code from Code Institute's Blog project
 * Initializes deletion functionality for the provided delete buttons.
 *
 * For each button in the `deleteButtons` collection:
 * - Retrieves the associated habits's ID upon click.
 * - Updates the `deleteConfirm` link's href to point to the
 * deletion endpoint for the specific comment.
 * - Displays a confirmation modal (`deleteModal`) to prompt
 * the user for confirmation before deletion.
 */

for (let button of deleteButtons) {
    console.log(button);
  button.addEventListener("click", (e) => {
    console.log("clicked delete btn");
    let habitId = e.target.getAttribute("habit_id");
    deleteConfirm.href = `delete_habit/${habitId}`;
    deleteModal.show();
  });
}
