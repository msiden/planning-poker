const COOKIE = document.cookie.replace("uuid=", "");
const URL = window.location.hostname;
var request = new XMLHttpRequest();
var gameId;
var gameName;


function CreateNewGame() {
    var gameName = document.getElementById("inputNewGame").value;

    request.onreadystatechange = function() {
        if (request.readyState === 4) {
            gameId = request.response;
            console.log(gameId);
            document.getElementById("gamesList").style = "display: true";
            }
        }

    request.open("POST", "new_game");
    request.send(JSON.stringify({"name": gameName}));
}

function CreateNewIssue() {
    var issueName = document.getElementById("inputNewIssue").value;

    request.onreadystatechange = function() {
        if (request.readyState === 4) {
            issueId = request.response
            document.getElementById("issuesList").style = "display: true";
            }
        }
    console.log(issueName);
    console.log(gameId);
    request.open("POST", "new_issue");
    request.send(JSON.stringify({"name": issueName, "game_id": gameId}));
}

