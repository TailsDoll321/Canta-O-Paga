import pygame
import random

newsong = 1
i = 176
turno = 1
jugador = 0
njug = 0
pj1 = -1
pj2 = 0
pj3 = 0
pj4 = 0
txturn = ""
txpun = ""
txwin = ""
n = 17
newpunishment = 0

pygame.init()
screen = pygame.display.set_mode((750, 500))

Title = "Canta o Paga"
pygame.display.set_caption(Title)

song = {1 : "Los Malaventurados No Lloran - PXNDX", 2 : "Starlight - Muse", 3 : "Ya Lo Veia Venir - Moderatto", 4 : "Knights of Cydonia - Muse", 5 : "Hustle Bones - Death Grips",
        6 : "Renai Circulation - Kana Hanazawa", 7 : "Zombie - The Cranberries", 8 : "Clint Eastwood - Gorillaz", 9 : "In The End - Linkin Park", 10 : "Numb - Linkin Park",
        11 : "Labios Rotos - Mana", 12 : "Stressed Out - Twenty One Pilots", 13 : "La Cancion - Bad Bunny X J Balvin", 14 : "Callaita - Bad Bunny", 15 : "QUE PRETENDES - Bad Bunny X J Balvin",
        16 : "Chop Suey - System of a Down", 17 : "Toxicity - System of a Down", 18 : "Aerials, System of a Down", 19 : "I Don't Love You - My Chemical Romance",
        20 : "Helena - My Chemical Romance", 21 : "Welcome to the Black Parade - My Chemical Romance", 22 : "That's What You Get - Paramore", 23 : "Still Into You - Paramore",
        24 : "Misery Business - Paramore", 25 : "Ain´t It Fun - Paramore", 26 : "My Blood - Twenty One Pilots", 27 : "Devuelveme a mi Chica - Hombres G",
        173 : "La Celula que Explota - Caifanes", 174 : "Sognare - Division Minuscula", 175 : "Anda y Ve - Jose Jose", 176 : "El Triste - Jose Jose", 177 : "Gavilan o Paloma - Jose Jose",
        28 : "Blinding Lights - The Weekend", 29 : "Circles - Post Malone", 30 : "This Love - Maroon 5", 31 : "Viva la Vida - Coldplay", 32 : "La Nave del Olvido - Jose Jose",
        33 : "Run - Joji", 34 : "Slow Dancing in the Dark - Joji", 35 : "I Don't Wanna Waste my Time - Joji" ,36 : "17 Años - Angeles Azules", 37 : "The Beach - The Neighborhood",
        38 : "Ties - Years & Years", 39 : "Palo Santo - Years & Years", 40 : "El Amar y el Querer - Jose Jose", 41 : "40 y 20 - Jose Jose", 42 : "Te Quiero - Barney",
        43 : "Baby Shark", 44 : "La Vaca Lola", 45 : "El Pollito Pio", 46 : "Mi Pollito Amarillito", 47 : "La Gallina Turuleca", 48 : "El Patito Juan", 49 :"Si Veo a tu Mama - Bad Bunny",
        50 : "Sigues con El - Arcángel", 51 : "Hola Remix - Dalex", 52 : "Bellaquita - Dalex", 53 : "Girls Like You - Maroon 5", 54 : "Ride It - Regard", 55 : "Feel So Close - Calvin Harris",
        56 : "Just Can´t Get Enough - Black Eyed Peas", 57 : "Meet Me Halfway - Black Eyes Peas", 58 : "Thunder - Imagine Dragons", 59 : "Amsterdam - Imagine Dragons",
        60 : "Dance Monkey - Tones and I", 61 : "Jangueo - Alex Rose", 62 : "Ignorantes - Bad Bunny", 63 : "Cuando Calienta el Sol - Luis Miguel", 64 : "Prometiste - Pepe Aguilar",
        65 : "Por que me Haces Llorar - Juan Gabriel", 66 : "Empire State of Mind - Jay Z", 67 : "Love the Way you Lie - Eminem", 68 : "My Way - Frank Sinatra", 69 : "Atrevetetete - Calle 13",
        70 : "What A Wonderful World - Louis Armstrong", 71 : "Gasolina - Daddy Yankee", 72 : "Mis Ojos Lloran Por Ti - Big Boy", 73 : "Ven Bailalo - Angel y Khriz", 74 : "Snuff - Slipknot",
        75 : "Duality - Slipknot", 76 : "Psychosocial - Slipknot", 77 : "The Animal I've Become - Three Days Grace", 78 : "Sugar, We´re Going Down - Fall Out Boy",
        79 : "Time of Dying -  Three Days Grace", 80 : "Smells Like a Teen Spirit - Nirvana", 81 : "Come As You Are - Nirvana", 82 : "The Man Who Sold The World - Nirvana",
        83 : "Heart-Shaped Box - Nirvana", 84 : "The Ballad of Mona Lisa - Panic! at the Disco", 85 : "Blow Me Away - Breaking Benjamin", 86 : "My Immortal - Evanescence",
        87 : "Bring Me To Life - Evanescence", 88 : "Tiny Little Adiantum", 89 : "Last Resort - Papa Roach", 90 : "All The Small Things - Blink 182", 91 : "What's My Age Again - Blink 182",
        92 : "Can't Stop - Red Hot Chili Peppers", 93 : "Californication - Red Hot Chili Peppers", 94 : "PPAP - Pikotaro", 95 : "Otherside - Red Hot Chili Peppers",
        96 : "Boss Bitch - Doja Cat", 97 : "CANDY - Doja Cat", 98 : "Electric Feel - MGMT", 99 : "Kids - MGMT", 100 : "Instant Crush - Daft Punk", 101 : "Bitchcraft - Drake Bell",
        102 : "I Know - Drake Bell", 103 : "Procedimiento Para Llegar a un Comun Acuerdo - PXNDX", 104 : "Something About Us - Daft Punk", 105 : "Get Lucky - Daft Punk",
        106 : "American Boy - Estelle", 107 : "Lying Is The Most Fun A Girl Can Do Without Taking Her Clothes - Panic! At The Disco", 108 : "Thnks Fr Th Mmrs - Fall Out Boy",
        109 : "S.O.S - Jonas Brothers", 110 : "Mr. Brightside - The Killers", 111 : "Burnin' Up - Jonas Brothers", 112 : "Fireflies - Owl City", 113 : "Kangaroo Court - Capital Cities",
        114 : "On Melancoholy Hill - Gorillaz", 115 : "Stylo - Gorillaz", 116 : "Rock The House - Gorillaz", 117 : "Stronger - Kanye West", 118 : "I Love Kanye - Kanye West",
        119 : "I'm Not The Only One - Sam Smith", 120 : "Luna - Zoe", 121 : "Hurt - Johnny Cash", 122 : "Sk8er Boi - Avril Lavigne", 123 : "Complicated - Avril Lavigne",
        124 : "What the Hell - Avril Lavigne", 125 : "Hey! Ya - Outkast", 126 : "Boulevard of Broken Dreams - Green Day", 127 : "21 Guns - Green Day", 128 :"Holiday - Green Day",
        129 : "Know Your Enemy - Green Day", 130 : "American Idiot - Green Day", 131 : "Poker Face - Lady Gaga", 132 : "Bad Day - Daniel Powter", 133 : "Electromovimiento - Calle 13",
        134 : "Bad Romance - Lady Gaga", 135 : "Billie Jean - Michael Jackson", 136 : "Don - Miranda", 137 : "The Way You Make Me Feel - Michael Jackson", 138 : "Limon Y Sal - Julieta Venegas",
        139 : "Ella es Bonita - Natalia Lafourcade", 140 : "Yofo - Molotov", 141 : "Electricity - Dua Lipa", 142 : "Zodiaco - Moderatto", 143 : "Mil Demonios - Moderatto",
        144 : "I Want It That Way - Backstreet Boy", 145 : "It's Gotta Be You - Backstreet Boy", 146 : "Raging - Kygo", 147 : "21 Questions - 50 Cent", 148 : "Brillas - Leon Larregui",
        149 : "Azul - Zoe", 150 : "Dry Ice - Green Day", 151 : "Letterbomb - Green Day", 152 : "Llamado de Emergencia - Daddy Yankee", 153 : "Soñe - Zoe", 154 : "China - Daddy Yankee",
        155 : "Desvelado - Bobby Pulido", 156 : "Enseñame - Bobby Pulido", 157 : "Amor Prohibido - Selena", 158 : "El Liston de tu Pelo - Angeles Azules", 159 : "Crei en Ti - Angeles Azules",
        160 : "Donde Estas - Intocable", 161 : "Loco - Pesado", 162 : "Te Amo - Pesado", 163 : "El Ruido de Tus Zapatos - Banda Limon", 164 : "Total Eclipse of the Heart - Bonnie Tyler",
        165 : "Every Breath You Take - The Police", 166 : "My Name Is - Eminem", 167 : "Houdini - Foster the People", 168 : "TUSA - Karol G", 169 : "Wake Me Up Before You Go-Go - Wham!",
        170 : "Careless Whisper - George Michael", 171 : "Baby Please - Allsion", 172 : "Fragil - Allison"}

castigo = ["Cortarle la uña de un dedo con los dientes a un jugador ", "Hacer un baile de Tik-Tok", "Marcale/Envia mensaje a un/una ex",
           "Comete un chile habanero", "Dar vueltas por 10 segundos y bailar payaso de rodeo con vuelta y brinco", "Come algo echado a perder",
           "Di un secreto vergonzoso", "Huele la axila de otro jugador", "Chupa la axila a otro jugador", "Lambe tu propio codo",
           "Hacer 3 lagartijas con aplauso seguidas", "Dile un piropo a algun desconocido", "Meter la mano en un inodoro", "Recibir una cachetada de otro jugador",
           "Declaratele a algun desconocido", "Actuar como un animal, a votacion de jugadores", "Comete el moco de algun jugador",
           "Marcarle a tus padres y decirle que saliste del closet"]

# Colores
black = (0, 0, 0)
grey = (87, 89, 93)
white = (255, 255, 255)
green = (26, 148, 49)
light_green = (89, 182, 91)
red = (255, 0, 0)
light_red = (244, 86, 44)
blue = (0, 0, 255)
light_blue = (63, 183, 227)
yellow = (255, 255, 0)
light_yellow = (255, 255, 102)
violet = (238,130,238)
light_violet = (221,160,221)


clock = pygame.time.Clock()

#Tipo de Letra
small = pygame.font.SysFont("Centhury Gothic", 25)
smallm = pygame.font.SysFont("Centhury Gothic", 35)
medium = pygame.font.SysFont("Centhury Gothic", 50)
large = pygame.font.SysFont("Centhury Gothic", 70)

def text_ob(text, color, size=small):
    if size == "small":
        textSurface = small.render(text, True, color)
    if size == "medium":
        textSurface = medium.render(text, True, color)
    if size == "large":
        textSurface = large.render(text, True, color)
    if size == "smallm":
        textSurface = smallm.render(text, True, color)

    return textSurface, textSurface.get_rect()

def msg_screen(msg, color, y_displace = 0, x_displace = 0, size = "small"):
    textSurf, textRect = text_ob(msg, color, size)
    textRect.center = ((750/2) + x_displace, (500/2)+ y_displace)
    screen.blit(textSurf, textRect)

def text_b(msg, color, buttonx, buttony, buttonwidth, buttonheight, size = "small"):
    textSurf, textRect = text_ob(msg,color,size)
    textRect.center = ((buttonx+(buttonwidth/2)), buttony+(buttonheight/2))
    screen.blit(textSurf, textRect)

def boton(nombre, ancho, largo, posx, posy, color_a, color_b, acc = None):
    global newsong, njug, turno, newpunishment, jugador
    cur = pygame.mouse.get_pos()
    # print(posy + largo)
    # print(posx + ancho)

    if (posx + ancho) > cur[0] > posx and (posy + largo) > cur[1] > posy:
        pygame.draw.rect(screen, color_a, (posx, posy, ancho, largo))

        if pygame.mouse.get_pressed()[0]:
            pygame.time.delay(450)

            if acc == "J":
                jugadores()

            if acc == "I":
                instrucciones()

            if acc == "Q":
                pygame.quit()
                quit()

            if acc == "2":
                #print("Have you heard the legend")
                njug = 2
                puntuacionpos()
                #print(njug)
                game()

            if acc == "3":
                #print("of Darth Plagueis?")
                njug = 3
                puntuacionpos()
                game()

            if acc == "4":
                #print("It's not something a Jedi wold tell you")
                njug = 4
                puntuacionpos()
                game()

            if acc == "C":
                puntuacionpos()
                turno += 1
                newsong = 1

            if acc == "P":
                newpunishment = 1
                
                castigos()

            if acc == "+":
                puntuacionneu()
                turno +=1
                newsong = 1
                game()

            if acc == "-":
                puntuacionneg()
                newsong = 1
                turno += 1
                game()

            if acc == "reset":
                reset()

            if acc == "eq":
                equipo()
                              
                

    else:
        pygame.draw.rect(screen, color_b, (posx, posy, ancho, largo))


def intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(white)
        msg_screen("CANTA O PAGA", black, -150, size="large")
        boton("Inicio", 400, 75, 170, 175, light_green, green, acc = "J")
        boton("Instrucciones", 400, 75, 170, 280, light_blue, blue, acc = "I")
        boton("Salir", 400, 75, 170, 385, light_red, red, acc = "Q")
        boton("Equipo", 100, 50, 630, 440, light_violet, violet, acc = "eq")

        text_b("JUGAR", black, 170, 175, 400, 75)
        text_b("INSTRUCCIONES", black, 170, 280, 400, 75)
        text_b("SALIR", black, 170, 385, 400, 75)
        text_b("EQUIPO", black, 630, 440, 100, 50)
        
        pygame.display.update()

def equipo():
    equi = True
    while equi:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            screen.fill(green)
            msg_screen("EQUIPO 4 PENSAMIENTO CREATIVO M2", violet, -220, size = "medium")
            msg_screen("1859114 AVILA RANGEL JAVIER ALEJANDRO", black, -180, size = "small")
            msg_screen("1818283 CESEÑA MARTINEZ FERNANDO WENCESLAO", black, -155, size = "small")
            msg_screen("1942654 EDGAR SALDAÑA ERO", black, -130, size = "small")
            msg_screen("1634092 HERNANDEZ CORTES OSCAR ADOLFO", black, -105, size = "small")
            msg_screen("1855970 JAIME REYES IVAN AZAEL", black, -80, size = "small")
            msg_screen("1811025 MARTINEZ CALDERON ADOLFO", black, -55, size = "small")
            msg_screen("1812990 MORENO SANDOVAL LAURA", black, -30 , size = "small")
            msg_screen("1889390 PALATO HERNANDEZ CARLOS", black, -5, size = "small")
            msg_screen("1722403 RODRIGUEZ PEREZ CHRISTIAN", black, 20, size = "small")
            msg_screen("1793936 SALINAS RODRIGUEZ CAROLINA", black, 45, size = "small")
            msg_screen("1942494 VEGA DE LA CRUZ RAUL JAVIER", black, 70, size = "small")

            boton("Inicio", 150, 75, 105, 410, light_violet, violet, acc = "J")
            boton("Salir", 150, 75, 505, 410, light_red, red, acc = "Q")
            boton("Instrucciones", 150, 75, 305, 410, light_blue, blue, acc = "I")
            
            text_b("INSTRUCCIONES", black, 305, 410, 150, 75)
            text_b("JUGAR", black, 105, 410, 150, 75)
            text_b("SALIR", black, 505, 410, 150, 75)
            
            pygame.display.update()

def instrucciones():
    instru = True

    while instru:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(white)

        msg_screen("INTRUCCIONES", blue, -190, size = "large")
        msg_screen("Canta la cancion que salga en la pantalla, los demas jugadores decidiran", black, -130, size = "small")
        msg_screen("si estuvo correcto o no, de ser asi se te otorgara un punto, pero si no,", black, -110, size = "small")
        msg_screen("se impondra un castigo por la misma pantalla, si no lo realizas se te quita", black, -90, size = "small")
        msg_screen("un punto, si se realiza, quedas neutro.", black, -70, size = "small")
        msg_screen("Obten 7 puntos para ganar.", red, 0, size = "medium")

        boton("Inicio", 150, 75, 105, 410, light_green, green, acc = "J")
        boton("Salir", 150, 75, 505, 410, light_red, red, acc = "Q")

        text_b("JUGAR", black, 105, 410, 150, 75)
        text_b("SALIR", black, 505, 410, 150, 75)
        
        pygame.display.update()

def jugadores():
    jugador = True

    while jugador:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(white)
        msg_screen("Seleccione el numero de jugadores:", red, -190, size = "medium")
        boton("2", 560, 130, 80, 100, light_green, green, acc = "2")
        boton("3", 250, 130, 80, 300, light_yellow, yellow, acc = "3")
        boton("4", 250, 130, 390, 300, light_violet, violet, acc = "4")

        text_b("2", black, 80, 100, 560, 130)
        text_b("3", black, 80, 300, 250, 130)
        text_b("4", black, 390, 300, 250, 130)

        pygame.display.update()

def puntuacionpos():
    global jugador, njug, turno, pj1, pj2, pj3, pj4, txturn
    if njug == 2:

        if (turno % njug) == 1:

            pj1 += 1
            #print(pj1)
            jugador = 1
            #print(jugador)
            #turno += 1
            #print(turno)

        elif (turno % njug) == 0:

            pj2 += 1
            #print(pj2)
            jugador = 2
            #print(jugador)
            #turno += 1
            #print(turno)

    if njug == 3:
        if (turno % njug) == 1:

            pj1 += 1
            jugador = 1
            
        elif (turno % njug) == 2:

            pj2 += 1
            jugador = 2
            #turno += 1

        elif (turno % njug) == 0:

            pj3 += 1
            jugador = 3
            #turno += 1

    if njug == 4:

        if (turno % njug) == 1:

            pj1 += 1
            jugador = 1
            #turno += 1
        elif (turno % njug) == 2:

            pj2 += 1
            jugador = 2
            #turno += 1

        elif (turno % njug) == 3:

            pj3 += 1
            jugador = 3
            #turno += 1

        elif (turno % njug) == 0:

            pj4 += 1
            jugador = 4
            #turno += 1

def puntuacionneu():
    global jugador, njug, turno, pj1, pj2, pj3, pj4, txturn
    if njug == 2:

        if (turno % njug) == 1:

            #print(pj1)
            jugador = 1
            #print(jugador)
            #turno += 1
            #print(turno)

        elif (turno % njug) == 0:

            #print(pj2)
            jugador = 2
            #print(jugador)
            #turno += 1
            #print(turno)

    if njug == 3:
        if (turno % njug) == 1:

            jugador = 1
            
        elif (turno % njug) == 2:

            jugador = 2
            #turno += 1

        elif (turno % njug) == 0:

            jugador = 3
            #turno += 1

    if njug == 4:

        if (turno % njug) == 1:

            jugador = 1
            #turno += 1
        elif (turno % njug) == 2:

            jugador = 2
            #turno += 1

        elif (turno % njug) == 3:

            jugador = 3
            #turno += 1

        elif (turno % njug) == 0:

            jugador = 4
            #turno += 1
    
def puntuacionneg():
    global jugador, njug, turno, pj1, pj2, pj3, pj4, txturn
    if njug == 2:

        if (turno % njug) == 1:

            pj1 -= 1
            #print(pj1)
            jugador = 1
            print(jugador)
            #turno += 1
            #print(turno)

        elif (turno % njug) == 0:

            pj2 -= 1
            #print(pj2)
            jugador = 2
            #print(jugador)
            #turno += 1
            #print(turno)

    if njug == 3:
        #print(turno)
        #print(njug)
        #print(turno % njug)
        #print(jugador)
        if (turno % njug) == 1:

            #print("hola")
            pj1 -= 1
            jugador = 1
            
        elif (turno % njug) == 2:

            pj2 -= 1
            jugador = 2
            #turno += 1

        elif (turno % njug) == 0:

            pj3 -= 1
            jugador = 3
            #turno += 1

    if njug == 4:

        if (turno % njug) == 1:

            pj1 -= 1
            jugador = 1
            #turno += 1
        elif (turno % njug) == 2:

            pj2 -= 1
            jugador = 2
            #turno += 1

        elif (turno % njug) == 3:

            pj3 -= 1
            jugador = 3
            #turno += 1

        elif (turno % njug) == 0:

            pj4 -= 1
            jugador = 4
            #turno += 1

def scoreboard():
    global pj1, pj2, pj3, pj4, njug, jugador
    if njug == 2:
            tp1 = ("Jugador 1: "+str(pj1))
            tp2 = ("Jugador 2: "+str(pj2))
            msg_screen(tp1, black, -230, -150, size = "small")
            msg_screen(tp2, black, -230, 150, size = "small")
    if njug == 3:
        tp1 = ("Jugador 1: "+str(pj1))
        tp2 = ("Jugador 2: "+str(pj2))
        tp3 = ("Jugador 3: "+str(pj3))
        msg_screen(tp1, black, -230, -120, size = "small")
        msg_screen(tp2, black, -230, 0, size = "small")
        msg_screen(tp3, black, -230, 120, size = "small")
    if njug == 4:
        tp1 = ("Jugador 1: "+str(pj1))
        tp2 = ("Jugador 2: "+str(pj2))
        tp3 = ("Jugador 3: "+str(pj3))
        tp4 = ("Jugador 4:"+str(pj4))
        msg_screen(tp1, black, -230, -300, size = "small")
        msg_screen(tp2, black, -230, -100, size = "small")
        msg_screen(tp3, black, -230, 100, size = "small")
        msg_screen(tp4, black, -230, 300, size = "small")

def jugadortexto():
    global jugador, njug, turno, txturn, txpun

    if njug == 2:
        if turno > 1:
            if jugador == 2:
                txturn = ("Jugador 1 canta la siguiente cancion")
                txpun = ("HORA DEL CASTIGO JUGADOR 1")
            else:
                txturn = ("Jugador 2 canta la siguiente cancion")
                txpun = ("HORA DEL CASTIGO JUGADOR 2")
        else:
            txturn = ("Jugador 1 canta la siguiente cancion")
            txpun = ("HORA DEL CASTIGO JUGADOR 1")
    if njug == 3:
        if turno > 1:
            if jugador == 2:
                txturn = ("Jugador 3 canta la siguiente cancion")
                txpun = ("HORA DEL CASTIGO JUGADOR 3")
            elif jugador == 3:
                txturn = ("Jugador 1 canta la siguiente cancion")
                txpun = ("HORA DEL CASTIGO JUGADOR 1")
            elif jugador == 1:
                txturn = ("Jugador 2 canta la siguiente cancion")
                txpun = ("HORA DEL CASTIGO JUGADOR 2")
        else:
            txturn = ("Jugador 1 canta la siguiente cancion")
            txpun = ("HORA DEL CASTIGO JUGADOR 1")
    if njug == 4:
        if turno > 1:
            if jugador == 2:
                txturn = ("Jugador 3 canta la siguiente cancion")
                txpun = ("HORA DEL CASTIGO JUGADOR 3")
            elif jugador == 3:
                txturn = ("Jugador 4 canta la siguiente cancion")
                txpun = ("HORA DEL CASTIGO JUGADOR 4")
            elif jugador == 4:
                txturn = ("Jugador 1 canta la siguiente cancion")
                txpun = ("HORA DEL CASTIGO JUGADOR 1")
            elif jugador == 1:
                txturn = ("Jugador 2 canta la siguiente cancion")
                txpun = ("HORA DEL CASTIGO JUGADOR 2")
        else:
            txturn = ("Jugador 1 canta la siguiente cancion")
            txpun = ("HORA DEL CASTIGO JUGADOR 1")
        
def zeros():
    global pj1, pj2, pj3, pj4
    if pj1 < 0:
        pj1 = 0
    if pj2 < 0:
        pj2 = 0
    if pj3 < 0:
        pj3 = 0
    if pj4 < 0:
        pj4 = 0

def wintxt():
    global pj1, pj2, pj3, pj4, txwin
    if pj1 == 7:
        txwin = ("FELICIDADES JUGADOR 1, HAS GANADO")
    if pj2 == 7:
        txwin = ("FELICIDADES JUGADOR 2, HAS GANADO")
    if pj3 == 7:
        txwin = ("FELICIDADES JUGADOR 3, HAS GANADO")
    if pj4 == 7:
        txwin = ("FELICIDADES JUGADOR 4, HAS GANADO")
        
def winnerscreen():
    global txtwin

    wnnr = True
    while wnnr:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(green)
        wintxt()
        msg_screen(txwin, black, size = "medium")
        boton("Reset", 300, 135, 400, 300, light_green, green, acc = "reset")
        boton("Bye", 300, 135, 50, 300, light_red, red, acc = "Q")
        text_b("Jugar de nuevo", black, 400, 300, 300, 135)
        text_b("Salir del juego", black, 50, 300, 300, 135)

        pygame.display.update()
    
def reset():
    global pj1, pj2, pj3, pj4, jugador, turno, newsong, newpunishment, njug
    turno = 1
    jugador = 0
    njug = 0
    pj1 = 0
    pj2 = 0
    pj3 = 0
    pj4 = 0
    newsong = 1
    newpunishment = 0
    jugadores()

def game():
    global newsong, i, song, jugador, turno, txturn
    game = True

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if (pj1 is 7) or (pj2 is 7) or (pj3 is 7) or (pj4 is 7):
            winnerscreen()

        zeros()
        while newsong == 1:
            screen.fill(white)
            x = random.randint(1, i)
            cancion = song[x]
            #print(cancion)
            if x == 107:
                msg_screen(cancion, black, size = "small")
            else:
                msg_screen(cancion, black, size = "smallm")
            #print(turno)
            #print(jugador)
            newsong = 0

        scoreboard()
        jugadortexto()
        msg_screen(txturn, red, -175, size =  "medium")
        boton("Pos", 300, 135, 400, 300, light_green, green, acc = "C")
        boton("Cast", 300, 135, 50, 300, light_red, red, acc = "P")
        text_b("Parece que la esucucho hace rato", black, 400, 300, 300, 135)
        text_b("No se la supo", black, 50, 300, 300, 135)
        clock.tick(15)
        pygame.display.update()

def castigos():
    global jugador, n, newpunishment, txpun, castigo

    punishmentl = True
    while punishmentl:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        while newpunishment == 1:
            screen.fill(black)
            y = random.randint(1, n-1)
            np = castigo[y]
            if y == 4:
                msg_screen(np, white, -70, size = "small")
            else:                
                msg_screen(np, white, -70, size = "smallm")
            newpunishment = 0
        msg_screen(txpun, red, -175, size = "medium")
        boton("Si", 300, 135, 400, 300, light_green, green, acc = "+")
        boton("No", 300, 135, 50, 300, light_red, red, acc = "-")
        text_b("Si lo logro", black, 400, 300, 300, 135)
        text_b("No pudo hacerlo", black, 50, 300, 300, 135)
        clock.tick(15)
        pygame.display.update()

intro()
