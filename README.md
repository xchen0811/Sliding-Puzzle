# Sliding-Puzzle
Our project is a two-dimensional game called Sliding Puzzle with 3x3 tiles. It is an essential two-dimensional game that challenges a player to slide flat number pieces along certain routes on a board to establish an end-configuration. The player needs to rearrange the tiles to the original order by sliding block puzzle without lifting any piece off the board. 

Team members name:
    Xiafen Chen, Rongwei Gao, Jinyan Huang

B#：B00754506, , B00657239
    
How to run the program: 
    1. Open the terminal and install pygame by typing in “python3 -m pip in stall – U pygame – user”
    2. Run the game code in python or python 3
    3. The game window will display when you execute the code
    4. Just like all other games, use your mouse or keyboard (WASD or up, down, left, right) to move the eight tiles on the board.
    5. If you can’t solve the puzzle, you can click on the bottom left buttons (“New Game” or “Reset”) to either start a new game or reset the game 
    6. Also, you can click on the “Solve” button to solve the game for you
    7. Lastly, it will display a message “Congratulations” to indicate that you have won the game

Notes/Requirements for the program:
    1. Terminate the game by using pygame.quit() and sys.exit()
    2. Check for quit by using pygame.event.get(QUIT)
    3. Generate the staring board (shuffle the number order)
    4. Return board coordinates of the blank space
    5. A function is created to allow player to slide the tiles
    6. Another function is defined to demonstrate sliding animation
    7. Check if the move is valid with a new function defined
    8. Generate a new puzzle by using pygame.display.update() and pygame.time .wait()

What it is?/What does it do?/How does it work?:

    Our project is a two-dimensional game called Sliding Puzzle with 3x3 tiles. 
    It is an essential two-dimensional game that challenges a player to slide flat number pieces along certain routes on a board to establish an end-configuration. 
    The player needs to rearrange the tiles to the original order by sliding block puzzle without lifting any piece off the board. 

    Most of the main functionalities our project has is from the Pygame library. 
    Pygame is a free and open source python programming language library for making multimedia application like games built on top of the excellent SDL library. 
    It is highly portable and runs on nearly every platform and operating system. Our game has a simple GUI. 
    All we have to do is to install and import Pygame and call the functions it contains. 
    (pygame.init() initializes all the modules required for pygame; pygame. display.set_mode((width,height)) 
    will launch a window of the desired size and the return value is a surface object where you will perform graphical operations on; pygame.event.get() 
    get the event queue; pygame.quit uninitializes all modules that have been previously initialized and doesn’t exit the game.)


References:
    Pygame tutorial:
    https://www.youtube.com/watch?v=i6xMBig-pP4
    https://www.youtube.com/watch?v=2-DNswzCkqk
    https://www.youtube.com/watch?v=UdsNBIzsmlI

    Pygame functionality explanations:
    https://www.pygame.org/wiki/GettingStarted
    https://www.pygame.org/docs/tut/newbieguide.html
    https://www.pygame.org/docs/

    Sys tutorial:
    https://www.youtube.com/watch?v=7OrSEpv26D8&list=PL1H1sBF1VAKU1uIUq04iU2gbSF00zGx37

    How to program slide puzzle in python:
    https://www.youtube.com/watch?v=afC3dq9MeJg

    Slide puzzle python code:
    http://www.openbookproject.net/py4fun/tiles/tiles.html
    https://inventwithpython.com/pygame/chapter4.html
    https://www.daniweb.com/programming/software-development/threads/493259/slide-puzzle-game


    Code comments tutorial:
    https://inventwithpython.com/blog/2010/10/08/code-comments-tutorial-slide-puzzle-game/
