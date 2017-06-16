from mongoengine import *
connect('music_data', host='127.0.0.1', port=27017)

help(Document)

# Create your models here

class Artist_info(Document):
    name = StringField()
    nickname = StringField()
    brief = StringField()
    assess = StringField()
    album = ListField(StringField())
    tag = ListField(StringField())
    similar = ListField(StringField())
    meta = {'collection': 'artist_info'}

for i in Artist_info.objects:
    print(i.name)