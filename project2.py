#guessing random number generated by computer
import random 

def guess(n):
    num=random.randint(1,n)
    guess=0    
    while guess != num:
        guess = int(input(f"Guess a num between 1 and {n}: "))
        if guess < num:
            print("Low")
        elif guess > num:
            print("HIGH")
    print("Correct")   
guess(10)

#computer guesses the user number with hints 

x=int(input())

def computer(n):
    low=1
    high=n
    feedback=''
    a=5
    for i in range(0,a): #setting a limited number of attempts
        if(a!=2):             
            if low!=high:
                guess= random.randint(low,high)
            else:
                guess = high
            feedback=input(f'is {guess} correct : ').lower()
            if feedback=='high':
                high=guess-1
                print(f"you have {a-1} chances left")
                a=a-1
            elif feedback == 'low':
                low= guess+1
                print(f"you have {a-1} chances left")
                a=a-1
            elif feedback=='c':
                print("I WON !!")
                break
        else:
            x=input("Can you give us a hint\n yes or no:  ").lower()
            if x=='yes':
                lower=int(input('The nearest lower number in multiple of 10 of your number: '))
                higher=int(input('The nearest higher number in multiple of 10 of your number: '))
                for i in range(1,a):
                    if lower!=higher:
                        guess= random.randint(lower,higher)
                    else:
                        guess = higher
                    feedback=input(f'is {guess} correct : ').lower()
                    if feedback=='higher':
                        higher=guess-1
                        print(f"you have {a-1} chances left")
                        a=a-1
                    elif feedback == 'lower':
                        lower= guess+1
                        print(f"you have {a-1} chances left")
                        a=a-1    
            elif feedback=='c':
                print("I won!!")
                break
            elif x=='no':
                print("I accept defeat")       
computer(x)


#generating a game to guess the number 