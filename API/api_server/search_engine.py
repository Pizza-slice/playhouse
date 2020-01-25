import json
import os

import jellyfish


class SearchEngine:

    def __init__(self, search_query, item_list, item_type):
        self.item_list = []
        for item in item_list:
            self.item_list.append(Item(item_type, item))
        self.search_query = search_query
        self.search()

    def search(self):
        result = []
        for item in self.item_list:
            ratio = jellyfish.jaro_winkler(self.search_query, item.name)
            if ratio >= 0.4:
                item.ratio = ratio
                result.append(item)
        return sorted(result, key=lambda x: x.ratio, reverse=True)


class Item:
    SONG_DIR = "files_matadata\\song_matadata"
    ARTIST_DIR = "files_matadata\\artist_matadata"
    ALBUM_DIR = "files_matadata\\album_matadata"
    dir_by_type = {"song": SONG_DIR, "artist": ARTIST_DIR, "album": ALBUM_DIR}

    def __init__(self, item_type, item_id):
        self.item_type = item_type
        self.item_id = item_id
        self.name = self.get_name_by_id()
        self.ratio = 0

    def get_name_by_id(self):
        if os.path.exists(self.dir_by_type[self.item_type] + "\\" + self.item_id + ".json"):
            with open(self.dir_by_type[self.item_type] + "\\" + self.item_id + ".json") as f:
                return json.loads(f.read())["name"]
