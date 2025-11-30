import turtle

# --- Setup window ---
wn = turtle.Screen()
wn.bgcolor("lightblue")     # background color

# --- Setup turtle ---
t = turtle.Turtle()
t.color("darkred")          # turtle color
t.pensize(4)
t.speed(5)

# --- Draw Square Using FOR Loop ---
side_length = 150

for i in range(4):
    t.forward(side_length)
    t.right(90)

# Move turtle to top of square
t.left(90)
t.forward(side_length)

# --- Draw Triangle Using WHILE Loop ---
t.right(90)

count = 0
while count < 3:
    t.forward(side_length)
    t.left(120)
    count += 1

# --- Optional: Add a simple door for extra creativity ---
t.penup()
t.right(30)
t.forward(50)
t.right(90)
t.forward(150)
t.pendown()

t.color("brown")
t.begin_fill()
for i in range(2):
    t.forward(70)
    t.right(90)
    t.forward(40)
    t.right(90)
t.end_fill()

# Keep window open
wn.mainloop()
