<h1 align="center">Easy Python Projects</h1>

This repository is for IT/computer science students in primary or secondary school looking to do some extra coding in python! 

``` python
# List of current projects
[
'Text_To_Symbols.py',
'Turtle_Shape.py'
]
```

## Projects

#### Text_To_Symbols.py

Using python's pyfiglet module (not an in-built module) we can convert ASCII (normal) text and render it in ASCII art fonts!

1) Install the Pyfiglet module

``` python
pip install pyfiglet
```

2) Replace 'TEXT' with any text you wish to render in ASCII art. The font can also be changed to any of the pyfiglet fonts.

``` python
def main():
    print(figlet_format('TEXT', font='standard'))
```

3) To list all pyfiglet fonts, enter the following code into the terminal:

``` console
C:\Users\[USER]\PycharmProjects\pythonProject>pyfiglet -l

Output:
1943____    
3-d
3x5
4x4_offr    
5lineoblique
5x7
...    
```

#### Turtle_Shape.py

Using python's turtle module, we can draw an n-sided polygon onto the screen. By using the formula to work out exterior angles, we can ask the user to choose the number of sides and automatically use that information to create the instructions for the turtle to draw.

1) Import all the functions from the turtle module

``` python
from turtle import *
```

2) Ask the user for the number of sides

``` python
# Ask user the number of sides
n = input("Number of sides: ")

# Convert input to int if input is a number
if n.isnumeric():
    n = int(n)
```
3) Find the exterior angle of a regular polygon with n sides

``` python
# Where n is the number of sides
exteriorAngle = 360 / n
```

3) Iterate over the number of sides and tell the turtle to go forward and turn right

``` python
for i in range(n):
    forward(100)
    right(exteriorAngle)
```

4) Stop the turtle window from instantly closing after it is done

``` python
# So the program doesn't instantly close
Screen().exitonclick()
```

## Credits 

Everything is coded by Alex lo Storto

Licensed under the MIT License.
