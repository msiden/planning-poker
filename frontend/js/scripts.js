//const COOKIE = document.cookie.replace("uuid=", "");
const URL = window.location.hostname;
var request = new XMLHttpRequest();
//var gameId;
//var gameName;


function CreateNewGame() {
    var gameName = document.getElementById("inputNewGame").value;

    request.onreadystatechange = function() {
        if (request.readyState === 4) {
            loadTableData();
            }
        }

    request.open("POST", "new_game");
    request.send(JSON.stringify({"name": gameName}));
}

function CreateNewIssue() {
    var issueName = document.getElementById("inputNewIssue").value;
    var gameId = window.location.href.slice(-36)

    request.onreadystatechange = function() {
        if (request.readyState === 4) {
            loadIssues();
            }
        }

    request.open("POST", "/new_issue");
    request.send(JSON.stringify({"name": issueName, "game_id": gameId}));
}

function loadTableData() {

    var tableRef = document.getElementById("gamesTable");
    while ( tableRef.rows.length > 0 )
        {
            tableRef.deleteRow(0);
        }

    const table = document.getElementById("gamesBody");

    request.onreadystatechange = function() {
        if (request.readyState === 4) {
            var gamesList = request.response;
            gamesList = JSON.parse(gamesList);
            gamesList.forEach( item => {
                let row = table.insertRow();
                let name = row.insertCell(0);
                name.innerHTML = `<a href=/game/${item.id}>${item.name}</a>`
                });
            }
        }

    request.open("GET", "/list_games");
    request.send();
}

function loadIssues() {

    var gameId = window.location.href.slice(-36)
    var tableRef = document.getElementById("issuesTable");
    while ( tableRef.rows.length > 0 )
    {
        tableRef.deleteRow(0);
    }

    const table = document.getElementById("issuesBody");

    request.onreadystatechange = function() {
        if (request.readyState === 4) {
            var issuesList = request.response;
            issuesList = JSON.parse(issuesList);
            issuesList.forEach( item => {
            let row = table.insertRow();
            let name = row.insertCell(0);
            name.innerHTML = `<a href=/game/${item.id}>${item.name}</a>`
            });
        }
    }

    request.open("POST", "/list_issues");
    request.send(JSON.stringify({"id": gameId}));
}

