import json
import os

import jellyfish


class SearchEngine:
    THRESHOLD = 0.7
    def __init__(self, search_query, item_list, item_type):
        """
        :type search_query: str
        :type item_list: list
        :type item_type: str
        :param search_query:
        :param item_list:
        :param item_type:
        """
        self.item_list = []
        for item in item_list:
            self.item_list.append(Item(item_type, item))
        self.search_query = search_query

    def search(self):
        result = []
        if self.item_list:
            for item in self.item_list:
                ratio = jellyfish.jaro_winkler(self.search_query, item.name)
                if ratio >= self.THRESHOLD:
                    item.ratio = ratio
                    result.append(item)
            if result:
                return [item.item_id for item in sorted(result, key=lambda x: x.ratio, reverse=True)]
            else:

                return []
        return []


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
