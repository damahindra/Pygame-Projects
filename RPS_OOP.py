import pygame
import random

class Choice :
    def __init__(self, name) :
        self.name = name
        self.isPicked = False
    # setter and getter
    def setName(self, name) :
        self.name = name
    def getName(self) :
        return self.name

class States :
    def __init__(self) :
        self.state = False
    # setter and getter
    def setState(self, state) :
        self.state = state
    def getState(self) :
        return self.state

rock = Choice("rock")
paper = Choice("paper")
scissors = Choice("scissors")

choices = [scissors, rock, paper]

# font handling
white = (255, 255, 255)
yellow = (255, 204, 55)

def pixelFont(size) :
    font = pygame.font.Font("D:\Coding_VSCODE\PYTHON\com\pygame\Assets\Symtext.ttf", size)
    return font

def write(text, font, textColor, x, y) :
    image = font.render(text, True, textColor)
    screen.blit(image, (x, y)) 

# starting screen
def startScreen() :
    screen.fill(SCREEN_COLOR)
    write("ROCK PAPER SCISSORS", pixelFont(40), white, 150, 250)
    write("Press SPACE to Choose", pixelFont(20), white, 270, 350)

# choosing screen
def chooseScreen() :
    screen.fill(SCREEN_COLOR)
    write("PRESS UP OR DOWN TO CHOOSE", pixelFont(30), white, 140, 270)

rightArrow = ">"
leftArrow = "<"

# logic
def cont(turn) :
    if turn == 1:
        write("Press ENTER to Continue", pixelFont(20), white, 245, 500)
    elif turn == 2 :
        write("ENTER : COMPUTER'S TURN", pixelFont(20), white, 245, 500)

def choose(playerChoice) :
    if playerChoice is not None :
        if playerChoice == rock :
            screen.fill(SCREEN_COLOR)
            write(rightArrow + " " + playerChoice.getName() + " " + leftArrow, pixelFont(50), white, 285, 250)
            cont(1)
        elif playerChoice == paper :
            screen.fill(SCREEN_COLOR)
            write(rightArrow + " " + playerChoice.getName() + " " + leftArrow, pixelFont(50), white, 265, 250)
            cont(1)
        elif playerChoice == scissors :
            screen.fill(SCREEN_COLOR)
            write(rightArrow + " " + playerChoice.getName() + " " + leftArrow, pixelFont(50), white, 220, 250)
            cont(1)

def chosenScreen(playerChoice) :
    if playerChoice == rock :
        screen.fill(SCREEN_COLOR)
        write("YOU CHOSE " + playerChoice.getName() + "!", pixelFont(50), white, 160, 250)
        cont(2)
    elif playerChoice == paper :
        screen.fill(SCREEN_COLOR)
        write("YOU CHOSE " + playerChoice.getName() + "!", pixelFont(50), white, 140, 250)
        cont(2)
    elif playerChoice == scissors :
        screen.fill(SCREEN_COLOR)
        write("YOU CHOSE " + playerChoice.getName() + "!", pixelFont(50), white, 95, 250)
        cont(2)

def computerChoose(computerChoice) :
    if computerChoice == rock :
        screen.fill(SCREEN_COLOR)
        write("THE COMPUTER CHOSE " + computerChoice.getName() + "!", pixelFont(30), white, 160, 150)
    elif computerChoice == paper :
        screen.fill(SCREEN_COLOR)
        write("THE COMPUTER CHOSE " + computerChoice.getName() + "!", pixelFont(30), white, 150, 150)
    elif computerChoice == scissors :
        screen.fill(SCREEN_COLOR)
        write("THE COMPUTER CHOSE " + computerChoice.getName() + "!", pixelFont(30), white, 120, 150)

def winOrLose() :
    write("press esc to go again", pixelFont(15), white, 305, 550)
    if (playerChoice == rock and computerChoice == scissors) or (playerChoice == scissors and computerChoice == paper) or (playerChoice == paper and computerChoice == rock) :
        write("+ YOU WIN +" , pixelFont(50), yellow, 250, 250)
    elif playerChoice == computerChoice :
        write("= IT'S A DRAW =", pixelFont(50), yellow, 190, 250)
    else :
        write("- YOU LOSE -", pixelFont(50), yellow, 225, 250)

pygame.init()

WIDTH = 800
HEIGHT = 600

SCREEN_COLOR = (138,43,226)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Rock Paper Scissors!")

index = 0

# states
pressSpace_start = States()
pressDown_choose = States()
pressUp_choose = States()
pressEnter_choose = States()
pressEnter_comp = States()

ENTER_CLICKED = 0

# player and computer choice
playerChoice = None
computerChoice = None

running = True

while running :
    if not pressSpace_start.getState() :
        startScreen()
    else :
        chooseScreen()
        if pressDown_choose.getState() or pressUp_choose.getState():
            choose(playerChoice)
        if pressEnter_choose.getState() :
            chosenScreen(playerChoice)
        if pressEnter_comp.getState() :
            computerChoose(computerChoice)
            winOrLose()

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False
        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE :
                pressSpace_start.setState(True)
            elif event.key == pygame.K_DOWN :
                if pressEnter_choose.getState() :
                    pass
                else :
                    if index == 2 :
                        index = -1
                    index += 1
                    current = choices[index]
                    playerChoice = current
                    pressDown_choose.setState(True)
            elif event.key == pygame.K_UP :
                if pressEnter_choose.getState() :
                    pass
                else :
                    index -= 1
                    if index < 0 :
                        index = 2
                    current = choices[index]
                    playerChoice = current
                    pressUp_choose.setState(True)
            elif event.key == pygame.K_RETURN :
                if pressEnter_choose.getState() :
                    if ENTER_CLICKED == 0 :
                        computerChoice = random.choice(choices)
                        pressEnter_comp.setState(True)
                        ENTER_CLICKED += 1
                pressEnter_choose.setState(True)
            elif event.key == pygame.K_ESCAPE :
                pressSpace_start.setState(False)
                pressDown_choose.setState(False)
                pressUp_choose.setState(False)
                pressEnter_choose.setState(False)
                pressEnter_comp.setState(False)
                ENTER_CLICKED = 0

                

    pygame.display.update()

pygame.quit()
