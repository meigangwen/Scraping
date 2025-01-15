from bs4 import BeautifulSoup
from selenium import webdriver
import re


if __name__ == '__main__':
    #url = 'https://www.nio.cn/charger-map'
    url = 'https://chargermap.nio.com/pe/h5/static/chargermap?channel=official'
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)  #this waiting method does not work sometimes
    driver.get(url)

    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'lxml')

    # Realtime data of battery exchanges
    static_data = soup.find_all(class_='clearfix-IjPJw')
    data_string = ''
    for elem in static_data:
        data_string += elem.text
        print(elem.text)
    print(data_string)

    # Define a dictionary of patterns
    patterns = {
        "实时累计换电次数": r"实时累计换电次数([\d,]+)",
        "换电站": r"换电站([\d,]+)座",
        "其中高速公路换电站": r"其中高速公路换电站([\d,]+)座",
        "超充站": r"超充站([\d,]+)座",
        "高速公路充电站": r"高速公路充电站([\d,]+)座",
        "目的地充电站": r"目的地充电站([\d,]+)座",
        "接入第三方充电桩": r"接入第三方充电桩([\d,]+)根",
        "电区房覆盖率": r"电区房覆盖率([\d.]+)%"
    }

    results = {}
    for key, pattern in patterns.items():
        match = re.search(pattern, data_string)
        if match:
            results[key] = match.group(1)

    # Print results
    for key, value in results.items():
        print(f"{key}: {value}")
    driver.quit()