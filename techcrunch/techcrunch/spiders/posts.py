# -*- coding: utf-8 -*-
import scrapy


class PostsSpider(scrapy.Spider):
    name = 'posts'
    allowed_domains = ['techcrunch.com']
    start_urls = ['https://techcrunch.com/']

    def parse(self, response):
        posts = response.xpath('//div[@class="river river--homepage"]/div')
        for post in posts:
            title = post.xpath('.//header/h2/a/text()').get()
            slug = post.xpath('.//header/h2/a/@href').get()[23:]
            author = post.xpath('.//header/div/div/span/a/text()').get()
            hero_image = post.xpath('.//footer/figure/a/img/@src').get()
            pub_date = post.xpath('.//header/div/div/time/@datetime').get()

            yield {
                'title': title,
                'slug': slug,
                'author': author,
                'hero_image': hero_image,
                'pub_date': pub_date
            }
