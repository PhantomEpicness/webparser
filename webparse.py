import bs4
import requests
#activate internet tag finder
res = requests.get('http://marketwatch.com/investing/stock/GOOG')
res.raise_for_status()
goog = bs4.BeautifulSoup(res.text)

#find element that will give info
elems = goog.select('bg-quote[field="Last"]')
print("length of" , len(elems))
for x in elems:
	print(x.getText())
price = elems[0].getText()
#remov decimals
priceNoDec = price.replace(',','')
print(priceNoDec)
#roundprice
finalPriceFloat = (round(float(priceNoDec),0))
print(int(finalPriceFloat))
