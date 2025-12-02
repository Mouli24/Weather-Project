# main.py
from cli import get_args
from config import load_config
from fetcher import fetch_weather, get_coords_for_city
from cache import load_cache, save_cache
from logging_system import setup_logging

from alerts import check_alert

from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import Fore, Style
import logging


def build_city_list(args, cfg) -> list[str]:
    cities: list[str] = []

    if args.city:
        cities.extend(args.city)

    if args.cities:
        cities.extend(
            [c.strip() for c in args.cities.split(",") if c.strip()]
        )

    if not cities:
        cities = [cfg["city"]]

    return cities


def process_city(city, base_lat, base_lon, use_cache, alert_temp):
    print(f"\n{Fore.BLUE}====== {city.upper()} ======{Style.RESET_ALL}")
    logging.info(f"Processing city: {city}")

    # coordinates
    lat, lon = get_coords_for_city(city, base_lat, base_lon)
    logging.info(f"Coordinates for {city}: {lat}, {lon}")

    weather = None
    previous_temp = None

    # load cache + previous temp for trend
    if use_cache:
        cached, prev = load_cache(city)
        if cached:
            weather = cached
            previous_temp = prev
            print(f"{Fore.GREEN}Using cached weather for {city}:{Style.RESET_ALL}")
            print(weather)

    # fetch if needed
    if weather is None:
        logging.info(f"Fetching new weather data for {city}")
        weather = fetch_weather(lat, lon)
        if weather:
            print(f"{Fore.GREEN}Weather for {city}:{Style.RESET_ALL}")
            print(weather)
            save_cache(city, weather)
        else:
            logging.error(f"Failed to fetch weather for {city}")
            return

    # trend evaluation
    if previous_temp is not None:
        curr = weather["temperature"]
        diff = curr - previous_temp

        if diff > 0:
            print(f"{Fore.YELLOW}📈 Temperature Rising (+{diff:.1f}°C){Style.RESET_ALL}")
        elif diff < 0:
            print(f"{Fore.CYAN}📉 Temperature Dropping ({diff:.1f}°C){Style.RESET_ALL}")
        else:
            print(f"{Fore.WHITE}➖ Temperature Stable{Style.RESET_ALL}")
    else:
        print(f"{Fore.WHITE}No previous temperature to compare.{Style.RESET_ALL}")

    # alert system
    alert_triggered = check_alert(weather, alert_temp)

    if alert_triggered:
        print(f"{Fore.RED}⚠ Alert Active for {city}!{Style.RESET_ALL}")
    else:
        print(f"{Fore.GREEN}✅ No alert for {city}.{Style.RESET_ALL}")


def main():
    args = get_args()
    cfg = load_config(args.config)

    log_level = args.log_level or cfg["log_level"]
    setup_logging(log_level)

    use_cache = args.use_cache or cfg["use_cache"]
    alert_temp = args.alert_temp or cfg["alert_temp"]

    base_lat = args.lat or cfg["lat"]
    base_lon = args.lon or cfg["lon"]

    cities = build_city_list(args, cfg)

    logging.info(f"Cities to process: {cities}")
    logging.info(f"Caching enabled: {use_cache}")
    logging.info(f"Alert temperature threshold: {alert_temp}°C")

    # concurrency
    with ThreadPoolExecutor(max_workers=len(cities)) as executor:
        futures = [
            executor.submit(
                process_city,
                city,
                base_lat,
                base_lon,
                use_cache,
                alert_temp
            )
            for city in cities
        ]

        for f in as_completed(futures):
            pass

    logging.info("All cities processed.")
print(f"{Fore.GREEN}✅ All cities processed.{Style.RESET_ALL}")



if __name__ == "__main__":
    main()                         

