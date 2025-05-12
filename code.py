import requests

# ニュースを取得する関数
def get_news(api_key, keyword, page_size=10):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": f'"{keyword}"',  # 完全一致検索
        "apiKey": api_key,
        "pageSize": page_size,
        "sortBy": "relevancy"
    }
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            # キーワードがタイトルに含まれる記事のみ返す
            return [article for article in data.get("articles", []) if keyword.lower() in article["title"].lower()]
        else:
            print("ニュースの取得に失敗しました。ステータスコード:", response.status_code)
            return []
    except Exception as e:
        print("エラーが発生しました:", e)
        return []

# ニュースを表示する関数
def show_news(articles, title="ニュース一覧"):
    if len(articles) == 0:
        print(f"{title}が見つかりませんでした。")
    else:
        print(f"\n{title}:")
        for i, article in enumerate(articles):
            print(f"{i + 1}. タイトル: {article['title']}")
            print(f"   URL: {article['url']}")

# メイン処理
if __name__ == "__main__":
    API_KEY = "API"  # NewsAPIのAPIキーを入力
    if API_KEY == "ここにAPIキーを入力してください":
        print("APIキーを設定してください！")
    else:
        # ユーザーにキーワードを入力させる
        keyword = input("検索したいキーワードを入力してください: ").strip()
        print(f"\n=== '{keyword}'に基づく上位10件のニュース ===")
        news = get_news(API_KEY, keyword, page_size=10)
        show_news(news, title=f"'{keyword}'に基づく上位10件のニュース")
