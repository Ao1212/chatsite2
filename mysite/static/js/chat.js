$(document).ready(function () {
    const roomName = JSON.parse(document.getElementById("room_name").textContent);
    const chatSocket = new WebSocket(
        "ws://" + window.location.host + "/ws/chat/" + roomName + "/"
    );
    console.log(chatSocket);

    chatSocket.onmessage = function(e){
        const data = JSON.parse(e.data);
        var message = data["message"];
        $('.answer_balloon:last').after(`<div class="answer_balloon">${message}</div>`);
    }

    chatSocket.onclose = function(e){
        console.error("通信に失敗しました。");
    }

    $(".message_input").keypress(function (e) {
        if (e.which == 13) {
            document.querySelector(".box").click();
            }
    });

    $(".box").click(function () {
        // 送信
        var message = $('.message_input').val();
        if (message != "") {
            chatSocket.send(JSON.stringify({
                "message": message,
            }));
            $('.message_input').val("");
        }
        console.log(message);
    });

});