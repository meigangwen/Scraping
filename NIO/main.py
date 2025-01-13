from selenium import webdriver


if __name__ == '__main__':
    url = 'https://chargermap.nio.com/pe/h5/static/chargermap?channel=official'
    driver = webdriver.Chrome()
    driver.get(url)

    html_content = driver.page_source
    print(html_content)
    driver.quit()