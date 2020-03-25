import requests
import io
import pandas as pd
import random


geo_data = {'data':[
    {'country': 'United Kingdom', 'lat':55.3781, 'long':3.4360},
    {'country': 'Netherlands', 'lat':52.1326, 'long':5.2913},
    {'country': 'Denmark', 'lat': 56.2639, 'long': 9.5018},
    {'country': 'France', 'lat': 46.2276, 'long': 2.2137},
    {'country': 'China', 'lat': 35.8617, 'long': 104.1954},
    {'country': 'US', 'lat': 37.0902, 'long': 95.7129},
    {'country': 'Australia', 'lat': 25.2744, 'long': 133.7751},
    {'country': 'Canada', 'lat': 56.1304, 'long': 106.3468},]}

def get_list_of_countries_with_multiple_rows(df):
    multi_rows = df[df.duplicated(['Country/Region'], keep=False)]
    return multi_rows['Country/Region'].unique().tolist()

def group_regions_into_a_country(df):
    for d in geo_data['data']:
        if d['country'] in get_list_of_countries_with_multiple_rows(df):
            lat = d['lat']
            long = d['long']
            df.loc[df['Country/Region'] == d['country'], 'Lat'] = lat
            df.loc[df['Country/Region'] == d['country'], 'Long'] = long
    return df

def get_sum_of_cases_per_country(df):
    groups = group_regions_into_a_country(df).drop_duplicates(subset=['Country/Region'], keep=False)
    for country in get_list_of_countries_with_multiple_rows(df):
        group_sum = pd.DataFrame(df.loc[df['Country/Region'] == country].iloc[:, 4:].sum()).transpose()
        group = pd.DataFrame(df.loc[df['Country/Region'] == country]).drop_duplicates(subset=['Country/Region'], keep='first')
        group.iloc[:, 4:] = group_sum.values
        groups = groups.append(group, sort=False)
    return groups


class CovidUpdates:
    try:
        def __init__(self):
            return

        def get_dataframe(self, csv_data):
            r = requests.get(csv_data).content
            data = pd.read_csv(io.StringIO(r.decode('utf-8')))
            return data

        def generate_text(self, confirmed_df, death_df):
            link = 'https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_time_series'
            c = get_sum_of_cases_per_country(confirmed_df)
            d = get_sum_of_cases_per_country(death_df)
            c = c.sort_values(c.columns[-1], ascending=False).head(25)
            latest = c.columns[-1]
            rndm_country = random.choice([country for country in c['Country/Region'].tolist()])
            new_c = int((c.loc[c['Country/Region'] == rndm_country]).iloc[0][-1]) - int(
                (c.loc[c['Country/Region'] == rndm_country]).iloc[0][-2])
            new_d = int((d.loc[d['Country/Region'] == rndm_country]).iloc[0][-1]) - int(
                (d.loc[d['Country/Region'] == rndm_country]).iloc[0][-2])
            return "#COVID19 stats in {} ({}): {} total confirmed cases ({} new), {} total deaths ({} new). Data from JHU CSSE {}".format(
                rndm_country,
                latest,
                int((c.loc[c['Country/Region'] == rndm_country]).iloc[0][-1]),
                new_c,
                int((d.loc[d['Country/Region'] == rndm_country]).iloc[0][-1]),
                new_d, link)

    except IndexError:
        print("Index error")

    except AttributeError:
        print("Attribute error")

    except TypeError:
        print("Type error")
