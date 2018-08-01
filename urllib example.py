import urllib.request

url1 = "https://metrouk2.files.wordpress.com/2017/12/888848052.jpg?w=748&h=505&crop=1&quality=80"
url2 = "https://cdn.images.dailystar.co.uk/dynamic/58/photos/561000/620x/Cristiano-Ronaldo-683731.jpg"
url3 = "https://e00-marca.uecdn.es/assets/multimedia/imagenes/2018/06/07/15283977760213.jpg"

urllistesi = [url1,url2,url3]
say = 1
for url in urllistesi:
    urllib.request.urlretrieve(url,"Resim"+str(say)+".jpg")
    say+=1