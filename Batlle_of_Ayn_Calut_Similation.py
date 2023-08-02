import turtle
import time
turtle.bgcolor("sandybrown")
turtle.speed(9)
def mongol_solcir():
    turtle.color("red")
    turtle.begin_fill()
    for i in range(2):
        turtle.fd(100)
        turtle.left(90)
        turtle.fd(50)
        turtle.left(90)
    turtle.end_fill()
def memluk_solcir():
    turtle.color("green")
    turtle.begin_fill()
    for i in range(2):
        turtle.fd(100)
        turtle.left(90)
        turtle.fd(50)
        turtle.left(90)
    turtle.end_fill()
turtle.penup()
turtle.goto(-300,-200)
turtle.pendown()
memluk_solcir()
for i in range(5):
    turtle.penup()
    turtle.fd(100)
    turtle.pendown()
    turtle.penup()
    turtle.fd(65)
    turtle.pendown()
    memluk_solcir()
turtle.penup()
turtle.goto(-300,120)
turtle.pendown()
mongol_solcir()
for i in range(3):
    turtle.penup()
    turtle.fd(100)
    turtle.pendown()
    turtle.penup()
    turtle.fd(65)
    turtle.pendown()
    mongol_solcir()
time.sleep(5)
turtle.clear()
turtle.penup()
turtle.goto(-300,120)
turtle.pendown()
mongol_solcir()
for i in range(3):
    turtle.penup()
    turtle.fd(100)
    turtle.pendown()
    turtle.penup()
    turtle.fd(65)
    turtle.pendown()
    mongol_solcir()
turtle.penup()
turtle.goto(-300,-200)
turtle.pendown()
memluk_solcir()
for i in range(2):
    turtle.penup()
    turtle.fd(100)
    turtle.pendown()
    turtle.penup()
    turtle.fd(65)
    turtle.pendown()
    memluk_solcir()
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.penup()
turtle.pendown()
memluk_solcir()
for i in range(2):
    turtle.penup()
    turtle.fd(100)
    turtle.pendown()
    turtle.penup()
    turtle.fd(65)
    turtle.pendown()
    memluk_solcir()
time.sleep(2)
turtle.clear()
def achivment():
    turtle.penup()
    turtle.goto(-300,-200)
    turtle.pendown()
    memluk_solcir()
    for i in range(5):
        turtle.penup()
        turtle.fd(100)
        turtle.pendown()
        turtle.penup()
        turtle.fd(65)
        turtle.pendown()
        memluk_solcir()
    turtle.penup()
    turtle.goto(-300,-120)
    turtle.pendown()
    mongol_solcir()
    for i in range(3):
        turtle.penup()
        turtle.fd(100)
        turtle.pendown()
        turtle.penup()
        turtle.fd(65)
        turtle.pendown()
        mongol_solcir()
achivment()
time.sleep(2)
turtle.clear()
turtle.penup()
turtle.goto(-200,400)
turtle.pendown()
def not_disipline_mongol_solcir():
    turtle.color("red")
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()
    turtle.penup()
    turtle.right(5)
    turtle.fd(40)
    turtle.pendown()
for i in range(10):
    not_disipline_mongol_solcir()
turtle.penup()
turtle.goto(-300,-200)
turtle.pendown()
memluk_solcir()
for i in range(5):
    turtle.penup()
    turtle.fd(100)
    turtle.pendown()
    turtle.penup()
    turtle.fd(65)
    turtle.pendown()
    memluk_solcir()
time.sleep(3)
turtle.clear()
achivment()
time.sleep(4)
turtle.clear()
turtle.penup()
turtle.goto(-300,-200)
turtle.pendown()
memluk_solcir()
for i in range(5):
    turtle.penup()
    turtle.fd(100)
    turtle.pendown()
    turtle.penup()
    turtle.fd(65)
    turtle.pendown()
    memluk_solcir()
time.sleep(7)
turtle.clear()
# Yazıyı ayarla
text = "Bu bir simülasyon açıklamasıdır.\nBu savaşta önce Baybars komutasındaki atlı birlikler Moğol ordusuna saldırdı.\n Daha sonra geri çekildiler ve bombalar ve oklar ile Moğulları kuşattılar ve dağıttılar. Kaçan Moğol ordusu Ketboğa'nın emriyle harp nizamına girip intihar dalışı gerçekleştirdi ve hepsi öldürüldü."

# Ekranı ayarla
wn = turtle.Screen()
wn.bgcolor("white")

# Turtle'ı ayarla
t = turtle.Turtle()
t.speed(1)

# Metni yazdır
t.penup()
t.goto(-500, 200)  # Yazının başlangıç konumunu ayarla
t.pendown()
t.write(text, align="left", font=("Arial", 12, "normal"))
time.sleep(3)
turtle.clear()
# Yazıyı ayarla
text = "1260 Ayn Calut Meydan Muharebesi\nKesin Memlük Zaferi"

# Ekranı ayarla
wn = turtle.Screen()
wn.bgcolor("black")

# Turtle'ı ayarla
t = turtle.Turtle()
t.speed(1)
t.color("red")
t.penup()
t.goto(-200, 0)  # Yazının başlangıç konumunu ayarla
t.pendown()

# Metni yazdır
t.write(text, align="left", font=("Arial", 30, "bold"))
turtle.done()
###batlle_of_ayn_calut_similation###
    


