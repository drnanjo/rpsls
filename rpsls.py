 
import random
 
# game functions
 
def name2number(name):
    if(name.lower() == ('rock').lower()):
        return 0;
    elif(name.lower() == ('Spock').lower()):
        return 1;
    elif(name.lower() == ('paper').lower()):
        return 2;
    elif(name.lower() == ('lizard').lower()):
        return 3;
    elif(name.lower() == ('scissors').lower()):
        return 4;
    else:
        print("Error")
        quit()
        

def number2name(number):
     
    if(number == 0):
        return 'rock';
    elif(number == 1):
        return 'Spock';
    elif(number == 2):
        return 'paper';
    elif(number == 3):
        return 'lizard';
    elif(number == 4):
        return 'scissors';
    else:
        print("Error")
        
def rpsls(choice): 
 
    print('\n')
     
    # prompt
    print("You chose " + choice)
     
    # conversion of player choice
    player_number = name2number(choice)
     
    # compute random number draw
    comp_number = random.randrange(0, 4)
     
    # conversion of computer choice to string
    comp_choice = number2name( comp_number );
     
    # print out the message for computer's choice
    print("Computer chose " + comp_choice)
     
    # compute difference to determine winnder
    diff = (comp_number - player_number) % 5
     
    # control structure for win
    if( diff == 1 or diff == 2 ):
        print("Computer wins!")
    elif ( diff == 4 or diff == 3 ):
        print("You win!")
    elif( diff == 0 ):
        print("Tie game!")
         
#main runs game until quit
def main():
    play = input("Press any key to play game or q to quit: ")
    
    while (play != ('q').lower()):
        choice = input("Rock, Paper, Scissors, Lizard, Spock?  ")
        rpsls(choice)
        play = input("Press any key to play game or q to quit: ")
        
    print("Goodbye")    
    
main()
    
    
