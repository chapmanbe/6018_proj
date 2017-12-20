# Multi-Game Menu with High Scores
the purpose of this project is to make multiple simple games in python and tie them together in a game menu
in that menu you can choose which game to play, to see high scores or to quit

## organization
within the parent directory there are files for:
* Game Menu-initial interface (game_interface.py)
* Maze Game (game_1.py)
* flying game (game_2.py)
* High Scores (high_score.py)
* HighScore file (highscores.pkl)
* License
* readme (this)
* setup

## modules used and dependencies
Modules require to run this package are
#### Non-standard modules
* turtle
* pygame

#### standard modules
* math, random, os

## install and play instructions

#### To Install
1. download the 6018_proj directory
2. install turtle and pygame if not already done

#### To Play
1. open terminal or shell
2. move to the 6018_proj directory
    * cd ~.../6018_proj
3. open the interface file
    * python game_interface.py
4. choose menu option

##### References
* interface: http://www.nebelhom.com/2013/08/14/create-a-simple-game-menu-with-pygame-pt-1-writing-the-menu-options-to-the-screen/
* game 1: http://christianthompson.com/   https://www.youtube.com/watch?v=inocKE13DEA
* game 2:

# delete this , movie narrative
Happy Holidays!

This project brought to you by Annie Bowles and Robyn Pack.
For our final project we decided to work together and make a game in python

Our initial idea was to make a maze type game, where you move through levels picking up objects and treasure

neither of us had ever done this sor of thing before, so we went looking for game tutorials

Christian thompson at christian thompson.com and his you tube channel for the game ideas and help
credit for the interface ideas goes to Johannes Vogel on the 'Learning the machine' blog. Links to these projects
can be found in the readme.md file

Lets start with the overall organization. We tried to structure this project like a package. Inside the main directory
we have the following files
A setup.py file which describes project metedata such as modules needed, author info, keywords, license info, etc.
a readme.md file which describes the project itself and how to install and run it
a license.txt file -we chose the MIT license-- which is a permissive free software license. It has few restrictions
a highscores.plk file to keep the best score from each run of the games
and our modules
the game interface.py file is the starting point. it displays the menu items and lets you pick a game to play.
the game_1 and game_2.py files are the modules for each of the games we made, very simple games

We are now going to go over each of the three modules and explain what we did and how they work.

Starting with the game_interface:
this is a simple interface
we have defined two classes here, 
this first one is inheriting from the pygame.font.Font class

we use this class to set up the appearance of our menu items.
methods defined here are the 
set position method - this tells the instance of MenuItem where to go on the screen
the mouse selection method determines if the mouse is hovering over the item
and the mouse select font color changes the items color  

the second class GameMenu is the screen itself. 
here we set defaults for the appearance of the display screen such as size, color ect. 
within the __init__ method there is a for loop. This section goes through each menu item and moves them to more appropriate places. In the MenuItem class, each item is default 0,0 which stacks them all on the center of the screen. this loop does a little bit of math to stact the items vertically

next, the run method describes how the screen is drawn and determines what happens when the various items are clicked. This is where the methods in MenuItem come up with text selection and color change

Lastly, we define a few functions to do something when the inems are clicked and then create the screen.

Here is the open game_interface, lets hit game 1

and there it plays!

Moving onto describing how game 1 works:
Game 1 is a maze game. We used the turtle module to built this one. 
there are several classes here, all inheriting from the turtle.Turtle class
we have
player-this is the red guy we move around
blocks - this draws the maze walls
coins - treasure we can pick up to increase our score
bad guys - evil green triangles that chase us and steal our money
and an exit class-this is used to move from one level to the next.
most of the methods in the classes are similar
and for the most part contained in player

in the player class the __init__ method sets up the appearance of the player ...thing a red square in this case.

we then have methods for up, down, left, and right movement. this tells our little square how many pixels to move when keyboard keys are clicked.  bad guys also have similar methods
the walls variable is a list of all the wall positions so we don't walk into them.

there is also a is_collision method which determines the proximity of a player to another game element like an enemy or a coin

the coin and bad guy have methods to remove them from the screen a 'pocket' and a 'die' respectively. When those methods are called they coins or bad guys seem to disappear.

bad guy has another method is_close which influences the movement direction of the bad guy. if you are close, it can sense you and follows you a bit
there is also a timer here to keep bad guys from going too fast

then we define the levels, this could be put in a seperate file if desired to clean up the code

I use X for wall positions P for player C for coin and E (enemy) for bad guys

the make_maze function constructs the screen. It first looks at the length of the level --each level is a list, and then at the length of each element in the level. 

the positions of each element are determined again with a little simple math. then the 'kind' of element is determined XPCE or O and they are appended to each respective list. X Blocks are stamped at each location, meaning their image stays on the screen

we then have some keyboard bindings, we get the bad guys movement started and then open up the main game loop

make maze level 0 and start

the main game loop keeps the game running and continually checks for collision with coins, bad guys, or the exit. 

when you reach the exit, we remove all bad guys and leftover coins, clear out the lists for the coins, walls, bad guys and exit, clear off the stamped blocks from before and make a new maze level to continue play!

Script about game 2 and high score file.
Used turtle package because it provides an easy way to make games. Start by making the screen using turtle.Screen, then set the color to black, the title, and a background picture (gif works best for some reason). Game class inherits from turtle.Turtle class. We make it so the player can get points all the way up to and including the boarders and set the score equal to 0. We then create a method which changes the score by however many points we want and use an update_score method to clear the old score and print the current score at the top of the screen. A sound also plays when the score increases. Our boarder class also inherits from turtle.Turtle (all our classes do), and it tells the pen where to go to draw the boarder. The player class initializes the avatar the player controls (a white triangle) at a speed of 1 (movement speed). It also defines the movements and makes sure it turns at the boarders, instead of going through them. When the left and right keys are hit, the avatar moves 60 degrees to the left or right, and the up and down keys control the speed. The goal class initializes the yellow coins the player tries to catch with the same parameters as the player class with a few additions. They are moving twice as fast as the player initially, and start moving from random locations in random directions. When they collide with the player (defined later), they ‘jump’ to a random location. They also have the same boarder checking as the player. The is_collision function checks for a collision between the player and the goal using the Pythagorean theorem to measure the distance between them. We then create our class instances for the game, draw the boarder, and create multiple goals (we made 6). Setting the keyboard bindings makes it so the turtle knows what keys are being used to control the avatar movements. Wn.tracer(0) is used to speed up the game before setting up the main loop. We made the main loop only update once per loop (which also speeds up the game), called the player.move method, used a for loop to make all the goals move, and checked for collisions between the player and goal. When there is a collision, the score is increased by a number of points and after the game ends (timer runs out), the score is added to the high_score pickle file.
