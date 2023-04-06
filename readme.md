# Bangla Medical ChatBot💬 WebApp (Build with Rasa and Flask)

[https://camo.githubusercontent.com/38f5db5524ba43e7262dfbca1f7d3631ba127fb1596785dfd707d5fc671821c9/687474703a2f2f466f7254686542616467652e636f6d2f696d616765732f6261646765732f6d6164652d776974682d707974686f6e2e737667](https://camo.githubusercontent.com/38f5db5524ba43e7262dfbca1f7d3631ba127fb1596785dfd707d5fc671821c9/687474703a2f2f466f7254686542616467652e636f6d2f696d616765732f6261646765732f6d6164652d776974682d707974686f6e2e737667)

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

![1.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5885a05f-cbde-40f3-945f-57b5cb9d903d/1.png)

![2.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c057ea0e-91c0-4d97-9ea1-882cb498c51b/2.png)

![3.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5dca8d8b-03e6-4b9e-8167-a52904c8bac0/3.png)

![5.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/05693687-28a5-4662-81eb-2ee514e0d75f/5.png)

![6.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c95aa84f-2b91-463c-9614-d8164f33deb5/6.png)

## Notes:-

- **This is just basic chatbot, you can improve chatbot learning. Read [documentation](https://rasa.com/docs/)**
- **Also the bangla word formation for this application is not yet complete. The library used here to  detect a begali word from a romanized bengali word is not giving a good accuracy.**
- **You can build a better chatbot by using the model by changing the dataset. You can use english or any other language for this purpose. Just need to change the intents and responses.**

## If you like my work follow me and Star⭐ my repository