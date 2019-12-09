import json

with open('activity.json', 'r') as file:
    data = json.load(file)

act = data.get('place_activity')
print(f'{act.get("id")}\n'
      f'{act.get("title")}\n'
      f'{act.get("action_kicker")}\n'
      f'{act.get("description")}\n'
      f'{act.get("place").get("city")}\n'
      f'{act.get("place").get("country")}\n'
      f'{act.get("place").get("lat")}\n'
      f'{act.get("place").get("lng")}\n'
      f'{act.get("place").get("phone")}\n'
      f'{act.get("place").get("website")}')
