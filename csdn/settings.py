# -*- coding: utf-8 -*-

# Scrapy settings for stack project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'csdn'
DOWNLOAD_DELAY = 5
SPIDER_MODULES = ['csdn.spiders']
NEWSPIDER_MODULE = 'csdn.spiders'
ITEM_PIPELINES = ['csdn.pipelines.CsdnPipeline',]
MONGODB_SERVER="localhost"
MONGODB_PORT=27017
MONGODB_DB="csdn"
MONGODB_COLLECTION="article"
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'stack (+http://www.yourdomain.com)'
