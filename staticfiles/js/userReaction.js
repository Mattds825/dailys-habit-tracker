document.addEventListener("DOMContentLoaded", function () {

    console.log("loaded userReaction.js");

    const reactButtons = document.getElementsByClassName("reactBtn");

    const reactionEmojiMap = {
        0: "👏",
        1: "👍",
        2: "♥️",
        3: "🏆",
    };

    for(let reactBtn of reactButtons){
        console.log("button found");
        reactBtn.addEventListener("click", function(){
            const habitId = reactBtn.getAttribute("data-habit-id");
            const habitUser = reactBtn.getAttribute("data-habit-user");
            const reactionType = parseInt(reactBtn.getAttribute("data-reaction-type"));
            const fromUser = reactBtn.getAttribute("data-user");

            console.log(habitId, habitUser, reactionType, fromUser);

            // open django view url in window
            // window.open(`/${fromUser}/user_reaction/${habitId}/${reactionType}/`, "_self");
            window.open(`/user_reaction/${habitId}/${reactionType}`, "_self");
            // fetch(`/${fromUser}/user_reaction/${habitId}/${reactionType}/`)
            // fetch(`/explore/`)

            

        });
    }

});