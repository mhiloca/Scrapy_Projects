# -*- coding: utf-8 -*-
import scrapy


class GdpDebtSpider(scrapy.Spider):
    name = 'gdp_debt'
    allowed_domains = ['worldpopulationreview.com/countries/countries-by-national-debt']
    start_urls = ['http://worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        countries = response.xpath('//table[@class="table table-striped"]/tbody/tr')
        for country in countries:
            name = country.xpath('.//td[1]/a/text()').get()
            gdp_debt = country.xpath('.//td[2]/text()').get()
            population = country.xpath('.//td[3]/text()').get()

            yield {
                'country_name': name,
                'gdp_debt': gdp_debt,
                'population': population
            }
