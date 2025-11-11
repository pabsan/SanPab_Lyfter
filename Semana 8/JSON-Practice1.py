import json

def save_to_json(data, filename):
  try:
    with open(filename,'w') as json_file:
      json.dump(data, json_file, indent=4)
    print(f"Successfully converted to json file {filename}")
  except IOError as e:
    print(f"Error saving data file: {e}")



my_json = '{"name": "Carlos","age": 35,"car": "nissan"}'

my_dict = {
  "name": "Austin",
  "subscriber count": 850,
  "is YouTuber": "true",
  "friends": [
    "John",
    "Sam",
    "Matthew"
  ],
  "physical attributes": {
    "height": 6,
    "weight": 200,
    "eyes": "brown",
    "is male": "true"
  }
}


data = json.loads(my_json)
save_to_json(data,'json_data1.json')
save_to_json(my_dict,'json_data2.json')



"""try:
  with open('json-data.json','w'):
    json.dumps(my_dict, 'json-data.json', indent=4)
  print(f"Successfully converted to json file")
except IOError as e:
  print(f"Error saving data file: {e}")"""