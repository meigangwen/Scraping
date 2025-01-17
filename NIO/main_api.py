from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    url = 'https://chargermap-fe-gateway.nio.com/pe/bff/gateway/powermap/h5/charge-map/v2/power/around/summary?client=pc&app_id=100119&channel=official&timestamp='
    response = requests.get(url)
    print(response)

    try:
        data = response.json()['data']

        for key, value in data.items():
            data[key] = value.replace(",", "")
        print(data)

        print(data)  # Print or use the data as needed
        date = data['statistic_update_time']
        print(date)   # convert this into a python date object

        swap_station = int(data['swap_number'])
        print(swap_station)

        highway_swap_station = int(data['high_speed_swap_number'])
        print(highway_swap_station)

        super_station = int(data['nio_npc_charger_number'])
        print(super_station)

        super_connector = int(data['nio_npc_connector_number'])
        print(super_connector)

        highway_charge_station = int(data['high_speed_nio_charger_number'])
        print(highway_charge_station)

        highway_charge_connector = int(data['high_speed_nio_connector_number'])
        print(highway_charge_connector)

        dest_charge_station = int(data['nio_dest_charger_number'])
        print(dest_charge_station)

        dest_connector = int(data['nio_dest_connector_number'])
        print(dest_connector)

        third_party_connector = int(data['third_connector_number'])
        print(third_party_connector)

        cover_rate = float(data['ps_district_housing_covered_rate'])
        print(cover_rate)

        total_swap = ''.join([ch for ch in data['total_swap_times_number'] if ch.isdigit()])
        total_swap = int(total_swap) * 10000
        print(total_swap)

    except ValueError:
        print("Response content is not valid JSON")

