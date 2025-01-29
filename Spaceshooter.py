import turtle
import os
import math
import random
import os
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout


#atributos da tela
ti = turtle.Screen()
ti.bgcolor('black')
ti.title('Space Shooter')
ti.bgpic("./PP.png")
#Desenhando a bordar e limitando
turtle.register_shape("inimigo.GIF")
turtle.register_shape("1.GIF")


border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color('white')
border_pen.penup()
border_pen.setposition(-300,-300 )
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

pontos = 0 
pontoVis = turtle.Turtle()
pontoVis.speed(0)
pontoVis.color('white')
pontoVis.penup()
pontoVis.setposition(-290, 270)    
pontuacao = "Pontos: %s" %pontos  
pontoVis.write(pontuacao, False, align="left", font=("Arial", 14, "normal"))
pontoVis.hideturtle()


#criando o jogador

jogador = turtle.Turtle()
jogador.color("white")
jogador.shape("1.GIF")
jogador.penup()
jogador.speed(0)
jogador.setposition(0,-250)
jogador.setheading(90)
jogadorvel = 20

#criando inimigos
inimigos = []
numero_inimigos = 5

for i in range(numero_inimigos):
    inimigos.append(turtle.Turtle())
    
for inimigo in inimigos:
    inimigo.color("red")
    inimigo.shape("inimigo.GIF")
    inimigo.penup()
    inimigo.speed(0)
    x = random.randint(-200, 280)
    y = random.randint(100, 250)
    inimigo.setposition(x, y)
    inimigovel = 2
    


#colocando o jogador pra atirar

municao = turtle.Turtle()
municao.color("yellow")
municao.shape("triangle")                                          
municao.penup()
municao.speed(0)
municao.setheading(90)
municao.shapesize(0.5, 0.5)
municao.hideturtle()

municaovel = 30
recarga = "ready"

#movimentação do jogador


def move_left():
    x = jogador.xcor()
    x -= jogadorvel
    if x < -280:
        x = -280
    jogador.setx(x)
    
def move_right():
    x = jogador.xcor()
    x += jogadorvel
    if x > 280:
        x = 280
    jogador.setx(x)
def atirar():
    global recarga
    if recarga == "ready":
        os.system("afplay D:/PROJETO/site-simples/Nova Pasta/laser.wav")
        recarga = "fire"
        x = jogador.xcor()
        y = jogador.ycor() + 10
        municao.setposition(x, y)
        municao.showturtle()
        
def colisao(c1, c2):
    distancia = math.sqrt(math.pow(c1.xcor()-c2.xcor(), 2) + math.pow(c1.ycor()-c2.ycor(), 2))
    if distancia < 15:
        return True
    else:
        return False
#atriuindo ações ao teclado

turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_left, "a")
turtle.onkey(move_right, "Right")
turtle.onkey(move_right, "d")
turtle.onkey(atirar, "space")
#adicionando a movimentacção do inimigo


while True: 
    for inimigo in inimigos:
        x = inimigo.xcor()
        x += inimigovel
        inimigo.setx(x)
        
        if inimigo.xcor() > 280:
            for i in inimigos:
                y = i.ycor()
                y -= 40
                i.sety(y)  
                inimigovel *= -1  
        if inimigo.xcor() < -280:
           for i in inimigos:
                y = i.ycor()
                y -= 40
                i.sety(y)
                inimigovel *= -1  
            
        if  colisao(municao, inimigo):
            municao.hideturtle()
            recarga = "ready"
            municao.setposition(0, -400)
            x = random.randint(-200, 280)
            y = random.randint(100, 250)
            inimigo.setposition(x, y)
            pontos += 10
            pontuacao = "Pontos: %s" %pontos
            pontoVis.clear()
            pontoVis.write(pontuacao, False, align="left", font=("Arial", 14, "normal"))
            
        if colisao(jogador, inimigo):
            jogador.hideturtle()
            inimigo.hideturtle()
            print("Game Over")
            
    if recarga == "fire":
        y = municao.ycor()
        y += municaovel
        municao.sety(y)
        
    if municao.ycor() > 275:
        municao.hideturtle()
        recarga = "ready"
        
        
delay = input("aperte Enter para finalizar.")
