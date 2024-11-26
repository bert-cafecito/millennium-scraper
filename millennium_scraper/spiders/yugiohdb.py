import scrapy


class YugiohDBCardsSpider(scrapy.Spider):
    name = "yugiohdb_cards"
    allowed_domains = ["yugioh-card.com"]
    start_urls = ["https://www.db.yugioh-card.com/yugiohdb/card_list.action?clm=1&wname=CardSearch"]
    source = "yugiohdb"

    custom_settings = {
        "LOG_ENABLED": True,
        "LOG_FILE": f"logs/{source}/cards.log",
        "FEEDS": {
            f"outputs/{source}/cards.json": {
                "format": "json",
                "overwrite": True
            }
        }
    }

    def parse(self, response):
        # Get all product URLs on the page
        product_urls = response.css("div.pack_en").css("input.link_value::attr(value)").getall()
        # Let's count the number of product URLs
        product_count = len(product_urls)
        self.logger.info(f"Found {product_count} products on the page")

        # Loop through each product URL
        # Let's folllow the product URL to get more details
        for product_url in product_urls[:5]:
            yield response.follow(product_url, self.parse_product)

    def parse_product(self, response):
        # Get all the card URLs on the product page
        card_urls = response.css("div#card_list.list").css("div.t_row.c_normal.open").css("input.link_value::attr(value)").getall()
        # Let's count the number of card URLs
        card_count = len(card_urls)
        self.logger.info(f"Found {card_count} cards on the product page")

        # Loop through each card URL
        # Let's folllow the card URL to get more details
        for card_url in card_urls[:5]:
            # Make a request to the card URL
            yield response.follow(card_url, self.parse_card)
    
    def parse_card(self, response):
        pass