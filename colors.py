

import turtle as tt
colors=['red','blue','orange','green','yellow','purple']
a1=tt.Turtle()
for x in range(360):
    a1.pencolor(colors[x%6])
    a1.width(x/100+1)
    a1.forward(x)
    a1.left(59)
tt.done()
