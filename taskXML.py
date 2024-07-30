
import xml.etree.ElementTree as ET

tree = ET.parse('movie.xml')
root = tree.getroot()

for movie in root.iter('movie'):
    print(movie.attrib)

for description in root.iter('description'):
    print(description.text)

# Initialize counters
favorite_count = 0
not_favorite_count = 0
# open the file
with open("movie.xml", "r") as f:
    for line in f:
        if "movie" in line:

            if "favorite = True" in line:
                favorite_count += 2
            else:
                not_favorite_count += 2

print("Number of movies:", favorite_count)

print("Number not of movies:", not_favorite_count)