const createHabitBtn = document.getElementById('createHabitBtn');
const habitForm = document.getElementById('habitForm');
const habitFormCancelBtn = document.getElementById('habitFormCancelBtn');

if(createHabitBtn === null || habitForm === null || habitFormCancelBtn === null) {
    // elements not found on page
}else{
    createHabitBtn.addEventListener('click', () => {
        habitForm.style.display = 'block';
        createHabitBtn.style.display = 'none';
    });
    
    habitFormCancelBtn.addEventListener('click', () => {
        // clear habitForm and set display to none
        habitForm.reset();
        habitForm.style.display = 'none';
        createHabitBtn.style.display = 'inline-block';
    });
}



console.log("i am here");