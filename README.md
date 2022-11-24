# Langton's ant
Langton's ant is a two-dimensional universal Turing machine with a very simple set of rules but complex emergent behavior. It was invented by Chris Langton in 1986 and runs on a square lattice of black and white cells.

# Rule Set
- At a white square, turn 90° clockwise, flip the color of the square, move forward one unit
- At a black square, turn 90° counter-clockwise, flip the color of the square, move forward one unit

# Result
![alt text](https://github.com/theExplodeGuy/Langton-Ant-Pygame/blob/main/Results/original.png?raw=true)
produced with original.py

# Extension to Multiple Colours
The Cellular Automaton can be extended to more colours and rules.
For example LRRRRRLLR where L = Left and R = Right. 
This rule set will cause the ant:
- to turn L on colour 0 and add 1 to change the colour
- to turn R on colour 1 and add 1 to change the colour
- to turn R on colour 2 and add 1 to change the colour
and so on.

Two variations are shown bellow:

![alt text](https://github.com/theExplodeGuy/Langton-Ant-Pygame/blob/main/Results/cardioid.png?raw=true)
Rule Set: **LLRR**, produced with cardioid.py

![alt text](https://github.com/theExplodeGuy/Langton-Ant-Pygame/blob/main/Results/square.png?raw=true)
Rule Set: **LRRRRRLLR**, produced with square.py
