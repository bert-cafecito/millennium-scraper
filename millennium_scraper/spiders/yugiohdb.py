import scrapy


class YugiohDBCardsSpider(scrapy.Spider):
    name = "yugiohdb_cards"
    allowed_domains = ["yugioh-card.com"]
    start_urls = ["https://www.db.yugioh-card.com/yugiohdb/card_list.action?clm=1&wname=CardSearch"]
    source = "yugiohdb"

    custom_settings = {
        "LOG_FILE": f"logs/{source}/cards.log",
        "FEEDS": {
            f"outputs/{source}/cards.json": {
                "format": "json",
                "overwrite": True
            }
        },
        "ITEM_PIPELINES": {
            "millennium_scraper.pipelines.CardPipeline": 100,
            "millennium_scraper.pipelines.MillenniumScraperPipeline": 200
        },
        "LOG_FILE": f"logs/{source}/cards.log"
    }

    def parse(self, response):
        # Get all product URLs on the page
        product_urls = response.css("div.pack_en").css("input.link_value::attr(value)").getall()
        # Let's count the number of product URLs
        product_count = len(product_urls)
        # Log the number of products found on the page
        self.logger.info(f"Found {product_count} products on the page")

        # Loop through each product URL
        # Let's folllow the product URL to get more details
        for product_url in product_urls:
            # Make a request to the product URL
            yield response.follow(product_url, self.parse_product)

    def parse_product(self, response):
        # Extract the product name
        extracted_product_name = response.css("header#broad_title").css("strong::text").get()

        # Check if the product name is a valid string
        if extracted_product_name:
            # Strip the product name of leading and trailing whitespaces and capitalize the first letter of each word
            extracted_product_name = extracted_product_name.strip().title()

        # Log the extracted product name
        self.logger.info(f"Extracting cards from product name: {extracted_product_name}")

        # Get all the card URLs on the product page
        card_urls = response.css("div#card_list.list").css("div.t_row.c_normal.open").css("input.link_value::attr(value)").getall()
        # Let's count the number of card URLs
        card_count = len(card_urls)
        # Log the number of cards found on the product page
        self.logger.info(f"Found {card_count} cards on the product page")

        # If the card count is 0, skip the product
        if card_count == 0:
            self.logger.info("Skipping product due to lack of cards")
            return

        # Loop through each card URL
        # Let's folllow the card URL to get more details
        for card_url in card_urls:
            # Make a request to the card URL
            yield response.follow(card_url, self.parse_card)
    
    def parse_card(self, response):
        # Create a dictionary to store the card information
        card = dict()

        # Extract the card name
        extracted_card_name = response.css("div#CardSet").css("div#cardname").css("h1::text").get()

        # Add extracted card name to the card dictionary
        card["card_name"] = extracted_card_name

        # Extract the card sets
        extracted_sets = response.css("div#update_list.list").css("div.t_row")

        # Create a list to store the card sets
        card_sets = list()

        # Loop through each card set
        # Let's see what sets the cards are in
        for extracted_set in extracted_sets:
            # Extract the set release date
            extracted_set_release_date = extracted_sets.css("div.time::text").get()
            
            # Extract the set card number
            extracted_set_card_number = extracted_sets.css("div.card_number::text").get()
            
            # Extract the set name
            extracted_set_name = extracted_sets.css("div.pack_name::text").get()

            # Extract the set card rarity
            extracted_set_rarity = extracted_sets.css("div.icon").css("span::text").get()

            # Create a dictionary to store the set information
            set_info = dict()

            # Add extracted set release date to the set dictionary
            set_info["set_release_date"] = extracted_set_release_date

            # Add extracted set card number to the set dictionary
            set_info["set_card_number"] = extracted_set_card_number

            # Add extracted set name to the set dictionary
            set_info["set_name"] = extracted_set_name

            # Add extracted set rarity to the set dictionary
            set_info["set_rarity"] = extracted_set_rarity

            # Append the set dictionary to the card sets list
            card_sets.append(set_info)

        # Add the card sets list to the card dictionary
        card["card_sets"] = card_sets

        # Extract the card sets
        extracted_text_item_boxes = response.css("div#CardSet").css("div.item_box")

        # Loop through each text item box
        # Let's see what other information the cards have
        for extracted_text_item_box in extracted_text_item_boxes:
            # Extract the item box title
            item_box_title = extracted_text_item_box.css("span.item_box_title::text").getall()

            # Extract the item box value
            item_box_value = extracted_text_item_box.css("span.item_box_value::text").getall()

            # Check if the item box title is a list
            if isinstance(item_box_title, list):
                self.logger.info("Item box title is a list")

                # Join the item box title list into a string
                item_box_title = " ".join(item_box_title)

            # Check if the item box value is a list
            if isinstance(item_box_value, list):
                self.logger.info("Item box value is a list")

                # Join the item box value list into a string
                item_box_value = " ".join(item_box_value)

            # Strip the item box title of leading and trailing whitespaces
            item_box_title = item_box_title.strip()

            # Replace spaces with underscores
            item_box_title = item_box_title.replace(" ", "_")

            # Lowercase the item box title
            item_box_title = item_box_title.lower()

            # Check if the item box item is empty and skip it
            if not item_box_title:
                self.logger.info(f"Skipping item box title because it is empty")
                continue

            # Check if the item box value is empty and skip it
            if not item_box_value:
                self.logger.info(f"Skipping item box value because it is empty")
                continue

            self.logger.info(f"Item box title: {item_box_title}")
            self.logger.info(f"Item box value: {item_box_value}")

            # Add the item box title and value to the card dictionary
            card[f"card_{item_box_title}"] = item_box_value

        # Yield the card dictionary
        yield card

