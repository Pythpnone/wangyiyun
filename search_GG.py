from bs4 import BeautifulSoup
import requests
import pymongo
import multiprocessing
import urllib
import time

mongodb = pymongo.MongoClient('localhost', 27017)
music_data = mongodb['music_data']
artist_url = music_data['artist_url']
info_url = music_data['info_url']
info_search = music_data['info_search']
album_url = music_data['album_data']


def downPic(url, filename):
    web_data = urllib.request.urlopen(url)
    pic = web_data.read()
    file = open("d:\\python\\163data\\image\\%s"%filename, "wb")
    file.write(pic)
    file.close()
    return
    # downPic("http://www.iplaypython.com/uploads/allimg/160127/2-16012G52024328.jpg", "a.jpg")

# search_key = ""
# search_key = urllib.parse.quote(search_key)
# url = "http://baike.baidu.com/item/" + search_key

header = {
    'Host': 'music.163.com',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
    'Referer': 'https://www.baidu.com/link?url=3VudAB40U09aqET7JhpW3FmhWc_mnx2qo4W-o7mtAzC&wd=&eqid=ac21f8a50002516b00000004581e989e',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'Cookie': "vjuids=be7880ef6.1556c80c362.0.abd21b1a; _ntes_nnid=6219eb7553b31f8e284eb20eff778347,1466404225896; _ntes_nuid=6219eb7553b31f8e284eb20eff778347; usertrack=c+5+hVd+QDYmzgr067B2Ag==; __utma=187553192.1714647792.1466408510.1467069946.1468055613.4; __utmz=187553192.1466845295.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __oc_uuid=72b12dd0-36ba-11e6-b576-2f9d079e64d1; nteslogger_exit_time=1469529692545; __gads=ID=90d9f0c9c72031dc:T=1469617125:S=ALNI_MafSd4Rm8ybgvBb1UdAdu0BP2OCZw; NTES_CMT_USER_INFO=50529804%7C1806234223%7Chttps%3A%2F%2Fsimg.ws.126.net%2Fe%2Fmimg.126.net%2Fp%2Fbutter%2F1008031648%2Fimg%2Fface_big.gif.39x39.100.jpg%7Cfalse%7CMTgwNjIzNDIyM0BxcS5jb20%3D; vjlast=1466404226.1476150956.11; NTES_REPLY_NICKNAME=1806234223%40qq.com%7C1806234223%7C8265482336456558623%7C6116989598%7Chttp%3A%2F%2Fmimg.126.net%2Fp%2Fbutter%2F1008031648%2Fimg%2Fface_big.gif%7CLQogx4qENy.1HPRGiBBdFNymvOAkxhF_tqRnIW3KBQrohhzS8RdvBw.FHPtBt_PCX3glB2ZTbaZ56JEm56UTKUeYMvJQ26sRa%7C1%7C2; vinfo_n_f_l_n3=e4f5e66368bfec88.1.11.1466404225907.1475647100406.1476150987276; _jzqco=%7C%7C%7C%7C%7C1.1414289132.1475901812140.1476327543303.1476327546564.1476327543303.1476327546564.72b4e46481c2481faf04a5d43e91bbee.1.0.7.7; P_INFO=m18607007147_1@163.com|1477196835|0|yanxuan_web|00&99|jix&1476327554&fa#jix&360100#10#0#0|186147&1||18607007147@163.com; _ga=GA1.2.1714647792.1466408510; JSESSIONID-WYYY=a08d970c0b0817158efdaffaf6b36d04b1af2c21ffefd091f1235a155f15ac6691ad5c2007e3696d8d22cbb10d83ae7ebb257800f4195deba5c6572a25bc1c37049568bd42ad671e528f806270b34b1af42dec73942fda551b8c7f1e9f78c45d81aa60c64ee6d77a8276193f092e28abb32e1f13a16bf024c28ec0dea6ddcaa30071baf3%3A1478452482345; _iuqxldmzr_=25; __remember_me=true; MUSIC_U=979b2dad494f0c71fd30671cc215694334d6fca6a91a7ce53ddcf0814940a274e178cdf3bbf7380e2b1faec046126b0641049cea1c6bb9b6; __csrf=96a6fdfdced02f1457a916d3acf5f85c; NETEASE_WDA_UID=64236446#|#1429324896073; __utma=94650624.1498581925.1466321311.1478405187.1478448060.23; __utmb=94650624.62.10.1478448060; __utmc=94650624; __utmz=94650624.1478400162.21.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic"
}


def checkExists(url):
    wb_data = requests.get(url, headers=header)
    print(wb_data)
    soup = BeautifulSoup(wb_data.text, "html5lib")
    artist_name = soup.select("#artist-name")
    print(artist_name)
    artist_pic = soup.select("div.g-bd4.f-cb > div.g-mn4 > div > div > div.n-artist.f-cb > img")[0].get('src')
    if artist_pic != "http://p3.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg?param=640y300":
        downPic(artist_pic, artist_name+".jpg")

artist_urls = ["http://music.163.com/#/artist?id={}".format(str(i)) for i in range(0, 10000000)]

# if __name__ == "__main__":
#     pool = multiprocessing.Pool(processes=4)
#     for artist_url in artist_urls:
#         print("处理网页 : " + artist_url.split("id=")[1])
#         pool.apply_async(checkExists, (artist_url,))
#         print("完成处理 : " + artist_url.split("id=")[1])
#     pool.close()
#     pool.join()

url = "http://music.163.com/#/artist/?id=81245"
print(url)
checkExists(url)