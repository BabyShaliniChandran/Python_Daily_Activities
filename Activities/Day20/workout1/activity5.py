import json
data='{"product":"Book","price":9.99}'
value=json.loads(data)
print(value["product"],value["price"])


