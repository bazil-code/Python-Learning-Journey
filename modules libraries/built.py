# built heart
from turtle import *
color('red', 'yellow')
begin_fill()
left(140)
forward(111)

# first curve
for i in range(200):
    right(1)
    forward(1)
left(120)

# second curve
for i in range(200):
    right(1)
    forward(1)
forward(111)
end_fill()
done()