import argparse
import importlib.util
import os
import sys
from pathlib import Path

try:
    from .favorites import FavoritesManager
    from .weather_api import (
        WeatherAPI,
        format_current_weather,
        format_forecast,
    )
except ImportError:
    from favorites import FavoritesManager
    from weather_api import (
        WeatherAPI,
        format_current_weather,
        format_forecast,
    )


FAVORITES_FILE = Path(__file__).resolve().parent / "favorites.json"


def load_api_key():
    """Load the API key from the environment or local config.py."""
    key = os.environ.get("WEATHER_API_KEY")
    if key:
        return key

    config_path = Path(__file__).resolve().parent / "config.py"
    if not config_path.exists():
        return None

    try:
        spec = importlib.util.spec_from_file_location(
            "weather_local_config", config_path
        )
        if spec is None or spec.loader is None:
            return None

        config = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(config)

        return (
            getattr(config, "WEATHER_API_KEY", None)
            or getattr(config, "API_KEY", None)
        )
    except (ImportError, OSError, SyntaxError):
        return None


def build_parser():
    parser = argparse.ArgumentParser(
        description="Command-line weather application"
    )
    commands = parser.add_subparsers(dest="command", required=True)

    current_parser = commands.add_parser(
        "current", help="Get current weather"
    )
    current_parser.add_argument("location")

    forecast_parser = commands.add_parser(
        "forecast", help="Get weather forecast"
    )
    forecast_parser.add_argument("location")
    forecast_parser.add_argument(
        "--days", type=int, choices=range(1, 4), default=3
    )

    favorites_parser = commands.add_parser(
        "favorites", help="Manage favorite locations"
    )
    favorites_commands = favorites_parser.add_subparsers(
        dest="favorites_command", required=True
    )

    add_parser = favorites_commands.add_parser("add")
    add_parser.add_argument("name")
    add_parser.add_argument("location")

    favorites_commands.add_parser("list")

    remove_parser = favorites_commands.add_parser("remove")
    remove_parser.add_argument("name")

    return parser


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    favorites = FavoritesManager(FAVORITES_FILE)

    if args.command == "favorites":
        if args.favorites_command == "add":
            if not favorites.add(args.name, args.location):
                print(
                    f"Error: could not add favorite '{args.name}'.",
                    file=sys.stderr,
                )
                return 1

            print(f"Added favorite '{args.name}'.")
            return 0

        if args.favorites_command == "list":
            saved = favorites.list_all()

            if not saved:
                print("No favorites saved.")
            else:
                for name, location in saved.items():
                    print(f"{name}: {location}")
            return 0

        if args.favorites_command == "remove":
            if not favorites.remove(args.name):
                print(
                    f"Error: favorite '{args.name}' not found.",
                    file=sys.stderr,
                )
                return 1

            print(f"Removed favorite '{args.name}'.")
            return 0

    api_key = load_api_key()
    if not api_key:
        print(
            "Error: missing API key. Set WEATHER_API_KEY or configure "
            "week08/config.py.",
            file=sys.stderr,
        )
        return 1

    location = args.location
    favorite_location = favorites.get_location(location)
    if favorite_location is not None:
        location = favorite_location

    api = WeatherAPI(api_key)

    if args.command == "current":
        data = api.get_current_weather(location)
        if data is None:
            print("Error: could not retrieve current weather.", file=sys.stderr)
            return 1

        print(format_current_weather(data))
        return 0

    if args.command == "forecast":
        try:
            data = api.get_forecast(location, args.days)
        except ValueError as error:
            print(f"Error: {error}", file=sys.stderr)
            return 1

        if data is None:
            print("Error: could not retrieve forecast.", file=sys.stderr)
            return 1

        print(format_forecast(data))
        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
