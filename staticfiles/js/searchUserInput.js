document.addEventListener('DOMContentLoaded', function() {

    const searchUserInput = document.getElementById('searchUserInput');
    const searchUserButton = document.getElementById('searchUserBtn');

    searchUserButton.addEventListener('click', function() {
        const searchUserInputValue = searchUserInput.value;
        window.location.href = `/search_users/${searchUserInputValue}`;
    });

});