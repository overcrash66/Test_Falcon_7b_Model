import requests

while True:
    question = input("ask me a question: ")
    resp = requests.get("http://127.0.0.1:8000/chat?question="+'"'+str(question)+'"')
    msg = str(resp.text)
    msg =msg.replace('\\n',': ')
    msg =msg.replace('\\','')
    msg =msg.replace('/','')
    msg =msg.replace('/','')
    msg = msg.replace('"','')
    msg =msg.replace(' user','')
    print(str(msg)+'\n')
    f= open("data.txt","a+")
    f.write(str(msg)+'\n')
    f.close()    
    