import urllib.request
import time
import datetime
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


from flask import Blueprint, render_template, url_for
import xml.etree.ElementTree as element_tree

metar_weather_data = Blueprint('metar_weather_data', __name__)

URL_FOR_WEATHER = 'https://www.aviationweather.gov/adds/dataserver_current/' \
        'httpparam?dataSource=metars&requestType=retrieve&format=xml&hoursBeforeNow' \
        '=5&mostRecentForEachStation=true&stationString='
GUST_THRESHOLD = 10


def get_website_weather_data(airports: list) -> str:
    url: str = URL_FOR_WEATHER + ','.join([item for item in airports if item != 'NULL'])
    req: str = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows ' \
        'NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
        'Chrome/86.0.4240.198 Edg/86.0.622.69'})
    content: str = urllib.request.urlopen(req).read()
    return content


def get_weather_conditions(head):
    conditions:dict = {}
    stations:list[str] = []

    for reports in head.iter('METAR'):
        station_id = reports.find('station_id').text
        if reports.find('flight_category') is None:
            print(f'Data for {station_id} is not found.')
            continue

        flight_category:str = reports.find('flight_category').text
        observation_time:str = reports.find('observation_time').text if reports.find('observation_time') is not None else 'NT'
        temp_c:float = float(reports.find('temp_c').text) if reports.find('temp_c') is not None else 0.0
        dewpoint_c:float = float(reports.find('dewpoint_c').text) if reports.find('dewpoint_c') is not None else 0.0
        wind_dir_degrees:int = int(reports.find('wind_dir_degrees').text) if reports.find('wind_dir_degrees') is not None else 0
        wind_speed_kt:int = int(reports.find('wind_speed_kt').text) if reports.find('wind_speed_kt') is not None else 0
        visibility_statute_mi:float = float(reports.find('visibility_statute_mi').text) if reports.find('visibility_statute_mi') is not None else 0.0
        altim_in_hg:float = float(reports.find('altim_in_hg').text) if reports.find('altim_in_hg') is not None else 0.0

        wind_gust_kt:int = int(reports.find('wind_gust_kt').text) if reports.find('wind_gust_kt') is not None else 0.0
        is_gusting:bool = True if (wind_gust_kt - wind_speed_kt) > GUST_THRESHOLD else False

        precip_in:float = float(reports.find('precip_in').text) if reports.find('precip_in') is not None else 0.0
        elevation_m:float = float(reports.find('elevation_m').text) if reports.find('elevation_m') is not None else 0.0

        sky_conditions:list = []
        for skies in reports.iter('sky_condition'):
            tmp = {"cover" : skies.get('sky_cover'), "cloud_base_ft_agl" : int(skies.get('cloud_base_ft_agl', default=0))}
            sky_conditions.append(tmp)

        print(f'Station ID: {station_id}\nFlight Category: {flight_category}\nTemp (C): {temp_c:0.2f}\nDewpoint (C): {dewpoint_c:0.2f}\n' \
                f'WindDirection (degrees): {wind_dir_degrees}\nWind Speed (kt): {wind_speed_kt}\nWind Gust (kt): {wind_gust_kt}\n' \
                f'Is it gusting?: {"Yes" if is_gusting else "No"}\nVisibility (st. mi.): {visibility_statute_mi:0.2f}\n' \
                f'Alim in hg: {altim_in_hg:2.2f}\nPrecipitation (in): {precip_in:0.3f}\nElevation (m): {elevation_m:0.1f}\n\n' \
                f'Cloud Layers (ft.): {sky_conditions}')


        stations.append(station_id)
        conditions[station_id] = {
                'flight_category' : flight_category,
                'observation_time' : observation_time,
                'temp_c' : temp_c,
                'dewpoint_c' : dewpoint_c,
                'wind_dir_degrees' : wind_dir_degrees,
                'wind_speed_kt': wind_speed_kt,
                'wind_gust_kt' : wind_gust_kt,
                'is_gusting' : is_gusting,
                'visibility_statute_mi' : visibility_statute_mi,
                'altim_in_hg' : altim_in_hg,
                'precip_in' : precip_in,
                'elevation_m' : elevation_m,
                'sky_conditions' : sky_conditions
                }
    return conditions, stations


@metar_weather_data.route('/projects/metar/')
def render_metar_weather_main_page(name: str = 'KSHN-KBFI-KPUW-KHQM'):
    airports: list = list(name.split('-'))
    content: str = get_website_weather_data(airports)
    conditions, stations = get_weather_conditions(element_tree.fromstring(content))
    return render_template(
            'metar_weather_page.html',
            conditions = conditions,
            stations = stations,
            )


@metar_weather_data.route('/projects/metar/<string:airport_list>/')
def render_metar_weather_custom_main_page(airport_list: str):
    airports: list = list(airport_list.split('-'))
    content: str = get_website_weather_data(airports)
    conditions, stations = get_weather_conditions(element_tree.fromstring(content))
    return render_template(
            'metar_weather_page.html',
            conditions = conditions,
            stations = stations,
            )
