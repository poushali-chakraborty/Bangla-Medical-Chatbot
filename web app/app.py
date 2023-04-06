from flask import Flask, redirect, url_for, request, render_template
import requests
import json
import jyserver.Flask as jsf
import avro


app = Flask(__name__)
@jsf.use(app)
class App:
    def __init__(self):
       self.count = 0 # Set self variable count equal to 0
       self.test_input=[
          "হাই, আপনি কেমন আছেন?",
          "আমি অসুস্থ বোধ করছি। আপনি কি আমাকে সাহায্য করবেন?",
          "শরীর ব্যথা",
          "মাথায় ব্যথা করেছে",
          "শরীরে ঠাণ্ডা লাগছে",
          "একটি অ্যাপয়েন্টমেন্ট করুন"
       ]


    def test(self):
       if self.count>=len(self.test_input):
          self.count=0
       self.js.document.getElementById('textInput').value = self.test_input[self.count]
       self.increment()
       
       
    def increment(self):
       self.count += 1 # Increment count
        
    def translate(self):
       string= self.js.document.getElementById('textInput').value
       translated= avro.parse(string)
       print("translated: " + translated)
       self.js.document.getElementById('textInput').value = translated

    def send(self):
       print("send")
       result=""
       string= self.js.document.getElementById('textInput').value
       user_msg="user : " + str(string)
       print(user_msg)
       self.js.document.getElementById('textInput').value = ""
       #self.js.document.getElementById('data').innerHTML= user_msg
       self.js.addMsg(user_msg)
       data=json.dumps({"sender": "Rasa","message": user_msg})
       headers = {'Content-type': 'application/json', 'Accept':     'text/plain'}
       response = requests.request("POST",   url="http://localhost:5005/webhooks/rest/webhook", headers=headers, data=data)
 
       response=response.json()

       #result=response[0]["text"]
       for res in response:
          result+=res["text"]+" "
       #self.js.document.getElementById('data').innerHTML= "bot : "+result
       self.js.addMsg("bot : "+result)
       
       


@app.route('/' )
def index():
 return  App.render(render_template('index.html'))



 
if __name__ == '__main__':
  app.run(debug=True)