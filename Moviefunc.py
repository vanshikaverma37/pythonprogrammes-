Movies = [
    {"name": "Rio", "year": 2014, "actor": ["blu"]},
    {"name": "Race", "year": 2008, "actor": ["Salman"]},
    {"name": "3 idiots", "year": 2009, "actor": ["Aamir khan"]},
    {"name": "Yjhd", "year": 2013, "actor": ["Ranveer"]},
    {"namee": "dangal", "year": 2016, "actor": ["Aamir khan",{"name":"test","age":[1,12,3]}]}]
def actorr( actor_name):
    for movie in Movies:
        if actor_name in movie["actor"]:
            return movie["name"]
        
        
print(actorr('Ranveer'))


