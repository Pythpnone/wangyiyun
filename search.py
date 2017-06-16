from bs4 import BeautifulSoup
import pymongo
import os
import requests
import multiprocessing
import urllib
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from langconv import *

mongodb = pymongo.MongoClient('localhost', 27017)
music_data = mongodb['music_data']
huge_album_url = music_data['huge_album_url']
fail_list = music_data['fail_list']
artist_info = music_data['artist_info']
album_info = music_data['album_info']
song_info = music_data['song_info']
artist_urls_40w = music_data['artist_urls_40w']
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


def setUsed(url):
    artist_urls_40w.update({'url': url}, {'$set': {'used': '1'}})


def kickSpace(s):
    i = 0
    j = -1
    while s[i] == ' ':
        i += 1
    s1 = s[i:]
    while s1[j] == ' ':
        j -= 1
    if j == -1:
        res = s1
    else:
        res = s1[:j]
    return res


def kickErrorName(s):
    res = None
    flag = 3
    while flag - 1 > 0:
        res = s.replace('\\', '')
        res = res.replace('/', '')
        res = res.replace(':', '')
        res = res.replace('*', '')
        res = res.replace('?', '')
        res = res.replace('\\\\', '')
        res = res.replace('>', '')
        res = res.replace('<', '')
        res = res.replace('|', '')
        res = res.replace('"', '')
        flag -= 1
    return res



header = {
    'Host': 'p3.music.126.net',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
    'Referer': 'http://music.163.com',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
}


def downPic(url, artist, filename):
    print("             p : " + url)
    url = url.replace('120y120', '428y428').replace('640y300', '640y520')
    artist = kickErrorName(kickSpace(artist)).replace('.', '')
    filename = kickErrorName(kickSpace(filename))
    try:
        pic_data = requests.get(url, headers=header, stream=True)
        if pic_data.status_code != 200:
            data = {
                'url': url,
                'dir': "./image/" + artist,
                'file_name': "./image/" + artist + "/" + filename,
                'filename': filename
            }
            fail_list.insert(data)
            return
    except:
        data = {
            'url': url,
            'dir': "./image/" + artist,
            'file_name': "./image/" + artist + "/" + filename,
            'filename': filename
        }
        fail_list.insert(data)
        return
    if not os.path.isdir("./image/" + artist):
        os.makedirs("./image/" + artist)
    file_path = "./image/" + artist + "/"
    file_name = file_path + filename
    if not os.path.exists(file_name):
        file = open(file_path + filename, "wb")
        for chunk in pic_data:
            file.write(chunk)
    return


def wikiIt(url):
    driver = webdriver.PhantomJS()
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "html5lib")
    driver.quit()

    try:
        if not soup.title.get_text().split('_')[0]:
            print('\n=== No this Wiki Page ===\n')
            return None, None
    except AttributeError:
        print('\n=== No this Wiki Page ===\n')
        return None, None
    try:
        assess = soup.select('div.para-title + .para')[-1].get_text().replace(u'\xa0', u' ').replace('&nbsp;', ' ').replace('\n', '').replace(' ', '')
    except IndexError:
        print('\n=== Index Nop - Wiki ===\n')
        return None, None
    r = re.compile(r'\[.*?\]')
    for each in r.findall(assess):
        assess = assess.replace(str(each), '')
    tags = []
    for tag in soup.select("#open-tag span"):
        tags.append(tag.get_text().replace('\n', ''))
    return assess, tags


def eatIt(url):
    desc_url = url.split('?')[0] + "/desc?" + url.split('?')[1]
    driver = webdriver.PhantomJS()
    print("          Desc : " + desc_url)
    driver.get(desc_url)
    try:
        WebDriverWait(driver, 2000, 0.5).until(EC.presence_of_element_located((By.ID, 'g_iframe')))
    except:
        pass
    try:
        driver.switch_to.frame("g_iframe")
    except:
        pass
    soup = BeautifulSoup(driver.page_source, "html.parser")
    [script.extract() for script in soup.findAll('script')]
    [style.extract() for style in soup.findAll('style')]

    try:
        artist_names = soup.select("#artist-name")[0].get('title')
    except IndexError:
        print("\n===== No " + url.split('id=')[1] + "th Artists =====\n")
        setUsed(url)
        return
    try:
        brief = soup.select('div.n-artdesc p')[0].get_text().replace(u'\xa0', u' ').replace('&nbsp;', ' ').replace('\n', '').replace(' ', '')
    except IndexError:
        brief = ""
    wb_similar_artists = soup.select('#rec-similar-artists p a')
    similar_artists = []
    for similar_artist in wb_similar_artists:
        similar_artists.append(similar_artist.get('title'))

    artist_name = Converter('zh-hans').convert(artist_names.split(' - ')[0]).encode('utf-8')
    search_key = urllib.parse.quote(artist_name)
    wiki_url = "http://baike.baidu.com/item/" + search_key
    print("      百科补充 : " + wiki_url)
    assess, tags = wikiIt(wiki_url)

    # down artist_pic
    try:
        artist_pic = soup.select("div.n-artist.f-cb > img")[0].get('src')
    except:
        pass
    pic_flag = artist_pic.split('==/')[1].split('.jpg')[0]
    if not os.path.isdir("./image/" + kickErrorName(kickSpace(artist_name.decode('utf-8')))):
        os.makedirs("./image/" + kickErrorName(kickSpace(artist_name.decode('utf-8'))))
    if pic_flag != "5639395138885805":
        downPic(artist_pic, artist_name.decode('utf-8'), "@"+artist_name.decode('utf-8')+".jpg")
    # ---------------

    album_url = url.split('?')[0] + "/album?" + url.split('?')[1] + "&limit=500"
    print("         Album : " + album_url)
    driver.get(album_url)
    try:
        WebDriverWait(driver, 2000, 0.5).until(EC.presence_of_element_located((By.ID, 'g_iframe')))
    except:
        pass
    try:
        driver.switch_to.frame("g_iframe")
    except:
        pass
    soup = BeautifulSoup(driver.page_source, "html.parser")
    [script.extract() for script in soup.findAll('script')]
    [style.extract() for style in soup.findAll('style')]

    # huge_album
    if soup.select('div.g-bd4.f-cb > div.g-mn4 > div > div > div.u-page'):
        print("\n===== A Huge Album " + url.split('id=')[1] + " =====\n")
        data = {
            'url': album_url
        }
        huge_album_url.insert(data)
        setUsed(url)
        return
    # ----------

    single_albums_url = []
    albums_name = []
    albums_img = []
    wb_albums_img = soup.select('#m-song-module div img')
    albums_time = []
    wb_albums_time = soup.select('#m-song-module p span')
    wb_albums = soup.select('#m-song-module p a')
    for single in wb_albums_img:
        img = single.get('src')
        albums_img.append(img)
    for single in wb_albums_time:
        publish_time = single.get_text()
        albums_time.append(str(publish_time))
    for single in wb_albums:
        url = "http://music.163.com/#/" + single.get('href')
        single_albums_url.append(url)
        name = single.get_text().replace(u'\xa0', u' ').replace('&nbsp;', ' ').replace('\n', '').replace(' ', '')
        albums_name.append(str(name))
    for album_img, album_name in zip(albums_img, albums_name):
        downPic(album_img, artist_name.decode('utf-8'), album_name+'.jpg')

    # artist_info
    album_name_time = []
    for (name, publish_time) in zip(albums_name, albums_time):
        album_name_time.append(name + '_' + publish_time)
    data = {
        'name': artist_name.decode('utf-8'),
        'nickname': artist_names,
        'album': album_name_time,
        'tag': tags,
        'similar': similar_artists,
        'brief': brief,
        'assess': assess,
    }
    artist_info.insert(data)
    # -----------
    print("          Name : " + artist_name.decode('utf-8'))

    for single_album_url in single_albums_url:
        print("  Single_Album : " + single_album_url)
        driver.get(single_album_url)
        try:
            WebDriverWait(driver, 2000, 0.5).until(EC.presence_of_element_located((By.ID, 'g_iframe')))
        except:
            pass
        try:
            driver.switch_to.frame("g_iframe")
        except:
            pass
        soup = BeautifulSoup(driver.page_source, "html.parser")
        [script.extract() for script in soup.findAll('script')]
        [style.extract() for style in soup.findAll('style')]

        try:
            album_name = soup.select('div.tit h2')[0].get_text().replace(u'\xa0', u' ').replace('&nbsp;', ' ')
        except IndexError:
            album_name = ""
        try:
            nick_name = soup.select('div.tit div.subtit')[0].get_text().replace(u'\xa0', u' ').replace('&nbsp;', ' ').replace('\n', '')
        except IndexError:
            nick_name = ""
        try:
            artist_name = soup.select('div.topblk p.intr')[0].get_text().split('：')[1].replace(u'\xa0', u' ').replace('&nbsp;', ' ').replace('\n', '')
        except IndexError:
            artist_name = ""
        try:
            publish_time = soup.select('div.topblk p.intr')[1].get_text().split('：')[1].replace(u'\xa0', u' ').replace('&nbsp;', ' ').replace('\n', '')
        except IndexError:
            publish_time = ""

        songs_url = []
        wb_songs_url = soup.select('table.m-table tr span.txt a')
        for song_url in wb_songs_url:
            songs_url.append("http://music.163.com/#" + song_url.get('href'))
        songs_name = []
        wb_songs_name = soup.select('table.m-table tr span.txt b')
        for song_name in wb_songs_name:
            songs_name.append(song_name.get_text().replace(u'\xa0', u' ').replace('&nbsp;', ' ').replace('\n', ''))
        songs_time = []
        wb_songs_time = soup.select('table.m-table tr span.u-dur')
        for song_time in wb_songs_time:
            songs_time.append(song_time.get_text().replace(u'\xa0', u' ').replace('&nbsp;', ' ').replace('\n', ''))
        songs_artist = []
        wb_songs_artist = soup.select('table.m-table div.text')
        for song_artist in wb_songs_artist:
            songs_artist.append(song_artist.get('title').replace(u'\xa0', u' ').replace('&nbsp;', ' ').replace('\n', ''))

        # album_info & song_info
        song_name_time_artist = []
        for (song_name, song_time, song_artist, song_url) in zip(songs_name, songs_time, songs_artist, songs_url):
            song_name_time_artist.append(song_name + '_' + song_time + '_' + song_artist)
            data = {
                'name': song_name,
                'time': song_time,
                'artist': song_artist,
                'url': song_url
            }
            song_info.insert(data)
        data = {
            'name': album_name,
            'nickname': nick_name,
            'artist': artist_name,
            'time': publish_time,
            'song': song_name_time_artist
        }
        album_info.insert(data)
        # -----------------------

    driver.quit()


if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=64)
    # test_urls = ["http://music.163.com/#/artist?id=88148"]ZDSX C
    artist_urls = []
    for artist_url in artist_urls_40w.find():
        # setused
        if artist_url['used'] == '0':
            artist_urls.append(artist_url['url'])
    pool.map(eatIt, artist_urls)
    pool.close()
    pool.join()