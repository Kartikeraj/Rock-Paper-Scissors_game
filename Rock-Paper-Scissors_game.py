<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rock Paper Scissors - Python</title>
    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/brython/3.11.3/brython.min.js"></script>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; padding: 20px; }
        pre { background: #f4f4f4; padding: 15px; border-radius: 5px; text-align: left; overflow-x: auto; }
        button { padding: 10px 20px; font-size: 16px; cursor: pointer; margin-top: 10px; }
        #output { margin-top: 20px; white-space: pre-line; text-align: left; }
        .footer { margin-top: 30px; font-size: 16px; font-weight: bold; }
        .linkedin-button {
            display: inline-block;
            margin-top: 10px;
            padding: 10px 15px;
            background-color: #0077b5;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            font-size: 16px;
        }
        .linkedin-button:hover { background-color: #005a8e; }
    </style>
</head>
<body onload="brython()">

    <h1>Rock Paper Scissors - Python</h1>

    <h3>Python Code:</h3>
    <pre>
import random

stone = \"\"\" 
 ----- 
|     |
| ✊  |
|     |
 ----- 
\"\"\"

paper = \"\"\" 
 ----- 
|     |
| ✋  |
|     |
 ----- 
\"\"\"

scissors = \"\"\" 
 ----- 
|     |
| ✌  |
|     |
 ----- 
\"\"\"

user1 = input(\"Choose Stone, Paper, or Scissors (ST/P/S): \").strip().upper()

if user1 == \"ST\": user2 = stone
elif user1 == \"P\": user2 = paper
elif user1 == \"S\": user2 = scissors

list1 = [stone, paper, scissors]
rand1 = random.choice(list1)

print(\"\\nYou chose:\")
print(user2)
print(\"--------------------------------\")
print(\"Computer chose:\")
print(rand1)

if rand1 == user2:
    print(\"It's a Draw!!!\")
elif (rand1 == stone and user2 == paper) or \
     (rand1 == paper and user2 == scissors) or \
     (rand1 == scissors and user2 == stone):
    print(\"You win 🎉🎉\")
else:
    print(\"You lose 😢\")
    </pre>

    <button onclick="runPython()">Run Python Code</button>

    <h3>Output:</h3>
    <div id="output"></div>

    <script type="text/python">
import random
from browser import document, html, window

def runPython():
    output = document["output"]
    output.text = ""

    stone = \"\"\" 
 ----- 
|     |
| ✊  |
|     |
 ----- 
\"\"\"

    paper = \"\"\" 
 ----- 
|     |
| ✋  |
|     |
 ----- 
\"\"\"

    scissors = \"\"\" 
 ----- 
|     |
| ✌  |
|     |
 ----- 
\"\"\"

    user1 = window.prompt("Choose Stone, Paper, or Scissors (ST/P/S)").strip().upper()

    if user1 == "ST":
        user2 = stone
    elif user1 == "P":
        user2 = paper
    elif user1 == "S":
        user2 = scissors
    else:
        output.text = "Invalid Choice!"
        return

    list1 = [stone, paper, scissors]
    rand1 = random.choice(list1)

    output.text += "You chose:\\n" + user2 + "\\n------------------------------\\n"
    output.text += "Computer chose:\\n" + rand1 + "\\n"

    if rand1 == user2:
        output.text += "It's a Draw!!!"
    elif (rand1 == stone and user2 == paper) or \
         (rand1 == paper and user2 == scissors) or \
         (rand1 == scissors and user2 == stone):
        output.text += "You win 🎉🎉"
    else:
        output.text += "You lose 😢"

document["runPython"] = runPython
    </script>

    <div class="footer">
        Made by Kartike Raj Choudhary
        <br>
        <a class="linkedin-button" href="https://www.linkedin.com/in/kartike-raj-choudhary/" target="_blank">Connect on LinkedIn</a>
    </div>

</body>
</html>
