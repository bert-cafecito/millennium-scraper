# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MillenniumScraperPipeline:
    def process_item(self, item, spider):
        return item
    
class CardPipeline:
    def process_item(self, item, spider):
        # Create an ItemAdapter for the item
        adapter = ItemAdapter(item)

        # Check if "card_name" is in the adapter
        if "card_name" in adapter:
            # Strip the card name of leading and trailing whitespaces and capitalize the first letter of each word
            adapter["card_name"] = adapter["card_name"].strip().title()

        # Check if "card_sets" is in the adapter
        if "card_sets" in adapter:
            # Loop through each set in the card_sets list
            for card_set in adapter["card_sets"]:
                # Strip the release date of leading and trailing whitespaces and capitalize the first letter of each word
                card_set["set_release_date"] = card_set["set_release_date"].strip().title()

                # Strip the card number of leading and trailing whitespaces
                card_set["set_card_number"] = card_set["set_card_number"].strip()

                # Strip the set name of leading and trailing whitespaces and capitalize the first letter of each word
                card_set["set_name"] = card_set["set_name"].strip().title()

                # Strip the set rarity of leading and trailing whitespaces and capitalize the first letter of each word
                card_set["set_rarity"] = card_set["set_rarity"].strip().title()

        # Check if "card_icon" is in the adapter
        if "card_icon" in adapter:
            # Strip the card icon of leading and trailing whitespaces
            adapter["card_icon"] = adapter["card_icon"].strip()

        # Check if "card_attribute" is in the adapter
        if "card_attribute" in adapter:
            # Strip the card attribute of leading and trailing whitespaces and capitalize the first letter of each word
            adapter["card_attribute"] = adapter["card_attribute"].strip().title()

        # Check if "card_level" is in the adapter
        if "card_level" in adapter:
            # Strip the card level of leading and trailing whitespaces
            adapter["card_level"] = adapter["card_level"].strip()

        # Check if "card_atk" is in the adapter
        if "card_atk" in adapter:
            # Strip the card atk of leading and trailing whitespaces
            adapter["card_atk"] = adapter["card_atk"].strip()

        # Check if "card_def" is in the adapter
        if "card_def" in adapter:
            # Strip the card def of leading and trailing whitespaces
            adapter["card_def"] = adapter["card_def"].strip()

        # Check if "card_link" is in the adapter
        if "card_link" in adapter:
            # Strip the card link of leading and trailing whitespaces
            adapter["card_link"] = adapter["card_link"].strip()

        # Check if "card_rank" is in the adapter
        if "card_rank" in adapter:
            # Strip the card rank of leading and trailing whitespaces
            adapter["card_rank"] = adapter["card_rank"].strip()

        # Check if "card_pendulum_scale" is in the adapter
        if "card_pendulum_scale" in adapter:
            # Strip the card pendulum scale of leading and trailing whitespaces
            adapter["card_pendulum_scale"] = adapter["card_pendulum_scale"].strip()

        # Return the item
        return item
