/* 
created by Matthew G Da Silva 20/02/2025

This script is used to populate the notification collapse with the appropriate text
*/

const reactionEmojiMap = {
  0: "👏",
  1: "👍",
  2: "♥️",
  3: "🏆",
};

$(document).ready(function () {
  // set up collapse for notification button
  $("#notificationButton").click(function () {
    $("#notificationCollapse").collapse("toggle");
  });

  // populate notification collapse
  const notificationTexts = document.getElementsByClassName("notificationText");
  const dismissNotificationBtns = document.getElementsByClassName("dismissNotificationBtn");

  for (let notificationText of notificationTexts) {
    console.log("notificationText found");
    const reactionType = parseInt(
      notificationText.getAttribute("data-reaction-type")
    );
    const fromUser = notificationText.getAttribute("data-from-user");

    notificationText.textContent = `You received a ${reactionEmojiMap[reactionType]} from ${fromUser}`;
  }

  // add event listener to dismiss notification button
  for (let dismissNotificationBtn of dismissNotificationBtns) {
    dismissNotificationBtn.addEventListener("click", function () {
        const reactionId = dismissNotificationBtn.getAttribute("data-reaction-id");
        const userId = dismissNotificationBtn.getAttribute("data-user");

        console.log(reactionId);

        window.open(`dismiss_reaction/${reactionId}`, "_self");
    });
  }
});
