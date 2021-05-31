# How to use the script

1. Create a folder
mkdir docker
cd docker

2. Create Dockerfile
# vi Dockerfile
`FROM python:3.8-slim`

`RUN pip install requests`

`ADD movie.py /`

`ENTRYPOINT [ "python", "./movie.py" ]`


3. Create movie.py
# vi movie.py
#!/usr/bin/python3
import sys
import requests

name = sys.argv[1]
apikey = "f46744fc"
path = "http://omdbapi.com/?t=" + name + "&apikey=" + apikey
data = requests.get(path).json()
print(f"Movie Name - {name}")
print("Rotten Tomatoes rating : ",data["Ratings"][1]["Value"])
print("=================")


4. Build the Docker image
# docker build -t image4 .

5. Run the Docker image and get Rotten Tomatoes rating
**# docker run -it image4 "the godfather"
# docker run -it image4 interstellar
# docker run -it image4 tenet
# docker run -it image4 13**
