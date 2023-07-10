import turtle as t


t.shape("turtle")
screen = t.getscreen()

for i in range(5):
    t.forward(100)
    t.right(144)
    t.forward(100)
    t.left(72)

screen.listen()
screen.mainloop()
