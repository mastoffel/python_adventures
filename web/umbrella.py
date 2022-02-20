from weatherService import WeatherService
import time
import argparse

parser = argparse.ArgumentParser(description='Do you need an umbrella?')
parser.add_argument('city', type=str,
                    help='a city')
parser.add_argument('country', type=str,
                    help='a country')
args = parser.parse_args()

def within_time(item, start, end):
    return item['dt'] >= start and item['dt'] <= end

def makeUmbrellaDecision(city, country) -> bool:
    current_time = time.time()
    end_time = current_time + 12 * 3600
    wx = WeatherService.getForecast(city, country)
    wx = [x for x in wx if within_time(x, current_time, end_time)]
    rain = [x['rain']['3h'] for x in wx if 'rain' in x]
    if len(rain) > 0 and (max(rain) > 0.1):
        return True
    else:
        return False
    
if __name__ == "__main__":
    print(makeUmbrellaDecision(args.city, args.country))


time.time() + 12*3600