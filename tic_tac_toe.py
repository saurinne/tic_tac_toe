SIZE = 3
TO_WIN = 3

def create_game():
    board = list()
    
    for line in range(SIZE): 
        board.append(["_"] * SIZE)
        
    return board

def draw_board(board):
    """vykreslí tabulku, prozatím jednoduše"""
    for line in board: 
        for place in line: 
            print(place, end=" ")
        print()

def move_input():
    x = input("Write line: ")
    y = input("Write collumn: ")
    
    return x, y

def check_coordinates(x,y, board): 
    if (x not in range(SIZE)) or (y not in range(SIZE)): 
        raise IndexError("Coordinates outside the board. Try again.")
    
    if board[x][y] != "_": 
        raise IndexError("This position has been already taken. Try different one.")
    
    return "ok"
        
def process_input(board): 
    while True: 
        x, y = move_input()
        
        try: 
            x, y = int(x), int(y)
            check_coordinates(x, y, board)
            return x, y
        except ValueError:
            print("Coordinates must be a number. Try again.")     
        except IndexError as error: 
            print(error)
            
    
def move(board, x, y, symbol):
    board[x][y] = symbol
    
    return board

def end_line(board): 
    for line in board: 
        counter_x = 0
        counter_o = 0
        
        for item in line: 
            if item == "x": 
                counter_x += 1
                counter_o = 0
            elif item == "o": 
                counter_x = 0
                counter_o += 1
            else: 
                counter_x = 0
                counter_o = 0
                
            if counter_x >= TO_WIN: 
                return "x"
            elif counter_o >= TO_WIN: 
                return "o"
        
    return "_"


def end_column(board): 
    for column_number in range(SIZE):
        counter_x = 0
        counter_o = 0
        
        for line in board: 
            if line[column_number] == "x": 
                counter_x += 1
                counter_o = 0
            elif line[column_number] == "o": 
                counter_x = 0
                counter_o += 1
            else: 
                counter_x = 0
                counter_o = 0
                
            if counter_x >= TO_WIN: 
                return "x"
            elif counter_o >= TO_WIN: 
                return "o"
            
    return "_"       
    

def end_diagonal(board): 
    """TO DO"""
    pass
        
def end(board): 
    result = [end_line(board), end_column(board)]

    for item in result: 
        if item != "_": 
            return "The winner is " + item
        
    return ""
    
    
    
def game(): 
    board = create_game()

    for i in range(SIZE**2):
        if i % 2 == 0: 
            symbol = "x"
        else:
            symbol = "o"
            
        draw_board(board)
        
        x, y = process_input(board)
        board = move(board, x, y, symbol)
        
        if end(board): 
            print(end(board))
            break
        
        print()
    
    
game()