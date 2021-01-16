class Locators:

    """Page 1"""
    
    # main locators
    ADRESS = '//div[@class="property-address"]/h1//text()'
    PRICE = '//*[@class="property-info__price qa-property-price" or @class="removed-listing__price qa-property-price"]/text()'
    SQUARE_METERS = '//div[@class="property-attributes-table__row qa-living-area-attribute"]/dd//text()'
    BALCONY = ''
    CITY = '//div[@class="property-address"]/div/span//text()'
    
    # additional locators
    DATA = '/html/head/script[40]/text()'
    # ITEM_DATA = '(//script[@type="application/ld+json"])[3]/text()'
    PAGES_AMOUNT = '//div[@class="pagination"]/a[last()-1]/text()'

    """Page 2"""
    
    # main locators
    
    # additional locators
