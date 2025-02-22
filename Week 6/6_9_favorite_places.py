favorite_places = {
    'roger': ['austin', 'new orleans', 'seattle'],
    'lisa': ['punta cana', 'wilmington'],
    'milo': ['lookout', 'beaver lake'],
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")