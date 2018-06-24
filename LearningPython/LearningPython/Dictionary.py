sammy = {'username': 'sammy-shark', 'online': True, 'followers': 987}
print(sammy)
print(sammy["username"])
print(sammy["online"])
print(sammy["followers"])

print(sammy.keys())
print(sammy.values())
print(sammy.items())

for items in sammy.keys():
    print(sammy[items])