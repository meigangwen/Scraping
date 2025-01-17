from bs4 import BeautifulSoup
import requests
import re


if __name__ == '__main__':
    url = 'https://chargermap-fe-gateway.nio.com/pe/bff/gateway/powermap/h5/charge-map/v2/power/around/summary?app_ver=5.2.0&client=pc&container=brower&lang=zh&region=CN&app_id=100119&channel=official&brand=nio&area_code=000000&longitude=104.32311750545072&latitude=37.98802757150653&type=region&timestamp=1737093018072'
    response = requests.get(url)
    print(response)

    try:
        data = response.json()  # This method parses the JSON string from the response
        print(data)  # Print or use the data as needed
    except ValueError:
        print("Response content is not valid JSON")





    '''
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
    '''