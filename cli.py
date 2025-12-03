# # cli.py
# import argparse

# def get_args():
#     parser = argparse.ArgumentParser(description="Weather Harvester CLI")

#     # Multiple cities: -c Delhi -c Pune
#     parser.add_argument(
#         "-c", "--city",
#         action="append",
#         help="City name (can be given multiple times: -c Delhi -c Pune)"
#     )

#     # Alternative: comma-separated cities
#     parser.add_argument(
#         "-C", "--cities",
#         type=str,
#         help="Comma-separated list of cities: --cities Delhi,Mumbai"
#     )

#     # Coordinate override (used as fallback if city not in known list)
#     parser.add_argument(
#         "--lat",
#         type=float,
#         help="Latitude value (used if city has no predefined coordinates)"
#     )

#     parser.add_argument(
#         "--lon",
#         type=float,
#         help="Longitude value (used if city has no predefined coordinates)"
#     )

#     # Cache toggle
#     parser.add_argument(
#         "--use-cache",
#         action="store_true",
#         help="Use cached data if available"
#     )

#     # Logging level
#     parser.add_argument(
#         "--log-level",
#         type=str,
#         choices=["DEBUG", "INFO", "WARNING", "ERROR"],
#         help="Logging level"
#     )

#     # Alert threshold
#     parser.add_argument(
#         "--alert-temp",
#         type=float,
#         help="Temperature threshold to trigger alert (°C)"
#     )

#     # Config path
#     parser.add_argument(
#         "--config",
#         type=str,
#         default="config/config.ini",
#         help="Path to configuration file"
#     )

#     return parser.parse_args()


import argparse

def get_args(arg_list=None):
    parser = argparse.ArgumentParser(description="Weather Harvester CLI")

    parser.add_argument("-c", "--city", dest="cities", action="append",
                        help="City name", default=[])
    
    parser.add_argument("--alert-temp", type=float, default=None,
                        help="Temperature threshold for alerts")
    
    parser.add_argument("--log-level", type=str, default="INFO",
                        help="Logging level")
    
    parser.add_argument("--config", type=str, default="config/config.ini",
                        help="Path to config file")

    parser.add_argument("--lat", type=float, default=None)
    parser.add_argument("--lon", type=float, default=None)
    parser.add_argument("--use-cache", action="store_true")

    if arg_list is not None:
        return parser.parse_args(arg_list)

    return parser.parse_args()

