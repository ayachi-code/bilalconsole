import math
from datetime import datetime

# Benodigde functies en variablen
nu = datetime.now()


# Start code
print("Bilal console V6.0")

# begin scherm

naam = input("type je gebruiksnaam: ")
wachtwoord = input('wachtwoord: ')



# Home

def home():
  aa = input("a is voor rekenmachine b voor een quiz z voor update menu y voor account info en c voor Assistent ")


aa = input("a is voor rekenmachine b voor een quiz z voor update menu y voor account info en c voor Assistent ")

# Function Rekenmachine

def rekenmachine():
  while True:
    a = int(input("Type een getal "))
    b = input("Type een karakternaam ")
    c = int(input("Type een getal "))
    if c == 0 and  b != "+" and b != "-" and b != "*": # and b == "/"
      print("Dat mag niet ")
    else:
      if b == "+":
        som = a + c
        print("Dit is je antwoord " +  str(som))
      elif b == "-":
        som2 = a - c
        print("Dit is je antwoord " + str(som2))
      elif b == "*":
        som3 = a * c
        print("Dit is je antwoord " + str(som3))
      elif b == "/":
        som4 = a / c
        print("Dit is je antwoord " + str(som4))
    


# Quiz

def quiz():
  score = 0
  aaa = input("Wat is de hoofdstad van Nederland ")
  if aaa == "amsterdam":
    print("CORRECT")
    score = score+ 1
    print(score)
    f = int(input("Wat is 8 keer 8 "))
    if f == 64:
        print("Correct ")
        score = score+ 1
        print(score)
        g = int(input("Wat is de wortel van 49 "))
        if g == 7:
            print("Correct")
            score = score+ 1
            print(score)
            vraag = input("Wat is de hoofdstad van belgie ")
        if vraag == "brussel":
            print("Correct")
            score = score+ 1
            print(score) 
            print("Dit waren alle vragen je score is " + str(score))
         
       

# Credit Info

def info():
  z = input("Druk op z om  de Update geschiedenis weertegeven druk op i om de account settings weertegeven ")
  if z == "z":
    print("Welkom bij de update geschiedenis ")
    print("Version 1.0: Rekenmachine is toegevoegd")
    print("Version 1.5: Quiz Versie 1 is toegevoegd")
    print("Version 2.0: Rekenmachine is bijgewerkt: Delen door 0 is niet toegestaan")
    print("Version 2.5: Info menu is toegevoegd")
    print("Version 3.0: Account Center is toegevoegd")
    print("Version 3.5: Je kunt nu je account gegevens")
    print("Version 4.0: Je hebt nu score bij de quiz")
    print("Version 5.0: Bugs zijn gefikst van account gegevens en home : )))")


# account info

def account():
  spanje = input("Druk op d om naar je account gegevens tegaan ")
  if spanje == "d":
      print("Gebruiksnaam: " + str(naam))
      print("Wachtwoord: " + str(wachtwoord))
      nederland = input("Wil je naar de home menu gaan ")
      if nederland == "ja":
          home()
      else:
          print("Ingevoeren karakter is onjuist ")
          account()



# Admin account login gebruiksnaam 

def naamadminlogin():
  anaam = input("Type gebruiksnaam van admin: ")
  if anaam == "bilal":
    print("Correct gebruiksnaam : ) ")
    wachtwoordadminlogin()
  elif anaam != "bilal":
    print("Fout gebruiksnaam of wachtwoord probeer het nog eens ")
    naamadminlogin()


# Admin account login wachtwoord

def wachtwoordadminlogin():
  awachtwoord = input('wachtwoord van Admin : ')
  if awachtwoord == "test123":
    print("Correct wachtwoord : ) ")
    admin()
  elif awachtwoord != "test123":
    print("Fout wachtwoord")
    naamadminlogin()   
  


# Admin account bilal 

def admin():
  print("Welkom admin bilal : ) ")
  admin = input("a is voor gebruiker beheer ")
  if admin == "a":
    adminu()
 



# Admin: gebruiker beheer 

def adminu():
  print("Welkom bij admin user beheer  ")
  print("gebruiker1 username: " + str(naam))
  print("gebruiker1 wachtwoord: " + str(wachtwoord))
  x = input("Wil je naar de Admin menu gaan ja of nee ? ")
  if x == "ja":
    admin()
  elif x == "nee":
    adminu()



# Assistent hulp 

def hulp():
  while True:
    xx = input("Waarmee kan ik u helpen: ")
    if xx == "welke dag is het vandaag":
      print("Het is vandaag de " + str(nu.day) + " dag van de maand")
    elif xx == "hoe laat is het":
      print('het is %s:%s:%s' % (nu.hour, nu.minute, nu.second))
    elif xx == "wie is de maker":
      print("De maker is bilal")
    elif xx == "hallo":
      print("Hallo " + str(naam))
    elif xx == "hoe gaat het":
      print("met mij gaat het goed ")
    elif xx == "wie ben jij":
      print("Ik ben jouw virtuelen Assistent : )")
    elif xx == "Welke Versie ben jij":
      print("Hmmm vraag dat maar aan de admin")
    elif xx == "wie is de admin":
      print("Dat is bilal")
    elif xx == "wat is mijn wachtwoord":
      print("Dat mag ik niet zeggen")
    elif xx == "wat is mijn naam":
      print("Jow naam is " + str(naam))
    elif xx == "vind je me aardig":
      print("Ja")
    elif xx == "ik vind je niet aardig":
      print("Oke")
    elif xx == "wat is 1 + 1":
      print("Dat is 2")
    elif xx == "wat is de hoofdstad van nederland":
      print("Dat is amsterdam")
    elif xx == "wat vind jij van de admin":
      print("Hij is een geweldig persoon")
    elif xx == "kan ik inloggen als admin":
      print("Nee jij niet")
    else:
      print("Geen juisten opdracht ):")
    
    


   

# Brengt je naar een categorie : )
if aa == "a":
  print("Welkom bij de rekenmachine : )")
  rekenmachine()
elif aa == "b":
  print("Welkom bij de Quiz ")
  quiz()      
elif aa == "z":
  info()
elif aa == "y":
    print("Welkom bij de account Center ")
    account()
elif aa != "a" and aa != "b" and aa != "z" and aa != "y" and aa != "admin" and aa != "c":
  print("Fout karakter ")
  home()
elif aa == "admin":
  naamadminlogin()
elif aa == "c":
  hulp()      
else:
  print("Fout karakter ")
  home()
