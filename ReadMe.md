# TMDB Movies Dataset Analysis

## Table of Content
- This analysis is divided into 3 parts:

> - Data Cleaning
> - Data Wrangling
> - Data Exploration
> - Conclusion


## Installation
The following packages are required to run the notebook:
- pandas
- matplotlib
- seaborn
- numpy
- ast


## Features
- The project is made up of a main .ipynb file that explains the steps taken to clean, transform and explore the TMDB movies dataset.
- The dataset has some missing values in the fields: Cast, Director and Genre. These values were researched and manually inputted into .txt files in a json file structure. The .txt files are:
  > unknown_cast.txt <br>
  > unknown_genres.txt <br>
  > unknown_directors.txt<br>
- The above txt files were converted into json files and then read into the main file using the module txt_to_json.py, which is imported into the main file.
