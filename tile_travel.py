
def check_directions(x_pos, y_pos):

    """
    Argument: position of player

    Returns: String of legal directions
    """
    #For each direction, if movement is legal, add to output string
    out_str = ""
    if x_pos == 1:
        if y_pos == 3:
            out_str += "es"
        if y_pos == 2:
            out_str += "nes"
        if y_pos == 1:
            out_str += "n"
            
    if x_pos == 2:
        if y_pos == 3:
            out_str += "ew"
        if y_pos == 2:
            out_str += "sw"
        if y_pos == 1:
            out_str += "n"

    if x_pos == 3:
        if y_pos == 3:
            out_str += "sw"
        if y_pos == 2:
            out_str += "ns"
        if y_pos == 1:
            out_str += "n"

    return out_str

def move_player(x_pos, y_pos, dir_str):

    """
    Argument: Position and direction to move

    Returns: New position
    """
    #Add appropirate values to x_pos and y_pos and return them
    if dir_str == "n":
        y_pos += 1
    elif dir_str == "s":
        y_pos -= 1
    elif dir_str == "e":
        x_pos += 1
    else:
        x_pos -= 1
    return x_pos, y_pos

def print_options(legal_options):
    """
    Argument: all lowercase options
    Prints options
    """
    directions_str = 'You can travel:'
    multiple = False
    
    for ch in legal_options:
        if multiple:
            directions_str += ' or'
        if ch == 'n':
            directions_str += ' (N)orth'
        if ch == 's':
            directions_str += ' (S)outh'
        if ch == 'e':
            directions_str += ' (E)ast'
        if ch == 'w':
            directions_str += ' (W)est'
        multiple = True
        #Sets the multiple value to True after every iteration of the loop. So every added direction after the first gets ' or' prefixed
    directions_str += '.'

    print(directions_str)
    

    

def game_loop():
        
    x_pos = 1
    y_pos = 1

    while not (x_pos == 3 and y_pos == 1):

        legal_options = check_directions(x_pos, y_pos)
        
        print_options(legal_options)

        direction = input('Direction: ')
        direction = direction.lower()

        if len(direction) == 1 and direction in legal_options:
            x_pos, y_pos = move_player(x_pos, y_pos, direction)

        else:
            print('Not a valid direction!')

    else:
        print('Victory!')

game_loop()