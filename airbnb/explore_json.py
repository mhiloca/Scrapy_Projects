import json

with open('gastronomia.json', 'r') as file:
    data = json.load(file)

trips = data.get('explore_tabs')[0].get('sections')[1].get('trip_templates')

for trip in trips:
    title = trip.get('display_text')
    kicker = trip.get('kicker_text')
    picture = trip.get('picture').get('original_picture')
    lat = trip.get('lat')
    lon = trip.get('lng')
    print(f'{title}\n{kicker}\n{picture}\n{lat}\n{lon}')
    print('- ' * 15)
