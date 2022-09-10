import atexit
import csv
import os
import logging

from toi_scrapper import ToiScraper

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
log = logging.getLogger(__name__)

obj_toi = ToiScraper()


def main():
    log.info('Starting Main')
    obj_toi.start_scraping()


@atexit.register
def on_exit():
    log.info("Saving File for Persistence")

    # text only csv header
    text_only_fieldnames = ['date', 'title', 'article', 'cms_id']
    # text_img csv header
    text_img_fieldnames = ['date', 'title',
                           'article', 'cms_id', 'img_link', 'img_id']

    with open('text_only.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=text_only_fieldnames)
        writer.writeheader()
        writer.writerows(obj_toi.get_text_only_rows)

    with open('text_img.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=text_img_fieldnames)
        writer.writeheader()
        writer.writerows(obj_toi.get_text_img_rows)


if __name__ == "__main__":
    main()
