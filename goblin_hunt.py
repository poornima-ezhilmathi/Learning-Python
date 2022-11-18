import random
def goblin_hunt():
    print("Welcome to the Angry Goblin Hunt")
    print("An award-winning game full of adventure and excitement (!)")
    input("Type in your name:")
    print("Stephen, do you think you can find the goblin hiding in the kitchen cupboards?")
    num=int(input("Input the level of difficulty"))
    cupboard="|_|"
    cupboards = (num * cupboard)
    print(cupboards)
    while True:
          val=int(input("Which cupboard do you think the goblin is in [type in number]:"))
          usernum=random.randint(1, num)
          print(usernum)
          if val == usernum:
            print("Well done!! You have found the goblin. He was so scared he ran away.")
            break
          else:
            print("Sorry! The goblin is still lurking somewhere else")
goblin_hunt()