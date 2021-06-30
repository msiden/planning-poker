var request = new XMLHttpRequest();
var issueId = window.location.href.slice(-36);
var gameId = window.location.href.replace(issueId, "");
gameId = gameId.slice(-37, -1);
const TEXT = "Total votes: "

function updateVotes() {

    setInterval(function() {

        request.onreadystatechange = function() {
        if (request.readyState === 4) {
            var votes = request.response;
            votes = JSON.parse(votes);
            document.getElementById("noVotes0").innerHTML = TEXT + votes[0];
            document.getElementById("noVotes1").innerHTML = TEXT + votes[1];
            document.getElementById("noVotes2").innerHTML = TEXT + votes[2];
            document.getElementById("noVotes3").innerHTML = TEXT + votes[3];
            document.getElementById("noVotes5").innerHTML = TEXT + votes[5];
            document.getElementById("noVotes8").innerHTML = TEXT + votes[8];
            document.getElementById("noVotes13").innerHTML = TEXT + votes[13];

            getTotalScore()
            }
        }

        request.open("POST", "/list_votes");
        request.send(JSON.stringify({"game_id": gameId, "issue_id": issueId}));

    }, 1000);

}

function getTotalScore () {

    request.onreadystatechange = function() {
        if (request.readyState === 4) {
            var totScore = request.response;
            document.getElementById("totScoreText").innerHTML = totScore;
            };
        }

    request.open("POST", "/total_score");
    request.send(JSON.stringify({"game_id": gameId, "issue_id": issueId}));

}
