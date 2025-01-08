import requests
from bs4 import BeautifulSoup


def scraper(url):
    # request the target website
    response = requests.get(url)

    # verify the response status
    if response.status_code != 200:
        return f"status failed with {response.status_code}"
    else:

        # parse the HTML content
        soup = BeautifulSoup(response.text, "html.parser")

        # empty list to collect data
        scraped_data = []

        # get the product containers
        products = soup.find_all("div", class_="product-item")

        # iterate through the product containers and extract the product content
        for product in products:
            name_tag = product.find(class_="product-name")
            price_tag = product.find(class_="product-price")

            data = {
                "name": name_tag.text if name_tag else "",
                "price": price_tag.text if price_tag else "",
            }

            # append the data to the empty list
            scraped_data.append(data)
        # return the scraped data
        return scraped_data


if __name__ == '__main__':
    # specify the API URL without the offset
    target_url = "https://www.scrapingcourse.com/ajax/products"

    # set an initial request count
    offset_count = 0
    # array to collect scraped data
    product_data = []
    # scrape infinite scroll by intercepting API request
    # in the Network tab (150 offsets/10 = 15 offsets)
    for page in range(0, 15):
        # simulate the full URL format
        requested_page_url = f"{target_url}?offset={offset_count}"

        # execute the scraper function
        collected_data = scraper(requested_page_url)

        # extend the new list with the scraped data
        product_data.extend(collected_data)

        # increment the request count
        offset_count += 10

    print(product_data)


