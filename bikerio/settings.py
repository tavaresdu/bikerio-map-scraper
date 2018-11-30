# -*- coding: utf-8 -*-
from datetime import datetime

BOT_NAME = 'bikerio'

SPIDER_MODULES = ['bikerio.spiders']
NEWSPIDER_MODULE = 'bikerio.spiders'

ROBOTSTXT_OBEY = True

TELNETCONSOLE_ENABLED = False

ITEM_PIPELINES = {
   'bikerio.pipelines.BikerioPipeline': 300,
}

LOG_STDOUT = True
LOG_FILE = 'bikerio/log/' + datetime.now().isoformat() + '.log'