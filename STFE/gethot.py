import requests

url = "https://s.weibo.com/top/summary?cate=realtimehot"

# r= requests.get("https://s.weibo.com/ajax/jsonp/gettopsug?uid=2212376751&ref=PC_topsug&url=https%3A%2F%2Fs.weibo.com%2Ftop%2Fsummary%3Fcate%3Drealtimehot&Mozilla=Mozilla%2F5.0%20(Macintosh%3B%20Intel%20Mac%20OS%20X%2010.14%3B%20rv%3A68.0)%20Gecko%2F20100101%20Firefox%2F68.0&_cb=STK_15749444841593")

r= requests.get(url)
print(r.text)