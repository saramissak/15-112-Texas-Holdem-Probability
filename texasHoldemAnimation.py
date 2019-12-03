import pygame
import random
# from playingAgainstComputer import play
# from playingAgainstComputer import *

pygame.init()

windowW = 900
windowH = 600
screen = pygame.display.set_mode((windowW, windowH))

# image taken from: http://pngimg.com/download/8460
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

def pickCards(remaining):
    cardsPicked = set()
    while len(cardsPicked) != remaining:
        cardP = random.choice(list(cards))
        cardsPicked.add(cardP)
    return cardsPicked

def trialSucceeds(deck):
    handTypes = {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0,
            'D': 0, 'H': 0, 'S': 0, 'C': 0}
    cardsPicked = pickCards(7 - len(deck))
    cardsDown = list(cardsPicked) + list(deck)
    pairs = 0
    triples = 0
    singles = 0
    quadruple = 0
    D = 0
    H = 0
    S = 0
    C = 0 
    straight = False
    for card in cardsDown:
        handTypes[card.suit] = handTypes.get(card.suit, 0) + 1
        handTypes[card.rank] = handTypes.get(card.rank, 0) + 1
    for key in handTypes:
        if key in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
            if handTypes[key] == 2:
                pairs += 1
            elif handTypes[key] == 3:
                triples += 1
            elif handTypes[key] == 4:
                quadruple += 1
            elif handTypes[key] == 1:
                singles += 1
        if key in ['C', 'S', 'D', 'H']:
            if key == 'D':
                D = handTypes[key]
            if key ==  'H':
                H = handTypes[key]
            if key == 'S':
                S = handTypes[key]
            if key == 'C':
                C = handTypes[key]
    # if D >= 5 or H >= 5 or S >= 5 or C >= 5:
    if flush(cardsDown)[0] == True and flush(cardsDown)[1] == 14: return 'Royal Flush'
    elif flush(cardsDown)[0] == True: return 'Straight Flush'
    elif pairs >= 1 and triples >= 1: return 'Full House'
    elif quadruple == 1: return "Four Of A Kind"
    elif D >= 5 or H >= 5 or S >= 5 or C >= 5: return "Flush"
    elif checkStraight(cardsDown): return 'Straight'
    elif pairs == 0 and triples >= 1: return 'Triple'
    elif pairs >= 2 and triples == 0: return 'Two pair'
    elif pairs == 1 and triples == 0: return 'One pair'
    else:  return 'No Pair'

def checkStraight(deck):
    numbers = []
    for card in deck:
        numbers.append((card.value, card.suit))
    numbers.sort()
    count = 1
    previous = numbers[len(numbers)-1][0]
    for val in range(len(numbers)-2, -1,  -1): 
        if numbers[val][0] == previous:
            break
        if numbers[val][0] == previous - 1:
            count += 1
        else:
            count = 1
        previous = numbers[val][0]
        if count == 5:
            return True
    return (count >= 5)

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
    
def handOdds(trials, deck):
    royalFlush = 0
    straightFlush = 0
    fullHouse = 0
    fourOfAKind = 0
    flush = 0
    straight = 0
    triple = 0
    twoPair = 0
    onePair = 0
    noPair = 0
    for trial in range(trials):
        if trialSucceeds(deck) == 'Royal Flush':
            royalFlush += 1
        if trialSucceeds(deck) == 'Straight Flush':
            straightFlush += 1
        if trialSucceeds(deck) == 'Full House':
            fullHouse += 1 
        if trialSucceeds(deck) == "Four Of A Kind":
            fourOfAKind += 1
        if trialSucceeds(deck) == "Flush":
            flush += 1 
        if trialSucceeds(deck) == 'Straight':
            straight += 1
        if trialSucceeds(deck) == 'Triple':
            triple += 1 
        if trialSucceeds(deck) == 'Two pair':
            twoPair +=1 
        if trialSucceeds(deck) == 'One pair':
            onePair += 1
        if trialSucceeds(deck) == 'No Pair':
            noPair += 1
    return (royalFlush/trials, straightFlush/trials, fullHouse/trials,
    fourOfAKind/trials, flush/trials, straight/trials, triple/trials,
    twoPair/trials, onePair/trials, noPair/trials)

def initial():
    screen.fill((0,255,150))
    # text on the screen
    font = pygame.font.SysFont("comicsansms", 36)
    text = font.render("Welcome to Texas Holdem Probability", True, (0, 0, 0))
    # cool cards image in the middle of the screen

    # image taken from: http://pngimg.com/download/8460
    bgImage = pygame.image.load('backgroundimage.png')
    bgImage = pygame.transform.scale(bgImage, (600, 450))
    screen.blit(bgImage, (windowW//7, windowH//6))
    screen.blit(text,(100, 10))
    # click here image
    # image taken from: https://www.kc-beauty.com/salon-services
    click = pygame.image.load('clickHere.png')
    click = pygame.transform.scale(click, (200, 150))
    screen.blit(click, (windowW/2.5, windowH/1.4))

def currentTableScreen(): 
    screen.fill((0,255,150))
    playerList = []
    for key in playerHandCord:
        playerList.append(key)
    if len(playerList) >= 1:
        # image taken from: http://acbl.mybigcommerce.com/52-playing-cards/
        card = pygame.image.load(f'{playerList[0].rank}{playerList[0].suit}.png')
        card = pygame.transform.scale(card, (150, 200))
        screen.blit(card, (windowW/5.0, windowH/1.7))
    else: 
        # first in hand   
        # image taken from: www.vonsheatingandair.com/images/Dotted%20Line%20Coupon.png 
        hand1 = pygame.image.load('outline.png')
        hand1 = pygame.transform.scale(hand1, (150, 200))
        screen.blit(hand1, (windowW/5.0, windowH/1.7))
    if len(playerList) >= 2:
        # image taken from: http://acbl.mybigcommerce.com/52-playing-cards/
        hand2 = pygame.image.load(f'{playerList[1].rank}{playerList[1].suit}.png')
        hand2 = pygame.transform.scale(hand2, (150, 200))
        screen.blit(hand2, (windowW/2.5, windowH/1.7))
    else: 
        # second in hand
        # image taken from: www.vonsheatingandair.com/images/Dotted%20Line%20Coupon.png
        hand2 = pygame.image.load('outline.png')
        hand2 = pygame.transform.scale(hand2, (150, 200))
        screen.blit(hand2, (windowW/2.5, windowH/1.7))
    if len(playerList) >= 3:
        # image taken from: http://acbl.mybigcommerce.com/52-playing-cards/
        table1 = pygame.image.load(f'{playerList[2].rank}{playerList[2].suit}.png')
        table1 = pygame.transform.scale(table1, (150, 200))
        screen.blit(table1, (windowW/19, windowH/9))
    else:
        # first card on table
        # image taken from: www.vonsheatingandair.com/images/Dotted%20Line%20Coupon.png
        table1 = pygame.image.load('outline.png')
        table1 = pygame.transform.scale(table1, (150, 200))
        screen.blit(table1, (windowW/19, windowH/9))

    if len(playerList) >= 4:
        # image taken from: http://acbl.mybigcommerce.com/52-playing-cards/
        table2 = pygame.image.load(f'{playerList[3].rank}{playerList[3].suit}.png')
        table2 = pygame.transform.scale(table2, (150, 200))
        screen.blit(table2, (windowW/4.2, windowH/9))
    else:
        # second card on table
        # image taken from: www.vonsheatingandair.com/images/Dotted%20Line%20Coupon.png
        table2 = pygame.image.load('outline.png')
        table2 = pygame.transform.scale(table2, (150, 200))
        screen.blit(table2, (windowW/4.2, windowH/9))

    if len(playerList) >= 5: 
        # image taken from: http://acbl.mybigcommerce.com/52-playing-cards/
        table3 = pygame.image.load(f'{playerList[4].rank}{playerList[4].suit}.png')
        table3 = pygame.transform.scale(table3, (150, 200))
        screen.blit(table3, (windowW/2.35, windowH/9))
    else:
        # third card on table
        # image taken from: www.vonsheatingandair.com/images/Dotted%20Line%20Coupon.png
        table3 = pygame.image.load('outline.png')
        table3 = pygame.transform.scale(table3, (150, 200))
        screen.blit(table3, (windowW/2.35, windowH/9))
    if len(playerList) >= 6:
        # image taken from: http://acbl.mybigcommerce.com/52-playing-cards/
        hand4 = pygame.image.load(f'{playerList[5].rank}{playerList[5].suit}.png')
        hand4 = pygame.transform.scale(hand4, (150, 200))
        screen.blit(hand4, (windowW/1.64, windowH/9))
    else:
        # fourth card on table
        # image taken from: www.vonsheatingandair.com/images/Dotted%20Line%20Coupon.png
        hand4 = pygame.image.load('outline.png')
        hand4 = pygame.transform.scale(hand4, (150, 200))
        screen.blit(hand4, (windowW/1.64, windowH/9))
    if len(playerList) >= 7:
        # image taken from: http://acbl.mybigcommerce.com/52-playing-cards/
        hand5 = pygame.image.load(f'{playerList[6].rank}{playerList[6].suit}.png')
        hand5 = pygame.transform.scale(hand5, (150, 200))
        screen.blit(hand5, (windowW/1.26, windowH/9))
    else:
        # fifth card on table
        # image taken from: www.vonsheatingandair.com/images/Dotted%20Line%20Coupon.png
        hand5 = pygame.image.load('outline.png')
        hand5 = pygame.transform.scale(hand5, (150, 200))
        screen.blit(hand5, (windowW/1.26, windowH/9))
    # box with probabilities
    # image taken from: http://www.adelarahayucv.com/images/login_box.png
    probBox = pygame.image.load('squareProbBox.png')
    probBox = pygame.transform.scale(probBox, (400, 300))
    screen.blit(probBox, (windowW/1.7, windowH/1.9))
    # probability text
    font = pygame.font.SysFont('comicsansms', 14)
    text = font.render(f"Royal Flush: %.02f" % (royalFlush * 100), True, (0,0,0))
    screen.blit(text, (windowW/1.5, windowH/1.62))

    font = pygame.font.SysFont('comicsansms', 14)
    text = font.render(f"Straight Flush: %.02f" % (straightFlush * 100), True, (0,0,0))
    screen.blit(text, (windowW/1.5, windowH/1.54))

    font = pygame.font.SysFont('comicsansms', 14)
    text = font.render(f"Four of a Kind: %.02f" % (fourOfAKind * 100), True, (0,0,0))

    screen.blit(text, (windowW/1.5, windowH/1.47))

    font = pygame.font.SysFont('comicsansms', 14)
    text = font.render(f"Full House %.02f" % (fullHouse * 100), True, (0,0,0))
    screen.blit(text, (windowW/1.5, windowH/1.41))

    font = pygame.font.SysFont('comicsansms', 14)
    text = font.render(f"Flush: %.02f" % (flushHand * 100), True, (0,0,0))
    screen.blit(text, (windowW/1.5, windowH/1.345))

    font = pygame.font.SysFont('comicsansms', 14)
    text = font.render(f"Straight: %.02f" % (straight * 100), True, (0,0,0))
    screen.blit(text, (windowW/1.5, windowH/1.29))

    font = pygame.font.SysFont('comicsansms', 14)
    text = font.render(f"Triple: %.02f" % (triple * 100), True, (0,0,0))
    screen.blit(text, (windowW/1.5, windowH/1.24))

    font = pygame.font.SysFont('comicsansms', 14)
    text = font.render(f"Two Pair: %.02f" % (twoPair * 100), True, (0,0,0))
    screen.blit(text, (windowW/1.5, windowH/1.19))

    font = pygame.font.SysFont('comicsansms', 14)
    text = font.render(f"One Pair: %.02f" % (onePair * 100), True, (0,0,0))
    screen.blit(text, (windowW/1.5, windowH/1.15))

    font = pygame.font.SysFont('comicsansms', 14)
    text = font.render(f"No Pair: %.02f" % (noPair * 100), True, (0,0,0))
    screen.blit(text, (windowW/1.5, windowH/1.11))

    # next card button
    # image taken from: http://www.clker.com/cliparts/m/S/m/C/X/Q/black-square-rounded-corners-hi.png
    rectangle = pygame.image.load('roundSquare.png')
    rectangle = pygame.transform.scale(rectangle, (windowW//5, windowH//7))
    screen.blit(rectangle, (windowW/100, windowH/1.483))
    # next card button text
    font = pygame.font.SysFont('comicsansms', 28)
    text = font.render("Next Card", 56, (255, 255, 255))
    screen.blit(text, (windowW/32, windowH/1.42))

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

def cardsToPickFrom(): 
    row = 0
    col = -1
    screen.fill((0,255,150))
    for suit in ['S', 'D', 'C', 'H']:
        for rank in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
            if row % 13 == 0:
                row = 0
                col += 1
            if Card(rank, suit) in playerHandCord: 
                # image taken from: www.vonsheatingandair.com/images/Dotted%20Line%20Coupon.png
                card = pygame.image.load('outline.png')
                card = pygame.transform.scale(card, (65, 115))
                screen.blit(card, (.05 + row*(windowW/12.98), 120*col))
            else:
                # image taken from: http://acbl.mybigcommerce.com/52-playing-cards/
                card = pygame.image.load(f'{rank}{suit}.png')
                card = pygame.transform.scale(card, (65, 115))
                screen.blit(card, (.05 + row*(windowW/12.98), 120*col))
                
            row += 1

def pickingScreen():
    screen.fill((0,255,150))
    # Question
    font = pygame.font.SysFont('comicsansms', 36)
    text = font.render("Would you like the app to run faster ", 56, (0,0,0))
    screen.blit(text, (150, 25))
    font = pygame.font.SysFont('comicsansms', 36)
    text = font.render("or be more accurate in the probabilities?", 56, (0,0,0))
    screen.blit(text, (125, 25+36))
    # next card button
    # image taken from: http://www.clker.com/cliparts/m/S/m/C/X/Q/black-square-rounded-corners-hi.png
    rectangle = pygame.image.load('roundSquare.png')
    rectangle = pygame.transform.scale(rectangle, (windowW//2, windowH//5))
    screen.blit(rectangle, (windowW/100, windowH/2.2))
    # next card button text
    font = pygame.font.SysFont('comicsansms', 36)
    text = font.render("Run Faster", 56, (255, 255, 255))
    screen.blit(text, (windowW/7, windowH/2))

    # next card button
    # image taken from: http://www.clker.com/cliparts/m/S/m/C/X/Q/black-square-rounded-corners-hi.png
    rectangle = pygame.image.load('roundSquare.png')
    rectangle = pygame.transform.scale(rectangle, (windowW//2, windowH//5))
    screen.blit(rectangle, (windowW/2, windowH/2.2))
    # next card button text
    font = pygame.font.SysFont('comicsansms', 36)
    text = font.render("Accuracy", 56, (255, 255, 255))
    screen.blit(text, (windowW/1.55, windowH/2))

def pickPlayingMode():
    screen.fill((0,255,150))
    font = pygame.font.SysFont('comicsansms', 36)
    text = font.render("Would you like to calculate your ", 56, (0,0,0))
    screen.blit(text, (150, 25))
    font = pygame.font.SysFont('comicsansms', 36)
    text = font.render("probabilities or play Texas Holdem?", 56, (0,0,0))
    screen.blit(text, (125, 25+36))

    # next card button
    # image taken from: http://www.clker.com/cliparts/m/S/m/C/X/Q/black-square-rounded-corners-hi.png
    rectangle = pygame.image.load('roundSquare.png')
    rectangle = pygame.transform.scale(rectangle, (windowW//2, windowH//5))
    screen.blit(rectangle, (windowW/100, windowH/2.2))
    # next card button text
    font = pygame.font.SysFont('comicsansms', 36)
    text = font.render("Probabilities", 56, (255, 255, 255))
    screen.blit(text, (windowW/7, windowH/2))

    # next card button
    # image taken from: http://www.clker.com/cliparts/m/S/m/C/X/Q/black-square-rounded-corners-hi.png
    rectangle = pygame.image.load('roundSquare.png')
    rectangle = pygame.transform.scale(rectangle, (windowW//2, windowH//5))
    screen.blit(rectangle, (windowW/2, windowH/2.2))
    # next card button text
    font = pygame.font.SysFont('comicsansms', 36)
    text = font.render("Play Poker", 56, (255, 255, 255))
    screen.blit(text, (windowW/1.55, windowH/2))



running = True
initalScreen = True
tableScreen = False
cardScreen = False
cards = {}
playerHandCord = {}
playerHand = {}
nextScreen = False
down = False
pickEfficiency = False
trials = 10**5
pickPlay = False
(royalFlush, straightFlush, fullHouse, fourOfAKind, flushHand, straight, triple, twoPair, onePair, noPair) = 0,0,0,0,0,0,0,0,0,0

makeDeck()
while running:
    clock = pygame.time.Clock()
    clock.tick(50)
    # just code to exit game
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
             running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            down = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                running = True
                initalScreen = True
                tableScreen = False
                cardScreen = False
                cards = {}
                playerHandCord = {}
                playerHand = {}
                nextScreen = True
                down = False
                makeDeck()
                (royalFlush, straightFlush, fullHouse, fourOfAKind, flushHand, straight, triple, twoPair, onePair, noPair) = 0,0,0,0,0,0,0,0,0,0
    
    # runs the welcome screen if the boolean is true (which it is initally, but doesnt turn true again afterwards)
    if initalScreen:
        initial()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if (332 < pos[0] < 505 and 461 < pos[1] < 544):
                initalScreen = False
                pickPlay = True
        pygame.display.update()
        
    if pickPlay:
        pickPlayingMode()
        for event in pygame.event.get(): 
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if 30 <= pos[0] <= 420 and 276 <= pos[1] <=380:
                    pickEfficiency = True
                    pickPlay = False
                elif 469 <= pos[0] <= 858 and 276 <= pos[1] <= 381:
                    pickPlay = False
                    from playingAgainstComputer import *    
                down = False
                continue
        
    if pickEfficiency:
        pickingScreen()
        if down:
            pos = pygame.mouse.get_pos()
            if 30 <= pos[0] <= 420 and 276 <= pos[1] <=380:
                trials = 12**3
                pickEfficiency = False
                tableScreen = True
            elif 469 <= pos[0] <= 858 and 276 <= pos[1] <= 381:
                trials = 10**5
                pickEfficiency = False
                tableScreen = True

    if tableScreen:
        currentTableScreen()
        if down:
            pos = pygame.mouse.get_pos()
            if len(playerHandCord) != 7:
                if (19 < pos[0] < 170 and 409 < pos[1] < 479): # these are the positions of the first blank card
                    # this is where it changes screens
                    tableScreen = False
                    cardScreen = True

    elif cardScreen:
        cardsToPickFrom()
        lenCards = len(cards)
        if down:
            cardpos = pygame.mouse.get_pos()
            for key in cards:
                if (cards[key][0] < cardpos[0] < cards[key][1] and cards[key][2] < cardpos[1] < cards[key][3]):
                    # the next four lines are just to add the card to a dictionary of cards that are picked already
                    playerHandCord[key] = playerHandCord.get(key, cards[key])
                    playerHand[key.suit] = playerHand.get(key.suit, 0) + 1
                    playerHand[key.rank] = playerHand.get(key.rank, 0) + 1
                    del cards[key]
                    # this is where it changes screens
                    tableScreen = True
                    cardScreen = False 
                    break
            if lenCards != len(cards):
                if flush(playerHandCord)[0] == True and flush(playerHandCord)[1] == 14: 
                    ( straightFlush, fullHouse, fourOfAKind, flushHand, 
                    straight, triple, twoPair, onePair, noPair) = 0,0,0,0,0,0,0,0,0
                    royalFlush = 1
                elif flush(playerHandCord)[0] == True: 
                    (royalFlush, fullHouse, fourOfAKind, flushHand, 
                    straight, triple, twoPair, onePair, noPair) = 0,0,0,0,0,0,0,0,0
                    straightFlush = 1
                else:  
                    (royalFlush, straightFlush, fullHouse, fourOfAKind, flushHand, 
                    straight, triple, twoPair, onePair, noPair) = handOdds(trials, playerHandCord)
                    fullHouse += triple
                    triple = 0

    down = False
    pygame.display.update()

