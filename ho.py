pip install python-aiml
import aiml
kernel = aiml.Kernel() 
kernel.learn("C:\\Users\\admin\\Desktop\\New folder\\smile.xml") 
kernel.respond("load assi D")

while True: 
 input_txt= input(">input:")
 if input_txt.lower() == "thank you":
    print("> Bot: Bey Take care ")
    print(">Bot: Eat helthy and stay helthy")	
    break
 response =kernel.respond(input_txt) 
 print(">Bot: "+response)