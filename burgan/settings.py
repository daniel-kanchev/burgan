BOT_NAME = 'burgan'
SPIDER_MODULES = ['burgan.spiders']
NEWSPIDER_MODULE = 'burgan.spiders'
LOG_LEVEL = 'WARNING'
ROBOTSTXT_OBEY = False
ITEM_PIPELINES = {
   'burgan.pipelines.DatabasePipeline': 300,
}
USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0'