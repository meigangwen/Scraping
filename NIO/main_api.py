from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    url = 'https://chargermap-fe-gateway.nio.com/pe/bff/gateway/powermap/h5/charge-map/v2/power/around/summary?client=pc&app_id=100119&channel=official&timestamp='
    response = requests.get(url)
    print(response)

    try:
        data = response.json()  # This method parses the JSON string from the response
        print(data['data'])  # Print or use the data as needed
    except ValueError:
        print("Response content is not valid JSON")