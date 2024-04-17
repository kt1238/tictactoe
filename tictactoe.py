import random

def display_grid(grid):
        """Prints out the given grid

        Args:
            grid (list) : a 2D list that represents the board playing board
        """
        print("\n")
        print(f" {grid[0][0]} | {grid[0][1]} | {grid[0][2]}")
        print("---+---+---")
        print(f" {grid[1][0]} | {grid[1][1]} | {grid[1][2]}")
        print("---+---+---")
        print(f" {grid[2][0]} | {grid[2][1]} | {grid[2][2]}")
        print("\n")

def update_grid(grid, cell, mark):
        """Updates The Given Board if cell is empty

        Args:
            grid (list) : a 2D list that represents the playing board
            cell (list): a 1D list of [x,y] that represents a single cell on our board
            mark (string): a character X,O to put in cell depending on player
        Returns:
            boolean: True if successful, False if not successful
        """
        if check_cell_empty(grid,cell):
                grid[cell[0]][cell[1]] = mark
                display_grid(grid)
                return True
        else:
                print("That cell is occupied, try again.")
                return False

def check_cell_empty(grid, cell):
        """Checks given cell to see if its empty

        Args:
            grid (list): a 2D list that represents the playing board
            cell (list): a 1D list of [x,y] that represents a single cell on our board

        Returns:
            boolean: True if empty, False if not empty
        """
        if grid[cell[0]][cell[1]] == " ":
                return True
        return False

def check_grid_full(grid):
        for i in range(3):
                for j in range(3):
                        if check_cell_empty(grid, [i,j]):
                                return False
        return True
                                

def generate_ai_cell(grid):
        while True:
                ai_cell = [random.randint(0,2),random.randint(0, 2)]
                if check_cell_empty(grid,ai_cell) :
                        return ai_cell

def row_found(grid):
        marks = ["X","O"]
        for mark in marks:
                for i in range(3):
                        if grid[i][0] == mark and grid[i][1] == mark and grid[i][2] == mark:
                                return True

def col_found(grid):
        marks = ["X","O"]
        for mark in marks:
                for i in range(3):
                        if grid[0][i] == mark and grid[1][i] == mark and grid[2][i] == mark:
                                return True

def diag_found(grid):
        marks = ["X","O"]
        for mark in marks:
                if grid[0][0] == mark and grid[1][1] == mark and grid[2][2] == mark:
                        return True


# Start Up Message
print("\n\nWelcome to Tic-Tac-Toe\n")
print("A quick tutorial:\n")
print(" 0,0 | 0,1 | 0,2 ")
print("-----+-----+-----")
print(" 1,0 | 1,1 | 1,2 ")
print("-----+-----+-----")
print(" 2,0 | 2,1 | 2,1 ")
print("\nThis is how the board is arranged. To place a 'X' at the top left, type '0,0' when prompted")

# Initialize grid
grid = [[" "," "," "],
        [" "," "," "],
        [" "," "," "]]

# Game Loop
while True:

        # Player's Turn
        while True:
                player_cell = input("Place 'X' at: ")
                player_cell = player_cell.split(",")
                player_cell = [int(char) for char in player_cell]
                if update_grid(grid, player_cell, "X") == True:
                        break
        
        # Check if anyone won?
        if row_found(grid) or col_found(grid) or diag_found(grid):
                print("Player Wins")
                break

        # Check board full
        if check_grid_full(grid):
                print("It's a draw!")
                break

        # Computer's Turn
        print("Computer's Turn")
        ai_cell = generate_ai_cell(grid)
        update_grid(grid, ai_cell, "O")

        # Check if anyone won?
        if row_found(grid) or col_found(grid) or diag_found(grid):
                print("Computer Wins")
                break
        

print("Thanks for playing!")