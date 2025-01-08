import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import asyncio
from pyppeteer import launch

async def scrape(url):
    # Launch a headless browser
    browser = await launch(headless=True)
    page = await browser.newPage()

    # Navigate to the URL
    await page.goto(url, {'waitUntil': 'networkidle0'})

    # Wait for the necessary element to ensure it's loaded
    await page.waitForSelector('body')

    # Get the HTML content of the page
    html_content = await page.content()
    print(html_content)

    # Close the browser
    await browser.close()

if __name__ == '__main__':
    url = 'https://chargermap.nio.com/pe/h5/static/chargermap?channel=official'
    asyncio.get_event_loop().run_until_complete(scrape(url))



