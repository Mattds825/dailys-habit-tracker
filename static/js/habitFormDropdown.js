/**
 * Create by Matthew G Da Silva 13/02/2025
 * 
 * File is used to assist in function of the user_habits page
 * it has function to create a new habit, edit a habit, delete a habit and check in a habit
 * it also control the display of the habit form and the check in form
 * 
 * some of the code is from the Code Institute's Blog project
 */

const createHabitBtn = document.getElementById("createHabitBtn");
const habitForm = document.getElementById("habitForm");
const habitFormCancelBtn = document.getElementById("habitFormCancelBtn");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

const editButtons = document.getElementsByClassName("btn-edit");

const checkInButtons = document.getElementsByClassName("btn-checkin");
const checkInModal = new bootstrap.Modal(document.getElementById("checkInModal"));
const checkInConfirm = document.getElementById("checkInConfirm");
const checkInForm = document.getElementById("checkInForm");

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

// console.log("length",deleteButtons.length);

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
  button.addEventListener("click", (e) => {
    console.log("clicked delete btn");
    let habitId = e.target.getAttribute("habit_id");
    deleteConfirm.href = `delete_habit/${habitId}`;
    deleteModal.show();
  });
}

for(let button of editButtons) {
    button.addEventListener("click", (e) => {
        let habitId = e.target.getAttribute("habit_id");
        let habit_name = e.target.getAttribute("habit_name");
        let habit_description = e.target.getAttribute("habit_description");
        let habit_color = e.target.getAttribute("habit_color");
        let habit_visibility = e.target.getAttribute("habit_visibility");         
        let username = e.target.getAttribute("data_user");

        console.log("clicked edit btn2", habitId, username);

        habitForm.style.display = "block";
        createHabitBtn.style.display = "none";

        document.getElementById("id_title").value = habit_name;
        document.getElementById("id_description").value = habit_description;
        document.getElementById("id_color").value = habit_color;
        document.getElementById("id_visibility").value = habit_visibility;

        habitForm.setAttribute("action", `/${username}/edit_habit/${habitId}/`);
    });
}


for (let button of checkInButtons) {
  button.addEventListener("click", (e) => {
    let habitId = e.target.getAttribute("data-habit-id");    

    console.log("clicked checkin btn", habitId);

    // checkInConfirm.href = `check_in/${habitId}`;
    checkInModal.show();
    checkInForm.setAttribute("action", `check_in/${habitId}/`);
  });
}