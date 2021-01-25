import time 
import csv
import sys
import os

from Color_Console import * #https://pypi.org/project/Color-Console/

def main_menu():
  menu()


def menu():

    #ctext("test", "green", "black")

    print("                      Doctor Shoppin'\nBy N1g3l Armenia")
    print()

    choice = input("""
                      A: Play
                      B: Exit
                      C: Credits

                      Please enter your choice: """).lower()

    if choice == "a":
        login()
    elif choice == "b":
        sys.exit()
    elif choice == "c":
        credits()
    else:
        print("You must only select either A or B")
        print("Please try again")
        menu()
    
def login():
   pass

def credits():
    print("NigelAmrenia\n\nSpecial thanks to VolunteerManning,\nOzjew")
    time.sleep(3)
    os.system('cls')
    (menu())
    
    

def end_game():
    print("Start over? Y/N")
    choice = input(">>> Y/N ")
    if choice in yes:
      os.system('cls')
      (intro())
    else:
      sys.exit()

menu()

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes", "Yes"]
no = ["N", "n", "no", "No"]

pills = 0
syringes = 0
condoms = 0

required = ("\nUse only A, B, C, or Y/N\n...\nyou fucking moron.\n")


#"intro"
def intro():
  print ("You wake up in your cramped but cozy double-wide, itchy and constipated. "
  "You check your stash under your bed for them\nsweet, sweet oxies. You grab your "
  "bottle and give it a shake, but you hear no rattle. Lamenting,\nyou don your Carhartt duck canvas "
  "jacket, weathered Timberland steel toes, and set out on your adventure.\nYou decide you should bring "
  "something to pass the time while you wait in the clinic "
  "for the doctor. Do you bring:")
  time.sleep(1)
  print ("""  A. Can of Copenhagen
  B. Sun Drop
  C. A roll of condoms""")
  choice = input(">>> ") 
  if choice in answer_A:
    option_dip()
  elif choice in answer_B:
    print ("\n*My stomach don't feel too good. Oh no! This is the antifreeze laced "
    "Sun Drop I was going to give to my good fer nothin' landlord!!* "
    "\n\nYou die alone, depressed, without pills, waiting on another round "
    "of stimulus checks.")
    time.sleep(2)
    (end_game())

  elif choice in answer_C:
    option_condoms()
  else:
    print (required)
    intro()


#DipOption for which clinic
def option_dip(): 
  print ("\nYou get into your trusty Chevy S10 truck, and hear the squeaks and groans "
  "as you climb aboard the drivers seat. After 3 failed starts, she fires up and you drive on to the clinic. "
  "Do you go to:")
  time.sleep(1)
  print ("""  A. Your brother's wife's nephew's uncle's General Practioner Clinic.
  B. Your childhood friend who has perscribed you benzos before.
  C. The new practice that just opened up in town run by a sultry yet mysterious doctor lady.""")
  choice = input(">>> ")
  if choice in answer_A:
    option_brothersWife()
  elif choice in answer_B:
    print ("\nYou make the turn for the clinic. As you drive down the road, you fumble with your can and narrowly avoid getting "
    "t-boned by a MAC truck hauling Sun Drop. Relieved, you decide to place a massive fucking chaw in your mouth to "
    "celebrate your near destruction. The second you place the fatty-daddy chaw in your mouth, "
    "he 8 point buck you maimed last deer season jumps out "
    "right in front of your car, startling you and causing you to "
    "inhale the mother of all chaws. \n\nYou die alone, depressed, without pills, waiting on a nother round of stimulus checks.")
    time.sleep(2)
    (end_game())
  elif choice in answer_C:
    option_doctorLady()
  else:
    print (required)
    option_dip()



#With option_dip
def option_brothersWife():
  print ("\nYou pull up to your brother's wife's nephew's uncle's clinic,\nonly to see it in derelict condition. "
  "IN your optiate incuded haze of the past 3 years, you forgot Jimbo set fire to "
  "it after they stopped supplying him with dilauded patches. "
  "You could head in and scavenge anything left inside, or head to the "
  "mysterious Lady Doctor's clinic if you don't since it is nearby "
  "Do you check out the inside Y/N?")
  choice = input(">>> ")
  time.sleep(3)
  if choice in yes:
    print ("\nA rusty, termite infested wooden beam comes crashing down "
    "on your head the second you open the door, and you die "
    "without pills, alone, depressed, and waiting on another round of stimulus checks")
    time.sleep(3)
    (end_game())
  else:
    print ("\nAs you head out of the parking lot, a police car roles by and asks what you are doing " 
    "\n'None of your buisness, pig', you reply. He proceeds to beat your ass and lock you up on made up charges. "
    "\nYou sit alone and depressed in county lock up, sick from withdrawl, and waiting on another round of "
    "stimulus checks.")
    time.sleep(3)
    (end_game())


#condom option for which clinic
def option_condoms(): 
  print ("\nYou get into your trusty Chevy S10 truck, and hear the squeaks and groans\n "
  "as you climb aboard the drivers seat. After 3 failed starts, she fires up and you drive on to the clinic. "
  "Do you go to:")
  time.sleep(3)
  print ("""  A. Your brother's wife's nephew's uncle's General Practioner Clinic.
  B. Your childhood friend who has perscribed you benzos before.
  C. The new practice that just opened up in town run by a sultry yet mysterious doctor lady.""")
  choice = input(">>> ")
  if choice in answer_A:
    option_brothersWife2()
  elif choice in answer_B:
    print ("\nYou make the turn for the clinic. As you drive, "
    "you see ole Diamond Phillips, a hooker of which you are very familiar. "
    "You decide your crippling addiction can wait a few moments "
    "\nand you pull up next to her with a "
    "20 dollar bill and the condoms. Right before you're about "
    "to get it on, 3 unmarked police cars roll up "
    "\nand arrest you for solicitation of a prostitute, "
    "but mainly because she's the sheriff deputy's wife "
    " \n\nYou detox alone and depressed in county lock up, "
    "no pills and waiting on another round of stimulus checks.")
    time.sleep(3)
    (end_game())
  elif choice in answer_C:
    option_doctorLady()
  else:
    print (required)
    option_brothersWife2()


#Condom option for brothers wifes clinic
def option_brothersWife2():
  print ("\nYou pull up to your brother's wife's nephew's uncle's clinic, only to see it in derelict condition. "
  "\nIN your optiate incuded haze of the past 3 years, you forgot Jimbo set fire to "
  "it after they stopped supplying him with dilauded patches. "
  "\nYou could head in and scavenge anything left inside, or head to the "
  "mysterious Lady Doctor's clinic if you don't since it is nearby "
  "\n\nDo you check out the inside Y/N?")
  choice = input(">>> ")
  time.sleep(3)
  if choice in yes:
    print ("\nA rusty, termite infested wooden beam comes crashing down "
    "on your head the second you open the door, and you die "
    "without pills, alone, depressed, and waiting on another round of stimulus checks")
    time.sleep(3)
    (end_game())
  else:
    print ("\nAs you head out of the parking lot, a police car roles by and asks what you are doing " 
    "\n\n'None of your buisness, pig', you reply. He proceeds to beat your ass and lock you up on made up charges "
    "\n\nYou sit alone and depressed in county lock up, sick from withdrawl, and waiting on another round of "
    "stimulus checks.")
    time.sleep(3)
    (end_game())


#Option for Doctor Lady With Dip or Condoms
def option_doctorLady():
  print ("\nYou arrive at the mysterious Doctor Lady's practice. You sign in, and since "
  "\nyou are the only patient in its oddly ramshackle lobby, the administrator tells you to head into the examination room. "
  "\nAs you walk by an empty room, you see a bottle of pills sitting unattended.\n\nDo you snag the pills Y/N?")
  choice = input(">>> ")
  if choice in yes:
    pills = 1 #adds pills
  else:
    pills = 0
  print ("\nThe Doctor Lady enters the room and says 'Alright Mr. Lets begin by removing your pants and underwear so I "
  "Can examine\nyour balls and penis")
  time.sleep(3)
  print ("""  A. Reply- ...
  B. Reply- Yes ma'am
  C. Reply- My back hurts. Slipped 'n fell in a Walmart""")
  choice = input(">>> ")
  if choice in answer_A and pills < 0:
    print ("\nShe stares at you vaguely, asks if you're a cop, then tells you to get the fuck out. "
    "\n\nYou go back home to work through the withdrawls, alone and depressed, "
    "with no pills")
    time.sleep(3)
    (end_game())
  if choice in answer_A and pills > 0:
    print ("\nShe stares at you vaguely, asks if you're a cop, then tells you to get the "
    "fuck out.\n\nYou go back home to work through the withdrawls, alone and depressed, "
    "You take the pills but then realize they are herpes medications.")
    time.sleep(3)
    (end_game())
  elif choice in answer_B:
   if pills > 0:
    print ("\nShe begins to beat your meat like a Gorilla in a zoo beats a dumb stupid head child that fell into its enclosure. "
    "After you bust one, you give a curt nod of the head and leave, confused and still fiending for some oxies. You get back home alone, depressed, "
    "and with a bottle of herpes medicine you mistook for opiods. \n\nYou cry and wait for another round of stimulus checks")
    time.sleep(3)
    (end_game())
   else: #If the user didn't grab the pills
     print ("\nShe begins to beat your meat like a Gorilla in a zoo beats a dumb stupid head child that fell into its enclosure. "
    "\nAfter you bust one, you give a curt nod of the head and leave, confused and still fiending for some oxies. You get back home alone, depressed, "
    "\n\nYou cry and wait for another round of stimulus checks. ")
  elif choice in answer_C:
    print ("She looks confused, and asks you if you're a cop")
    option_copDip()
  else:
    print (required)
    print ("\nShe stares at you vaguely, asks if you're a cop, then tells you to get the fuck out. "
    "\n\nYou go back home to work through the withdrawls, alone and depressed, "
    "with no pills")
    time.sleep(3)
    (end_game())


#Option with condoms
def option_copCondoms():
  print ("\nYou feel relief thinking that she will give you the pills "
  "You reply:")
  time.sleep(3)
  print ("""  A. Hell naw, raise hale praise dale.
  B. Are YOU a cop?
  C. No but my back hurts.""")
  choice = input(">>> ")
  if choice in answer_A:
    print ("She replies- 'I don't think you have enough teeth or money to enough my services'. "
    "\n\nYou leave confused and without pills. Alone and depressed, you wait for another round of stimulus checks as you suffer the wirthdrawls.")
    time.sleep(3)
    (end_game())
  elif choice in answer_B:
    print ("\nThe reply satisfies her, and she begins to jerk you off. Realizing you have a roll of condoms, you put one on and she lets you hit it. Nice. "
    "\nYou leave with confusion and a pep in your step that quickly turns to crushing withdrawls. You return home alone and depressed, with no pills. "
    "\n\nYou cry and wait for another round of stimulus checks")
    time.sleep(3)
    (end_game())
  elif choice in answer_C:
    option_backHurts()
  else:
    print (required)
    option_backHurts()


#Option with Dip
def option_copDip():
  print ("\nYou feel relief thinking that she will give you the pills "
  "You reply:")
  time.sleep(3)
  print ("""  A. Hell naw, raise hale praise dale.
  B. Are you a cop?
  C. No but my back hurts.""")
  choice = input(">>> ")
  if choice in answer_A:
    print ("She replies- 'I don't think you have enough teeth or money to enough my services'. "
    "\n\nYou leave confused and without pills. Alone and depressed, you wait for another round of stimulus checks as you suffer the wirthdrawls.")
    time.sleep(3)
    (end_game())
  elif choice in answer_B and pills < 0:
    print ("\nThe reply satisfies her, and she begins to jerk you off like a baker making dough for a wedding cake that is a day late. "
    "You leave with confusion and a pep in your step that quickly turns to crushing withdrawls. You return home alone and depressed, with no pills. "
    "\n\nYou cry and wait for another round of stimulus checks")
    time.sleep(3)
    (end_game())
  elif choice in answer_C:
    option_backHurts()
  else:
    print (required)
    option_backHurts()


#endgame condition
def option_backHurts():
  print ("\nShe replies- 'Well what the fuck am I supposed to do about that? "
  "\nAs you leave confused and sick from withdrawls, you notice a "
  "\nsyringe in a patient room, next to a man in a leather daddy suit with a blindfold, ball gag, and headphones on. "
  "\n\nDo you grab it? Y/N")
  choice = input(">>> ")
  if choice in yes:
    syringes = 1 #adds a syringe
  else:
    syringes = 0
  print ("You get back home, lay down in the bed in your double wide, alone and waiting on\nanother round of stimulus checks.")
  time.sleep(3)
  if syringes > 0:
    print ("\n inject yourself with the syringe you found, and "
  "you notice you have a painfully large and throbbing erection. \nChecking the needle, you realized you "
  "injected yourself with super-viagra, not morphine"
  "\n\nYou wait for another round of stimulus checks.")
  time.sleep(3)
  (end_game())
  #else: #If the user didn't grab the pills
     #print ("\nYou get back to your double wide, shaking, depressed, sick, and without pills. "
     #"\n\nYou wait for another round of stimulus checks.")
     #time.sleep(3)
     #(end_game())


(intro())
(option_dip())
(option_brothersWife())
(option_condoms())
(option_brothersWife2())
(option_doctorLady())
(option_copCondoms())
(option_copDip())
(option_backHurts())
