# Se cambia hoyo
import random

# Función para imprimir el tablero
def imprimir_tablero(tablero):
    print("\t\t\t","_"* 19)
    for fila in tablero:
        print("\t\t\t|"," | ".join(map(str, fila)),"|")
        print("\t\t\t|","_"* 17,"|")

#Función para el hedor
def hedor(tablero):
    for i in range(4):
        for j in range(4):
            if tablero[i][j] == "A " and j == 0 and i < 3:
                if tablero[i+1][j]== "W " or tablero[i][j+1]== "W " or tablero[i-1][j]== "W ":
                    print("Huele feo")
            elif tablero[i][j] == "A " and i == 0 and j < 3:
                if tablero[i+1][j]== "W " or tablero[i][j+1]== "W " or tablero[i][j-1]== "W ":
                    print("Huele feo")
            elif tablero[i][j] == "A " and i >0 and i < 3 and j > 0 and j < 3:
                if tablero[i][j+1]== "W " or tablero[i][j-1]== "W " or tablero[i+1][j]== "W " or \
                    tablero[i-1][j]== "W ":
                    print("Huele feo")        
            elif tablero[i][j] == "A " and i == 3 and j ==3:
                if tablero[i][j-1]== "W " or tablero[i-1][j]== "W ":
                    print("Huele feo")        
            elif tablero[i][j] == "A " and i == 3 :
                if tablero[i][j-1]== "W " or tablero[i][j+1]== "W " or tablero[i-1][j]== "W ":
                    print("Huele feo")
            elif tablero[i][j] == "A " and j == 3 :
                if tablero[i][j-1]== "W " or tablero[i+1][j]== "W " or tablero[i-1][j]== "W ":
                    print("Huele feo")

#Función para sentir el viento
def viento(tablero):
    for i in range(4):
        for j in range(4):
            if tablero[i][j] == "A " and j == 0 and i < 3:
                if tablero[i+1][j]== "H " or tablero[i][j+1]== "H " or tablero[i-1][j]== "H ":
                    print("Hay viento")
            elif tablero[i][j] == "A " and i == 0 and j < 3:
                if tablero[i+1][j]== "H " or tablero[i][j+1]== "H " or tablero[i][j-1]== "H ":
                    print("Hay viento")
            elif tablero[i][j] == "A " and i >0 and i < 3 and j > 0 and j < 3:
                if tablero[i][j+1]== "H " or tablero[i][j-1]== "H " or tablero[i+1][j]== "H " or \
                    tablero[i-1][j]== "H ":
                    print("Hay viento")        
            elif tablero[i][j] == "A " and i == 3 and j ==3:
                if tablero[i][j-1]== "H " or tablero[i-1][j]== "H ":
                    print("Hay viento")        
            elif tablero[i][j] == "A " and i == 3 :
                if tablero[i][j-1]== "H " or tablero[i][j+1]== "H " or tablero[i-1][j]== "H ":
                    print("Hay viento")
            elif tablero[i][j] == "A " and j == 3 :
                if tablero[i][j-1]== "H " or tablero[i+1][j]== "H " or tablero[i-1][j]== "H ":
                    print("Hay viento")

# Función para encontrar al jugador en el tablero
def encontrar_jugador(tablero):
    for i in range(4):
        for j in range(4):
            if tablero[i][j] == "A ":
                return (i, j)

# Función para verificar si se ha ganado el juego
def juego_ganado(tablero2):
    if tablero2[0][0]!="T " and tablero2[0][1]!="T " and tablero2[0][2]!="T " and tablero2[0][3]!="T " \
        and tablero2[1][0]!="T " and tablero2[1][1]!="T " and tablero2[1][2]!="T " and tablero2[1][3]!="T " \
        and tablero2[2][0]!="T " and tablero2[2][1]!="T " and tablero2[2][2]!="T " and tablero2[2][3]!="T " \
        and tablero2[3][0]=="A " and tablero2[3][1]!="T " and tablero2[3][2]!="T ":
        imprimir_tablero(tablero2)
        return True

#Función para encontrar el tesoro  
def encontrar_tesoro(tablero2):
    if tablero2[0][0]!="T " and tablero2[0][1]!="T " and tablero2[0][2]!="T " and tablero2[0][3]!="T " \
        and tablero2[1][0]!="T " and tablero2[1][1]!="T " and tablero2[1][2]!="T " and tablero2[1][3]!="T " \
        and tablero2[2][0]!="T " and tablero2[2][1]!="T " and tablero2[2][2]!="T " and tablero2[2][3]!="T " \
        and tablero2[3][0]!="T " and tablero2[3][1]!="T " and tablero2[3][2]!="T ":
        print("¡Tienes el Tesoro!")

# Función para mezclar el tablero
def preparar_tablero(tablero2):
    probPozo = 0
    wumpus_x = random.randint(0,2)
    tesoro_x = random.randint(0,2)
    wumpus_y = random.randint(0,3)
    tesoro_y = random.randint(0,3)

    for i in range(4):   
        for j in range(4):
            probPozo = random.randint(1,5)
            if probPozo == 1:
                tablero2[i][j]="H "
    tablero2[wumpus_x][wumpus_y] = "W "
    tablero2[tesoro_x][tesoro_y] = "T "
    tablero2[3][0]="A "
            
        
# Inicializar el tablero
tablero = [["  ", "  ", "  ", "  "], ["  ", "  ", "  ", "  "], ["  ", "  ", "  ", "  "], ["A ", "  ", "  ", "  "]]
tablero2 = [["  ", "  ", "  ", "  "], ["  ", "  ", "  ", "  "], ["  ", "  ", "  ", "  "], ["  ", "  ", "  ", "  "]]

# Mezclar el tablero
preparar_tablero(tablero2)

numMov=0

# Juego principal
while not juego_ganado(tablero2):

    imprimir_tablero(tablero)
    #imprimir_tablero(tablero2)

    viento(tablero2)
    hedor(tablero2)
    encontrar_tesoro(tablero2)

    movimiento = input("Ingresa una dirección (arriba (W), abajo (S), izquierda (A), derecha (D)): ")

    player_x, player_y = encontrar_jugador(tablero)

    if (movimiento == "w" or movimiento == "W") and player_x > 0 and player_x < 4: #arriba
        if tablero2[player_x - 1][player_y] == "W ":
            print("\n\t\tTe ha matado el Wumpus. Perdiste")
            break
        elif tablero2[player_x - 1][player_y] == "H ":
            print("\n\t\tHas caído en un pozo. Perdiste")
            break
        else:
            tablero[player_x - 1][player_y] = "A "
            tablero[player_x][player_y] = "  "
            tablero2[player_x - 1][player_y] = "A "
            tablero2[player_x][player_y] = "  "
    elif (movimiento == "s" or movimiento == "S") and player_x >= 0 and player_x < 3: #abajo
        if tablero2[player_x + 1][player_y] == "W ":
            print("\n\t\tTe ha matado el Wumpus. Perdiste")
            break
        elif tablero2[player_x + 1][player_y] == "H ":
            print("\n\t\tHas caído en un pozo. Perdiste")
            break
        else:
            tablero[player_x + 1][player_y] = "A "
            tablero[player_x][player_y] = "  "
            tablero2[player_x + 1][player_y] = "A "
            tablero2[player_x][player_y] = "  "
    elif (movimiento == "a" or movimiento == "A") and player_y > 0 and player_y < 4: #izquierda
        if tablero2[player_x][player_y - 1] == "W ":
            print("\n\t\tTe ha matado el Wumpus. Perdiste")
            break
        elif tablero2[player_x][player_y - 1] == "H ":
            print("\n\t\tHas caído en un hoyo. Perdiste")
            break
        else:
            tablero[player_x][player_y - 1] = "A "
            tablero[player_x][player_y] = "  "
            tablero2[player_x][player_y - 1] = "A "
            tablero2[player_x][player_y] = "  "
    elif (movimiento == "d" or movimiento == "D") and player_y >= 0 and player_y < 3: #derecha
        if tablero2[player_x][player_y + 1] == "W ":
            print("\n\t\tTe ha matado el Wumpus. Perdiste")
            break
        elif tablero2[player_x][player_y + 1] == "H ":
            print("\n\t\tHas caído en un pozo. Perdiste")
            break
        else:
            tablero[player_x][player_y + 1] = "A "
            tablero[player_x][player_y] = "  "
            tablero2[player_x][player_y + 1] = "A "
            tablero2[player_x][player_y] = "  "
    else:
        print("Movimiento no válido. Intenta de nuevo.")
imprimir_tablero(tablero2)

if juego_ganado(tablero2):
    print("\t\t¡Felicidades! ¡Has ganado!")
