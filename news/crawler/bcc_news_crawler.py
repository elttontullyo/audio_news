from selenium import webdriver
import time

class BccCrawler():
    """Crawler fuction.
        this method through the url, get the news from the site.
         """

    def start_surch(self, page=1):
        driver = webdriver.Firefox(executable_path="../news/drivers/geckodriver")
        driver.get("https://www.bbc.com/portuguese/topics/c404v027pd4t")
        time.sleep(5)

        list_news = list()
        count = 1

        for i in range(page):
            titles = driver.find_elements_by_class_name("lx-stream-post__header-text.gs-u-align-middle")
            dates = driver.find_elements_by_class_name("qa-post-auto-meta")
            abstracts = driver.find_elements_by_class_name('lx-stream-related-story--summary.qa-story-summary')

            for post in range(len(titles)):
                try:
                    date = dates[post].text
                    title = titles[post].text
                    abstract = abstracts[post].text
                    news = (date, title, abstract)
                    list_news.append(news)
                except:
                    pass

            if page > count:
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                time.sleep(3)
                right = driver.find_element_by_class_name("lx-pagination__controls.lx-pagination__controls--right.qa-pagination-right")
                next = right.find_element_by_class_name("lx-pagination__btn-icon")
                next.click()
                time.sleep(3)

            count +=1

        driver.close()
        driver.quit()

        return list_news


