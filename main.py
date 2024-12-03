from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time


"""
######### RUN THE run.py to Run the scraper #########
---> You have to run the run.py first for executing the scraper
"""


option = webdriver.EdgeOptions()
option.add_argument("--headless=new")
driver = webdriver.Edge(options=option)


def greenprint(text, end="\n"):
    print("\033[0;32m", text, "\033[0m", end=end)


# Open the URL
url = "https://www.stubhub.com/explore?lat=MjUuNDQ3ODg5OA%3D%3D&lon=LTgwLjQ3OTIyMzY5OTk5OTk5&to=253402300799999&tlcId=2"


driver.get(url)


events = []
try:
    item_list = []

    greenprint("⌛ Scraper is running...")

    time.sleep(2)

    for i in range(1, 10):
        title_xpath = f"/html/body/div[1]/div[1]/div[4]/section/div[2]/div/div[3]/ul/li[{i}]/div/a/div[2]/p[1]"
        datetime_xpath = f"/html/body/div[1]/div[1]/div[4]/section/div[2]/div/div[3]/ul/li[{i}]/div/a/div[2]/p[2]"

        location_xpath = f"/html/body/div[1]/div[1]/div[4]/section/div[2]/div/div[3]/ul/li[{i}]/div/a/div[2]/p[3]"

        img_xpath = f"/html/body/div[1]/div[1]/div[4]/section/div[2]/div/div[3]/ul/li[{i}]/div/a/div[1]/img"

        title_elm = driver.find_element(by=By.XPATH, value=title_xpath)
        datetime_elm = driver.find_element(by=By.XPATH, value=datetime_xpath)
        location_elm = driver.find_element(by=By.XPATH, value=location_xpath)
        img_elm = driver.find_element(by=By.XPATH, value=img_xpath)

        item_list.append(
            {
                "title": title_elm.text,
                "datetime": datetime_elm.text,
                "location": location_elm.text,
                "image_link": img_elm.get_attribute("src"),
            }
        )

        greenprint(f"Finding elements & collecting data{'.'*i}\r", end="")

    with open("sports_events_data.json", "w") as f:
        f.write(json.dumps(item_list, indent=4))

finally:
    driver.quit()
    greenprint("\nSuccessfully saved ✅")
