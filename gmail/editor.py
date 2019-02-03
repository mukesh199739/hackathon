import speech_recognition as sr
import pyttsx3
from convert_text_to_int import text2int
r=sr.Recognizer()
engine=pyttsx3.init()
print("say something");
engine.say('do you like to start the bot ?')
engine.setProperty('volume',0.9)
engine.runAndWait()
while True:
    with sr.Microphone() as source:
        print("listening ..........")
        audio=r.listen(source)
        speech=r.recognize_google(audio)
        print("listened "+speech)
        if speech == "start":
            print("inside start")
            file = open("testfile.txt","w")
            engine.say('opened the python file in readable format. What header files you want to add?')
            engine.setProperty('volume',0.9)
            engine.runAndWait()
            print("listening to audio1 ........")
            audio1=r.listen(source)
            speech1=r.recognize_google(audio1)
            if speech1=="standard":
                print("inside standard")
                file.write("#include<iostream> \n")
                file.write("using namespace std;\n")
                print("added header file");
                engine.say('should i add int main')
                engine.setProperty('volume',0.9)
                engine.runAndWait()
                file.close()
            else:
                continue;
        elif speech == 'main':
            print("inside main")
            file=open("testfile.txt","a")
            file.write("int main(){")
            engine.say('do you want to add any variable ?')
            engine.setProperty('volume',0.9)
            engine.runAndWait()
            file.close()
        elif speech == 'open':
            print("inside open")
            engine.say('how many variables do you want to add ?')
            engine.setProperty('volume',0.9)
            engine.runAndWait()
            print("listening to audio3.............")
            audio3=r.listen(source)
            speech3=r.recognize_google(audio3)
            print(speech)
            i=0
            file=open("testfile.txt","a")
            while i < int(speech3):
                engine.say('enter the value of the variable')
                engine.setProperty('volume',0.9)
                engine.runAndWait()
                print("listen to the value......")
                audio3=r.listen(source)
                speech4=r.recognize_google(audio3)
                print(speech4)
                file.write("int a"+str(i)+"="+speech4+";\n")
                i=i+1
            file.close()

        elif speech == "output":
            print("inside output")
            file=open("testfile.txt","a")
            file.write("cout<<a1<<a2;\n")
            file.close()
            
                    

        elif speech=="over":
            file=open("testfile.txt","a")
            filewrite("}\n")
            file.close()
            print("no problem")
            break;
        else:
            print("inside else")
            break;
            
            
            
            
        


