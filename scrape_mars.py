# Dependencies
from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import datetime as dt


# executable_path = {"executable_path": "\Users\ekatu\Downloads\chromedriver"}
# browser = Browser("chrome", **executable_path, headless=False)

def scrape_all():


# Scrape the Latest News Title
    news_title = slide_element.find("div", class_="content_title").get_text()
    news_paragraph = slide_element.find("div", class_="article_teaser_body").get_text()
    featured_image = 'https://linktoimage.png'
    mars_facts = 'Testing'
    news_title = 'Testing'
    hemispheres_list_of_dicts = [
        {"title": "Title of Hemisphere Image",
        "img_url": 'https://linktoimage.png'},

        {"title": "Title of Hemisphere Image",
        "img_url": 'https://linktoimage.png'},

        {"title": "Title of Hemisphere Image",
        "img_url": 'https://linktoimage.png'},
        
        {"title": "Title of Hemisphere Image",
        "img_url": 'https://linktoimage.png'},
    ]

    scraped_data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image,
        "facts": mars_facts,
        "hemispheres": hemispheres_list_of_dicts,
        "last_modified": dt.datetime.now()
    }

    return scraped_data