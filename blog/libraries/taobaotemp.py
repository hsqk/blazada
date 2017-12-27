import json, requests
import bs4

url_1 = "https://item.taobao.com/item.htm?id=558402991465&ali_trackid=2:mm_56305873_13364096_53086045:1514212636_359_46994810&clk1=7cc148f29c0a0c85a88f580f56ddb47c&upsid=7cc148f29c0a0c85a88f580f56ddb47c"

response = requests.get(url_1)
soup = bs4.BeautifulSoup(response.text, "html.parser")
data = soup.find("div", {"id": "J_Pine"})
itemId = data.get_attribute_list("data-itemid")
sellerId = data.get_attribute_list("data-sellerid")

url_3 = 'https://detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=558402991465&sellerId=1014483995&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,upp,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract&callback=onSibRequestSuccess'
html3 = requests.get(url_3, headers={'referer': 'https://item.taobao.com/item.htm?id=558402991465'})
html3.text


url_2 = "https://detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm"
headers = {'user-agent':'curl/7.52.1', 'referer': url_1, 'content-type':'text/plain;charset=utf8'}

headers = {'Host': 'detailskip.taobao.com', 
'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0',
'Accept': '*/*',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br',
'Referer': 'https://item.taobao.com/item.htm?id=558402991465&ali_trackid=2:mm_56305873_13364096_53086045:1514212636_359_46994810&clk1=7cc148f29c0a0c85a88f580f56ddb47c&upsid=7cc148f29c0a0c85a88f580f56ddb47c',
'Cookie': 'thw=sg; isg=Anh4l0TkVpmBX7oeaQx0XjTESi8K4dxrMzF4arLoVLNzzRm3V_Hh-5-t6f4D; t=35215280239acab37113173cd3c0a421; cna=bfJIEqMHlgECAawRMUQJh4ou; hng=SG%7Czh-CN%7CSGD%7C702; mt=ci=-1_0; _m_h5_tk=fe49c7e4de46fa213dd1e76d8017bd25_1514272809877; _m_h5_tk_enc=6d63d53bc34d67cfcad0e3af2de5bb9f; UM_distinctid=1608e18a4c414f-0e629f8787a5428-73226751-100200-1608e18a4c5330; miid=60508205546994810; um=55F3A8BFC9C50DDA6B272A9F48A7CF2B95383EBA1AD723306B41FECA697ABDB09946399E53B7F4E9CD43AD3E795C914CD0396FA17792DDF35B64662D14EA18EB; cookie2=1a693a9296af1603d5e74c79cfaac6b8; v=0; _tb_token_=7d3b7ad3bb787; uc1=cookie14=UoTdf1JKoEnXzg%3D%3D',
'DNT': '1',
'Connection': 'keep-alive',}


url_3 = 'https://detailskip.taobao.com/service/getData/1/p1/item/detail/sib.htm?itemId=558402991465&sellerId=1014483995&modules=dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,upp,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract&callback=onSibRequestSuccess'
params1 = {'itemId': itemId, 'sellerId': sellerId,  }
html1 = requests.get(url_2, data = params1, headers=headers)
params2 = {'itemId': itemId, 'sellerId': sellerId, 'modules': 'dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,upp,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract', 'callback': 'onSibRequestSuccess'}
html2 = requests.get(url_2, data = params2, headers=headers)

headers = {'user-agent':'curl/7.52.1', 'referer': url_1, 'content-type':'text/plain;charset=utf8'}


url_4='https://detailskip.taobao.com/json/dyn_combo.do'

html4 = requests.get(url_4, headers={'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0', 'referer': 'https://item.taobao.com/item.htm?id=558402991465'})

headers = {'content-type: text/plain;charset=utf8'}
result = json.loads(html.text)

import os
os.chdir("/home/huang/Desktop")
with open('temp1.txt', 'w') as txtfile:
    txtfile.write(html1.text)

with open('temp2.txt', 'w') as txtfile:
    txtfile.write(html2.text)

558402991465



itemId	558402991465
sellerId	1014483995
modules	dynStock,qrcode,viewer,price,duty,xmpPromotion,delivery,upp,activity,fqg,zjys,couponActivity,soldQuantity,originalPrice,tradeContract
callback	onSibRequestSuccess



