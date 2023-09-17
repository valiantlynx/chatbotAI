docker build --no-cache -t chatbotai-main .
docker run --name chatbotai-main -d -p 8000:8000 -v $(pwd):/code chatbotai-main:latest 
docker exec chatbotai-main /bin/bash
