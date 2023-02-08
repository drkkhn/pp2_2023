import random
def guess_number():
    unknown = random.randint(1,20)
    t = n = 0 
    name = input("Hello! What is your name?\n")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.\n")
    while n!=unknown:
        n = int(input("Take a guess\n"))
        t+=1
        if n <unknown:
            print("Your guess is too low.")
        elif n > unknown:
            print("Your guess is too big.")
    print (f"Good job,{name}! You guessed my number in {t} guesses!")
guess_number()

def func2(F):
    C = (5/9)*(F-32)
    return(C)
n = int(input())
print(func2(n))


