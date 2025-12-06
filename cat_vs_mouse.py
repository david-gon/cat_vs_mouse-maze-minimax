
import os#te permite interactuar con el sistema operativo, la utilizo para que la interfaz en la terminal siempre se limpie
import msvcrt#es un modulo de la libria c de microsoft, la utilizo para detectar si se presiona una tecla sin detener el programa o sin necesidad de usar enter para continuar
import math# se usa para generar operaciones matematica mas avanzadas, la utilizo para generar la formula euclidiana 

#genero mis laberintos
lab=[
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

]
lab2=[
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
#genero mis personajes y le doy una ubicacion
gato="😾"
raton='🐭'
queso="🧀"
lab[13][11]=raton
lab[2][1]=gato
#defino los movimientos que podran hacer mis personajes
D=(0,1)
A=(0,-1)
W=(-1,0)
S=(1,0)
#genero una funcion para poder encontrar la ubicacion del jugador
def encontrar_jugador(lab,jugador):
    #busco por filas y columnas a la matriz; i=filas, j=columna
    for i in range(len(lab)):
        for j in range(len(lab[i])):
            #cuando encuentro al jugador en su posicion...
            if lab[i][j]==jugador:
                #retorno su ubicacion
                return [i,j]

#guardo la ubicacion de los personajes
cat_ubi=encontrar_jugador(lab,gato)
mouse_ubi=encontrar_jugador(lab,raton)
cheese_ubi=encontrar_jugador(lab,queso)
#la funcion de generar laberinto sirve para darle un diseño a la matriz, por ejemplo, 
#genero las paredes, los caminos y dejando intactos a los personajes
def generar_laberinto(lab):  
    #recorro la matriz por filas y columnas  
    for i in lab:
        for j in i:
            #si es uno coloco la pared
            if j==1:
                print('██',end='')
            else:
                #si en el recorrido encuentro a algun personaje lo dejo asi como está
                if j=="🐭":
                    print('🐭',end='')
                elif j=="😾":
                    print("😾",end="")
                elif j=="🧀":
                    print("🧀",end='')
                #caso contrario es un camino entonces lo genero
                else:
                    print('  ',end='')
        #imprimo un salto de pagina
        print()
#defino una funcion para poder mover al jugador, para ello necesito el laberinto en donde voy a moverme, al jugador que voy a mover, y el movimiento que vot a realizar
def mover_jugador(lab,jugador,movimiento):
    #recorro la matriz fila por columna
    for i in range(len(lab)):
        for j in range(len(lab[i])):
            #recorremos la matriz hata encontrar al jugador, para obtener su ubucacion
            if lab[i][j]==jugador:
                x,y=i,j
                #verfico hacia que direccion se dirije
                if movimiento==D:
                    #accedo hacia que direccion se dirije
                    next_x,next_y=D
                    # genero el movimiento 
                    new_a, new_b= x+next_x, y + next_y
                    #verifico si el moviento está dentro del laberinto para prevenir que salga de ahi y no pueda atravesar las paredes
                    if  0<=new_a <len(lab) and 0<=new_b<len(lab[0]) and lab[new_a][new_b]!=1:
                            lab[new_a][new_b]="🐭"
                            lab[x][y]=' '
                            return lab
                #repito la misma logica para cada movimiento
                elif movimiento==A:
                    next_x,next_y=A
                    new_a, new_b= x+next_x, y + next_y
                    if  0<=new_a <len(lab) and 0<=new_b<len(lab[0]) and lab[new_a][new_b]!=1:
                            lab[new_a][new_b]="🐭"
                            lab[x][y]=' '
                            return lab
                elif movimiento==W:
                    next_x,next_y=W
                    new_a, new_b= x+next_x, y + next_y
                    if  0<=new_a <len(lab) and 0<=new_b<len(lab[0]) and lab[new_a][new_b]!=1:
                            lab[new_a][new_b]="🐭"
                            lab[x][y]=' '
                            return lab
                elif movimiento==S:
                    next_x,next_y=S
                    new_a, new_b= x+next_x, y + next_y
                    if  0<=new_a <len(lab) and 0<=new_b<len(lab[0]) and lab[new_a][new_b]!=1:
                            lab[new_a][new_b]="🐭"
                            lab[x][y]=' '
                            return lab
    #retorno el laberinto con el resultado
    return lab

#la funcion de movimientos_posibles sirve para dirce al gato que movimientos puede hacer, 
#como por ejemplo prevenir que el gato se quede en callejones sin salidas, o que no se quede en un bucle infinito de avanzar y retroceder
#para ello accedemos a la ubicacion del jugador, la matriz en donde está, y su posicion aneterior
def movimientos_posibles(jugador,lab,posicion_anterior=None):
    x,y=jugador
    #generamos un atupla pra pasarle los movimientos que podra realizar desde dicha posicion
    movimiento=set()
    for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
        nx,ny=x+dx,y+dy#generamos el movimiento
        if 0<=nx<len(lab) and 0<=ny<len(lab[0]) and lab[nx][ny]!=1:#validamos que pueda moverse en ese movimiento
            if posicion_anterior is None or (nx, ny) != tuple(posicion_anterior):#verificamos que no haya sido el movimiento anterior
                movimiento.add((nx,ny))#guardamos el movimiento
    return movimiento#retornamos el movimiento
#utilizamos la formula de distancia euclidiana para acceder a una mejor distnacia, mas corta y mas precisa
def hallar_distancia(cat_ubi,mouse_ubi):
    dist_cat_mouse = math.sqrt((cat_ubi[0]-mouse_ubi[0])**2 + (cat_ubi[1]-mouse_ubi[1])**2)
    
    return dist_cat_mouse

MAX_DEPTH=7
#seccion del minimax, los parametros son el laberinto en el que se encuentra, la unicacion del gato, raton y queso, la profundidad + 1, la posicion anterior del gato y del raton
#el objetivo del minimax es que el gato tenga que acortar la distancia entre el gato y el ratón, y el onjetivo del ratón es el de acortar el aumentar esa distancia
def minimax(lab,cat_ubi,mouse_ubication,depth,ia_turn,posicion_anterior_raton=None, posicion_anterior_gato=None):
    #obtenemos la distancia entre el gato y el raton
    cat_mouse=hallar_distancia(cat_ubi,mouse_ubi)
    #si en unos de sus movimientos el gato encuentra al raton, priorisará ese evento ya que lo que busca el numero mas bajo entre ellos
    if cat_ubi==mouse_ubi:
        return -999999
    #en caso de no encontrar al raton aun, lo que hara será devolver la distancia para ver cual camino es el mas corto
    if depth==MAX_DEPTH:
        return cat_mouse
    #si es el turno de la IA
    if ia_turn:
        #definimos una variable con valor de inifnito, para relizar la primera comparacion entre las distanicas
        best_core=float("inf")
        #verifico todos los posibles movimientos que tiene para realizar el gato en su posicion
        for movimiento in movimientos_posibles(cat_ubi,lab,posicion_anterior_gato):
        #generamos la recursividad, esto con el objetivo de que la IA pueda ver y predecir la futuras jugadas y retornar el menor valor
            value=minimax(lab,movimiento,mouse_ubication,depth+1,False, posicion_anterior_raton, cat_ubi)
            #verificamos que la distancia entre el gato y el ratón enviado sea menor al anterior
            if value<best_core:
                #en caso de que el valor enviado sea menor al anterior, lo dejamos como el mejor valor o movimiento, para la IA
                best_core=value
                #lo retornamos una vez analizado todos los movimientos
        return best_core
    #si es el turno del raton
    else:
        #definimos una variable con valor de menos inifnito, para relizar la primera comparacion entre las distanicas
        best_core=float("-inf")
        #verificamos los movimientos posibles que tiene para realizar el raton en su posicion
        for movimiento in movimientos_posibles(mouse_ubi,lab,posicion_anterior_raton):
            #verficamos que la distancia entre el gato y el raton enviado sea mayor que el anterior
            value=minimax(lab,cat_ubi,movimiento,depth+1, True,mouse_ubi, posicion_anterior_gato)
            #en caso de que sea mayor, lo dejamos coo el mejor valor para el raton ya que lo que el quiere es maximizar la distancia
            if value>best_core:
                #en caso de que sea mayor, lo definimos como mejor movimiento para el raton
                best_core=value
                #retornamos ese valor como el mejor movimiento
        return best_core
ultima_distancia = None

#con get_best_move() lo que hacemos es acceder al mejor movimietno que nos envie el minimax, en ella simulamos el movimiento de la IA con el fin de utilizar la recursividad para hallar el mejor movimiento
#en ella le paso los parametros del laberintom la posicion del gato, del raton y sus posiciones anteriores
def get_best_move(lab,cat_ubi,mouse_ubi,posicion_anterior_raton=None, posicion_anterior_gato=None):
    #definimos una variable infinita para comparar la distancia más corta entre el gato y el raton
    best_score=float('inf')
    #definmos una variable para el mojor movimiento
    best_move= None
    #verificamos los mejores movimientos para el gato
    for movimiento in movimientos_posibles(cat_ubi,lab,posicion_anterior_gato):
        #verificamos con la recursividad que es lo que pasaría si es que ejecuta ese movimiento
        value=minimax(lab,movimiento,mouse_ubi,0,True,posicion_anterior_raton, cat_ubi)
        #comparamos la distancia mas corta, para encontrar el mejor movimiento
        if value <best_score:
            best_score=value
            #en caso de que encontremos la distancia, dfinimos que ese movimiento es el mejor
            best_move=movimiento
    #etornamos el valor   
    return best_move
ultimo_movimiento_raton = None
ultimo_movimiento_gato = None
def play():
    # seccion de dificultad
    # ia_moves=list()
    global mouse_ubi,lab,queso
    global ultimo_movimiento_raton
    global ultimo_movimiento_gato
    move=1
    print("""escoja su dificultad
1) facil
2) medio
3) dificil
4) hardcore""")

    dificultad=msvcrt.getch()
    dificultad=dificultad.decode("utf-8")
    # print(dificultad)
    if dificultad=='1':
        print("entramos")
        lab=lab
        lab[5][3]=queso
    elif dificultad=='2':
        lab=lab
        lab[5][3]=queso
        lab[13][1]=queso
        lab[1][13]=queso
    elif dificultad=='3':
        lab=lab2 
        lab[13][14]=gato
        lab[23][15]=raton
        lab[1][1]=queso
        lab[1][28]=queso
        lab[1][12]=queso
        lab[9][14]=queso
        lab[7][1]=queso
        lab[17][9]=queso
        lab[23][2]=queso
        lab[17][24]=queso
        lab[28][28]=queso
        lab[23][21]=queso
    elif dificultad=='4':
        lab=lab2
        lab[2][1]=gato
        lab[1][1]=queso
        lab[28][28]=raton
        move=2



    generar_laberinto(lab)
    ia_turn=True

    while True:
        if ia_turn:
            for i in range(move):
                pos_actual=encontrar_jugador(lab,gato)
                old_x,old_y=pos_actual
                print(mouse_ubi)
                pos_antes_de_mover_gato = list(pos_actual)
                ia_move=get_best_move(lab,pos_actual,mouse_ubi,ultimo_movimiento_raton, ultimo_movimiento_gato)
                new_x,new_y=ia_move
                if lab[new_x][new_y]==queso:
                    lab[new_x][new_y]="🧀"
                    lab[old_x][old_y]="  "
                    pos_queso=get_best_move(lab,(new_x,new_y),mouse_ubi,ultimo_movimiento_raton, ultimo_movimiento_gato)
                    xq,yq=pos_queso
                    lab[xq][yq]="😾"
                    
                else:
                    lab[new_x][new_y]="😾"
                    lab[old_x][old_y]="  "
                ultimo_movimiento_gato=pos_antes_de_mover_gato
                pos_actual=(new_x,new_y)
                ia_turn=False
        
        else:
            print('ingrese un movimiento')
            movimiento=msvcrt.getch()
            movimiento=movimiento.decode('utf-8').lower()
            if movimiento=='d':
                # os.system('cls')
                mover_jugador(lab,raton,D)
                
                ia_turn=True
            elif movimiento=='a':
                # os.system('cls')
                mover_jugador(lab,raton,A)
                
                ia_turn=True
            elif movimiento=='w':
                # os.system('cls')
                mover_jugador(lab,raton,W)
                ia_turn=True
            elif movimiento=='s':
                mover_jugador(lab,raton,S)
                ia_turn=True
        mouse_ubi=encontrar_jugador(lab,raton)

        os.system('cls')
        generar_laberinto(lab)
        if encontrar_jugador(lab,raton)==None or encontrar_jugador(lab,queso)==None:
            print("game over")
            return False
play()