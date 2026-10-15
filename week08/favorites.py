import json
from pathlib import Path


class FavoritesManager:
    def __init__(self, filename):
        self.filename = Path(filename)
        self.favorites = {}
        self._load()

    def _load(self):
        try:
            with self.filename.open("r", encoding="utf-8") as file:
                data = json.load(file)
            if isinstance(data, dict):
                self.favorites = data
        except (OSError, json.JSONDecodeError):
            self.favorites = {}

    def _save(self):
        try:
            self.filename.parent.mkdir(parents=True, exist_ok=True)
            with self.filename.open("w", encoding="utf-8") as file:
                json.dump(self.favorites, file, indent=2)
        except OSError:
            return False
        return True

    def _find_name(self, name):
        for saved_name in self.favorites:
            if saved_name.casefold() == name.casefold():
                return saved_name
        return None

    def add(self, name, location):
        if self._find_name(name) is not None:
            return False

        self.favorites[name] = location
        if not self._save():
            del self.favorites[name]
            return False

        return True

    def remove(self, name):
        saved_name = self._find_name(name)
        if saved_name is None:
            return False

        location = self.favorites.pop(saved_name)
        if not self._save():
            self.favorites[saved_name] = location
            return False

        return True

    def list_all(self):
        return dict(self.favorites)

    def get_location(self, name):
        saved_name = self._find_name(name)
        if saved_name is None:
            return None
        return self.favorites[saved_name]
