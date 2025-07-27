'''
a = 5       # Binary: 0101
b = 3       # Binary: 0011


ones_complement = ~a

print(bin(ones_complement))

print(a & b)   # AND: 0001 -> 1
print(a | b)   # OR: 0111 -> 7
print(a ^ b)   # XOR: 0110 -> 6

print(~a)      # NOT: -(a+1) -> -6

print(a << 1)  # Left Shift: 1010 -> 10
print(a >> 1)  # Right Shift: 0010 -> 2


import turtle

t = turtle.Turtle()
t.forward(100)
t.left(90)
t.forward(100)
turtle.done()

import tkinter as tk

root = tk.Tk()
root.title("Simple GUI")

label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

root.mainloop()

a = 5       # Binary: 0101
b = 3       # Binary: 0011


ones_complement = ~a

print(bin(ones_complement))



a=set("abc")
b={"a","b"}
c={"a","b","c"}
print()
print(b<=a and a<=c)


'''

a={1,2,3}
b={1,2,3,4,5}
c={1,2}


A=set()
B={frozenset()}
C={frozenset(),frozenset({1})}
print(B.issubset(C))


nes_set={
{1,2},
{3,4}}
print(nes_set)




