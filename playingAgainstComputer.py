import pygame
import random
import time

pygame.init()

windowW = 900
windowH = 600
screen = pygame.display.set_mode((windowW, windowH))

pygame.display.set_caption('Texas Holdem Probability')
icon = pygame.image.load('pc.png')
pygame.display.set_icon(icon)

class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        if rank == 'A':
            self.value = 14
        elif rank == 'J':
            self.value = 11
        elif rank == 'Q':
            self.value = 12
        elif rank == 'K':
            self.value = 13
        else:
            self.value = int(rank)

    def __eq__(self, other):
        return isinstance(other, Card) and self.rank == other.rank and self.suit == other.suit

    def __hash__(self):
        return hash((self.rank, self.suit))

    def __repr__(self):
        return f'{self.rank}{self.suit}'

# EDITS WERE MADE
def winner(tableCards, playerHandPlaying, opponentCards):
    playerHandTypes = {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0,
            'D': 0, 'H': 0, 'S': 0, 'C': 0}
    opponentHandTypes = {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0,
            'D': 0, 'H': 0, 'S': 0, 'C': 0}
    player = list(tableCards) + list(playerHandPlaying)
    opponent = list(tableCards) + list(opponentCards)
    pairsP = 0
    triplesP = 0
    singlesP = 0
    quadrupleP = 0
    DP = 0
    HP = 0
    SP = 0
    CP = 0 
    pairsO = 0
    triplesO = 0
    singlesO = 0
    quadrupleO = 0
    DO = 0
    HO = 0
    SO = 0
    CO = 0 
    highestsP = 0
    highestsO = 0
    straight = False
    quadNumO = 0
    quadNumP = 0
    highO = 0
    highP = 0
    for card in player:
        playerHandTypes[card.suit] = playerHandTypes.get(card.suit, 0) + 1
        playerHandTypes[card.rank] = playerHandTypes.get(card.rank, 0) + 1
    for key in playerHandTypes:
        if key in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
            if opponentHandTypes[key] != 0: highP = key 
            if playerHandTypes[key] == 2:
                pairsP += 1
                pairHP = key
            elif playerHandTypes[key] == 3:
                triplesP += 1
                highestsP = key
            elif playerHandTypes[key] == 4:
                quadrupleP += 1
                quadNumP = key
            elif playerHandTypes[key] == 1:
                singlesP += 1
                singleHP = key
        if key in ['C', 'S', 'D', 'H']:
            if key == 'D':
                DP = playerHandTypes[key]
            if key ==  'H':
                HP = playerHandTypes[key]
            if key == 'S':
                SP = playerHandTypes[key]
            if key == 'C':
                CP = playerHandTypes[key]
    for card in opponent:
        opponentHandTypes[card.suit] = opponentHandTypes.get(card.suit, 0) + 1
        opponentHandTypes[card.rank] = opponentHandTypes.get(card.rank, 0) + 1
    for key in opponentHandTypes:
        if key in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
            if opponentHandTypes[key] != 0: highO = key 
            if opponentHandTypes[key] == 2:
                pairsO += 1
                pairHO = key
            elif opponentHandTypes[key] == 3:
                triplesO += 1
                highestsO = key
            elif opponentHandTypes[key] == 4:
                quadrupleO += 1
                quadNumO = key
            elif opponentHandTypes[key] == 1:
                singlesO += 1
                singleHO = key
        if key in ['C', 'S', 'D', 'H']:
            if key == 'D':
                DO = playerHandTypes[key]
            if key ==  'H':
                HO = playerHandTypes[key]
            if key == 'S':
                SO = playerHandTypes[key]
            if key == 'C':
                CO = playerHandTypes[key]
    # if D >= 5 or H >= 5 or S >= 5 or C >= 5:
    if flush(player)[0] == True and flush(player)[1] == 14 and flush(opponent)[0] == True and flush(opponent)[1] == 14:
        return None 
    elif flush(opponent)[0] == True and flush(opponent)[1] == 14: # checks if the opponenet has a royal flush
        return False # True if the player wins, False is opponnent wins and None if they both have the same
    elif flush(player)[0] == True and flush(player)[1] == 14: # checks if the player has a royal flush
        return True
    elif flush(player)[0] == True and flush(opponent)[0] == True: # checks if both have a straight flush
        if flush(player)[1] > flush(opponent)[1]:
            return True
        elif flush(player)[1] > flush(opponent)[1]:
            False
        else: 
            return None
    elif flush(player)[0] == True:  # checks if player has a straight flush
        return True
    elif flush(opponent)[0] == True: # checks if opponent has a straight flush
        return False
    elif pairsP >= 1 and triplesP >= 1 and pairsO >= 1 and triplesO >= 1: 
        if highestP == 'A':
            return True
        elif highestO == 'A':
            return False
        else:
            return highestP > highestO
    elif quadrupleP == 1 and quadrupleO == 1: 
        if quadNumP == quadNumO:
            return None
        else:
            return quadNumP > quadNumO
    elif quadrupleP == 1: 
        return True
    elif quadrupleO == 1:
        return False
    elif (DP >= 5 or HP >= 5 or SP >= 5 or CP >= 5) and (DO >= 5 or HO >= 5 or SO >= 5 or CO >= 5): 
        if DP >= 5:
            for card in player:
                if card.suit == 'D' and card.value > highP:
                    highP = card.value      
        if HP >= 5:
            for card in player:
                if card.suit == 'H' and card.value > highP:
                    highP = card.value
        if SP >= 5:
            for card in player:
                if card.suit == 'S' and card.value > highP:
                    highP = card.value
        if CP >= 5:
            for card in player:
                if card.suit == 'S' and card.value > highP:
                    highP = card.value
        if DO >= 5:
            for card in opponent:
                if card.suit == 'D' and card.value > highO:
                    highO = card.value
        if HO >= 5:
            for card in opponent:
                if card.suit == 'H' and card.value > highO:
                    highO = card.value
        if SO >= 5:
            for card in opponent:
                if card.suit == 'S' and card.value > highO:
                    highO = card.value
        if CO >= 5:
            for card in opponent:
                if card.suit == 'C' and card.value > highO:
                    highO = card.value
        if highP == 14:
            return True
        if highO == 14:
            return False
        return highP > highO
    elif (DP >= 5 or HP >= 5 or SP >= 5 or CP >= 5): 
        return True
    elif DO >= 5 or HO >= 5 or SO >= 5 or CO >= 5:
        return False
    elif checkStraight2(player)[0] and checkStraight2(opponent)[0]: 
        return returnValue(checkStraight2(player)[1]) > returnValue(checkStraight2(opponent)[1])
    elif checkStraight2(player)[0]:
        return checkStraight2(player)[0]
    elif checkStraight2(opponent)[0]:
        return checkStraight2(opponent)[0]
    elif pairsP == 0 and triplesP >= 1 and pairsO == 0 and triplesO >= 1: 
        if highestsP == 'A':
            return True
        if highestsO == 'A':
            return False
        return returnValue(highestsP) > returnValue(highestsO)
    elif pairsP == 0 and triplesP >= 1:
        return True
    elif pairsO == 0 and triplesO >= 1:
        return False
    elif pairsP >= 2 and triplesP == 0 and pairsO >= 2 and triplesO == 0: 
        if pairHP == 'A' and pairHO == 'A':
            return None
        elif returnValue(pairHP) > returnValue(pairHO):
            return True
        else:
            return False
    elif pairsP >= 2 and triplesP == 0:
         return True
    elif pairsO >= 2 and triplesO == 0:
        return False
    elif pairsP == 1 and triplesP == 0 and pairsO == 1 and triplesO == 0:
        if returnValue(singleHP) > returnValue(singleHO):
            return True
        else:
            False
    elif pairsP == 1 and triplesP == 0:
        return True
    elif pairsO == 1 and triplesO == 0:
        return False 
    else:  
        return returnValue(highP) > returnValue(highP)

def returnValue(val):
    if val == 'A':
        return 14
    elif val == 'J':
        return 11
    elif val == 'Q':
        return 12
    elif val == 'K':
        return 13
    else:
        return int(val)

def checkStraight2(deck):
    numbers = []
    for card in deck:
        numbers.append((card.value, card.suit))
    numbers.sort()
    count = 1
    high = numbers[len(numbers)-1][0]
    previous = numbers[len(numbers)-1][0]
    for val in range(len(numbers)-2, -1,  -1): 
        if numbers[val][0] == previous:
            break
        if numbers[val][0] == previous - 1:
            count += 1
        else:
            count = 1
            high = numbers[val][0]
        previous = numbers[val][0]
        if count == 5:
            return (True, high)
    return (count >= 5, high)

def flush(deck):
    numbers = []
    for card in deck:
        numbers.append((card.value, card.suit))
    numbers.sort()
    count = 1
    previous = numbers[len(numbers)-1][0]
    previousSuit = numbers[len(numbers)-1][1]
    highest = numbers[len(numbers)-1][0]
    for val in range(len(numbers)-2, -1,  -1): 
        if numbers[val][0] == previous:
            break
        if numbers[val][0] == previous - 1:
            if numbers[val][1] == previousSuit:
                count += 1
        else:
            highest = numbers[val][0]
            count = 1
        previous = numbers[val][0]
        previousSuit = numbers[val][1]
        if count == 5:
            return (True, highest)
    return (count >= 5, highest)

def makeDeck():
    row = 0
    col = -1
    for suit in ['S', 'D', 'C', 'H']:
        for rank in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
            if row % 13 == 0:
                row = 0
                col += 1
            cards[Card(rank, suit)] = [.05 + row*(windowW/12.98),
                                    .05 + (1+row)*(windowW/12.98),
                                    120*col,
                                    120*(1+col)]
            row += 1

running = True
justStarted = True
cards = {}
playerHandPlaying = set()
tableCards = set()
opponentCards = set()
playerMoney = 500
CPUMoney = 500
gameOver = False
onTable = 0

makeDeck()
def pickCards(remaining):
    cardsPicked = set()
    while len(cardsPicked) != remaining:
        cardP = random.choice(list(cards))
        cardsPicked.add(cardP)
    return cardsPicked

def drawPlaying():
    screen.fill((0,255,150))
    playerList = list(playerHandPlaying)
    # first player card
    card = pygame.image.load(f'{playerList[0].rank}{playerList[0].suit}.png')
    card = pygame.transform.scale(card, (150, 200))
    screen.blit(card, (windowW/5.0, windowH/1.7))
    # second player card
    card = pygame.image.load(f'{playerList[1].rank}{playerList[1].suit}.png')
    card = pygame.transform.scale(card, (150, 200))
    screen.blit(card, (windowW/2.0, windowH/1.7))

    # Fold
    blueButton = pygame.image.load('blueSquare.jpg')
    blueButton = pygame.transform.scale(blueButton, (100, 50))
    screen.blit(blueButton, (windowW/1.3, windowH/1.7))

    font = pygame.font.SysFont('comicsansms', 18)
    text = font.render('Fold', True, (255,255,255))
    screen.blit(text, (windowW/1.24, windowH/1.7))

    # Check
    blueButton = pygame.image.load('blueSquare.jpg')
    blueButton = pygame.transform.scale(blueButton, (100, 50))
    screen.blit(blueButton, (windowW/1.3, windowH/1.45))

    font = pygame.font.SysFont('comicsansms', 18)
    text = font.render('Check', True, (255,255,255))
    screen.blit(text, (windowW/1.25, windowH/1.45))

    # Raise
    blueButton = pygame.image.load('blueSquare.jpg')
    blueButton = pygame.transform.scale(blueButton, (100, 50))
    screen.blit(blueButton, (windowW/1.3, windowH/1.26))

    font = pygame.font.SysFont('comicsansms', 18)
    text = font.render('Raise', True, (255,255,255))
    screen.blit(text, (windowW/1.25, windowH/1.26))


    # if not gameOver:
    if not gameOver:
        blueButton = pygame.image.load('purple_back.png')
        blueButton = pygame.transform.scale(blueButton, (100, 2*(200//3)))
        screen.blit(blueButton, (windowW/3, windowH/33))

        blueButton = pygame.image.load('purple_back.png')
        blueButton = pygame.transform.scale(blueButton, (100, 2*(200//3)))
        screen.blit(blueButton, (windowW/2.2, windowH/33))
    else:
        CPUlist = list(opponentCards)
        blueButton = pygame.image.load(f'{CPUlist[0].rank}{CPUlist[0].suit}.png')
        blueButton = pygame.transform.scale(blueButton, (100, 2*(200//3)))
        screen.blit(blueButton, (windowW/3, windowH/33))

        blueButton = pygame.image.load(f'{CPUlist[1].rank}{CPUlist[1].suit}.png')
        blueButton = pygame.transform.scale(blueButton, (100, 2*(200//3)))
        screen.blit(blueButton, (windowW/2.2, windowH/33))

def drawMoney(CPU, player, onTable):
    font = pygame.font.SysFont("comicsansms", 18)
    text = font.render(f"Opponent: ${CPU}", True, (0, 0, 0))
    screen.blit(text,(100, 30))

    font = pygame.font.SysFont("comicsansms", 18)
    text = font.render(f"Your money: ${player}", True, (0, 0, 0))
    screen.blit(text,(windowW/2 - 85, windowH - 40))

    font = pygame.font.SysFont("comicsansms", 18)
    text = font.render(f"On the Table: ${onTable}", True, (0, 0, 0))
    screen.blit(text,(windowW - 300, 30))

def fold(CPUMoney, onTable): 
    CPUMoney += onTable
    justStarted = True
    cards = {}
    playerHandPlaying = set()
    tableCards = set()
    opponentCards = set()
    gameOver = False
    onTable = 0
    return (CPUMoney, onTable, justStarted, cards, playerHandPlaying, tableCards, opponentCards, gameOver, onTable)
    

def check(): 
    if len(tableCards) < 5:
        newCards = pickCards(1)
        for card in newCards:
            tableCards.add(card)
            del cards[card]

def raiseMoney(CPUMoney, onTable, playerMoney): 
    onTable += 100
    CPUMoney -= 50
    playerMoney -= 50
    return (CPUMoney, onTable, playerMoney)

down = False
end = False
while running:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
             running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            down = True
    # time.sleep(5)
    if down and end:
        (CPUMoney, onTable, justStarted, cards, playerHandPlaying, tableCards, opponentCards, gameOver, onTable) = fold(CPUMoney, onTable)
        makeDeck()
        gameOver = False
        end = False
    if justStarted:
        playerHandPlaying = pickCards(2)
        for card in playerHandPlaying:
            del cards[card]
        opponentCards = pickCards(2)
        for card in opponentCards:
            del cards[card]
        justStarted = False
    
    drawPlaying()
    if down:
        pos = pygame.mouse.get_pos()
        if end == False:
            if 691 <= pos[0] <= 790 and 352 <= pos[1] <= 401:
                # (CPUMoney, onTable, justStarted, cards, playerHandPlaying, tableCards, opponentCards, gameOver, onTable) = fold(CPUMoney, onTable)
                # makeDeck()
                end = True
            if 691 <= pos[0] <= 790 and 414 <= pos[1] <= 462:
                check()
            if 691 <= pos[0] <= 790 and 475 <= pos[1] <= 524:
                if CPUMoney > 0 and playerMoney > 0:
                    (CPUMoney, onTable, playerMoney) = raiseMoney(CPUMoney, onTable, playerMoney)
                check()
        if len(tableCards) == 5: 
            end = True
    if end:
        gameOver = True
        whoWon = winner(tableCards, playerHandPlaying, opponentCards)
        if whoWon: #True if the player won, false if opponenet, and none if tie
            playerMoney += onTable
            onTable = 0
        if whoWon == False:
            CPUMoney += onTable
            onTable = 0
        if whoWon == None:
            CPUMoney += onTable//2
            playerMoney += onTable//2
            onTable = 0
        # clock = pygame.time.Clock()
        # clock.tick(100000)\gameOver = False

        

    count = 0
    space1 = 9.0
    space2 = 4.5
    space3 = 2.9
    space4 = 2.1
    space5 = 1.7

    for card in tableCards:
        count += 1
        if count == 1:
            spacing = space1
        if count == 2:
            spacing = space2
        if count == 3:
            spacing = space3
        if count == 4:
            spacing = space4
        if count == 5:
            spacing = space5

        card = pygame.image.load(f'{card.rank}{card.suit}.png')
        card = pygame.transform.scale(card, (150, 200))
        screen.blit(card, (windowW/spacing, windowH/4))
    
    drawMoney(CPUMoney, playerMoney, onTable)

    down = False
    pygame.display.update()
