# Bangla Medical ChatBot💬 WebApp (Developed with Rasa and Flask)

![image](https://user-images.githubusercontent.com/39009087/230365124-0fe4a80b-3c36-4e17-8fa6-2297d145bd95.svg)


## Features:

1. Provide a responsive user interface (aiding user’s to type in bangla fonts. It will try to guess the bengali word for a romanized word  eg : aami ⇒ আমি)
2. Use entity recognition and actions to provide a dynamic chat environment
3. Trained on a large dataset [[https://www.kaggle.com/datasets/abijitbarua/bangla-healthcare-chatbot-json-data](https://www.kaggle.com/datasets/abijitbarua/bangla-healthcare-chatbot-json-data)] and able to identify variety of text and queries.
4. Can identify symptoms of a potential disease and can give a suitable response according to it.
5. Can inform user about their health based on bmi classification [using api : [https://rapidapi.com/bejjaothmane/api/mega-fitness-calculator1](https://rapidapi.com/bejjaothmane/api/mega-fitness-calculator1)]

## How to use:

1. Install Python (recommended: Python 3.10.7)
2. Download this repository via GIT or zip.
3. Open terminal in directory of this repository, lets called it main
4. Type `pip install -r requirements.txt` and run.
5. Open two more terminals inside the /assistant directory
6. In one of them type `rasa train` and run.
7. After successful execution of the previous command type  `rasa run --enable-api --cors="*”`  and run.
8. This will start a rasa server.
9. Now on the next terminal type `rasa run actions` and run.
10. This will start the action endpoint
11. Now go back to the main terminal
12. From main terminal go to the directory /web app
13. There type `python [app.py](http://app.py/)`
14. This will run your web app on [http://127.0.0.1:5000](http://127.0.0.1:5000/)
15. In your browser go to  [http://127.0.0.1:5000](http://127.0.0.1:5000/) and start chatting

## Screenshots:
<img width="914" alt="1" src="https://user-images.githubusercontent.com/39009087/230365371-9c2f7ec2-4e6d-4d03-a87f-239d2f7f7bd1.png">

<img width="915" alt="2" src="https://user-images.githubusercontent.com/39009087/230365386-6d884ec1-a409-4fb1-ac76-3cd11bd89c2e.png">
<img width="912" alt="3" src="https://user-images.githubusercontent.com/39009087/230365428-a5c5ba7f-d07f-41f4-bd33-b3cc88aa7a9f.png">

<img width="913" alt="5" src="https://user-images.githubusercontent.com/39009087/230365453-190188ed-b800-4b1d-9786-fd47ae729592.png">

<img width="914" alt="6" src="https://user-images.githubusercontent.com/39009087/230365474-b25f0edf-a09c-4b1f-a16d-12e4e9fb573c.png">



## Notes:-

- **This is just basic chatbot, you can improve chatbot learning. Read [documentation](https://rasa.com/docs/)**
- **Also the bangla word formation for this application is not yet complete. The library used here to  detect a begali word from a romanized bengali word is not giving a good accuracy.**
- **You can build a better chatbot by using the model by changing the dataset. You can use english or any other language for this purpose. Just need to change the intents and responses.**

## If you like my work follow me and Star⭐ my repository
