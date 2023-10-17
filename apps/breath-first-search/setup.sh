docker build -t python-development-environment-image .
docker run --name python-development-environment-container -d -p 8000:8000 -v $(pwd):/code python-development-environment-image
