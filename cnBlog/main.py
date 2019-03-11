from scrapy import cmdline
cmdline.execute("scrapy crawl blog -o blog.json".split())