import pymongo

mongodb = pymongo.MongoClient('localhost', 27017)
music_data = mongodb['music_data']
huge_album_url = music_data['huge_album_url']
fail_list = music_data['fail_list']
artist_info = music_data['artist_info']
album_info = music_data['album_info']
song_info = music_data['song_info']
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

# for each in artist_urls_20w.find():
#     artist_urls_20w.update({'_id': each['_id']}, {'$set': {'used': '0'}})

for each in artist_urls_40w.find():
    artist_urls_40w.update({'_id': each['_id']}, {'$set': {'used': '0'}})