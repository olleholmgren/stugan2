# The Wilderness

The live project site can be found here

The Wilderness is a 2-in-1 app containing a mix of well-being consultation as well as an adventure game!

Do yourself a favor and take some time dedicated just for your own well-being.

## Purpose
The aim for for this game is simply to just give the player a minute by themselves. A mix of mindfulness and navigation adventure is the core idea for this project.

## Wireframe
This is my first time I actually used the wireframe software. I have use Balsamiq for this project wireframe. It helped me a lot when I got stuck with coding. I only feel good if I am inside a work flow. When I am stuck with coding then I just step over to work on the wireframe and the idea of the game.
![wireframe-image](/assets/Images/wireframe.png)

## Gameplay
The player is greeted when run.py is launched. In the beginning the computer will ask the player about the mood for this day and if the player chooses to continue talk to the computer, there will be more questions - the game works like a computed therapist. 
If the player then wants to play the adventure game, the game will start, or if not, the player will be waved goodbye to and be told to come back when feeling better.
![map-environment-image](/assets/Images/game-map-environment.png)

## Game map
The game map is simple. Just a grid structure with boxes that each have a corrensponding number. I found myself numbering in an order that I wanted, then it hit me - the boxes are structured just like the Fibonacci Numbers. This coincidence got me scared for a while but I decided to move on.

![map-image](/assets/Images/game-map.png)

## Flow chart
In order to organise my ideas and brainwork, I decided to make a flow-chart with Balsamiq
![flow-chart-image](/assets/Images/flow-chart.png)

## User goals

## User stories

# Testing

### Manual Testing

The game was tested thoroughly for handling invalid user input and correct game output

| User Action         | Expected Result                 | Actual Result                   | Pass / Fail |
|---------------------|---------------------------------|---------------------------------|-------------|
| Run the application | Show player greeting and intro  | Showed player greeting and intro| Pass        |
| Answer questions    | Get follow-up question          | Got follow-up question          | Pass        |
| Run game answer(n)  | Get restarted from 1st question | Restarted from 1st question     | Pass        |
| Run game answer(y)  | Get instructions for game play  | Displayed game play instructions| Pass        |
| Walk valid direction| Enter new environment           | Entered new environment         | Pass        |
| Walk invalid dir.   | Get invalid direction message   | Got invalid direction message   | Pass        |
| Walk invalid dir.   | Get valid direction suggestions | Got valid direction suggestions | Pass        |
|                     |                                 |                                 |             |
|                     |                                 |                                 |             |
|                     |                                 |                                 |             |
|                     |                                 |                                 |             |


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

 * Live deployment [Wilderness](https://.herokuapp.com/)

## Credits
- [Codeinstiute] (https://learn.codeinstitute.net/courses/course)
- 

## Acknowledgments

- Big Thank you to my mentor for this project - Spencer Bariball. His guidance and help made this project so much more do-able.