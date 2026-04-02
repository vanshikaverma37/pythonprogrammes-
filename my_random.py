Movies = [
    {"name": "Rio", "year": 2014, "actor": ["blu"]},
    {"name": "Race", "year": 2008, "actor": ["Salman"]},
    {"name": "3 idiots", "year": 2009, "actor": ["Aamir khan"]},
    {"name": "Yjhd", "year": 2013, "actor": ["Ranveer"]},
    {"namee": "dangal", "year": 2016, "actor": ["Aamir khan",{"name":"test","age":[1,12,3]}]}
]
'''
for i in Movies:
    print(i['name'])
for i in Movies:
    if i['year'] >2012 and i['year'] < 2018:
        print(i)

for i in Movies:
    if i['actor'] == ['Ranveer'] or i['actor'] == ['blu']:
        print(i)

Movies[0]['year'] = {"age":24}
print(Movies)
'''
print(Movies[4]['actor'][1]['age'][2])

