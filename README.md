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