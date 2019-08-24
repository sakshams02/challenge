print("Welcome to the 7-12 challenge\nThere are 2 jars with 7 balls in jar1 and 12 balls in jar2\nThe player has to take out some balls from the jars according to any one of the 2 methods mentioned below at each turn, the one who brings it to 0,0 wins the game.There is only one possibility to wi the game.\nMethod 1: Take out any number of balls from any one of the jars\nMethod 2: Take out equal number of balls from both the jars\nConditon: You start the 7-12 CHALLENGE ")
jar1=7
jar2=12
c=0
while(True):
  print("Your turn")
  x=int(input("Method 1 or 2?"))
  if x==1:
    y=int(input("Which jar?"))
    z=int(input("How many to remove from that jar?"))
    if y==1:
      jar1=jar1-z
    else:
      jar2=jar2-z
  else:
    m=int(input("How many balls to remove from both jars?"))
    jar1=jar1-m
    jar2=jar2-m
  print("Jar1 has",jar1,"balls, Jar2 has",jar2,"balls.")
  if jar1>jar2:
    c=c+1
    jar1,jar2=jar2,jar1
  if jar1==4 and jar2==7:
    print("You found the possibility of winning!!! You Win")
    break
  print("My turn")
  if (jar2-jar1==4 and jar1>6 and jar2>10) or (jar1==6 and jar2>10) or(jar1==10 and jar2>10):
    if jar1>6 and jar1!=10:
      if c==1:
        print("According to method 2, I remove",jar1-6,"from jar2 and",jar2-10,"from jar1")
        print("Jar1 has 10 balls, Jar2 has 6 balls.")
      else:
        print("According to method 2, I remove",jar1-6,"from jar1 and",jar2-10,"from jar2.")
        print("Jar1 has 6 balls, Jar2 has 10 balls.")
        jar1=6
        jar2=10
        if c==1:
          jar1,jar2=jar2,jar1
          c=c-1
    elif jar1==6:
      if c==1:
        print("According to method 1, I remove",jar2-10,"from jar1")
        print("Jar1 has 10 balls, Jar2 has 6 balls.")
      else:
        print("According to method 1, I remove",jar2-10,"from jar2")
        print("Jar1 has 6 balls, Jar2 has 10 balls.")
        jar1=6
        jar2=10
        if c==1:
          jar1,jar2=jar2,jar1
          c=c-1
    else:
      if c==1:
        print("According to method 1, I remove",jar2-6,"from jar1")
        print("Jar1 has 6 balls, Jar2 has 10 balls.")
      else:
        print("According to method 1, I remove",jar2-6,"from jar2")
        print("Jar1 has 10 balls, Jar2 has 6 balls.")
      jar1=10
      jar2=6
      if c==1:
        jar1,jar2=jar2,jar1
        c=c-1
  elif (jar2-jar1==3 and jar1>4 and jar2>7) or (jar1==4 and jar2>7) or (jar1==7 and jar2>7):
    if jar1>4 and jar1!=7:
      if c==1:
        print("According to method 2, I remove",jar1-4,"from jar2 and",jar2-7,"from jar1")
        print("Jar1 has 7 balls, Jar2 has 4 balls.")
      else:
        print("According to method 2, I remove",jar1-4,"from jar1 and",jar2-7,"from jar2.")
        print("Jar1 has 4 balls, Jar2 has 7 balls.")
      jar1=4
      jar2=7
      if c==1:
        jar1,jar2=jar2,jar1
        c=c-1
    elif jar1==4:
      if c==1:
        print("According to method 1, I remove",jar2-7,"from jar1")
        print("Jar1 has 7 balls, Jar2 has 4 balls.")
      else:
        print("According to method 1, I remove",jar2-7,"from jar2")
        print("Jar1 has 4 balls, Jar2 has 7 balls.")
      jar1=4
      jar2=7
      if c==1:
        jar1,jar2=jar2,jar1
        c=c-1
    else:
      if c==1:
        print("According to method 1, I remove",jar2-4,"from jar1")
        print("Jar1 has 4 balls, Jar2 has 7 balls.")
      else:
        print("According to method 1, I remove",jar2-4,"from jar2")
        print("Jar1 has 7 balls, Jar2 has 4 balls.")
      jar1=7
      jar2=4
      if c==1:
        jar1,jar2=jar2,jar1
        c=c-1
  elif (jar2-jar1==2 and jar1>3 and jar2>5) or (jar1==3 and jar2>5) or (jar1==5 and jar2>5):
    if jar1>3 and jar1!=5:
      if c==1:
        print("According to method 2, I remove",jar1-3,"from jar2 and",jar2-5,"from jar1")
        print("Jar1 has 5 balls, Jar2 has 3 balls.")
      else:
        print("According to method 2, I remove",jar1-3,"from jar1 and",jar2-5,"from jar2.")
        print("Jar1 has 3 balls, Jar2 has 5 balls.")
      jar1=3
      jar2=5
      if c==1:
        jar1,jar2=jar2,jar1
        c=c-1
    elif jar1==3:
      if c==1:
        print("According to method 1, I remove",jar2-5,"from jar1")
        print("Jar1 has 5 balls, Jar2 has 3 balls.")
      else:
        print("According to method 1, I remove",jar2-5,"from jar2")
        print("Jar1 has 3 balls, Jar2 has 5 balls.")
      jar1=3
      jar2=5
      if c==1:
        jar1,jar2=jar2,jar1
        c=c-1
    else:
      if c==1:
        print("According to method 1, I remove",jar2-3,"from jar1")
        print("Jar1 has 3 balls, Jar2 has 5 balls.")
      else:
        print("According to method 1, I remove",jar2-3,"from jar2")
        print("Jar1 has 5 balls, Jar2 has 3 balls.")
      jar1=5
      jar2=3
      if c==1:
        jar1,jar2=jar2,jar1
        c=c-1
  elif (jar2-jar1==1 and jar1>1 and jar2>2) or (jar1==1 and jar2>2) or (jar1==2 and jar2>2) :
    if jar1>1 and jar1!=2:
      if c==1:
        print("According to method 2, I remove",jar1-1,"from jar2 and",jar2-2,"from jar1")
        print("Jar1 has 2 balls, Jar2 has 1 ball.")
      else:
        print("According to method 2, I remove",jar1-1,"from jar1 and",jar2-2,"from jar2.")
        print("Jar1 has 1 ball, Jar2 has 2 balls.")
      jar1=1
      jar2=2
      if c==1:
        jar1,jar2=jar2,jar1
        c=c-1
    elif jar1==1 and jar2>2:
      if c==1:
        print("According to method 1, I remove",jar2-2,"from jar1")
        print("Jar1 has 2 balls, Jar2 has 1 ball.")
      else:
        print("According to method 1, I remove",jar2-2,"from jar2")
        print("Jar1 has 1 ball, Jar2 has 2 balls.")
      jar1=1
      jar2=2
      if c==1:
        jar1,jar2=jar2,jar1
        c=c-1
    else:
      if c==1:
        print("According to method 1, I remove",jar2-1,"from jar1")
        print("Jar1 has 1 ball, Jar2 has 2 balls.")
      else:
        print("According to method 1, I remove",jar2-1,"from jar2")
        print("Jar1 has 2 balls, Jar2 has 1 ball.")
      jar1=1
      jar2=2
      if c==1:
        jar1,jar2=jar2,jar1
        c=c-1
  elif jar2-jar1==0 or (jar1==0 and jar2>0):
    if jar1>0 and jar2>0:
      if c==1:
        print("According to method 2, I remove",jar1,"from jar2 and",jar2,"from jar1")
        print("Jar1 has 0 ball, Jar2 has 0 ball.")
      else:
        print("According to method 2, I remove",jar1,"from jar1 and",jar2,"from jar2.")
        print("Jar1 has 0 ball, Jar2 has 0 ball.")
    elif jar1==0:
      if c==1:
        print("According to method 1, I remove",jar2,"from jar1")
        print("Jar1 has 0 ball, Jar2 has 0 ball.")
      else:
        print("According to method 1, I remove",jar2,"from jar2")
        print("Jar1 has 0 ball, Jar2 has 0 ball.")
    else:
      if c==1:
        print("According to method 1, I remove",jar1,"from jar2")
        print("Jar1 has 0 ball, Jar2 has 0 ball.")
      else:
        print("According to method 1, I remove",jar1,"from jar1")
        print("Jar1 has 0 ball, Jar2 has 0 ball.")
    jar1=0
    jar2=0
    if c==1:
      jar1,jar2=jar2,jar1
      c=c-1
  if jar1==0 and jar2==0:
    print("You Lose, Try Again")
    break
