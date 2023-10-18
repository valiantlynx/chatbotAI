# chatbotAI
a bot i made right now it has very litle training materials. it reads what you write and from what it has learned answers back. it has only been trained if five types of resposes found in the form of a json file , look at the code
the more types of anwers or in otherwords types of training materials in form of jaon file it has the smarter it gets

# Requirements
- docker
- docker-compose

# where to get the data
```bash	
git clone https://github.com/valiantlynx/chatbotAI.git
cd chatbotAI
```


# Installation
I am using big libraries like tensorflow and keras so it is better to use docker to run this project.
i have included a docker-compose file to make it easier to run the project
run: 
```bash
docker-compose up --build -d 
``` 
to run the project in the background.

! you have to wait till the training is done.
it will go through 400 epochs. you can check the progress by:
```bash
docker-compose logs
```
once you see logs like this:
```bash
chatbotai-fastapi-1  | Epoch 400/400
 1/87 [..............................] - ETA: 0s - loss: 0.0723 - accuracy: 1.0013/87 [===>..........................] - ETA: 0s - loss: 0.4671 - accuracy: 0.8430/87 [=========>....................] - ETA: 0s - loss: 0.6276 - accuracy: 0.8146/87 [==============>...............] - ETA: 0s - loss: 0.6012 - accuracy: 0.8261/87 [====================>.........] - ETA: 0s - loss: 0.6107 - accuracy: 0.8374/87 [========================>.....] - ETA: 0s - loss: 0.5939 - accuracy: 0.8387/87 [==============================] - 0s 4ms/step - loss: 0.6126 - accuracy: 0.8329
chatbotai-fastapi-1  | /usr/local/lib/python3.11/site-packages/keras/src/engine/training.py:3079: UserWarning: You are saving your model as an HDF5 file via `model.save()`. This file format is considered legacy. We recommend using instead the native Keras format, e.g. `model.save('my_model.keras')`.
chatbotai-fastapi-1  |   saving_api.save_model(
chatbotai-fastapi-1  | INFO:     Started server process [8]
chatbotai-fastapi-1  | INFO:     Waiting for application startup.
chatbotai-fastapi-1  | INFO:     Application startup complete.
``` 
its done.

go to http://localhost:8000/ to see the project running as well as the explanation of how it works

to stop the project run:
```bash
docker-compose down
```

docker-compose down will stop the project and remove the container. you might want to remove the images as well to save space on your computer. to do that run:
```bash
docker rmi chatbotai-fastapi 
```
after running docker-compose down


# alternative installation
i have not tested it as i made quick. if you dont have docker compose, run the file setup.sh. with:
```bash
bash setup.sh
```
though if you have docker i recommend using docker-compose as it is easier to run the project with it


