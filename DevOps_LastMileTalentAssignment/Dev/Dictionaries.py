#Key value pairs
customer = {
    "name": "Bob Smith",
    "age": 30,
    "is_verified": True
}
print(customer.get("name")) #makes sure key exists otherwise returns None value
print(customer["age"])
customer["name"] = "Jason Rooz"
print(customer["name"])