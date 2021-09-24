from news.crawler.bcc_news_crawler import BccCrawler
from news.textSpeech.text_audio import TextSpeech

def main():
    """Main aplication fuction.
     Run this file to hear the latest news from the BCC Brazilian technology.
     The attribute pages indicates the number of news page you want listen
    """
    bcc = BccCrawler()
    news = bcc.start_surch(page=1)
    speech = TextSpeech()
    speech.get_news(news)


if __name__ == "__main__":
    main()
