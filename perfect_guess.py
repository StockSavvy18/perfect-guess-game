# PROJECT- THE PERFECT GUESS

import random
n=random.randint(1,100)
a=-1                                           # The loop starts because a != n (since n is always between 1 and 100, and -1 can never equal n).It avoids using a random or valid number, which might accidentally match n and skip the loop entirely.
guess=1
while(a!=n):

  a=int(input("Guess the number: "))
  if (a>n):
    print('pick a lower number please')
    guess+=1
  elif(a<n):
    print('pick a higher number please')
    guess+=1
print(f'you have guessed the correct number {n}, in {guess} attempts')
