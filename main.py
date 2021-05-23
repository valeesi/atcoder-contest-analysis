import urllib.request
from datetime import datetime
from bs4 import BeautifulSoup

url = "https://atcoder.jp/contests/archive?page="

dates = []
dates_st = []
for num in range(1, 8):
    req = urllib.request.urlopen(url + str(num))
    data = BeautifulSoup(req, "html.parser")
    for row in data.find_all('tr'):
        asd = 0
        if row.find('td') is not None:
            dt = datetime.strptime(row.find_all('td')[0].text, '%Y-%m-%d %H:%M:%S%z');
            dates.append(dt)
            dates_st.append(row.find_all('td')[0].text)
    print('#%d done' % num)

counter = 0
counterYear = 0
for ele in dates_st:
    if "21:00" in ele:
        counter += 1
print('Total count: %d' % counter)
print('Total: %d' % len(dates_st))
print('Percentage: %f' % (counter / len(dates_st) * 100))
