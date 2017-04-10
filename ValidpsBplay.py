from ps4a import *
import time
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    def isGoodhand(hand, word):
        mod=hand.copy();
        assert type(word) is str, False;
        try:
            for L in word:
                mod[L]=mod.get(L,0)-1;
            for i in mod.values():
                if i<0:
                    return False; #False if key in hand is used to much
            return True;

        except KeyError:
            return False;
    
    # Create a new variable to store the maximum score seen so far (initially 0)
    Mscore=0;

    # Create a new variable to store the best word seen so far (initially None)
    BigWord=None;  

    # For each word in the wordList
    for W in wordList:# If you can construct the word from your hand
        if isGoodhand(hand, W)==True:#keyerrors, or used too much will be False 
            
        
            NewScore=getWordScore(W, n);#get the new score for the new word on the list
            # Find out how much making that word is worth
            if NewScore>Mscore: # If the score for that word is higher than your best score
                Mscore=NewScore; #updates the highest score.
                BigWord=W;#updates the word 
            # Update your best score, and best word accordingly
    
    return BigWord;# return the best word you found.


#
# Problem #7: Computer plays a hand
#ScoreCT=0;
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    def displaynewHand(hand):
        """
        Displays the letters currently in the hand.
    
        For example:
        >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
        Should print out something like:
        a x x l l l e
        The order of the letters is unimportant.
    
        hand: dictionary (string -> int)
        """
        for letter in hand.keys():
            for j in range(hand[letter]):
                print letter,              # print all on the same line
        return''; 
    
    try:
        global ScoreCT;#keeps track of score, could use unbound err set ScoreCT to 0
        LScoreCT=ScoreCT;#just using LSCT to set off Error before print
        CPeer=False;
        while calculateHandlen(hand)>0: #while the hand dict still has words
        #STrack=ScoreT;
        
        # As long as there are still letters left in the hand:
        # Display the hand
            print 'Current Hand:  ', displaynewHand(hand)  
        # Ask user for input
        #word=raw_input('Enter word, or a "." to indicate that you are finished: ');#print str(word);
        #in this case the computer inputs
            word=compChooseWord(hand, wordList, n);
        #computer puts word
        #ScoreT=getWordScore(Ginput, n);
        # If the input is a single period:
            if word==None:#computer can't choose a word
                CPeer=True;
                break;
            # End the game (break out of the loop)
            else:
            # Otherwise (the input is not a single period):
            # If the word is not valid:
                if isValidWord (word, hand, wordList)==False:
                    print ('Invalid word, please try again.');
                    print
                    return (playHand(hand, wordList, n)); #recursion
            
                # Reject invalid word (print a message followed by a blank line)
            #Otherwise (the word is valid):
                else:
                    InPScore=getWordScore(word, n);
                    ScoreCT=ScoreCT+InPScore;
                    print ('"' + str(word) + '"' + ' earned ' + str(InPScore) +' points.' + ' Total: ' + str(ScoreCT) + ' points');
                    print
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                # Update the hand
                hand=updateHand(hand, word);
        if CPeer==True:
            print ('Total score: ' + str(ScoreCT)+ ' points.');
            ScoreCT=0;
        else:
            print('Run out of letters. Total score: ' + str(ScoreCT)+ ' points.')
            ScoreCT=0;
    except NameError:
        ScoreCT=0;
        return (compPlayHand(hand, wordList, n))

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    Choice=raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ');
    n=HAND_SIZE;
    def ReChoiceloop(hand, n):
        ReChoice=raw_input('Enter u to have yourself play, c to have the computer play: ')
        if ReChoice=='u':
            playHand(hand, wordList, n);#I have playHand from psA
        elif ReChoice=='c':#now the computer plays, I guess elif solved it
            
            compPlayHand(hand, wordList, n);
        else:
            print('Invalid command.');
            return (ReChoiceloop(hand, n));
            
    if Choice=='n':
        global hand;
        hand=dealHand(n); #new hand is dealt here and feed into ReChoice
        ReChoiceloop(hand,n); #the break from ReChoice breaks the whole thing
        #points me back down to return.
    
    elif Choice=='r':
        #print (hand)
        try:
            
            if len(hand)==0:#there is no hand dealt
                print('You have not played a hand yet. Please play a new hand first!');
                return (playGame(wordList));
            track=hand.copy();
            ReChoiceloop(hand, n);
        except UnboundLocalError:
            print('You have not played a hand yet. Please play a new hand first!');
            return (playGame(wordList));
        except NameError:
            print('You have not played a hand yet. Please play a new hand first!');
            return (playGame(wordList));

            
    
    elif Choice=='e':
        hand={}
        return None;
    
    else:
        print ('Invalid command.');
        return(playGame(wordList));
    #hand=hand.copy();
    #playHand(hand, wordList, n);
    return(playGame(wordList));


if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
compPlayHand({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList, 6);
compPlayHand({'a': 2, 'c': 1, 'b': 1, 't': 1}, wordList, 5);
compPlayHand({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList, 12)
