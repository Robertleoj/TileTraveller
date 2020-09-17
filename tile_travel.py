
def check_directions(x_pos, y_pos):

    """
    Argument: position of player

    Returns: String of legal directions
    """
    #For each direction, if movement is legal, add to output string
    out_str = ""
    if x_pos == 1:
        if y_pos != 3:
            out_str += "e"
        if y_pos != 3:
            out_str += "n"
        if y_pos != 1:
            out_str += "s"
            
    if x_pos == 2:
        if y_pos == 3:
            out_str += "ew"
        if y_pos == 2:
            out_str += "sw"
        if y_pos == 1:
            out_str += "n"

    if x_pos == 3:
        if y_pos == 3:
            out_str += "ws"
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
        x_pos += 1
    return x_pos, y_pos

def print_options(legal_options):
    """
    Argument: all lowercase options
    Prints options
    """
    output_str = 'You can travel:'
    multiple = False

    if 'n' in legal_options:
        output_str += ' (N)orth'

    

    


x_pos = 1
y_pos = 3

# while not (x_pos == 3 and y_pos == 1):

    #Check directions save output,
    #Print options
    #Prompt for direction input
    #Check if direction is valid (in string returned by check_directions())
    #   if not valid, prompt for input again

    #move_player()
    #Repeat until Victory

#else:
#   Print victory message
