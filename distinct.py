import pymongo
import time
import pprint

mongodb = pymongo.MongoClient('localhost', 27017)
music_data = mongodb['music_data']
time_line = music_data['time_line']
fail_list = music_data['fail_list']
huge_album_url = music_data['huge_album_url']
artist_info = music_data['artist_info']
album_info = music_data['album_info']
song_info = music_data['song_info']


def distinct():
    data = []
    for i in fail_list.find():
        if i not in data:
            data.append(i)

distinct()