import pyttsx3

if __name__ == '__main__':
    print('RObO Speaker initializing ....')
    while True:
        x = input('what do you want me to say: ')
        if x.lower() == 'exit':
            engine = pyttsx3.init()
            engine.say("Bye Bye My Friend")
            engine.runAndWait()
            break

        #init is used to initialize and here it is used for text to speech 
        engine = pyttsx3.init()

        # Queue the text for speech synthesis
        engine.say(x)

        # Process the speech synthesis queue and output the spoken text
        engine.runAndWait()
