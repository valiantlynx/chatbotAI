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
to run the project in the background
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
