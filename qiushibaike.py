from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.qiushibaike.com/')
response.encoding = response.apparent_encoding
soup = BeautifulSoup(response.text, 'html.parser')
# for i in soup.select('.content'):
#     next=i.text
#     print(next)

print('--------<span>----------------')
for x in soup.find_all('div', class_="content"):   #
    if x.text is not None:
        print(x.text)
        f=open('test.txt','a+')
        f.write(x.text)
        f.close()
# print(soup.)

# for t in soup今天在院里打扫雪，用铁楸铲雪往垃圾车上装的时候，突然想起来一件小时候发生的一件事童年趣事……<br>小时候，我和弟弟在家门口玩，弟弟拉了便便，由于老妈在忙，就让我拿着铁楸把弟弟拉的便便铲了，可能是年龄小，也可能是没拿过铁楸，当我拿着铁楸学着大人的样子，弓着腰，对着那坨翔，一用力，铁楸一扬，那坨便便飞出去一米远的距离，我走过去，接着瞄准，弓腰，用力一扬，那坨便便又飞出去一米远，然后就出现了这样的画面，一个小女孩在前面执着的拿着铁楸追着那坨便便，一个小男孩撅着屁股，一只手拉着裤子，一只手扬着纸，在后面追着.select('content'):
#     print(t.t…ext)
# print(soup.te</span>xt)
# print(soup.prettify())
# print(soup.a['class'])
# for i in soup.find_all('div', class_='content'):
#     print(i.string)
#     print(type(i.string))
#     print('------------------------------')
# print(soup.span.contents)
# for i in soup.find_all('span'):
#     print(i.get_text)

# print(soup.name)
# print(soup.a['href'])
# for i in soup.find_all('a'):
#     print(type(i))
# print(soup.prettify())
for m in soup.find_all('div', class_='content'):
    # if m.string is not None:
    print(m.text)
