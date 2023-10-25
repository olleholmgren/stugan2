# The Wilderness

The live project site can be found [here](https://stugan2.herokuapp.com)

- Screenshots of the deployed game

![screenshot1](/assets/Images/screenshot1.png)

![screenshot2](/assets/Images/screenshot2.png)

![screenshot3](/assets/Images/screenshot3.png)

![screenshot4](/assets/Images/screenshot4.png)


The Wilderness is a 2-in-1 app containing a mix of well-being consultation as well as an adventure game!

Do yourself a favor and take some time dedicated just for your own well-being.

## Purpose
The aim for for this game is simply to just give the player a minute by themselves. A mix of mindfulness and navigation adventure is the core idea for this project.

## Wireframe
This is my first time I actually used the wireframe software. I have use Balsamiq for this project wireframe. It helped me a lot when I got stuck with coding. I only feel good if I am inside a work flow. When I am stuck with coding then I just step over to work on the wireframe and the idea of the game.
![wireframe-image](/assets/Images/wireframe.png)

## Gameplay
The player is greeted when game.py is launched. In the beginning the program will ask the player about the mood for this day and no matter what the player answers, it will proceed with following up questions - the game works like a computed therapist. 
If the player then wants to play the adventure game, the game will start, or if not, the player will be politely wawed good bye and the program will shut down.

The gameplay works as following: All environments are presented with a headline. You can choose 4 different directions('n', 's', 'e', 'w'). If a chosen direction is not possible for the current environment that you are in, the program will give you an error message stating that your chosen direction is not valid. The program will then give you a list of valid directions. 
Screenshot for reference:

![errorhandling](/assets/Images/errorhandling.png)

When you navigate through the game and come to the ending environment number 15, you will get a game over message and the program will shut down.

![map-environment-image](/assets/Images/game-map-environment.png)

## Game map
The game map is simple. Just a grid structure with boxes that each have a corrensponding number. I found myself numbering in an order that I wanted, then it hit me - the boxes are structured just like the Fibonacci Numbers. This coincidence got me scared for a while but I decided to move on. Here you can see all the environments and directions available in this game.

![map-image](/assets/Images/game-map.png)

## Flow chart
In order to organise my ideas and brainwork, I decided to make a flow-chart with Balsamiq

![flow-chart-image](/assets/Images/flow-chart.png)

## User stories

* As a user, I want to use a text-based program asking me about my current mood.
* As a user, I want to be able to play a text-adventure game where I am guided through beautiful landscapes.
* As a user, I want the environments being described in text so that I can make them up in my own mind.

* As a text-game writer, I want to create a text-based game which is simple and without possible errors for the user.
* As a text-game writer, I want to add guidance for the player if they get lost.
* As a text-game writer, I want to add tweeks such as slow-printed text and lines for aesthetic purposes.

# Testing

### Manual Testing

The game was tested thoroughly for handling invalid user input and correct game output

| User Action         | Expected Result                 | Actual Result                   | Pass / Fail |
|---------------------|---------------------------------|---------------------------------|-------------|
| Run the application | Show player greeting and intro  | Showed player greeting and intro| Pass        |
| Answer questions    | Get follow-up question          | Got follow-up question          | Pass        |
| Blank question      | Get different answer            | Got different answer            | Pass        |
| Run game answer(n)  | Game over message and shut down | Game over message and shut down | Pass        |
| Run game answer(y)  | Get instructions for game play  | Displayed game play instructions| Pass        |
| Stay in tent        | Game over message and shut down | Game over message and shut down | Pass        |
| Walk valid direction| Enter new environment           | Entered new environment         | Pass        |
| Walk invalid dir.   | Get invalid direction message   | Got invalid direction message   | Pass        |
| Walk invalid dir.   | Get valid direction suggestions | Got valid direction suggestions | Pass        |
| Enter environment 15| Game over message and shut down | Game over message and shut down | Pass        |


### Validator testing

[Code Institute Python Linter](https://pep8ci.herokuapp.com/)

The code from this project has been tested in the CI Python Linter app to ensure it will comply with the Pylint standards.

- No errors in run.py

![linter_run](/assets/Images/linter_run.png)

- No errors in environments.py

![linter_env](/assets/Images/linter_env.png)

## Technologies used

- Python has been used as the main programming language for this application
- Python sys module has been imported and used to manipulate printed text in the slow_print function and also when exiting the game at the game over screen
- Python time module has been imported and used to set a pause while printing text throughout the game
- GitPod has been used as the IDE workspace throughout the project
- Github has been use to store the repository as well as version control with git
- Heroku has been used to deploy the project

## Bugs

- No bugs in current state of the project

## Future improvements

- Implementing a working solution to the problem with ignoring and preventing the user to write input while program is printing text.
  I have started on this function but never got it fully working.

## Deployment

### Version Control

The version control was maintained using Git within GitPod to push code to the main repository.

 * From the IDE terminal type 'git add .', to make changes and/or updates to the files.

 * Type 'git commit -m "insert a short descriptive text"', which commits the changes and updates the files.

 * Use the 'git push' command, which pushes the committed changes to the main repository. 

 ### Page Deployment

 The app was deployed to Heroku CLI. The steps to deploy are as follows:

 * After creating an account and logging in, click 'New' to create a new app from the dashboard.
 * Create a unique name for the app and select my region; press 'Create app'.
 * Go to 'Settings' and navigate to 'Config Vars'.
 * Add Config Vars. 
   * For this app was only used: `KEY` = `PORT` : `VALUE` = `8000`.
 * Add buildpacks `Python` and `NodeJS` - in this order.
 * Click the `Deploy Branch`.
 * Scroll Down to Deployment Method and select GitHub.
 * Select the repository to be deployed and connect to Heroku.
 * Scroll down to deploy: 
    * `Option 1` is selecting Automatic deploys (Will Update Automatically with every "git push"). This was chosen for this project.

 * Live deployment [Wilderness](https:/stugan2.herokuapp.com/)

## Credits
- Code Institute (https://learn.codeinstitute.net/courses/course)
- Inspiration for ReadMe content and structure taken from my fellow students at Code institute:
  * Anwar Dawoud (https://github.com/AnwarDawoud/p3-geographyQ)
  * Braxxian (https://github.com/Braxxian/Lost-in-the-woods)

## Acknowledgments

- Big Thank you to my mentor for this project - Spencer Bariball. His guidance and help made this project so much more do-able.