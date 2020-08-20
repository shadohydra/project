import pyttsx3
import os

print("How may i help you \n")
pyttsx3.speak("Hello Master! Let me know how may i help you")

pyttsx3.speak("Hear are some options listed below")

print("0 : Studies \n")
pyttsx3.speak("studies")

print("1 : Entertainment \n")
pyttsx3.speak("entertainment")

print("2 : Official work \n")
pyttsx3.speak("official works")

print("3 : Internet \n")
pyttsx3.speak("browsing internet")

print("4 : Programming \n")
pyttsx3.speak("programming")

print("5 : Help \n")
pyttsx3.speak("and help")

pyttsx3.speak("master make you choice")

a = input("make your choice : ")

if ("0" in a) or ("studies" in a) or ("Studies" in a) or ("study" in a):

  print("Your Have Selected Studies \n")
  pyttsx3.speak("Your have selected studies")

  print("Here are some topics which you can learn \n")
  pyttsx3.speak("here are some topics, which you can learn")

  print("1 : Linux \n")
  pyttsx3.speak("Linux")

  print("2 : Python \n")
  pyttsx3.speak("Python")

  print("3 : Docker \n")
  pyttsx3.speak("Docker")

  pyttsx3.speak("select topic, for studies")
  top = input("Select Topic, for studies : ")

  if ("Linux" in top) or ("linux" in top) or ("1" in top):
    print("You Have Selected Linux \n")
    pyttsx3.speak("you have selected linux, Enjoy your Linux Classes")
    os.system("chrome https://www.youtube.com/watch?v=8Q83qs2MAVA")

  elif ("Python" in top) or ("python" in top) or ("2" in top):
    print("You Have Selected Python \n")
    pyttsx3.speak("You have slected python, Enjoy your python classes")
    os.system("chrome https://www.youtube.com/watch?v=VW0PUBSxVxg")

  elif ("Docker" in top) or ("docker" in top) or ("3" in top):
    print("You Have Selected Docker \n")
    pyttsx3.speak("You Have Selected Docker, Enjoy your Docker Classes")
    os.system("chrome https://www.youtube.com/watch?v=-lpDRE3Fcj0")

  else:
    print("Topic Not Available")
    pyttsx3.speak("Topic not available")

if ("1" in a) or ("entertainmet" in a):
  print("You have selected Entertainment \n")
  pyttsx3.speak("you have selected entertainmert")

  print("How Can I Entertain You : \n")
  pyttsx3.speak("how i can entertain you master, by playing music, or by playing movies")
  ent = input()
  if ("playmusic" in ent) or ("music" in ent) or ("play music" in ent) or ("songs" in ent):
    print("Enjoy your Music")

    pyttsx3.speak("Enjoy your music master, hope your mind will get fresh \n")
    os.system("wmplayer")

  elif ("playmovie" in ent) or ("movies" in ent) or ("movie" in ent):
    pyttsx3.speak("which type of movie, you want to watch, master")
    print("1 : Horror \n")
    pyttsx3.speak("horror movies")

    print("2 : Romantic \n")
    pyttsx3.speak("or romantic movies")

    pyttsx3.speak("Select you movie mood \n")
    mov = input("Select your Mood : ")
    if ("horror" in mov) or ("horror movies" in mov) or ("horror movies" in mov) or ("1" in mov):
      print("Here are some list of Horror Movies ")
      pyttsx3.speak("choose some movies from the list")
      print("1 : Anabelle \n")
      pyttsx3.speak("Anabelle")

      print("2 : The Conjuring \n")
      pyttsx3.speak("The Conjuring")

      print("3 : A Quiet Place \n")
      pyttsx3.speak("or A quite place")

      pyttsx3.speak("choose one movie master")
      li = input("Enter a movie name : ")

      if ("Anabelle" in li) or ("anabelle" in li) or ("1" in li):
        print("Enjoy your Anabelle, Movie")
        pyttsx3.speak("enjoy anabelle movie, but dont't scare ")

      elif ("The Conjuring" in li) or ("theconjuring" in li) or ("2" in li):
        print("Enjoy your The Conjuring, Movie")
        pyttsx3.speak("enjoy conjuring movie, but dont't scare ")

      elif ("A Quiet place" in li) or ("aquiteplace" in li) or ("quite place" in li) or ("3" in li):
        print("Enjoy your A Quiet Place, Movie")
        pyttsx3.speak("enjoy a quiet place, but dont't scare ")
      else:
        print("Not-Availabele")
        pyttsx3.speak("sorry not available")

      os.system("wmplayer")

    if ("romantic" in mov) or ("romantic movies" in mov) or ("Romantic Movies" in mov) or ("2" in mov):
      print("Here are some Romantic movie list")

      print("1 : Dil Bechara")
      pyttsx3.speak("dil bechara")

      print("2 : Kedarnath")
      pyttsx3.speak("Kedarnath")

      print("3 : Raabta")
      pyttsx3.speak("raabta")

      pyttsx3.speak("enter a movie name")
      rl = input("Enter a movie name : ")

      if ("Dil Bechara" in rl) or ("dilbechara" in rl) or ("dil bechara" in rl) or ("1" in rl):
        print("Enjoy Dil Bechara movie")
        pyttsx3.speak("enjoy dil bechara movie, hope your mood will swing")

      elif ("Kedarnath" in rl) or ("2" in rl):
        print("Enjoy Kedarnath Movie")
        pyttsx3.speak("enjoy Kedarnath movie, hope your mood will swing ")

      elif ("Raabta" in rl) or ("raabta" in rl) or ("rabta" in rl) or ("3" in rl):
        print("Enjoy Raabta Movie")
        pyttsx3.speak("enjoy raabta movie, hope your mood will swing")

        os.system("wmplayer")

if ("work" in a) or ("officialwork" in a) or ("officework" in a) or ("2" in a):

  print("You have selected official work \n")
  pyttsx3.speak("you have selected official work")

  print("Here are some platform, where you can work \n")
  pyttsx3.speak("here are some platform where you can work")

  print("1 : Paint \n")
  pyttsx3.speak("paint")

  print("2 : Notepad \n")
  pyttsx3.speak("notepad")

  print("3 : Microsoft-Excel \n")
  pyttsx3.speak("microsoft excel")

  print("4 : Power-Point \n")
  pyttsx3.speak("power point")

  print("5 : Microsoft-Word \n")
  pyttsx3.speak("microsoft word")

  pyttsx3.speak("enter you choice")
  ow = input("Enter your Choice : ")

  if ("paint" in ow) or ("Paint" in ow) or ("1" in ow):
    print("You have selected paint \n")
    pyttsx3.speak("you have selected paint, happy painting")
    os.system("mspaint")

  elif ("Notepad" in ow) or ("notepad" in ow) or ("2" in ow):
    print("You have selected Notepad \n")
    pyttsx3.speak("you have selected notepad, happy working")
    os.system("notepad")

  elif ("microsoft excel" in ow) or ("micosoftexcel" in ow) or ("excel" in ow) or ("3" in ow):
    print("You have selected Microsoft-Excel \n")
    pyttsx3.speak("you have selected microsoft excel, happy working")
    os.system("EXCEL")

  elif ("powerpoint" in ow) or ("Power point" in ow) or ("4" in ow):
    print("you have selected Power-Point")
    pyttsx3.speak("you have selected power point, happy working")
    os.system("POWERPNT")

  elif ("Microsoftword" in ow) or ("word" in ow) or ("microsoft word" in ow) or ("5" in ow):
    print("you have selected Microsoft-Word")
    pyttsx3.speak("you have selected microsoft word, happy working")
    os.system("WINWORD")

if("internet" in a) or ("Internet" in a) or ("3" in a):
  print("You Have Selected Internet")

  print("What Would you Like to Surf")
  pyttsx3.speak("what would you like to surf, here are some topics")

  print("1 : Social Media \n")
  pyttsx3.speak("social media")

  print("2 : Google \n")
  pyttsx3.speak("google emgine")

  print("3 : Wikipedia \n")
  pyttsx3.speak("wikipedia")

  pyttsx3.speak("select your option")
  sel = input("Select you option : ")

  if ("socialmedia" in sel) or ("Social Media" in sel) or ("social media" in sel) or ("1" in sel):
    print("Here are some social media platform \n")
    pyttsx3.speak("here are some social media platform")

    print("1 : Facebook \n")
    pyttsx3.speak("Facebook")

    print("2 : Instagram \n")
    pyttsx3.speak("instagram")

    print("3 : Twitter \n")
    pyttsx3.speak("twitter")

    pyttsx3.speak("select you choice")
    sm = input("Select Your Choice : ")

    if ("facebook" in sm) or ("Facebook" in sm) or ("1" in sm) or ("fb" in sm):
      print("You Have Selected Facebook \n")
      pyttsx3.speak("you have selected facebook,")
      os.system("chrome https://www.facebook.com")

    elif ("instagram" in sm) or ("instagram" in sm) or ("insta" in sm) or ("2" in sm):
      print("You Have Selected Instagram")
      pyttsx3.speak("you have selected instagram")
      os.system("chrome https://www.instagram.com")

    elif ("Twitter" in sm) or ("twitter" in sm) or ("3" in sm):
      print("You Have Selected Twitter")
      pyttsx3.speak("you have selected twitter")
      os.system("chrome https://www.twitter.com")

    else:
      print("Other platform not available")
      pyttsx3.speak("other social media platform, is not available")

  if ("google" in sel) or ("Google" in sel) or ("2" in sel):
    print("You have selected google")
    pyttsx3.speak("you have selected google search engine, happy surfing")
    os.system("chrome https://www.google.com")

  if ("Wikipedia" in sel) or ("wikipedia" in sel) or ("3" in sel):
    print("Your have selected wikipedia")
    pyttsx3.speak("you have selected wikipedia, happy info gathering")
    os.system("chrome https://www.wikipedia.org")

if ("programming" in a) or ("coding" in a) or ("Programming" in a) or ("4" in a):
  print("You have selected programming \n")
  pyttsx3.speak("you have selected programming")

  print("We have only one language for programming \n")
  pyttsx3.speak(" there is only one language, available for programming")

  print("1 : Python \n")
  pyttsx3.speak("python")

  pyttsx3.speak("lets start progamming, with python \n")
  os.system("cmd /k python")


if ("help" in a) or ("5" in a):

  print("Your heave selected help section \n")
  pyttsx3.speak("welcome to help section")

  print("here are some topics \n")
  pyttsx3.speak("here are some, help related topics")

  print("1 : About Author \n")
  pyttsx3.speak("About author")

  print("2 : Update \n")
  pyttsx3.speak("update firmware")

  print("3 : Visit our Website \n")
  pyttsx3.speak("Visit Our website")

  pyttsx3.speak("input your choice")
  hl = input("input your choice : ")

  if ("about" in hl) or ("author" in hl) or ("aboutauthor" in hl) or ("About Author" in hl) or ("1" in hl):
    print("You have selected About Author \n")
    pyttsx3.speak("you have selected about author")
    os.system("chrome https://www.linkedin.com")

  elif ("update" in hl) or ("2" in hl):
    print("you have selected update \n")
    pyttsx3.speak("you have selected update")

    print("Checking for updates ... \n")
    pyttsx3.speak("checking for update")

    print("")
    print("")

    print("No update found")
    pyttsx3.speak("no updates found, currently you are up to date")

  if ("visit our website" in hl) or ("visit" in hl) or ("website" in hl) or ("Website" in hl) or ("Visit" in hl) or ("3" in hl):
    print("Hold a movement we are Redirecting you. \n")
    pyttsx3.speak("hold a movement we are redirecting you")
    os.system("chrome http://www.linuxworldindia.org/")