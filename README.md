# PLANNING POKER

This application is written in Python 3.8 using FastAPI. It's been tested on Chrome and Edge browsers on Windows 10 and Ubuntu but should also work on Macs.

### Installation
* Clone the repo
* cd into the project root folder
* Install dependencies:
```  
pip3 install -r requirements.txt
```

### Running the app
Go to the project root folder and type:
```
uvicorn planning_poker.main:app 
```

### Using the app
* Open a web browser and go to: http://127.0.0.1:8000/
* Create any number of games (polls) by entering a name into the box and select "Go"
* Select your game in the list
* Copy the link at the bottom of the page and share with other participants
* Enter any number of issues by entering a name into the box and then select "Go"
* Select an issue from the list
* Select an option from the list and press "Vote". You will be able to see the total score and number of votes per option in real time.
