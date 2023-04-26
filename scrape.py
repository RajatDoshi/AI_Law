# imports for scraping a website
import requests
import bs4
import re
import json
import os

# function to scrape a website
def scrape(url):
    # get the html from the url
    response = requests.get(url)
    # parse the html
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    # get the text from the html
    text = soup.get_text()
    # remove the newlines
    text = text.replace("\n", " ")
    return text

# function to write the text to a file


def write_to_file(text, file_name):
    # open the file in write mode
    file = open(file_name, "w")
    # write the text to the file
    file.write(text)
    # close the file
    file.close()

# function to read the text from a file


def read_from_file(file_name):
    # open the file in read mode
    file = open(file_name, "r")
    # read the text from the file
    text = file.read()
    # close the file
    file.close()
    return text

# clean the text input after scraping


def clean_text(text):
    # remove the newlines
    text = text.replace("\n", " ")
    # remove the extra spaces
    text = re.sub(" +", " ", text)
    # remove the extra tabs
    text = re.sub("\t+", " ", text)
    return text
