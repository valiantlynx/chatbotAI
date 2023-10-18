docker build --no-cache -t chatbotai-main .
docker run --name chatbotai-main -d -p 8000:8000 -v $(pwd):/code chatbotai-main:latest 
docker exec chatbotai-main /bin/bash

# make a brach on the main repo named the same as the monorepo
# add this as a subtree to the main repo
git subtree add --prefix=apps/chatbotAI https://github.com/valiantlynx/chatbotAI.git valiantlynx-turborepo --squash

# pull the subtree
git subtree pull --prefix=apps/chatbotAI https://github.com/valiantlynx/chatbotAI.git valiantlynx-turborepo --squash

# push the subtree
git subtree push --prefix=apps/chatbotAI https://github.com/valiantlynx/chatbotAI.git valiantlynx-turborepo

