import pygame, sys, random
from pygame.locals import *

# Create the basic game setting 
board_width = 3  # how many columns in the board
board_height = 3 # how many rows in the board
tile_size = 60
window_width = 600
window_height = 600
FPS = 30
BLANK = None

# Define the color in the game
#                 R    G    B
Black =          (  0,   0,   0)
White =          (255, 255, 255)
Bright_Blue =    (  0,  50, 255)
Dark_Turquoise = (  3,  54,  73)
Green =          (105, 176, 172)

BG_color = Dark_Turquoise
tile_color = Green
text_color = White
board_color = Bright_Blue
basic_font_size = 30

button_color = White
button_text_color = Black
message_color = White

x_margin = int((window_width - (tile_size * board_width + (board_width - 1))) / 2)
y_margin = int((window_height - (tile_size * board_height + (board_height - 1))) / 2)

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, RESET_SURF, RESET_RECT, NEW_SURF, NEW_RECT, SOLVE_SURF, SOLVE_RECT

    pygame.init()
    # To track game time
    FPSCLOCK = pygame.time.Clock() 
    # Initialize a window with given size
    DISPLAYSURF = pygame.display.set_mode((window_width, window_height))
    # Set the current window title
    pygame.display.set_caption('3X3 Slide Puzzle')
    BASICFONT = pygame.font.Font('freesansbold.ttf', basic_font_size)

    # Store the option buttons and their rectangles in OPTIONS.
    RESET_SURF, RESET_RECT = makeText('Reset',    text_color, tile_color, window_width - 200, window_height - 90)
    NEW_SURF,   NEW_RECT   = makeText('New Game', text_color, tile_color, window_width - 200, window_height - 60)
    SOLVE_SURF, SOLVE_RECT = makeText('Solution', text_color, tile_color, window_width - 200, window_height - 30)

    # Number of tile movements when the game starts
    mainBoard, solutionSeq = generate_New_Puzzle(40)
    # To solve game is remaking the board in a start state
    SOLVEDBOARD = get_StartingBoard() 
    # Store all moves made from the solved configuration in the list
    all_Moves = [] 

    # Start to loop the game 
    while True: 
        # the direction, if any, a tile should slide
        slideTo = None 
        # Display a message to user to start the game 
        msg = 'Click tile or press arrow keys to slide. '
        if mainBoard == SOLVEDBOARD:
            msg = 'Congratulation!'

        # To display the mainboard and message
        drawBoard(mainBoard, msg)

        check_Quit()
        for event in pygame.event.get(): # event handling loop
            if event.type == MOUSEBUTTONUP:
                spot_x, spot_y = clicked_spot(mainBoard, event.pos[0], event.pos[1])

                 # Check if the user clicked on an option button
                if (spot_x, spot_y) == (None, None):
                    if RESET_RECT.collidepoint(event.pos):
                        # Clicked on Reset button
                        # Reset the mainboard and clear the list, all_Moves
                        reset_Animation(mainBoard, all_Moves) 
                        all_Moves = []
                    elif NEW_RECT.collidepoint(event.pos):
                        # clicked on New Game button
                        mainBoard, solutionSeq = generate_New_Puzzle(40) 
                        all_Moves = []
                    elif SOLVE_RECT.collidepoint(event.pos):
                        reset_Animation(mainBoard, solutionSeq + all_Moves) # clicked on Solve button
                        all_Moves = []
                else:
                    # check if the clicked tile was next to the blank spot

                    blank_x, blank_y = get_Blank(mainBoard)
                    if spot_x == blank_x + 1 and spot_y == blank_y:
                        slideTo = LEFT
                    elif spot_x == blank_x - 1 and spot_y == blank_y:
                        slideTo = RIGHT
                    elif spot_x == blank_x and spot_y == blank_y + 1:
                        slideTo = UP
                    elif spot_x == blank_x and spot_y == blank_y - 1:
                        slideTo = DOWN

            # check if the user pressed a key to slide a tile
            elif event.type == KEYUP:
                if event.key in (K_LEFT, K_a) and valid_Move(mainBoard, LEFT):
                    slideTo = LEFT
                elif event.key in (K_RIGHT, K_d) and valid_Move(mainBoard, RIGHT):
                    slideTo = RIGHT
                elif event.key in (K_UP, K_w) and valid_Move(mainBoard, UP):
                    slideTo = UP
                elif event.key in (K_DOWN, K_s) and valid_Move(mainBoard, DOWN):
                    slideTo = DOWN

        if slideTo:
            # animation of tiles on mainboard  
            slide_Animation(mainBoard, slideTo, 'Click tile or press arrow keys to slide.', 8) # show slide on screen
            make_Move(mainBoard, slideTo)
            # Add the movements into all_moves
            all_Moves.append(slideTo) # record the slide
        pygame.display.update()
        # Update the clock
        FPSCLOCK.tick(FPS)


# To quit the game
def terminate():
    pygame.quit()
    sys.exit()


def check_Quit():
    # Event to terminate the game in pygame
    # Get all the QUIT events
    for event in pygame.event.get(QUIT): 
        # Terminate if any QUIT events are present
        terminate() 

    # Get all the KEYUP events
    for event in pygame.event.get(KEYUP): 
        # Use Esc key to quit the game
        if event.key == K_ESCAPE:
            terminate() 
        # Post a new keyup event in queue
        # Put the other KEYUP event objects back
        pygame.event.post(event) 


# Return a new board with tiles in the solved state
# For example, if board_width and board_height are both 3, this function returns [[1, 4, 7], [2, 5, 8], [3, 6, BLANK]]
def get_StartingBoard():
    counter = 1
    board = []
    for x in range(board_width):
        column = []
        for y in range(board_height):
            column.append(counter)
            counter += board_width
        board.append(column)
        counter -= board_width * (board_height - 1) + board_width - 1

    board[board_width-1][board_height-1] = BLANK
    return board

# Return the x and y of board coordinates of the blank space.
def get_Blank(board):
    for x in range(board_width):
        for y in range(board_height):
            if board[x][y] == BLANK:
                return (x, y)


# This function only define 4 moves in the game
def make_Move(board, move):
    blank_x, blank_y = get_Blank(board)

    if move == UP:
        board[blank_x][blank_y], board[blank_x][blank_y + 1] = board[blank_x][blank_y + 1], board[blank_x][blank_y]
    elif move == DOWN:
        board[blank_x][blank_y], board[blank_x][blank_y - 1] = board[blank_x][blank_y - 1], board[blank_x][blank_y]
    elif move == LEFT:
        board[blank_x][blank_y], board[blank_x + 1][blank_y] = board[blank_x + 1][blank_y], board[blank_x][blank_y]
    elif move == RIGHT:
        board[blank_x][blank_y], board[blank_x - 1][blank_y] = board[blank_x - 1][blank_y], board[blank_x][blank_y]


# This function checks whether the move is valid by coordination
def valid_Move(board, move):
    blank_x, blank_y = get_Blank(board)
    return (move == UP and blank_y != len(board[0]) - 1) or \
           (move == DOWN and blank_y != 0) or \
           (move == LEFT and blank_x != len(board) - 1) or \
           (move == RIGHT and blank_x != 0)


# This function starts with 4 basic movements
def random_Move(board, lastMove=None):
    
    validMoves = [UP, DOWN, LEFT, RIGHT]

    # Remove moves from the list as they are invalid
    # For example, if the last move is up, then remove the opposite direction (down)
    if lastMove == UP or not valid_Move(board, DOWN):
        validMoves.remove(DOWN)
    if lastMove == DOWN or not valid_Move(board, UP):
        validMoves.remove(UP)
    if lastMove == LEFT or not valid_Move(board, RIGHT):
        validMoves.remove(RIGHT)
    if lastMove == RIGHT or not valid_Move(board, LEFT):
        validMoves.remove(LEFT)

    # Return a random move from the list of remaining moves
    return random.choice(validMoves)


def get_Left_Top_Of_Tile(tileX, tileY):
    left = x_margin + (tileX * tile_size) + (tileX - 1)
    top = y_margin + (tileY * tile_size) + (tileY - 1)
    return (left, top)

# From the x & y pixel coordinates, get the x & y board coordinates
def clicked_spot(board, x, y):
    
    for tileX in range(len(board)):
        for tileY in range(len(board[0])):
            left, top = get_Left_Top_Of_Tile(tileX, tileY)
            tileRect = pygame.Rect(left, top, tile_size, tile_size)
            if tileRect.collidepoint(x, y):
                return (tileX, tileY)
    return (None, None)


# draw a tile at board coordinates tile_X and tile_Y, optionally a few pixels over (determined by adjx and adjy)
def draw_Tile(tilex, tiley, number, adjx=0, adjy=0):

    left, top = get_Left_Top_Of_Tile(tilex, tiley)
    pygame.draw.rect(DISPLAYSURF, tile_color, (left + adjx, top + adjy, tile_size, tile_size))
    textSurf = BASICFONT.render(str(number), True, text_color)
    textRect = textSurf.get_rect()
    textRect.center = left + int(tile_size / 2) + adjx, top + int(tile_size / 2) + adjy
    DISPLAYSURF.blit(textSurf, textRect)


# To create the Surface and Rect objects for some text
def makeText(text, color, BG_color, top, left):
   
    textSurf = BASICFONT.render(text, True, color, BG_color)
    textRect = textSurf.get_rect()
    textRect.topleft = (top, left)
    return (textSurf, textRect)


# Fill background color of the game with BG_color variable 
def drawBoard(board, message):
    DISPLAYSURF.fill(BG_color)
    if message:
        textSurf, textRect = makeText(message, message_color, BG_color, 5, 5)
        DISPLAYSURF.blit(textSurf, textRect)

    for tilex in range(len(board)):
        for tiley in range(len(board[0])):
            if board[tilex][tiley]:
                draw_Tile(tilex, tiley, board[tilex][tiley])

    left, top = get_Left_Top_Of_Tile(0, 0)
    width = board_width * tile_size
    height = board_height * tile_size
    pygame.draw.rect(DISPLAYSURF, board_color, (left - 5, top - 5, width + 11, height + 11), 4)

    DISPLAYSURF.blit(RESET_SURF, RESET_RECT)
    DISPLAYSURF.blit(NEW_SURF, NEW_RECT)
    DISPLAYSURF.blit(SOLVE_SURF, SOLVE_RECT)


# This function only demonstrate the sliding animation
def slide_Animation(board, direction, message, animationSpeed):

    blank_x, blank_y = get_Blank(board)
    if direction == UP:
        movex = blank_x
        movey = blank_y + 1
    elif direction == DOWN:
        movex = blank_x
        movey = blank_y - 1
    elif direction == LEFT:
        movex = blank_x + 1
        movey = blank_y
    elif direction == RIGHT:
        movex = blank_x - 1
        movey = blank_y

    # Prepare the base surface
    drawBoard(board, message)
    baseSurf = DISPLAYSURF.copy()
    # Draw a blank space over the moving tile on the baseSurf Surface.
    moveLeft, moveTop = get_Left_Top_Of_Tile(movex, movey)
    pygame.draw.rect(baseSurf, BG_color, (moveLeft, moveTop, tile_size, tile_size))

    # Animate the tile sliding over
    for i in range(0, tile_size, animationSpeed):
        check_Quit()
        DISPLAYSURF.blit(baseSurf, (0, 0))
        if direction == UP:
            draw_Tile(movex, movey, board[movex][movey], 0, -i)
        if direction == DOWN:
            draw_Tile(movex, movey, board[movex][movey], 0, i)
        if direction == LEFT:
            draw_Tile(movex, movey, board[movex][movey], -i, 0)
        if direction == RIGHT:
            draw_Tile(movex, movey, board[movex][movey], i, 0)

        pygame.display.update()
        FPSCLOCK.tick(FPS)


# From a starting configuration, make numSlides number of moves (and animate these moves).
def generate_New_Puzzle(numSlides):

    sequence = []
    board = get_StartingBoard()
    drawBoard(board, '')
    pygame.display.update()
    # Pause 500 milliseconds for effect
    pygame.time.wait(500) 
    lastMove = None
    for i in range(numSlides):
        move = random_Move(board, lastMove)
        slide_Animation(board, move, 'Generating new puzzle...', animationSpeed=int(tile_size / 3))
        make_Move(board, move)
        sequence.append(move)
        lastMove = move
    return (board, sequence)


# Make all of the moves in all_Moves in reverse
def reset_Animation(board, all_Moves):
 
    revAllMoves = all_Moves[:] 
    revAllMoves.reverse()

    for move in revAllMoves:
        if move == UP:
            oppositeMove = DOWN
        elif move == DOWN:
            oppositeMove = UP
        elif move == RIGHT:
            oppositeMove = LEFT
        elif move == LEFT:
            oppositeMove = RIGHT
        slide_Animation(board, oppositeMove, '', animationSpeed=int(tile_size / 2))
        make_Move(board, oppositeMove)

# Creating a new module and execute it as the main program, if condition satisfies then the function main() gets called
if __name__ == '__main__':
    main()
