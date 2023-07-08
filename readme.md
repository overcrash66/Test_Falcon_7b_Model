
# ===How to install and test ===
# ===tiiuae/falcon-7b-instruct===

``Tested with python 3.10``
``Windows 11``
``Ryzen 7 3800x 8core``
``RTX 3060 12gb``
``32GB RAM``

``Pip install -r requirements.txt``

``Run service.Py wait until it finishes downloading falcon model``

``Use sratFalconApi.bat to start the model and the API``

``After API is up and running run startFalconClient.bat (keep the API running)``

``Now you can chat / ask your question using "the client"``

``All chat history will be saved in data.txt file``

## My own review having tested Falcon 7b model:
 
-1. it feels heavy. (13.4gb full size)

-2. slow to return answers

-3. There are some limitations as it cannot answer questions related to basic math.

-4. is not 100% accurate. (do not return the right answer all times, or return wrong informations)