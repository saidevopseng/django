import scrapy

class ProductsSpider(scrapy.Spider):
    name = "products"
    start_urls = ["https://example-ecommerce.com/products"]

    def parse(self, response):
        for product in response.css("div.product"):
            yield {
                "name": product.css("h2.product-name::text").get(),
                "price": product.css("span.price::text").get(),
                "availability": product.css("p.availability::text").get(),
            }

        next_page = response.css("a.next::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
