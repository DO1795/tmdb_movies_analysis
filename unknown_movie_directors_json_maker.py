import json


def txt_to_json_converter(txtfilename):
    with open(fr"{txtfilename}") as file:
        lines = file.readlines()
        file.close()

    with open(r"unknown_movie_directors.json", "w") as json_file:
        lines_json= json.dump(lines, json_file)
        json_file.close()


txt_to_json_converter("unknown_movie_directors.txt")

    
