def describe_city(city_name, country_name='the united states'):
    """display information about a city."""
    print(f"\n{city_name.title()} is a city in {country_name.title()}.")
    
describe_city('tulum','mexico')
describe_city('punta cana','the dominican republic')
describe_city('barcelona','spain')
describe_city('new york')
describe_city('holden beach')