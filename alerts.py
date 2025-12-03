import logging
import platform
from colorama import Fore, Style, init
from turtle_alert import turtle_clean_skull_alert
init(autoreset=True)

def check_alert(weather: dict, alert_temp: float):
    if not weather or "temperature" not in weather:
        logging.warning("Weather data missing for alert check")
        return False

    temp = weather["temperature"]

    if temp >= alert_temp:
        logging.warning(f"ALERT! Temperature {temp}°C exceeded threshold {alert_temp}°C")
        print(f"\n{Fore.RED}🔥🔥🔥 TEMPERATURE ALERT 🔥🔥🔥")
        print(f"{Fore.RED}Current temperature: {temp}°C (Threshold: {alert_temp}°C)")
        play_alert_sound()
        turtle_clean_skull_alert()
        return True  # alert happened
    else:
        logging.info(f"No alert. Temperature {temp}°C is below threshold {alert_temp}°C")
        return False  # no alert

def play_alert_sound():
    os_name = platform.system()

    try:
        if os_name == "Windows":
            import winsound

            # Emergency pattern: repeated fast beeps
            for _ in range(10):  # number of beeps
                winsound.Beep(1500, 150)   # high pitch, short duration
                winsound.Beep(1000, 150)   # lower pitch, short duration

        elif os_name == "Darwin":
            import os
            os.system("say 'Emergency alert'")

        else:
            for _ in range(10):
                print("\a")

    except Exception as e:
        logging.error(f"Failed to play sound alert: {e}")
# import logging
# import platform
# from colorama import Fore, Style, init

# init(autoreset=True)


# def check_alert(weather: dict, high_threshold: float, low_threshold: float = None):
#     """Checks temperature and triggers alerts for high or low behavior."""
    
#     if not weather or "temperature" not in weather:
#         logging.warning("Weather data missing for alert check")
#         return False

#     temp = weather["temperature"]

#     # HIGH TEMPERATURE ALERT 🔥
#     if temp >= high_threshold:
#         logging.warning(f"🔥 ALERT! Temperature {temp}°C exceeded high threshold {high_threshold}°C")
        
#         print(f"\n{Fore.RED}{Style.BRIGHT}🔥🔥🔥 TEMPERATURE ALERT 🔥🔥🔥")
#         print(f"{Fore.RED}Current temperature: {temp}°C (Threshold: {high_threshold}°C)")
#         print(f"{Fore.YELLOW}⚠ Stay hydrated! It's getting hot!{Style.RESET_ALL}")

#         play_alert_sound()
#         return True

#     # LOW TEMPERATURE ALERT ❄️🥶 (OPTIONAL if user provided low threshold)
#     if low_threshold is not None and temp <= low_threshold:
#         logging.warning(f"❄ COLD ALERT! Temperature {temp}°C dropped below {low_threshold}°C")
        
#         print(f"\n{Fore.CYAN}{Style.BRIGHT}❄️🥶 COLD TEMPERATURE ALERT 🥶❄️")
#         print(f"{Fore.CYAN}Current temperature: {temp}°C (Low Threshold: {low_threshold}°C)")
#         print(f"{Fore.BLUE}🧊 Brrr... it's freezing! Dress warmly!{Style.RESET_ALL}")

#         play_alert_sound()
#         return True

#     # NO ALERT — safe temperature
#     logging.info(f"No alert. Temperature {temp}°C within safe range.")
#     print(f"{Fore.GREEN}✔ Temperature Normal ({temp}°C){Style.RESET_ALL}")

#     return False



# def play_alert_sound():
#     os_name = platform.system()

#     try:
#         if os_name == "Windows":
#             import winsound
            
#             # Emergency patterned beeps
#             for _ in range(5):
#                 winsound.Beep(1500, 120)
#                 winsound.Beep(900, 120)

#         elif os_name == "Darwin":  # macOS
#             import os
#             os.system("say 'Warning temperature alert!'")

#         else:  # Linux fallback
#             for _ in range(5):
#                 print("\a")

#     except Exception as e:
#         logging.error(f"Failed to play sound alert: {e}")
