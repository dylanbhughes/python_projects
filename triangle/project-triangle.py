# The aim of this project is to manipulate loops and conditionals 
# by drawing simple geometric figures.
# I provide a skeleton for each function.  Your job is to complete the functions.
#
# NAME: Dylan Hughes
#
def drawLeftTriangle(height,letter):
    """
    Draws a right-angle triangle of height lines made of letter
    with the right angle on the left.
    Always returns None.
    >>> drawLeftTriangle(2,'T')
    T
    TT
    >>> drawLeftTriangle(5,'A')
    A
    AA
    AAA
    AAAA
    AAAAA
    """
    for i in range(height):
        print(letter*(i+1))
    return None

def drawRightTriangle(height,letter):
    """
    Draws a right-angle triangle of height lines with the right angle on the right.
    Always returns None.
    >>> drawRightTriangle(2,'T')
     T
    TT
    >>> drawRightTriangle(5,'F')
        F
       FF
      FFF
     FFFF
    FFFFF
    """
    for i in range(height):
        print(' '*(height-i-1) + letter*(i+1))
    return None

def drawTriangle(height,letter):
    """
    Draws a right-angle triangle of height lines with the right angle on the right
    or on the left, according to the sign of the parameter height.
    Always returns None.
    >>> drawTriangle(5,'T')
    T
    TT
    TTT
    TTTT
    TTTTT
    >>> drawTriangle(-5,'T')
        T
       TT
      TTT
     TTTT
    TTTTT
    """
    if height >= 0:
        drawLeftTriangle(height,letter)
    else:
        drawRightTriangle((height * -1), letter)
    return None



if __name__=='__main__':
    import doctest
    print('Testing...')
    doctest.testmod()
    print('Testing over.')

