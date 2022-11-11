def goblin_hunt():
    print("Welcome to the Angry Goblin Hunt")
    print("n award-winning game full of adventure and excitement (!)")
    input("Type in your name:")
    print("Stephen, do you think you can find the goblin hiding in the kitchen cupboards?")
    print("|_||_||_||_||_|")
    i=0
    while i<=5:
          val=int(input("Which cupboard do you think the goblin is in [type in number]:"))
          if val==3:
            i=1
            print("Well done!! You have found the goblin. He was so scared he ran away.")
            break
          else:
            print("Sorry! The goblin is still lurking somewhere else")
            i=i+1

goblin_hunt()