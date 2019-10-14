# -*- coding: utf-8 -*-
import scrapy



class PostsSpider(scrapy.Spider):
    name = 'posts'
    allowed_domains = ['techcrunch.com']
    start_urls = ['https://techcrunch.com/']

    def start_requests(self):
        yield scrapy.Request(
            url='https://techcrunch.com/',
            callback=self.parse,
        )

    def parse(self, response):
        posts = response.xpath('//div[@class="river river--homepage"]/div')
        for post in posts:
            title = post.xpath('.//header/h2/a/text()').get()
            slug = post.xpath('.//header/h2/a/@href').get()[23:]
            author = post.xpath('.//header/div/div/span/a/text()').get()
            hero_image = post.xpath('.//footer/figure/a/img/@src').get()
            pub_date = post.xpath('.//header/div/div/time/@datetime').get()

            absolute_url = f'https://techcrunch.com/{slug}'
            yield scrapy.Request(
                url=absolute_url,
                callback=self.post_parse,
                meta={
                    'title': title,
                    'slug': slug,
                    'author': author,
                    'hero_image': hero_image,
                    'pub_date': pub_date
                }
            )

        next_page = response.xpath('//a[@class="load-more"]/@href').get()

        if next_page:
            yield scrapy.Request(
                url=next_page,
                callback=self.parse
            )


    def post_parse(self, response):
        title = response.request.meta['title']
        slug = response.request.meta['slug']
        author = response.request.meta['author']
        hero_image = response.request.meta['hero_image']
        pub_date = response.request.meta['pub_date']
        text = response.xpath(
            '//div[@class="article-content"]/p/text() | '
            '//div[@class="article-content"]/h2/text() | '
            '//div[@class="article-content"]/div/p/text()'
        ).getall()
        yield {
            'title': title,
            'slug': slug,
            'author': author,
            'hero_image': hero_image,
            'pub_date': pub_date,
            'text': ' '.join(text)[:200]
        }
