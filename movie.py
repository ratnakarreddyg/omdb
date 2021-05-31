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
