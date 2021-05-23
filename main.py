import urllib
import urllib.request
from datetime import datetime
from bs4 import BeautifulSoup

url = "https://atcoder.jp/contests/archive?page="

dates = []
for num in range(1, 8):
    req = urllib.request.urlopen(url + str(num))
    data = BeautifulSoup(req, "html.parser")
    for row in data.find_all('tr'):
        asd = 0
        if row.find('td') is not None:
            dates.append(datetime.strptime(row.find_all('td')[0].text, '%Y-%m-%d %H:%M:%S%z'))

    # if (row.find_all('td')[0] !== undefined):

    print('#%d done' % num)

# if __name__ == '__main__':
#     print_hi('PyCharm')
