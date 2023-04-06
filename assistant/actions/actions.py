# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
import re
import requests
import json
from rasa_sdk.events import AllSlotsReset

from dis import dis
from bangla import convert_english_digit_to_bangla_digit
from datetime import date, datetime
from typing import Any, Text, Dict, List


from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from sqlalchemy import false, true

class ActionShowTime(Action):

    def name(self) -> Text:
        return "action_show_time"

    def run(self, dispatcher, tracker, domain):
        now = datetime.now()
        am_pm_english = now.strftime("%p")
        am_pm = ""
        if am_pm_english == "AM":
            am_pm = "এএম"
        else:
            am_pm = "পিএম"

        current_time_english = now.strftime("%I:%M:%S")
        current_time = convert_english_digit_to_bangla_digit(current_time_english)
        dispatcher.utter_message(text="এখন সময় হচ্ছে \t {} {}".format(current_time, am_pm))

        return [AllSlotsReset()]

class ActionAppointment(Action):

    def name(self) -> Text:
        return "action_appointment"

    def run(self, dispatcher, tracker, domain):
        city_name = tracker.get_slot("city")
        now = datetime.now()
        current_time_english = now.strftime("%I%M%S")
        current_time = convert_english_digit_to_bangla_digit(current_time_english)
        dispatcher.utter_message(text="আপনার অ্যাপয়েন্টমেন্ট নম্বর হল \t {} | ঠিকানা আরএন ঠাকুর হাসপাতাল, {}".format(current_time,city_name ))

        return [AllSlotsReset()]
    
class ActionBmi(Action):
    def name(self) -> Text:
        return "action_bmi"
    
    def run(self, dispatcher, tracker, domain):
        weight = tracker.get_slot("weight")
        height = tracker.get_slot("height")
        weight=replace_alpha(weight)
        height=replace_alpha(height)
        sex = tracker.get_slot("sex")
        age = tracker.get_slot("age")
        sex =replace_alpha(sex)
        waist = tracker.get_slot("waist")
        
        sex =replace_alpha(waist)
        json_response= getBmi(weight,height,sex, age,waist)
        health= json_response["info"]["health"]
        if health == "Under Weight":
            health= "ওজন কম"
        elif health == "Normal Weight":
            health= "স্বাভাবিক ওজন"
        elif health == "Over Weight":
            health = "বেশি ওজন"
        elif health == "Obesity class I":
            health = "স্থূলতা ক্লাস I"
        elif health == "Obesity class II":
            health = "স্থূলতা ক্লাস II"
        elif health == "Obesity class III":
            health = "স্থূলতা ক্লাস III"
        else:
            health= "অজানা"
        
            
        
        dispatcher.utter_message(text=" আপনার স্বাস্থ্যের অবস্থা {} ".format(health))

        return [AllSlotsReset()]

def getBmi(w,h,s,a,wa):
    url = "https://mega-fitness-calculator1.p.rapidapi.com/bmi"

    querystring = {"weight":w,"height":h}

    headers = {
        "X-RapidAPI-Key": "6335b80c4emshd366e5b678f0601p138597jsnbc4d7f0c10df",
        "X-RapidAPI-Host": "mega-fitness-calculator1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    response_text = response.text
    response_json = json.loads(response_text)

    print(response.text)
    return response_json



def replace_alpha(s):
    # replace all alphabets with spaces
    s = re.sub('[a-zA-Z]+', ' ', s)
    # trim the resulting string
    s = s.strip()
    return s