
def scrape_all():
    # Dependencies
    from bs4 import BeautifulSoup as soup
    from splinter import Browser
    import pandas as pd
    import datetime as dt



    # executable_path = {"executable_path": "/Users/ekatu/.wdm/drivers/chromedriver/win32/90.0.4430.24/chromedriver.exe"} 
    executable_path = {"executable_path": "chromedriver.exe"}
    browser = Browser("chrome", **executable_path, headless=False)

    # News Titles and News Paragraphs    
    url = 'https://redplanetscience.com/'
    browser.visit(url)
    html = browser.html
    news_soup = soup(html, 'html.parser')
    slide_elem = news_soup.select_one('div.list_text')
    news_title = slide_elem.find("div", class_="content_title").get_text()
    news_paragraph = slide_elem.find("div", class_="article_teaser_body").get_text()
   
    # Featured imgaes 
    url = 'https://spaceimages-mars.com'
    browser.visit(url)
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()
    html = browser.html
    img_soup = soup(html, 'html.parser')
    img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
    featured_image = f'https://spaceimages-mars.com/{img_url_rel}'
  
    # Marrs Facts
    df = pd.read_html('https://galaxyfacts-mars.com')[0]
    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)
    mars_facts = df.to_html()
 
      #Mars Hemispheres
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    html = browser.html
    soup = soup(html, 'html.parser')

    titles = soup.find_all("h3")
    for title in titles:
        browser.click_link_by_partial_text("Hemisphere")

    results = soup.find_all("div", class_="description")
    mars_dict={}
    hemisphere_image_urls=[]
    for result in results:
        link = result.find('a')
        img_href = link['href']
        title_img = link.find('h3').text
        url = "https://astrogeology.usgs.gov" + img_href
        browser.visit(url)
        html = browser.html
        soup = soup(html, 'html.parser')
        pic = soup.find("a", target="_blank")
        pic_href = pic['href']
        hemisphere_image_urls.append({"title":title_img,"img_url":pic_href})


    scraped_data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image,
        "facts": mars_facts,
        "hemispheres": hemisphere_image_urls,
        "last_modified": dt.datetime.now()
    }

    browser.quit()

    return scraped_data