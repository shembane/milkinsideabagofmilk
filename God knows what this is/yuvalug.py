import pyttsx3
  

converter = pyttsx3.init()
converter.setProperty('rate', 200)
converter.setProperty('volume', 5)

converter.say("ligma")  
inp = input("ligma\n")


if inp == "whats ligma?":
    for i in range(3):
        converter.say("ligma balls")
  


converter.runAndWait()