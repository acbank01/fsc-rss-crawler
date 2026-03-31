import feedparser
import json
from datetime import datetime

def fetch_fsc_rss(url):
    # 解析 RSS Feed
    print(f"正在抓取資料：{url}")
    feed = feedparser.parse(url)
    
    # 檢查是否抓取成功
    if feed.bozo:
        print("抓取失敗，請檢查網路或網址是否正確。")
        return
    
    news_list = []
    
    # 遍歷每一則新聞
    for entry in feed.entries:
        news_item = {
            "title": entry.get("title", ""),
            "link": entry.get("link", ""),
            "description": entry.get("description", ""),
            "published": entry.get("published", ""),
            "id": entry.get("id", "")
        }
        news_list.append(news_item)
    
    # 建立回傳資料格式
    output_data = {
        "update_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "source": feed.feed.get("title", "金管會RSS"),
        "total_count": len(news_list),
        "items": news_list
    }
    
    # 儲存為 JSON 檔案
    file_name = "fsc_news.json"
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=4)
    
    print(f"抓取完成！已儲存至 {file_name}，共 {len(news_list)} 筆資料。")

if __name__ == "__main__":
    FSC_RSS_URL = "https://www.fsc.gov.tw/ch/news/rss.aspx"
    fetch_fsc_rss(FSC_RSS_URL)
