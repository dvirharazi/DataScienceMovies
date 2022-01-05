import numpy as np
import requests as requests
import webdriver_manager
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


def scrape_movie_years_links(wiki_url):
    years = []
    link_to_film_of_year = []
    for year_link in bs.findAll("li"):
        if "List of" in year_link.text and "s" not in year_link.text[-4:]:
            if 1970 <= int(year_link.text[-4:]) <= 2020:
                link_to_film_of_year.append(year_link.find('a')['href'])
                years.append(year_link.text[-4:])
    return pd.DataFrame({"year": years, "link_to_year": link_to_film_of_year})


def load_movies_per_years(year_url_address, driver):
    movie_name = []
    years = []
    length = []
    idbm_year = []
    genres = []
    rating = []
    stars = []
    writers = []
    directors = []
    for item in range(year_url_address.shape[0]):
        next = year_url_address.iloc[item][1]
        response = requests.get("https://en.wikipedia.org/" + next)
        soup = BeautifulSoup(response.text, "html.parser")
        try:
            tables = soup.find_all("table", class_="wikitable")
            for table in tables:
                trs = table.find_all("tr")
                for tr in trs[1:]:
                    movie_data = tr.find_all("i")
                    add_data_to_table_selenium(movie_data[0].text.strip(), driver, directors, writers, stars, rating,
                                               genres, idbm_year)
                    movie_name.append(movie_data[0].text.strip())
                    years.append(year_url_address.iloc[item][0])

        except:
            print("exeption")
            continue
    driver.close()
    return pd.DataFrame(
        {"name": movie_name, "year": years, "idbm_year": idbm_year, "director": directors, "writers": writers,
         "star": stars, "rating": rating, "genre": genres})


def add_data_to_table_selenium(movie_name, s, directors, writers, stars, rating, genres, idbm_year):
    list_of_directors = []
    list_of_writers = []
    list_of_genres = []
    list_of_stars = []
    try:
        driver.get('https://www.imdb.com/')
        inputElement = driver.find_element_by_id("suggestion-search")
        inputElement.send_keys(movie_name)
        click_btn = driver.find_element_by_id("suggestion-search-button")
        click_btn.click()
        results = driver.find_element_by_xpath("//table[@class='findList']/tbody/tr/td[@class='primary_photo']/a")
        results.click()  # clicks the first one
        c = driver.page_source
        bs = BeautifulSoup(c, "html.parser")
    except:
        print("connection lost")
        genres.append("")
        rating.append("")
        directors.append("")
        writers.append("")
        stars.append("")
        idbm_year.append("")
        return

    try:
        genre = bs.find("div", class_="ipc-chip-list").find_all('span', class_="ipc-chip__text")
        for g in genre:
            list_of_genres.append(g.text.strip())
        string_genres = ','.join(list_of_genres)
        genres.append(string_genres)
    except:
        genres.append("")
    try:
        year = bs.find("div", class_="TitleBlock__TitleMetaDataContainer-sc-1nlhx7j-2").find_all('li',
                                                                                                 class_="ipc-inline-list__item")
        y = year[0].find('span', class_='TitleBlockMetaData__ListItemText-sc-12ein40-2')
        idbm_year.append(y.text)
    except:
        idbm_year.append("")

    try:
        rate = bs.find("span", class_="AggregateRatingButton__RatingScore-sc-1ll29m0-1")
        rating.append(rate.text.strip())
    except:
        rating.append("")

    try:
        info_director_writer_stars = bs.find('div',
                                             class_="PrincipalCredits__PrincipalCreditsPanelWideScreen-hdn81t-0").find_all(
            'ul', class_='ipc-inline-list')
        director = info_director_writer_stars[0].find_all('a',
                                                          class_='ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link')
        writer = info_director_writer_stars[1].find_all('a',
                                                        class_='ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link')
        star = info_director_writer_stars[2].find_all('a',
                                                      class_='ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link')
        for d in range(len(director)):
            list_of_directors.append(director[d].text)
        string_directors = ','.join(list_of_directors)
        directors.append(string_directors)
        for w in range(len(writer)):
            list_of_writers.append(writer[w].text)
        string_writers = ','.join(list_of_writers)
        writers.append(string_writers)
        for s in range(len(star)):
            list_of_stars.append(star[s].text)
        string_stars = ','.join(list_of_stars)
        stars.append(string_stars)

    except:
        directors.append("")
        writers.append("")
        stars.append("")


def load_csv(file_name):
    df = pd.read_csv(file_name)
    return df

def clean_dataframe():
    df = load_csv('movie_wiki1.csv')
    df = df.dropna(axis=0, subset=['star'])
    df = df[df.year == df.idbm_year]
    df = df.drop(df.columns[0], axis=1)
    df = df.reset_index(drop=True)
    df.to_csv('movie_after_clean.csv')


# scraping movie data
# list_of_american_films_wiki = "https://en.wikipedia.org/wiki/Lists_of_American_films"
# r = requests.get(list_of_american_films_wiki)
# bs = BeautifulSoup(r.content, "html.parser")
# links_df = scrape_movie_years_links(bs.contents)
# driver = webdriver.Chrome(ChromeDriverManager().install())
# df_movie_year = load_movies_per_years(links_df, driver)
# print("Done locating data from wiki!!")
# df_movie_year.to_csv('movie_wiki1.csv')
clean_dataframe()



