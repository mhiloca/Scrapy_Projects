# -*- coding: utf-8 -*-
import scrapy
import json


class AirbnbsSpider(scrapy.Spider):
    name = 'airbnbs'
    allowed_domains = ['www.airbnb.com.br']

    def start_requests(self):
        yield scrapy.Request(
            url='https://www.airbnb.com.br/api/v2/explore_tabs?_format=for_explore_search_web&auto_ib=false&client_session_id=dd241a48-bdd0-4543-a165-21638fc6967f&currency=BRL&current_tab_id=all_tab&experiences_per_grid=20&federated_search_session_id=a6505e3b-f13b-4fc1-8c48-e6ebe2f19504&fetch_filters=true&guidebooks_per_grid=20&has_zero_guest_treatment=true&hide_dates_and_guests_filters=false&is_guided_search=true&is_new_cards_experiment=true&is_standard_search=true&items_offset=0&items_per_grid=18&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&last_search_session_id=9c8f53db-4694-4e8a-baab-78259ac2c51a&locale=pt&metadata_only=false&place_id=ChIJ1zLGsk45J5URRscEagtVvIE&query=Florian%C3%B3polis%20-%20SC&query_understanding_enabled=true&refinement_paths%5B%5D=%2Ffor_you&satori_version=1.1.9&screen_height=467&screen_size=medium&screen_width=983&search_type=autocomplete_click&section_offset=8&selected_tab_id=all_tab&show_groupings=true&supports_for_you_v3=true&tab_id=all_tab&timezone_offset=-180&version=1.7.0',
            callback=self.parse_id
        )

    def parse_id(self, response):
        pass

    def parse(self, response):
        pass
