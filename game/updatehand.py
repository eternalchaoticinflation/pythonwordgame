def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    n=0
    i=0
    for n in hand.values():#gets you integer of their values
       i=i+n;
   
    return i;

hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1, 'h':3};
print calculateHandlen(hand);

        