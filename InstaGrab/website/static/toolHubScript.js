document.addEventListener("DOMContentLoaded", function() {
    const menuContainer = document.querySelector(".menu-container");
    const leftBtn = document.querySelector(".left-btn");
    const rightBtn = document.querySelector(".right-btn");
    var listMenuButtons = document.querySelectorAll('.list');
    var listDisplays = document.querySelectorAll('.list-display');
    const newListBtn = document.querySelector('.new-list-btn');
    const cancelNewListBtn = document.querySelector('.cancel-new-list-btn');
    const addUsersBtn = document.querySelector('.actions-btn.add-users')
    const cancelAddUsersBtn = document.querySelector('.cancel-add-users-btn');
    const messageBtn = document.querySelector('.actions-btn.send-message');
    const cancelMsgBtn = document.querySelector('.cancel-send-message-btn');

    let selectedListId = null;

    leftBtn.addEventListener("click", function() {
        menuContainer.scrollBy({
            left: -100,
            behavior: "smooth"
        });
    });

    rightBtn.addEventListener("click", function() {
        menuContainer.scrollBy({
            left: 100,
            behavior: "smooth"
        });
    });

    listMenuButtons.forEach(function(button) {
        button.addEventListener("click", function() {
            selectedListId = button.classList[1];
            document.querySelectorAll("#list-id-input").forEach((input) => { input.value = selectedListId});
            listDisplays.forEach(function(displayer) {displayer.style.display = 'none'});
            document.querySelector('.list-display.number'+selectedListId).style.display = 'grid';
        });
    });

    newListBtn.addEventListener("click", function() {
        document.querySelector('.popup-bg.new-list').style.display = 'flex';
    });

    cancelNewListBtn.addEventListener("click", function() {
        document.querySelector('.popup-bg.new-list').style.display = 'none';
    });

    addUsersBtn.addEventListener("click", function() {
        document.querySelector('.popup-bg.add-users').style.display = 'flex';
    });

    cancelAddUsersBtn.addEventListener("click", function() {
        document.querySelector('.popup-bg.add-users').style.display = 'none';
    });

    messageBtn.addEventListener("click", function() {
        document.querySelector('.popup-bg.message').style.display = 'flex';
    });

    cancelMsgBtn.addEventListener("click", function() {
        document.querySelector('.popup-bg.message').style.display = 'none';
    });

});