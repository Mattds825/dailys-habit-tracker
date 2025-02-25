document.addEventListener('DOMContentLoaded', function() {

    const followBtns = document.getElementsByClassName('followBtn');
    const unfollowBtns = document.getElementsByClassName('unfollowBtn');

    for (let followBtn of followBtns) {
        followBtn.addEventListener('click', function() {
            const currentUser = followBtn.getAttribute('data-current-user');
            const followUser = followBtn.getAttribute('data-followed-user');

            let confirm = window.confirm(`Are you sure you want to follow user:${followUser}?`);

            if(confirm){
               window.location.href = `/follow_user/${followUser}`; 
            }
        });
    }

    for (let unfollowBtn of unfollowBtns) {
        unfollowBtn.addEventListener('click', function() {
            const currentUser = unfollowBtn.getAttribute('data-current-user');
            const unfollowUser = unfollowBtn.getAttribute('data-followed-user');

            let confirm = window.confirm(`Are you sure you want to unfollow user:${unfollowUser}?`);

            if(confirm){
               window.location.href = `/unfollow_user/${unfollowUser}`;
            }
        });
    }

});