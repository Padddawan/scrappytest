import scrapy

class WikiSpider(scrapy.Spider):
    name = "wiki_spider"
    start_urls = ['https://wiki.guildwars2.com/wiki/War_Room_Restoration_1']

    def parse(self, response):
        SET_SELECTOR = '.mediawiki'
        for wikiset in response.css(SET_SELECTOR):

            IMAGE_SELECTOR = '.image::text'
            BUILDING_SELECTOR = './/dl[dt/text() = " Building"]/dd/a/text()'
            yield {
                'building': wikiset.xpath(BUILDING_SELECTOR).extract_first(),
                'image': wikiset.css(IMAGE_SELECTOR).extract(),
}
            