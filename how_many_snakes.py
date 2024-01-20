how_many_snakes = 1
snake_string = """
Welcome to Python3!

             ____
            / . .\\
            \  ---<
             \  /
   __________/ /
-=:___________/

<3, Juno
"""

line = """
|
|
|"""
for i in range(3):
    print(line,end='')
print(snake_string * how_many_snakes)