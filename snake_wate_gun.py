import random
print("Welcome to SNAKE-WATER-GUN Game zone")
n = int(input("Enter the number of rounds"))
i = 1
won = 0
losse = 0
p = ['s', 'g', 'w']
while(i <= n):
    print("ROUND", i)
    c = input("Enter your choice: ")
    if(c!='g' and c!='s' and c != 'w'):
      print("Invalide input try again")
      continue
    p = random.choice(p)
    if (c == 'g' and p == 'w'):
      print("Cong...... You Won")
      print("Your choice", c)
      print("Opponent choice", p)
      won+=1
    elif (c == 'w' and p == 'g'):
      print("You Losse")
      print("Your choice", c)
      print("Opponent choice", p)
      losse += 1
    elif (c == 'w' and p == 'g'):
      print("Cong...... You Won")
      print("Your choice", c)
      print("Opponent choice", p)
      w+=1
    elif (c == 'g' and p == 's'):
      print("Cong...... You Won")
      print("Your choice", c)
      print("Opponent choice", p)
      losse += 1
    elif (c == 's' and p == 'w'):
      print("Cong...... You Won")
      print("Your choice", c)
      print("Opponent choice", p)

    elif (c == 's' and p == 'g'):
      print("You Losse")
      print("Your choice", c)
      print("Opponent choice", p)
    elif (c == p):
      print("Match Draw")
    i+=1
if (won > losse):
  print("You win the match")
  print("Your score is", won)
elif(won == losse):
  print("Match draw")
else:
  print("You Losse")
  print("Your score is", won)