// ---- F L A G   P O S T
btnFlag = post_id => alert(`Post ${post_id} has been flagged!`);


// ---- L I K E   P O S T
function btnLike(post_id) {
    var numLikes = parseInt($(`#likes-${post_id}`).text());
    $(`#likes-${post_id}`).html(`&nbsp ${numLikes + 1} &nbsp`);

    $.ajax({
        url: `/post/${post_id}/like`,
        type: 'GET',
        data: { post_id: post_id },
        success: res => {
            console.log("liked");
        },
        error: err => console.log(err)
    });
}


// ---- D I S L I K E   P O S T
function btnDislike(post_id) {
    var numLikes = parseInt($(`#dislikes-${post_id}`).text());
    $(`#dislikes-${post_id}`).html(`&nbsp ${numLikes + 1} &nbsp`);

    $.ajax({
        url: `/post/${post_id}/dislike`,
        type: 'GET',
        data: { post_id: post_id },
        success: res => {
            console.log("disliked");
        },
        error: err => console.log(err)
    });
}