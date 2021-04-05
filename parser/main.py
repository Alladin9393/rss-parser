"""
Script for download rss-feeds to json file.
"""
from time import sleep
import json
import feedparser


class FeedDownloader:
    def __init__(self, url_list: list):
        """
        """
        self.url_list = url_list

    @staticmethod
    def _write_feed(feeds):
        open('feeds.json', 'w').close()
        for feed in feeds:
            feed = json.dumps(feed[0])

            with open('feeds.json', 'a') as f:
                f.write(feed)

    def process_feeds(self):
        """
        :return:
        """
        while True:
            feeds = []
            for url in self.url_list:

                print(url)
                res_feed_tape = feedparser.parse(url)
                res_feeds = res_feed_tape.get('entries')
                feeds.append(res_feeds)

                sleep(5)

            self._write_feed(feeds)
            sleep(500)


if __name__ == '__main__':
    feeddown = FeedDownloader(['https://www.informationweek.com/rss_simple.asp', 'https://www.infoworld.com/index.rss'])
    feeddown.process_feeds()
