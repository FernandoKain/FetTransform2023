# Bibliotecas a serem usadas
import pyautogui
import time

# pyautogui.click(x=713, y=700)

# Solicita entrada do usuário em relação ao número de atividades entregues.
# var = int(input("Insira o número de alunos que entregaram as atividades: "))

pyautogui.PAUSE = 0.1


# Funções para otimizar o código
def alttab():
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    pyautogui.keyUp('alt')

def controlc():
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('c')
    pyautogui.keyUp('c')
    pyautogui.keyUp('ctrl')

def alttab2():
    pyautogui.keyDown('alt')
    time.sleep(.2)
    pyautogui.press('tab')
    pyautogui.press('tab')
    time.sleep(.2)
    pyautogui.keyUp('alt')

def f2():
    pyautogui.press('f2')

def controlv():
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('v')
    pyautogui.keyUp('v')
    pyautogui.keyUp('ctrl')

def enter():
    pyautogui.press('enter')

def down():
    pyautogui.press("down")

def up():
    pyautogui.press("up")

def right():
    pyautogui.press("right")

def left():
    pyautogui.press('left')

def loop_de_aulas():
    for i in range(5):
        # 1ª aula
        controlc()
        alttab()
        f2()
        controlv()
        enter()
        alttab()

        # 2ª aula
        down()
        controlc()
        alttab()
        f2()
        controlv()
        enter()
        alttab()

        # 3ª aula
        down()
        controlc()
        alttab()
        f2()
        controlv()
        enter()
        alttab()

        # 4ª aula
        down()
        controlc()
        alttab()
        f2()
        controlv()
        enter()
        alttab()

        # 5ª aula
        down()
        controlc()
        alttab()
        f2()
        controlv()
        enter()
        alttab()

        # 6ª aula
        down()
        controlc()
        alttab()
        f2()
        controlv()
        enter()
        enter()
        alttab()

        # ----------------Próximo dia no FET--------------
        up()
        up()
        up()
        up()
        up()
        right()
# -------------Código começa------------------------

# -------------Ajuste das janelas-------------------
alttab()
time.sleep(0.5)
alttab2()
time.sleep(0.5)
alttab()
time.sleep(0.5)
down()
up()


pyautogui.PAUSE = 0.1

#-----------------------6°ano A----------------------
# --------Inicia a transferência-----------
loop_de_aulas()


#-----------------------6°ano B----------------------
# --------Inicia a transferência-----------
# Seleciona a turma - FET
pyautogui.click(x=100, y=50)
for i in range(2):
    up()
for i in range(1):
    down()

pyautogui.click(x=200, y=250)
alttab()

# Seleciona a turma - Excel
for i in range(36):
    up()
right()
down()
alttab()

loop_de_aulas()


#-----------------------6°ano C----------------------
# --------Inicia a transferência-----------
# Seleciona a turma - FET
pyautogui.click(x=100, y=50)
for i in range(3):
    up()
for i in range(2):
    down()

pyautogui.click(x=200, y=250)
alttab()

# Seleciona a turma - Excel
for i in range(36):
    up()
right()
down()
alttab()

loop_de_aulas()


#-----------------------6°ano D----------------------
# --------Inicia a transferência-----------
# Seleciona a turma - FET
pyautogui.click(x=100, y=50)
for i in range(4):
    up()
for i in range(3):
    down()

pyautogui.click(x=200, y=250)
alttab()

# Seleciona a turma - Excel
for i in range(36):
    up()
right()
down()
alttab()

loop_de_aulas()

#-----------------------6°ano E----------------------
# --------Inicia a transferência-----------
# Seleciona a turma - FET
pyautogui.click(x=100, y=50)
for i in range(5):
    up()
for i in range(4):
    down()

pyautogui.click(x=200, y=250)
alttab()

# Seleciona a turma - Excel
for i in range(36):
    up()
right()
down()
alttab()

loop_de_aulas()

#-----------------------6°ano F----------------------
# --------Inicia a transferência-----------
# Seleciona a turma - FET
pyautogui.click(x=100, y=50)
for i in range(6):
    up()
for i in range(5):
    down()

pyautogui.click(x=200, y=250)
alttab()

# Seleciona a turma - Excel
for i in range(36):
    up()
right()
down()
alttab()

loop_de_aulas()

# --------------- BUSCA 9º ANO -------------------------

#-----------------------9°ano A----------------------
# --------Inicia a transferência-----------
# Seleciona a turma - FET
pyautogui.click(x=100, y=50)
for i in range(18):
    up()
for i in range(18):
    down()

pyautogui.click(x=200, y=250)
alttab()

# Seleciona a turma - Excel
for i in range(36):
    up()
right()
down()
alttab()

loop_de_aulas()


#-----------------------9°ano B----------------------
# --------Inicia a transferência-----------
# Seleciona a turma - FET
pyautogui.click(x=100, y=50)
for i in range(19):
    up()
for i in range(19):
    down()

pyautogui.click(x=200, y=250)
alttab()

# Seleciona a turma - Excel
for i in range(36):
    up()
right()
down()
alttab()

loop_de_aulas()

#-----------------------9°ano C----------------------
# --------Inicia a transferência-----------
# Seleciona a turma - FET
pyautogui.click(x=100, y=50)
for i in range(20):
    up()
for i in range(20):
    down()

pyautogui.click(x=200, y=250)
alttab()

# Seleciona a turma - Excel
for i in range(36):
    up()
right()
down()
alttab()

loop_de_aulas()

#-----------------------9°ano D----------------------
# --------Inicia a transferência-----------
# Seleciona a turma - FET
pyautogui.click(x=100, y=50)
for i in range(21):
    up()
for i in range(21):
    down()

pyautogui.click(x=200, y=250)
alttab()

# Seleciona a turma - Excel
for i in range(36):
    up()
right()
down()
alttab()

loop_de_aulas()

#-----------------------9°ano E----------------------
# --------Inicia a transferência-----------
# Seleciona a turma - FET
pyautogui.click(x=100, y=50)
for i in range(22):
    up()
for i in range(22):
    down()

pyautogui.click(x=200, y=250)
alttab()

# Seleciona a turma - Excel
for i in range(36):
    up()
right()
down()
alttab()

loop_de_aulas()


#-----------------------9°ano F----------------------
# --------Inicia a transferência-----------
# Seleciona a turma - FET
pyautogui.click(x=100, y=50)
for i in range(23):
    up()
for i in range(23):
    down()

pyautogui.click(x=200, y=250)
alttab()

# Seleciona a turma - Excel
for i in range(36):
    up()
right()
down()
alttab()

loop_de_aulas()






# ------------------- BUSCA 7º ANO A -----------------------------
#-----------------------7°ano A----------------------
# --------Inicia a transferência-----------
# Seleciona a turma - FET
pyautogui.click(x=100, y=50)
for i in range(24):
    up()
for i in range(6):
    down()

pyautogui.click(x=150, y=400)
alttab()

# Seleciona a turma - Excel
for i in range(36):
    up()
right()
right()
right()
down()
alttab()

loop_de_aulas()


#-----------------------7°ano B----------------------
# --------Inicia a transferência-----------
# Seleciona a turma - FET
pyautogui.click(x=100, y=50)
for i in range(7):
    up()
for i in range(7):
    down()

pyautogui.click(x=150, y=400)
alttab()

# Seleciona a turma - Excel
for i in range(36):
    up()
right()
down()
alttab()

loop_de_aulas()


#-----------------------7°ano C----------------------
# --------Inicia a transferência-----------
# Seleciona a turma - FET
pyautogui.click(x=100, y=50)
for i in range(8):
    up()
for i in range(8):
    down()

pyautogui.click(x=150, y=400)
alttab()

# Seleciona a turma - Excel
for i in range(36):
    up()
right()
down()
alttab()

loop_de_aulas()


#-----------------------7°ano D----------------------
# --------Inicia a transferência-----------
# Seleciona a turma - FET
pyautogui.click(x=100, y=50)
for i in range(9):
    up()
for i in range(9):
    down()

pyautogui.click(x=150, y=400)
alttab()

# Seleciona a turma - Excel
for i in range(36):
    up()
right()
down()
alttab()

loop_de_aulas()



#-----------------------7°ano E----------------------
# --------Inicia a transferência-----------
# Seleciona a turma - FET
pyautogui.click(x=100, y=50)
for i in range(10):
    up()
for i in range(10):
    down()

pyautogui.click(x=150, y=400)
alttab()

# Seleciona a turma - Excel
for i in range(36):
    up()
right()
down()
alttab()

loop_de_aulas()

#-----------------------7°ano F----------------------
# --------Inicia a transferência-----------
# Seleciona a turma - FET
pyautogui.click(x=100, y=50)
for i in range(11):
    up()
for i in range(11):
    down()

pyautogui.click(x=150, y=400)
alttab()

# Seleciona a turma - Excel
for i in range(36):
    up()
right()
down()
alttab()

loop_de_aulas()


#-----------------------8°ano A----------------------
# --------Inicia a transferência-----------
# Seleciona a turma - FET
pyautogui.click(x=100, y=50)
for i in range(12):
    up()
for i in range(12):
    down()

pyautogui.click(x=150, y=400)
alttab()

# Seleciona a turma - Excel
for i in range(36):
    up()
right()
down()
alttab()

loop_de_aulas()


#-----------------------8°ano B----------------------
# --------Inicia a transferência-----------
# Seleciona a turma - FET
pyautogui.click(x=100, y=50)
for i in range(13):
    up()
for i in range(13):
    down()

pyautogui.click(x=150, y=400)
alttab()

# Seleciona a turma - Excel
for i in range(36):
    up()
right()
down()
alttab()

loop_de_aulas()


#-----------------------8°ano C----------------------
# --------Inicia a transferência-----------
# Seleciona a turma - FET
pyautogui.click(x=100, y=50)
for i in range(14):
    up()
for i in range(14):
    down()

pyautogui.click(x=150, y=400)
alttab()

# Seleciona a turma - Excel
for i in range(36):
    up()
right()
down()
alttab()

loop_de_aulas()


#-----------------------8°ano D----------------------
# --------Inicia a transferência-----------
# Seleciona a turma - FET
pyautogui.click(x=100, y=50)
for i in range(15):
    up()
for i in range(15):
    down()

pyautogui.click(x=150, y=400)
alttab()

# Seleciona a turma - Excel
for i in range(36):
    up()
right()
down()
alttab()

loop_de_aulas()


#-----------------------8°ano E----------------------
# --------Inicia a transferência-----------
# Seleciona a turma - FET
pyautogui.click(x=100, y=50)
for i in range(16):
    up()
for i in range(16):
    down()

pyautogui.click(x=150, y=400)
alttab()

# Seleciona a turma - Excel
for i in range(36):
    up()
right()
down()
alttab()

loop_de_aulas()



#-----------------------8°ano F----------------------
# --------Inicia a transferência-----------
# Seleciona a turma - FET
pyautogui.click(x=100, y=50)
for i in range(17):
    up()
for i in range(17):
    down()

pyautogui.click(x=200, y=250)
alttab()

# Seleciona a turma - Excel
for i in range(36):
    up()
right()
down()
alttab()

loop_de_aulas()
