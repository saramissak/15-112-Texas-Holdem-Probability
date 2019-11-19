import pygame

pygame.init()

windowW = 900
windowH = 600
screen = pygame.display.set_mode((windowW, windowH))

pygame.display.set_caption('Texas Holdem Probability')
icon = pygame.image.load('pc.png')
pygame.display.set_icon(icon)

def initial():
    screen.fill((0,255,150))
    # text on the screen
    font = pygame.font.SysFont("comicsansms", 36)
    text = font.render("Welcome to Texas Holdem Probability", True, (0, 0, 0))
    # cool cards image in the middle of the screen
    bgImage = pygame.image.load('backgroundimage.png')
    bgImage = pygame.transform.scale(bgImage, (600, 450))
    screen.blit(bgImage, (windowW//7, windowH//6))
    screen.blit(text,(100, 10))
    # click here image
    click = pygame.image.load('clickHere.png')
    click = pygame.transform.scale(click, (200, 150))
    screen.blit(click, (windowW/2.5, windowH/1.4))

def currentTableScreen(): 
    screen.fill((0,255,150))
    # first in hand
    hand1 = pygame.image.load('outline.png')
    hand1 = pygame.transform.scale(hand1, (150, 200))
    screen.blit(hand1, (windowW/5.0, windowH/1.7))
    # second in hand
    hand2 = pygame.image.load('outline.png')
    hand2 = pygame.transform.scale(hand2, (150, 200))
    screen.blit(hand2, (windowW/2.5, windowH/1.7))

    # first card on table
    table1 = pygame.image.load('outline.png')
    table1 = pygame.transform.scale(table1, (150, 200))
    screen.blit(table1, (windowW/19, windowH/9))
    # second card on table
    table2 = pygame.image.load('outline.png')
    table2 = pygame.transform.scale(table2, (150, 200))
    screen.blit(table2, (windowW/4.2, windowH/9))
    # third card on table
    table3 = pygame.image.load('outline.png')
    table3 = pygame.transform.scale(table3, (150, 200))
    screen.blit(table3, (windowW/2.35, windowH/9))
    # fourth card on table
    hand4 = pygame.image.load('outline.png')
    hand4 = pygame.transform.scale(hand4, (150, 200))
    screen.blit(hand4, (windowW/1.64, windowH/9))
    # fifth card on table
    hand5 = pygame.image.load('outline.png')
    hand5 = pygame.transform.scale(hand5, (150, 200))
    screen.blit(hand5, (windowW/1.26, windowH/9))

    # box with probabilities
    probBox = pygame.image.load('squareProbBox.png')
    probBox = pygame.transform.scale(probBox, (400, 280))
    screen.blit(probBox, (windowW/1.7, windowH/1.9))

def makeDeck():
    row = 0
    col = -1
    for suit in ['S', 'D', 'C', 'H']:
        for rank in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
            if row % 13 == 0:
                row = 0
                col += 1
            cards[f'{rank}{suit}'] = [.05 + row*(windowW/12.98),
                                    .05 + (1+row)*(windowW/12.98),
                                    120*col,
                                    120*(1+col)]
            row += 1

def cardsToPickFrom(): 
    row = 0
    col = -1
    screen.fill((0,255,150))
    for suit in ['S', 'D', 'C', 'H']:
        for rank in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
            if row % 13 == 0:
                row = 0
                col += 1
            if f'{suit}{rank}' in playerHandCord: 
                card = pygame.image.load('outline.png')
                card = pygame.transform.scale(card, (65, 115))
                screen.blit(card, (.05 + row*(windowW/12.98), 120*col))
            else:
                card = pygame.image.load(f'{rank}{suit}.png')
                card = pygame.transform.scale(card, (65, 115))
                screen.blit(card, (.05 + row*(windowW/12.98), 120*col))
                
            row += 1

def royalFlush(): pass

def straightFlush(): pass

def fourOfAKind(): pass

def fullHouse():
    pairs = 0
    triples = 0
    single = 0
    for key in playerHand:
        if key in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
            if playerHand[key] ==2:
                pairs += 1
            elif playerHand[key] == 3:
                triples += 1
            elif playerHand[key] == 1:
                single += 1
    if pairs == 1 and triples == 1: 
        return 100
    elif (pairs == 1 and triples == 0 and singles == 3) or (pairs == 0 and triples == 1 and singles == 2): 
        return 0
    # elif 
    
def flush(): pass

def straight(): pass

def threeOfAKind(): 
    pairs = 0
    triples = 0
    single = 0
    for key in playerHand:
        if key in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
            if playerHand[key] == 2:
                pairs += 1
            elif playerHand[key] == 3:
                triples += 1
            elif playerHand[key] == 1:
                single += 1
    if len(cards) == 7 and triple == 1 and pairs == 0:
        return 100
    elif len(cards) == 6 and triple == 1 and pairs == 1:
        # calculate 1 / 46 -> probs not getting a full house and getting a triple
        return 0
    elif len(cards) == 6 and triple == 1:
        pass

def twoPair(): 
    pairs = 0
    triples = 0
    single = 0
    for key in playerHand:
        if key in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
            if playerHand[key] == 2:
                pairs += 1
            elif playerHand[key] == 3:
                triples += 1
            elif playerHand[key] == 1:
                single += 1
    if triple == 0 and single == 0 and pairs == 1: # GO BACK BECAUSE NUMBER OF CARDS IS 7 NOT 5
        return 100

def onePair(): 
    pairs = 0
    triples = 0
    single = 0
    for key in playerHand:
        if key in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
            if playerHand[key] == 2:
                pairs += 1
            elif playerHand[key] == 3:
                triples += 1
            elif playerHand[key] == 1:
                single += 1
    if triple == 0 and pairs == 0: # GO BACK BECAUSE NUMBER OF CARDS IS 7 NOT 5
        return 100
    else:
        return 0

def highCard(): 
    pairs = 0
    triples = 0
    single = 0
    D = 0
    S = 0
    H = 0
    C = 0
    for key in playerHand:
        if key in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'D', 'H', 'S', 'C']:
            if playerHand[key] == 2:
                pairs += 1
            elif playerHand[key] == 3:
                triples += 1
            elif playerHand[key] == 1:
                single += 1
            elif playerHand[key] == 'D':
                D += 1
            elif playerHand[key] == 'H': 
                H +=1
            elif playerHand[key] == 'S':
                S += 1
            elif playerHand[key] == 'C':
                C += 1
    if pairs == 0 and triples == 0 and D < 5 and C < 5 and H < 5 and S < 5 and singles != 0: # GO BACK BECAUSE NUMBER OF CARDS IS 7 NOT 5
        return 100
    else:
        return 0
    

running = True
initalScreen = True
tableScreen = False
cardScreen = False
cards = {}
playerHandCord = {}
playerHand = {}
nextScreen = True


makeDeck()
while running:
    pos = (-50, -20)
    # just code to exit game
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
             running = False
    # runs the welcome screen if the boolean is true (which it is initally, but doesnt turn true again afterwards)
    if initalScreen:
        initial()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if (332 < pos[0] < 505 and 461 < pos[1] < 544):
                initalScreen = False
                tableScreen = True
        pygame.display.update()

    elif tableScreen:
        enterClicked = False
        currentTableScreen()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if (48 < pos[0] < 195 and 67 < pos[1] < 262): # these are the positions of the first blank card
                print(playerHandCord)
                # pygame.display.flip()
                print('A', pos)
                # pygame.time.wait(100)
                # this is where it changes screens
                tableScreen = False
                cardScreen = True
        pygame.display.update()
        
    if cardScreen:
        cardsToPickFrom()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print('B', pos)
            for key in cards:
                if (cards[key][0] < pos[0] < cards[key][1] and cards[key][2] < pos[1] < cards[key][3]):
                    # the next four lines are just to add the card to a dictionary of cards that are picked already
                    playerHandCord[key] = playerHandCord.get(key, cards[key])
                    playerHand[key[-1]] = playerHand.get(key[-1], 0) + 1
                    playerHand[key[0:-1]] = playerHand.get(key[0:-1], 0) + 1
                    del cards[key]
                    print(playerHandCord) 
                    # this is where it changes screens
                    tableScreen = True
                    cardScreen = False 
                    print(key)
                    break
                
        pygame.display.flip()
        # pygame.time.wait(100)
        pygame.display.update()

    

