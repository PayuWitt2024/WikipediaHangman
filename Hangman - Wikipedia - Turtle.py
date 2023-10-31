# importing all required libraries, random for randomising word selection, turtle for graphics and urllib.request to open URLs
import random
import turtle
import urllib.request 
# obtains a response from the request of opening url https://en.wikipedia.org/wiki/Special:Random'
with urllib.request.urlopen('https://en.wikipedia.org/wiki/Special:Random') as response: 
  # .read() returns the bytes of the response object, and decodes the bytes by the standard Unicode Transformation Format 8. Stores the decoded text into var html
  html = response.read().decode('utf-8')

countx = 0 # will act as the validator for upcoming while loop
t1 = turtle.Turtle() # t1 will act as the "side-decorative" writer/drawer
t2 = turtle.Turtle() # t2 will act as the writer/drawer for hidden/revealed text display
life_turtle1 = turtle.Turtle() # life_turtle1 will act as the writer/drawer for "You have  lives left"
life_turtle2 = turtle.Turtle() # life_turtle 2 will act as the writer/drawer for the amount of lives shown on screen
t1.hideturtle() # hidesmturtles for aesthetic
t2.hideturtle()
life_turtle1.hideturtle()
life_turtle2.hideturtle()
turtle.hideturtle()
x = -80 # sets the coordinates for the basis of the main hangman drawings
y = -80 
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] # this will act as the validator variable in ensuring that no symbol/uppercase/number inputs etc. are bypassed
while countx == 0: # procedure to obtain random word from url
  county = 0 # variable to act as validator that every character from random word is a "valid" character (refer to list letters)
  wordlist = html.split() 
  wordchoice = random.choice(wordlist)
  length = len(wordchoice)
  while length < 6 or length > 10: # This section looks at all the randomly selected words, to find a suitable one for the game
    wordchoice = random.choice(wordlist) # the criteria is that the word is longer than 5 chars but less than 11 chars
    length = len(wordchoice)
  wordchoice =  wordchoice.lower().strip()
  for a in wordchoice: # after the word has been stripped of spaces and is turned into lowercase, the section checks whether every single character is a lowercase alphabetical char or not
    if a in letters:
      county += 1
  if county == len(wordchoice):
    countx += 1 # else previous check runs false (not every char is lowercase alphabetical the while loop starts over
if countx == 1:
  word = wordchoice
  countx -= 1
word_list = list(word) # makes a list where each element == each char of the word
plate = (("_") * len(word_list)) # makes a string var that will act as a sort of 'plate' to display revealed/hidden word characters on screen
print("""Welcome to Payu's hangman
You have 6 lives, good luck!
""")
hidden_word = list(plate)  # separates each underscore character of plate and puts into a list
guesses = []
count = 0 # count will be used for lives
draw_count = 0 # draw_count is used to determine whether to start drawing. eg. if the user guesses again but count is unchanged, program will redraw the part of the hangman drawing unless draw_count is used

def char_index(word,guess): # modularisation of function to return a list of the indices (positions) where a certain letter is found within a word
  indices = []
  for position in range(len(word)):
    letter = word[position]
    if letter == guess:
      indices.append(position)
  return indices

def head(x,y): # modularisation of function for turtle to draw every part of the hangman up to the head. Helps make upcoming while loop look less 'fat'
  turtle.clear()
  turtle.penup()
  turtle.setpos(x,y) #default: (-80,-80)
  turtle.pendown()
  turtle.forward(60)
  turtle.penup()
  turtle.setpos(x+30,y)
  turtle.left(90)
  turtle.pendown()
  turtle.forward(150)
  turtle.right(90)
  turtle.forward(100)
  turtle.right(90)
  turtle.forward(50)
  turtle.penup()
  turtle.setpos(x+120,y+90)
  turtle.pendown()
  turtle.circle(10)
  turtle.penup()

# Start the game by using turtle to write the title, by payu, welcome message, and life counter
t1.penup()
t1.setpos(0,150)
t1.write("Hangman", move=False, align=("center"), font=("Arial", 30, "bold"))
t1.penup()
t1.setpos(0,130)
t1.write("By Payu", move=False, align=("center"), font=("Arial", 10, "italic"))
turtle.setpos(0,0)
turtle.write("Welcome to Hangman!", move=False, align=("center"), font=("Arial", 30, "normal"))
t2.penup()
t2.setpos(0,-180)
t2.write(" ".join(plate), move=False, align=("center"), font=("Arial", 20, "normal"))
life_turtle1.penup()
life_turtle1.setpos(200,-180)
life_turtle1.write("You have    lives left!", move = False, align = "center", font = ("Arial", 10, "normal"))
life_turtle2.penup()
life_turtle2.setpos(200,-180)
life_turtle2.write(6-count, move = False, align = "center", font = ("Arial", 10, "normal"))

while hidden_word != word_list and count < 6:
  print(" ".join(plate),"\n")
  guess = input("Guess a letter: ")
  if len(guess) == 1:
    if guess in letters: # validation conditions for user input: 1 character only that is lowercase and in alphabet           
      if guess not in guesses:
        if guess in word_list: 
          indices = char_index(word_list,guess)
          for i in indices:
            hidden_word[i] = guess # for every single position that the user's guess is in the correct word, hidden_word's underscores are replaced by that letter at the same positions
            plate = hidden_word
          t2.clear() # clears/removes the empty plates on the screen and updates it with correct position(s) shown
          t2.penup()
          t2.setpos(0,-180)
          t2.write(" ".join(plate), move=False, align=("center"), font=("Arial", 20, "normal"))
          guesses.append(guess)
        else: 
          count += 1
          guesses.append(guess)
          print("Wrong! You have {} lives left".format(6-count))
        if count == 1 and draw_count == 0:
          life_turtle1.write("You have    lives left!", move = False, align = "center", font = ("Arial", 10, 
          "normal"))
          life_turtle2.clear()
          life_turtle2.color("#1b0501")
          life_turtle2.write(6-count, move = False, align = "center", font = ("Arial", 10, 
          "normal")) # updating the life counter before drawing the hangman
          head(x,y)
          draw_count += 1 # makes sure that this stage of the drawing is not repeated, used for other stages as well
        elif count ==  2 and draw_count == 1:
          life_turtle2.clear()
          life_turtle2.color("#360b01")
          life_turtle2.write(6-count, move = False, align = "center", font = ("Arial", 10, 
          "normal"))
          turtle.setpos(x+130,y+80)
          turtle.pendown()
          turtle.forward(35)
          turtle.penup()
          draw_count += 1
        elif count == 3 and draw_count == 2:
          life_turtle2.clear()
          life_turtle2.color("#800000")
          life_turtle2.write(6-count, move = False, align = "center", font = ("Arial", 10, 
          "normal"))
          turtle.setpos(x+130,y+75)
          turtle.right(45)
          turtle.pendown()
          turtle.forward(20)
          turtle.penup()
          draw_count += 1
        elif count == 4 and draw_count == 3:
          life_turtle2.clear()
          life_turtle2.color("#aa0000")
          life_turtle2.write(6-count, move = False, align = "center", font = ("Arial", 10, 
          "normal"))
          turtle.setpos(x+130,y+75)
          turtle.pendown()
          turtle.left(90)
          turtle.forward(20)
          turtle.penup()
          draw_count += 1
        elif count == 5 and draw_count == 4:
          life_turtle2.clear()
          life_turtle1.clear()
          life_turtle1.color("#d50000")
          life_turtle1.write("You have 1 life left!", move = False, align = "center", font = ("Arial", 10, "normal"))
          turtle.setpos(x+130,y+45)
          turtle.pendown()
          turtle.right(90)
          turtle.forward(22)
          turtle.penup()
          draw_count += 1
        elif count == 6 and draw_count == 5:
          turtle.setpos(x+130,y+45)
          turtle.pendown()
          turtle.left(90)
          turtle.forward(22)
          life_turtle1.clear()
          life_turtle2.clear()
          draw_count += 1
      else:
        print("This letter has already been guessed")
    else:
      print("Please enter a letter that is lowercase")
  else:
    print("Please enter one letter (lowercase) at a time")
    
if count == 6: # losing screen: grey background, no life counter, #a32004 losing message
  turtle.Screen().bgcolor("grey")
  print("You've lost! The word was:", word)
  turtle.penup()
  turtle.setpos(0,-120)
  turtle.color("#A32004")
  turtle.write("You've lost!", move=False, align=("center"), font=("Arial", 20, "bold"))
  turtle.setpos(0,-150)
  turtle.write("The word was: {}".format(word), move=False, align=("center"), font=("Arial", 20, "bold"))
  life_turtle2.clear()

if hidden_word == word_list and count > 0: # no life counter, green winning message
  life_turtle1.clear()
  life_turtle2.clear()
  print(" ".join(plate),"\n")
  print("Well done!")
  turtle.penup()
  turtle.setpos(0,-135)
  turtle.color("green")
  turtle.write("You've won!", move=False, align=("center"), font=("Arial", 20, "bold"))

if hidden_word == word_list and count == 0: # special ending for no wrong guesses made
  print(" ".join(plate),"\n")
  print("Well done!")
  turtle.clear()
  turtle.setpos(0,0)
  turtle.color("green")
  turtle.write("You've won!", move=False, align=("center"), font=("Arial", 20, "bold"))
  turtle.penup()
  turtle.setpos(0,-30)
  turtle.write("Flawless victory!", move=False, align=("center"), font=("Arial", 20, "bold","underline"))
