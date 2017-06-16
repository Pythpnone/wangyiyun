import pymongo
import multiprocessing

mongodb = pymongo.MongoClient('localhost', 27017)
music_data = mongodb['music_data']
artist_url = music_data['artist_url']
info_url = music_data['info_url']
info_search = music_data['info_search']
album_url = music_data['album_data']
artist_urls_20w = music_data['artist_urls_20w']
artist_urls_40w = music_data['artist_urls_40w']
artist_urls_60w = music_data['artist_urls_60w']
artist_urls_80w = music_data['artist_urls_80w']
artist_urls_100w = music_data['artist_urls_100w']
artist_urls_120w = music_data['artist_urls_120w']
artist_urls_140w = music_data['artist_urls_140w']
artist_urls_160w = music_data['artist_urls_160w']
artist_urls_180w = music_data['artist_urls_180w']
artist_urls_200w = music_data['artist_urls_200w']
artist_urls_220w = music_data['artist_urls_220w']
artist_urls_240w = music_data['artist_urls_240w']
artist_urls_260w = music_data['artist_urls_260w']
artist_urls_280w = music_data['artist_urls_280w']
artist_urls_300w = music_data['artist_urls_300w']
artist_urls_320w = music_data['artist_urls_320w']
artist_urls_340w = music_data['artist_urls_340w']
artist_urls_360w = music_data['artist_urls_360w']
artist_urls_380w = music_data['artist_urls_380w']
artist_urls_400w = music_data['artist_urls_400w']
artist_urls_420w = music_data['artist_urls_420w']
artist_urls_440w = music_data['artist_urls_440w']
artist_urls_460w = music_data['artist_urls_460w']
artist_urls_480w = music_data['artist_urls_480w']
artist_urls_500w = music_data['artist_urls_500w']
artist_urls_520w = music_data['artist_urls_520w']
artist_urls_540w = music_data['artist_urls_540w']
artist_urls_560w = music_data['artist_urls_560w']
artist_urls_580w = music_data['artist_urls_580w']
artist_urls_600w = music_data['artist_urls_600w']
artist_urls_620w = music_data['artist_urls_620w']
artist_urls_640w = music_data['artist_urls_640w']
artist_urls_660w = music_data['artist_urls_660w']
artist_urls_680w = music_data['artist_urls_680w']
artist_urls_700w = music_data['artist_urls_700w']
artist_urls_720w = music_data['artist_urls_720w']
artist_urls_740w = music_data['artist_urls_740w']
artist_urls_760w = music_data['artist_urls_760w']
artist_urls_780w = music_data['artist_urls_780w']
artist_urls_800w = music_data['artist_urls_800w']
artist_urls_820w = music_data['artist_urls_820w']
artist_urls_840w = music_data['artist_urls_840w']
artist_urls_860w = music_data['artist_urls_860w']
artist_urls_880w = music_data['artist_urls_880w']
artist_urls_900w = music_data['artist_urls_900w']
artist_urls_920w = music_data['artist_urls_920w']
artist_urls_940w = music_data['artist_urls_940w']
artist_urls_960w = music_data['artist_urls_960w']
artist_urls_980w = music_data['artist_urls_980w']
artist_urls_1000w = music_data['artist_urls_1000w']

artist_urls_20w_gen = ["http://music.163.com/#/artist?id={}".format(str(i)) for i in range(0, 200000)]
artist_urls_40w_gen = ["http://music.163.com/#/artist?id={}".format(str(i)) for i in range(200000, 400000)]
artist_urls_60w_gen = ["http://music.163.com/#/artist?id={}".format(str(i)) for i in range(400000, 600000)]
artist_urls_80w_gen = ["http://music.163.com/#/artist?id={}".format(str(i)) for i in range(600000, 800000)]
artist_urls_100w_gen = ["http://music.163.com/#/artist?id={}".format(str(i)) for i in range(800000, 1000000)]
artist_urls_120w_gen = ["http://music.163.com/#/artist?id={}".format(str(i)) for i in range(1000000, 1200000)]
artist_urls_140w_gen = ["http://music.163.com/#/artist?id={}".format(str(i)) for i in range(1200000, 1400000)]
artist_urls_160w_gen = ["http://music.163.com/#/artist?id={}".format(str(i)) for i in range(1400000, 1600000)]
artist_urls_180w_gen = ["http://music.163.com/#/artist?id={}".format(str(i)) for i in range(1600000, 1800000)]
artist_urls_200w_gen = ["http://music.163.com/#/artist?id={}".format(str(i)) for i in range(1800000, 2000000)]
artist_urls_220w_gen = ["http://music.163.com/#/artist?id={}".format(str(i)) for i in range(2000000, 2200000)]
artist_urls_240w_gen = ["http://music.163.com/#/artist?id={}".format(str(i)) for i in range(2200000, 2400000)]
artist_urls_260w_gen = ["http://music.163.com/#/artist?id={}".format(str(i)) for i in range(2400000, 2600000)]
artist_urls_280w_gen = ["http://music.163.com/#/artist?id={}".format(str(i)) for i in range(2600000, 2800000)]
artist_urls_300w_gen = ["http://music.163.com/#/artist?id={}".format(str(i)) for i in range(2800000, 3000000)]
artist_urls_320w_gen = ["http://music.163.com/#/artist?id={}".format(str(i)) for i in range(3000000, 3200000)]
artist_urls_340w_gen = ["http://music.163.com/#/artist?id={}".format(str(i)) for i in range(3200000, 3400000)]
artist_urls_360w_gen = ["http://music.163.com/#/artist?id={}".format(str(i)) for i in range(3400000, 3600000)]
artist_urls_380w_gen = ["http://music.163.com/#/artist?id={}".format(str(i)) for i in range(3600000, 3800000)]
artist_urls_400w_gen = ["http://music.163.com/#/artist?id={}".format(str(i)) for i in range(3800000, 4000000)]
artist_urls_420w_gen = ["http://music.163.com/#/artist?id={}".format(str(i)) for i in range(4000000, 4200000)]
artist_urls_440w_gen = ["http://music.163.com/#/artist?id={}".format(str(i)) for i in range(4200000, 4400000)]
artist_urls_460w_gen = ["http://music.163.com/#/artist?id={}".format(str(i)) for i in range(4400000, 4600000)]
artist_urls_480w_gen = ["http://music.163.com/#/artist?id={}".format(str(i)) for i in range(4600000, 4800000)]
artist_urls_500w_gen = ["http://music.163.com/#/artist?id={}".format(str(i)) for i in range(4800000, 5000000)]
artist_urls_520w_gen = ["http://music.163.com/#/artist?id={}".format(str(i)) for i in range(5000000, 5200000)]
artist_urls_540w_gen = ["http://music.163.com/#/artist?id={}".format(str(i)) for i in range(5200000, 5400000)]
artist_urls_560w_gen = ["http://music.163.com/#/artist?id={}".format(str(i)) for i in range(5400000, 5600000)]
artist_urls_580w_gen = ["http://music.163.com/#/artist?id={}".format(str(i)) for i in range(5600000, 5800000)]
artist_urls_600w_gen = ["http://music.163.com/#/artist?id={}".format(str(i)) for i in range(5800000, 6000000)]
artist_urls_620w_gen = ["http://music.163.com/#/artist?id={}".format(str(i)) for i in range(6000000, 6200000)]
artist_urls_640w_gen = ["http://music.163.com/#/artist?id={}".format(str(i)) for i in range(6200000, 6400000)]
artist_urls_660w_gen = ["http://music.163.com/#/artist?id={}".format(str(i)) for i in range(6400000, 6600000)]
artist_urls_680w_gen = ["http://music.163.com/#/artist?id={}".format(str(i)) for i in range(6600000, 6800000)]
artist_urls_700w_gen = ["http://music.163.com/#/artist?id={}".format(str(i)) for i in range(6800000, 7000000)]
artist_urls_720w_gen = ["http://music.163.com/#/artist?id={}".format(str(i)) for i in range(7000000, 7200000)]
artist_urls_740w_gen = ["http://music.163.com/#/artist?id={}".format(str(i)) for i in range(7200000, 7400000)]
artist_urls_760w_gen = ["http://music.163.com/#/artist?id={}".format(str(i)) for i in range(7400000, 7600000)]
artist_urls_780w_gen = ["http://music.163.com/#/artist?id={}".format(str(i)) for i in range(7600000, 7800000)]
artist_urls_800w_gen = ["http://music.163.com/#/artist?id={}".format(str(i)) for i in range(7800000, 8000000)]
artist_urls_820w_gen = ["http://music.163.com/#/artist?id={}".format(str(i)) for i in range(8000000, 8200000)]
artist_urls_840w_gen = ["http://music.163.com/#/artist?id={}".format(str(i)) for i in range(8200000, 8400000)]
artist_urls_860w_gen = ["http://music.163.com/#/artist?id={}".format(str(i)) for i in range(8400000, 8600000)]
artist_urls_880w_gen = ["http://music.163.com/#/artist?id={}".format(str(i)) for i in range(8600000, 8800000)]
artist_urls_900w_gen = ["http://music.163.com/#/artist?id={}".format(str(i)) for i in range(8800000, 9000000)]
artist_urls_920w_gen = ["http://music.163.com/#/artist?id={}".format(str(i)) for i in range(8800000, 9000000)]
artist_urls_940w_gen = ["http://music.163.com/#/artist?id={}".format(str(i)) for i in range(9000000, 9400000)]
artist_urls_960w_gen = ["http://music.163.com/#/artist?id={}".format(str(i)) for i in range(9400000, 9600000)]
artist_urls_980w_gen = ["http://music.163.com/#/artist?id={}".format(str(i)) for i in range(9600000, 9800000)]
artist_urls_1000w_gen = ["http://music.163.com/#/artist?id={}".format(str(i)) for i in range(9800000, 10000000)]

pool = multiprocessing.Pool()

if __name__ == "__main__":
    for url in artist_urls_20w_gen:
        data = {
            'url': url
        }
        print(data)
        artist_urls_20w.insert(data)
    for url in artist_urls_40w_gen:
        data = {
            'url': url
        }
        print(data)
        artist_urls_40w.insert(data)
    for url in artist_urls_60w_gen:
        data = {
            'url': url
        }
        print(data)
        artist_urls_60w.insert(data)
    for url in artist_urls_80w_gen:
        data = {
            'url': url
        }
        print(data)
        artist_urls_80w.insert(data)
    for url in artist_urls_100w_gen:
        data = {
            'url': url
        }
        print(data)
        artist_urls_100w.insert(data)
    for url in artist_urls_120w_gen:
        data = {
            'url': url
        }
        print(data)
        artist_urls_120w.insert(data)
    for url in artist_urls_140w_gen:
        data = {
            'url': url
        }
        print(data)
        artist_urls_140w.insert(data)
    for url in artist_urls_160w_gen:
        data = {
            'url': url
        }
        print(data)
        artist_urls_160w.insert(data)
    for url in artist_urls_180w_gen:
        data = {
            'url': url
        }
        print(data)
        artist_urls_180w.insert(data)
    for url in artist_urls_200w_gen:
        data = {
            'url': url
        }
        print(data)
        artist_urls_200w.insert(data)
    for url in artist_urls_220w_gen:
        data = {
            'url': url
        }
        print(data)
        artist_urls_220w.insert(data)
    for url in artist_urls_240w_gen:
        data = {
            'url': url
        }
        print(data)
        artist_urls_240w.insert(data)
    for url in artist_urls_260w_gen:
        data = {
            'url': url
        }
        print(data)
        artist_urls_260w.insert(data)
    for url in artist_urls_280w_gen:
        data = {
            'url': url
        }
        print(data)
        artist_urls_280w.insert(data)
    for url in artist_urls_300w_gen:
        data = {
            'url': url
        }
        print(data)
        artist_urls_300w.insert(data)
    for url in artist_urls_320w_gen:
        data = {
            'url': url
        }
        print(data)
        artist_urls_320w.insert(data)
    for url in artist_urls_340w_gen:
        data = {
            'url': url
        }
        print(data)
        artist_urls_340w.insert(data)
    for url in artist_urls_360w_gen:
        data = {
            'url': url
        }
        print(data)
        artist_urls_360w.insert(data)
    for url in artist_urls_380w_gen:
        data = {
            'url': url
        }
        print(data)
        artist_urls_380w.insert(data)
    for url in artist_urls_400w_gen:
        data = {
            'url': url
        }
        print(data)
        artist_urls_400w.insert(data)
    for url in artist_urls_420w_gen:
        data = {
            'url': url
        }
        print(data)
        artist_urls_420w.insert(data)
    for url in artist_urls_440w_gen:
        data = {
            'url': url
        }
        print(data)
        artist_urls_440w.insert(data)
    for url in artist_urls_460w_gen:
        data = {
            'url': url
        }
        print(data)
        artist_urls_460w.insert(data)
    for url in artist_urls_480w_gen:
        data = {
            'url': url
        }
        print(data)
        artist_urls_480w.insert(data)
    for url in artist_urls_500w_gen:
        data = {
            'url': url
        }
        print(data)
        artist_urls_500w.insert(data)
    for url in artist_urls_520w_gen:
        data = {
            'url': url
        }
        print(data)
        artist_urls_520w.insert(data)
    for url in artist_urls_540w_gen:
        data = {
            'url': url
        }
        print(data)
        artist_urls_540w.insert(data)
    for url in artist_urls_560w_gen:
        data = {
            'url': url
        }
        print(data)
        artist_urls_560w.insert(data)
    for url in artist_urls_580w_gen:
        data = {
            'url': url
        }
        print(data)
        artist_urls_580w.insert(data)
    for url in artist_urls_600w_gen:
        data = {
            'url': url
        }
        print(data)
        artist_urls_600w.insert(data)
    for url in artist_urls_620w_gen:
        data = {
            'url': url
        }
        print(data)
        artist_urls_620w.insert(data)
    for url in artist_urls_640w_gen:
        data = {
            'url': url
        }
        print(data)
        artist_urls_640w.insert(data)
    for url in artist_urls_660w_gen:
        data = {
            'url': url
        }
        print(data)
        artist_urls_660w.insert(data)
    for url in artist_urls_680w_gen:
        data = {
            'url': url
        }
        print(data)
        artist_urls_680w.insert(data)
    for url in artist_urls_700w_gen:
        data = {
            'url': url
        }
        print(data)
        artist_urls_700w.insert(data)
    for url in artist_urls_720w_gen:
        data = {
            'url': url
        }
        print(data)
        artist_urls_720w.insert(data)
    for url in artist_urls_740w_gen:
        data = {
            'url': url
        }
        print(data)
        artist_urls_740w.insert(data)
    for url in artist_urls_760w_gen:
        data = {
            'url': url
        }
        print(data)
        artist_urls_760w.insert(data)
    for url in artist_urls_780w_gen:
        data = {
            'url': url
        }
        print(data)
        artist_urls_780w.insert(data)
    for url in artist_urls_800w_gen:
        data = {
            'url': url
        }
        print(data)
        artist_urls_800w.insert(data)
    for url in artist_urls_820w_gen:
        data = {
            'url': url
        }
        print(data)
        artist_urls_820w.insert(data)
    for url in artist_urls_840w_gen:
        data = {
            'url': url
        }
        print(data)
        artist_urls_840w.insert(data)
    for url in artist_urls_860w_gen:
        data = {
            'url': url
        }
        print(data)
        artist_urls_860w.insert(data)
    for url in artist_urls_880w_gen:
        data = {
            'url': url
        }
        print(data)
        artist_urls_880w.insert(data)
    for url in artist_urls_900w_gen:
        data = {
            'url': url
        }
        print(data)
        artist_urls_900w.insert(data)
    for url in artist_urls_920w_gen:
        data = {
            'url': url
        }
        print(data)
        artist_urls_920w.insert(data)
    for url in artist_urls_940w_gen:
        data = {
            'url': url
        }
        print(data)
        artist_urls_940w.insert(data)
    for url in artist_urls_960w_gen:
        data = {
            'url': url
        }
        print(data)
        artist_urls_960w.insert(data)
    for url in artist_urls_980w_gen:
        data = {
            'url': url
        }
        print(data)
        artist_urls_980w.insert(data)
    for url in artist_urls_1000w_gen:
        data = {
            'url': url
        }
        print(data)
        artist_urls_1000w.insert(data)
