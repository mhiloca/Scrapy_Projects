# -*- coding: utf-8 -*-
import scrapy
import json


class XhrsSpider(scrapy.Spider):
    name = 'xhrs'

    payload = '''
        {"categoryId":"4","manufacturerId":"0","vendorId":"0","priceRangeFilterModel7Spikes":{"CategoryId":"4",
        "ManufacturerId":"0","VendorId":"0","SelectedPriceRange":{},"MinPrice":"1800","MaxPrice":"12500"},
        "specificationFiltersModel7Spikes":{"CategoryId":"4","ManufacturerId":"0","VendorId":"0",
        "SpecificationFilterGroups":[{"Id":27,"FilterItems":[{"Id":"103","FilterItemState":"Unchecked"},
        {"Id":"104","FilterItemState":"Unchecked"},{"Id":"3854","FilterItemState":"Unchecked"},
        {"Id":"2626","FilterItemState":"Unchecked"}]},{"Id":20,"FilterItems":[{"Id":"92","FilterItemState":"Unchecked"}]},
        {"Id":11,"FilterItems":[{"Id":"302","FilterItemState":"Unchecked"},{"Id":"2494","FilterItemState":"Unchecked"}]},
        {"Id":6,"FilterItems":[{"Id":"2461","FilterItemState":"Unchecked"},{"Id":"21","FilterItemState":"Unchecked"},
        {"Id":"25","FilterItemState":"Unchecked"},{"Id":"26","FilterItemState":"Unchecked"}]},
        {"Id":5,"FilterItems":[{"Id":"2742","FilterItemState":"Unchecked"},
        {"Id":"2743","FilterItemState":"Unchecked"},{"Id":"3493","FilterItemState":"Unchecked"}]},
        {"Id":2,"FilterItems":[{"Id":"8","FilterItemState":"Unchecked"},
        {"Id":"1451","FilterItemState":"Unchecked"}]},{"Id":8,"FilterItems":[{"Id":"61","FilterItemState":"Unchecked"},
        {"Id":"3458","FilterItemState":"Unchecked"},{"Id":"3719","FilterItemState":"Unchecked"}]},
        {"Id":334,"FilterItems":[{"Id":"2489","FilterItemState":"Unchecked"},{"Id":"2488","FilterItemState":"Unchecked"}]},
        {"Id":628,"FilterItems":[{"Id":"5080","FilterItemState":"Unchecked"}]},
        {"Id":680,"FilterItems":[{"Id":"4935","FilterItemState":"Unchecked"}]}]},
        "manufacturerFiltersModel7Spikes":{"CategoryId":"4","ManufacturerFilterItems":[{"Id":"2","FilterItemState":"Unchecked"},
        {"Id":"1","FilterItemState":"Unchecked"},{"Id":"44","FilterItemState":"Unchecked"},
        {"Id":"108","FilterItemState":"Unchecked"}]},
        "pageNumber":1,"orderby":"10","viewmode":"grid","pagesize":0,"queryString":"",
        "shouldNotStartFromFirstPage":false,"keyword":"","searchCategoryId":"0",
        "searchManufacturerId":"0","searchVendorId":"0","priceFrom":"","priceTo":"",
        "includeSubcategories":"False","searchInProductDescriptions":"False",
        "advancedSearch":"False","isOnSearchPage":"False"}
    '''

    def start_requests(self):
        yield scrapy.Request(
            url="http://eastasiaeg.com/en/getFilteredProducts",
            method="POST",
            body=self.payload,
            headers={"Content-type": "application/json"}
        )
        new_payload = json.loads(self.payload)
        for page in range(2,10):
            new_payload['pageNumber'] = page
            yield scrapy.Request(
                url="http://eastasiaeg.com/en/getFilteredProducts",
                method="POST",
                body =json.dumps(new_payload),
                headers={'Content-type': 'application/json'},
                callback=self.parse
            )

    def parse(self, response):
        for product in response.xpath("//div[@class='item-box']"):
            yield {
                "product-item": product.xpath("./div[@class='product-item']/div[@class='details']/h2/a/text()").extract_first()
            }
