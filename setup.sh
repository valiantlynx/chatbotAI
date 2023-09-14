docker build --no-cache -t chatbotai-main .
docker run --name chatbotai-main chatbotai-main:latest 
docker exec chatbotai-main /bin/bash
