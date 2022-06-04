"""
Alunos:
Alanis Oliveira Santos - 514114
Alonso Souza de Almeida Junior - 516266
Aline Vitoria Santana Nunes - 514814
"""
import turtle
import random
import time


score = 0
vidas = 3


tela = turtle.Screen()
tela.title("Salve a tartaruga")
tela.bgcolor("black")
tela.bgpic("fundodomar.gif")  # adicionar tela de fundo
tela.setup(width=800, height=600)
tela.tracer(0)

# Sprites que Aline fez
tela.register_shape("canudo.gif")
tela.register_shape("algapnng.gif")
tela.register_shape("tortuguitapng.gif")
tela.register_shape("maçaapng.gif")


# Tartaruga
tartaruga = turtle.Turtle()
tartaruga.speed(1)
tartaruga.shape("tortuguitapng.gif")
tartaruga.color("white")
tartaruga.penup()
tartaruga.goto(0, -250)
tartaruga.direction = "stop"  # para o jogador começar parado

# Criando uma lista de comida
# cada vez que pegar uma comida a lista de comidas aumenta

comida = []

for i in range(7):
    comidas = turtle.Turtle()
    comidas.speed(0)
    comidas.shape("algapnng.gif")
    comidas.color("green")
    comidas.penup()
    comidas.goto(-100, 250)
    comidas.speed = random.randint(1, 3)  # a velocidade é aleatória

    comida.append(comidas)

comida2s = []
for x in range(7):
    comida2 = turtle.Turtle()
    comida2.speed(0)
    comida2.shape("maçaapng.gif")
    comida2.color("green")
    comida2.penup()
    comida2.goto(-200, 250)
    comida2.speed = random.randint(1, 2)  # a velocidade é aleatória

    comida2s.append(comida2)
# Criando uma lista de canudos
canudo = []

for t in range(10):
    canudos = turtle.Turtle()
    canudos.speed(0)
    canudos.shape("canudo.gif")
    canudos.color("red")
    canudos.penup()
    canudos.goto(100, 250)
    # gerar menos canudos, jogo mais fácil
    canudos.speed = random.randint(1, 3)

    canudo.append(canudos)

# Pontuação
pontuacao = turtle.Turtle()
pontuacao.speed(0)
pontuacao.shape("square")
pontuacao.color("white")
pontuacao.penup()
pontuacao.hideturtle()
pontuacao.goto(0, 230)
pontuacao.write("Score: 0  vidas: 3", align="center",
                font=("Arial", 24, "normal"))


# Função de movimentação
def esquerda():
    tartaruga.direction = "left"


def direita():
    tartaruga.direction = "right"


# Teclado
tela.listen()
tela.onkeypress(esquerda, "Left")
tela.onkeypress(direita, "Right")

# loop
while True:
    tela.update()

    # movendo a tartaruga
    if tartaruga.direction == "left":
        tartaruga.setx(tartaruga.xcor() - 1)

    if tartaruga.direction == "right":
        tartaruga.setx(tartaruga.xcor() + 1)

    # checando para não sair da borda
    if tartaruga.xcor() < -390:
        tartaruga.setx(-390)

    elif tartaruga.xcor() > 390:
        tartaruga.setx(390)
#
    for comidas in comida:
        # move a comidas
        comidas.sety(comidas.ycor() - comidas.speed)

        # Checando se as coisas boas estão fora da borda
        if comidas.ycor() < -300:
            comidas.goto(random.randint(-300, 300), random.randint(400, 800))

        # colisão da tartaruga e da comida
        if tartaruga.distance(comidas) < 40:
            # Score
            score += 10

            # mostrando a pontuação
            pontuacao.clear()
            pontuacao.write("Score: {}  vidas: {}".format(
                score, vidas), align="center", font=("Arial", 24, "normal"))

            # movendo a comida pro topo
            comidas.goto(random.randint(-300, 300), random.randint(400, 800))

    for comidas2 in comida2s:
        # move a comidas
        comidas2.sety(comidas2.ycor() - comidas2.speed)

        # Checando se as coisas boas estão fora da borda
        if comidas2.ycor() < -300:
            comidas2.goto(random.randint(-300, 300), random.randint(400, 800))

        # colisão da tartaruga e da comida
        if tartaruga.distance(comidas2) < 40:
            # Score increases
            score += 100

            # mostrando a pontuação
            pontuacao.clear()
            pontuacao.write("Score: {}  vidas: {}".format(
                score, vidas), align="center", font=("Arial", 24, "normal"))

            # movendo a comida pro topo
            comidas2.goto(random.randint(-300, 300), random.randint(400, 800))

    for canudos in canudo:
        # Movendo o canudo
        canudos.sety(canudos.ycor() - canudos.speed)

        if canudos.ycor() < -300:
            canudos.goto(random.randint(-300, 300), random.randint(400, 800))

        if tartaruga.distance(canudos) < 40:
            # diminuir a pontuação
            score -= 100
            vidas -= 1

            # mostrando a pontuação
            pontuacao.clear()
            pontuacao.write("Score: {}  vidas: {}".format(
                score, vidas), align="center", font=("Arial", 24, "normal"))

            time.sleep(1)
            # movendo os canudos para o topo
            for canudos in canudo:
                canudos.goto(random.randint(-300, 300),
                             random.randint(400, 800))

    # zerando a pontuação
    if(vidas == 0):
        pontuacao.clear()
        pontuacao.write("Ops! A tartaruga morreu. Score: {}".format(
            score), align="center", font=("Arial", 24, "normal"))
        break
