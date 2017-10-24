# coding: utf-8

import sys
import time
import random

SHOP_FACTOR = 1.5

playerName = ''
inventory = {
    'carbon' : 5, 'hydrogen' : 5
}

bourse = 1000
equipedWeapon = ''
boughtWeapons = []

weaponsList = {
    'sporadique': {
        'name' : 'le celeri sporadique',
        'stats' : {
            'damage' : 5
        },
        'price' : 10
    }
}

stats = {
        'niveau': 1,
        'xpEnCours': 0,
        'charisme': 0,
        'force du zboubard' : 0,
        'taille du zboubard' : 0,
        'vie' : 10
}

bossList = {
    'rat des champs' : {
        'name' : 'rat des champs',
        'force' : 1,
        'goldGain' : 5,
        'levelNeeded' : 0,
        'level' : 1,
        'stats' : {
            'force' : 1,
            'vie' : 1
        },
        'drops' : {
            'diams' : 0.01,
            'hydrogen' : 0.4,
            'carbon' : 0.5
        },
        'xp' : 5
    },
    'rat des ville' : {
        'name' : 'rat des villes',
        'stats' : {
            'force' : 1,
            'vie' : 1
        },
        'goldGain' : 15,
        'levelNeeded' : 1,
        'level' : 5
    }
}
mixingTable = {
    'carbon-hydrogen' : 'carbogen',
    'carbogen-carbon' : 'carbonara',
    'carbogen-carbonara' : 'cacarbonara',
    'carbon-carbon' : 'megacarbon',
    'megacarbon-megacarbon' : 'gigarbon',
    'gigarbon-gigarbon' : 'hyparbon',
    'hyparbon-hyparbon' : 'diams',
    'carbon-dioxygen' : 'monoxyde'
}
discoveredElements = []

def seeInventory():
    print ('dans ta besace, tu as actuellement :')
    for item, numberItem in inventory.items():
        print item, ' x',numberItem

def shop() :
    print 'Bonjour, décides toi ou je monte les prix ! \n'
    buyableItems = [x for x in weaponsList if (x['price']*SHOP_FACTOR < bourse)]



def chooseBoss() :
    fightableBosses = []
    for boss in bossList:
        if bossList[boss]['levelNeeded'] < stats['niveau']:
            fightableBosses.append(boss)
    print('voici les boss que tu peut affronter (et te faire defonc\')\n')
    for boss in fightableBosses:
        print(bossList[boss]['name'], "  level :", bossList[boss]['level'])
        print('\n')
    print('qui veux tu combattre ? (dis non pour ne pas combattre, fiotte)\n')
    response = sys.stdin.readline().strip()
    if response != 'non' and response in fightableBosses:
        fightBoss(response)
    elif response == 'non':
        print('NOOB')
    else:
        print('soit tu sais pas écrire soit t\'as essayé de jouer aux petit malins ! dégage !')

def fightBoss(bossName):
    print('tu va te fritter contre ', bossName)
    # playerScore = stats['force']*0.5 + stats['taille du zboubard']*0.3 + stats['force du zboubard']
    # bossScore = 10
    # time.sleep(10)
    fightSuccess(bossName)

def expPlayer(gainedXp):
    neededXpForNextLevel = stats['niveau']*10  #TODO#
    progressPercent = gainedXp*100/neededXpForNextLevel
    levelProgression = stats['xpEnCours'] + progressPercent
    # import ipdb; ipdb.set_trace()
    if levelProgression > 99:
        stats['niveau'] += 1
        # import ipdb; ipdb.set_trace()
        stats['xpEnCours'] = levelProgression%100
    else :
        stats['xpEnCours'] = levelProgression
    
def printXp():
    # import ipdb; ipdb.set_trace()
    print('['+'X'*int(stats['xpEnCours'])+'.'*(100-int(stats['xpEnCours']))+']')

def fightSuccess(bossName):
    boss = bossList[bossName]
    expPlayer(boss['xp'])
    gainGold(boss['goldGain'])
    dropList = boss['drops']
    droppedItems = []
    for droppableItem, itemRate in dropList.items():
        fightDropResult = random.random()
        if fightDropResult > itemRate:
            inventory[droppableItem] = inventory.get(droppableItem, 0) + 1
            droppedItems.append(droppableItem)
    if len(droppedItems):
        print('\n voici les resultats de ton combat champion ! : \n')
        print (', '.join(droppedItems))

def gainGold(sum):
    print 'tu enrichi tes bourses de ', sum, ' pieces d\'or'
    bourse += sum
    
def mix(el1, el2):
    elArray = [el1, el2]
    elArray.sort()
    mixKey = '-'.join(elArray)
    if mixKey in mixingTable :
        if (inventory[el1]>0 and inventory[el2]>0) :
            inventory[el1] = inventory[el1]-1
            inventory[el2] = inventory[el2]-1
            inventory[mixingTable[mixKey]] =+ 1
            if mixingTable[mixKey] not in discoveredElements :
                discoveredElements.append(mixingTable[mixKey])
                print('\n')
                print('Kongratullassion tu as crée le nouvel element :', mixingTable[mixKey])
            else :
                print('encore un', mixingTable[mixKey], ',tu en possédes actuellement : ', inventory[mixingTable[mixKey]] )
        else : 
            print ("t'es sur une bonne piste mais t'as pas ce qui faut !")
        
    else :
        print("ça donne rien ton truc boloss")

def seeDiscovered():
    for recipe, element in mixingTable.items():
        if element in discoveredElements:
            print (recipe, '=', element)

def Intro():
    print(' /~~~\/~~\/~~~\/~~~\/~~\/~~~\                    /~~~\/~~\/~~~\/~~~\/~~\/~~~\ ')
    print(' | /\/ /\/ /\ || /\/ /\/ /\ |   Bienvenu chez    | /\ \/\ \/\ || /\ \/\ \/\ |')
    print(' \ \/ /\/ /\/ /\ \/ /\/ /\/ /                    \ \/\ \/\ \/ /\ \/\ \/\ \/ /')
    print("  \ \/\ \/\ \/  \ \/\ \/\ \/    l'Alchybriste     \/ /\/ /\/ /  \/ /\/ /\/ /")
    print(',_/\ \/\ \/\ \__/\ \/\ \/\ \______________________/ /\/ /\/ /\__/ /\/ /\/ /\_,')
    print('(__/\__/\__/\____/\__/\__/\________________________/\__/\__/\____/\__/\__/\__)')
    print('             ___     ___     ___     ___     ___     ___     ___     ___  ')
    print('     ___/   \___/   \___/   \___/   \___/   \___/   \___/   \___/   \___  ')
    print('    /   \___/   \___/   \___/   \___/   \___/   \___/   \___/   \___/   \ ')
    print('    \___/   \___/   \___/   \___/   \___/   \___/   \___/   \___/   \___/ ')
    print('    /   \___/                                                   \___/   \ ')
    print('    \___/     Chez l\'Alchybriste, ta vas pouvoir partir en quéte   \___/ ')
    print('    /   \                Du légendaire MEGA-CHYBRE                  /   \ ')
    print('    \___/                                                           \___/ ')
    print('    /   \  Pour ça tu vas devoir combiner moultes éléments avant    /   \ ')
    print('    \___/     de pouvoir enfin carresser la fine courbure de        \___/ ')
    print('    /   \     cette relique restée coincée dans les tréfonds du     /   \ ')
    print('    \___/              donjon de la SHAÄTAMIRAYE                    \___/ ')
    print('    /   \                                                           /   \ ')
    print('    \___/        Va jeune aventurier ! et ne reviens pas sans       \___/ ')
    print('    /   \    cette relique qui permet à son detenteur de gagner     /   \ ')
    print('    \___/           toutes les parties de BITOUCOUILLES             \___/ ')
    print('    /   \___                                                     ___/   \ ')
    print('    \___/   \___     ___     ___     ___     ___     ___     ___/   \___/ ')
    print('    /   \___/   \___/   \___/   \___/   \___/   \___/   \___/   \___/   \ ')
    print('    \___/   \___/   \___/   \___/   \___/   \___/   \___/   \___/   \___/ ')
    print('        \___/   \___/   \___/   \___/   \___/   \___/   \___/   \___/     ')

def Help():
    print("          .-.     .-.     .-.     .-.     .-.     .-.     .-.     .-.     .-.") 
    print("    .'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `.")
    print("   (    .     .-.     .-.     .-.     .-.     .-.     .-.     .-.     .    )")
    print("    `.   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   .'")
    print("      )    )                                                       (    (")
    print("    ,'   ,'    A tout moment de ta (que)quête, plusieurs actions    `.   `.")
    print("   (    (         sont a ta disposition. voici ton grimoire.         )    )")
    print("    `.   `.       pour effectuer une action, il te suffit de        .'   .'") 
    print("      )    )       taper son nom. L'Alchibriste les entendra       (    (")
    print("    ,'   ,'          et te repondra. Voici ces action               `.   `.")
    print("   (    (                                                             )    )")
    print("    `.   `.   aide : fait apparaitre ce menu                        .'   .'") 
    print("      )    )  inventaire : liste ce que tu posséde                 (    (")
    print("    ,'   ,'   mix : fusionne des éléments                           `.   `.")
    print("   (    (     recette : liste les recettes que tu as deja decouverte  )    )")
    print("    `.   `.   combattre : part a la chasse !                        .'   .'") 
    print("      )    )  shop : va donc claquer tes thunes !                  (    (")
    print("    ,'   ,'   xp : affiche ta barre d'xp et ton niveau              `.   `.")
    print("   (    (                                                             )    )")
    print("    `.   `.                                                         .'   .'") 
    print("      )    )       _       _       _       _       _       _       (    (")
    print("    ,'   .' `.   .' `.   .' `.   .' `.   .' `.   .' `.   .' `.   .' `.   `.")
    print("   (    '  _  `-'  _  `-'  _  `-'  _  `-'  _  `-'  _  `-'  _  `-'  _  `    )")
    print("    `.   .' `.   .' `.   .' `.   .' `.   .' `.   .' `.   .' `.   .' `.   .'")
    print("      `-'     `-'     `-'     `-'     `-'     `-'     `-'     `-'     `-'")
    print("\n")
    print("\n")

Intro()
Help()
print 'D\'abord, quel est ton nom étranger ? '
playerName = sys.stdin.readline().strip()
while(1):
    print('\n')
    print 'Alors ? Que veux tu faire,', playerName, ', jeune apprentrique ? \n'
    line = sys.stdin.readline().strip()
    if line == 'quit' :
        print ('Allé Ciao !')
        sys.exit()
    if line == 'inventaire' :
        seeInventory()
    if line == 'recettes' :
        seeDiscovered()
    if line == 'combattre' :
        chooseBoss()
    if line == 'xp' :
        printXp()
    if line == 'shop' :
        shop()
    if line == 'mix' :
        print("what do you want to mix ?")
        el1 = sys.stdin.readline().strip()
        print("whith what you douch ?")
        el2 = sys.stdin.readline().strip()
        mix(el1, el2)

