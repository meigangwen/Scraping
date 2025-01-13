from bs4 import BeautifulSoup
from selenium import webdriver


if __name__ == '__main__':
    url = 'https://chargermap.nio.com/pe/h5/static/chargermap?channel=official'
    driver = webdriver.Chrome()
    driver.get(url)

    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'lxml')

    # Realtime data of battery exchanges
    realtime_data = soup.find_all(class_='realtime-C_HVJ')
    for elem in realtime_data:
        print(elem.text)

    static_data = soup.find_all(class_='clearfix-IjPJw')
    for elem in static_data:
        print(elem.text)

    driver.quit()