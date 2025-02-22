rivers_countries = {
    'nile' : 'egypt',
    'mississippi' : 'united states',
    'amazon' : 'brazil',
}
for river, country in rivers_countries.items():
    print(f"The {river.title()} runs through {country.title()}.")

for river in rivers_countries:
    print(river.title())

for country in rivers_countries.values():
    print(country.title())  
