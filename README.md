# TicTacToe
A game of tic-tac-toe against an AI using the minimax algorithm.
This game does not use any data structures in order to highlight the capablity of the minimax algorithm.
A large increase in efficiency will be obtained through the simple implementation of the following:

```python
class Board:
    def __init__(self,layout):
        self.layout = layout #Layout of tic-tac-toe board
        self.children = [] #To be filled with other Board objects
        self.value = 0 #The value of any one specific node which is normally obtained through the minimax algorithm
```
