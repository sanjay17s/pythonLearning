cities = {
    'chennai' : {
        'country':'india',
        'liking':'dislike',
        'fact':'lot of beaches'
    },
     'bangalore' : {
        'country':'india',
        'liking':'dislike',
        'fact':'no  beaches'
    }
}

for city,city_info in cities.items():
    print(f"{city} is in {city_info['country']}")
