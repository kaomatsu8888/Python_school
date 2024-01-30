import requests
from bs4 import BeautifulSoup

# webページを取得して解析する
load_url = "https://www.yahoo.co.jp/categories/it"
html = requests.get(load_url)

# レスポンスの状態をチェックする
if html.status_code == 200:
    soup = BeautifulSoup(html.content, "html.parser")

    # 特定のクラス名を持つliタグを検索して、トピックスのテキストを表示する
    # 注意: クラス名は実際のウェブページに基づいて調整する必要があるかもしれません
    topics = soup.find_all("li", class_="sc-fHuLxr bowRh")[:8] # 最初の8個のトピックスを取得

    for topic in topics:
        link = topic.find("a")
        if link and link.text:
            print(link.text.strip()) # トピックスのテキストを表示
else:
    print("ウェブページの読み込みに失敗しました。ステータスコード:", html.status_code)
