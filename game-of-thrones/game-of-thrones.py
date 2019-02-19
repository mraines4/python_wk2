from characters import characters
from houses import houses
# print(len(characters))
# jon_snow = {"url":"https://anapioficeandfire.com/api/characters/583","name":"Jon Snow","gender":"Male","culture":"Northmen","born":"In 283 AC","died":"","titles":["Lord Commander of the Night's Watch"],"aliases":["Lord Snow","Ned Stark's Bastard","The Snow of Winterfell","The Crow-Come-Over","The 998th Lord Commander of the Night's Watch","The Bastard of Winterfell","The Black Bastard of the Wall","Lord Crow"],"father":"","mother":"","spouse":"","allegiances":["https://anapioficeandfire.com/api/houses/362"],"books":["https://anapioficeandfire.com/api/books/5"],"povBooks":["https://anapioficeandfire.com/api/books/1","https://anapioficeandfire.com/api/books/2","https://anapioficeandfire.com/api/books/3","https://anapioficeandfire.com/api/books/8"],"tvSeries":["Season 1","Season 2","Season 3","Season 4","Season 5","Season 6"],"playedBy":["Kit Harington"]}

# # print out the key names individually
# # for k in jon_snow:
# #     print(k)

# # print out just the values
# # for k in jon_snow:
# #     print(jon_snow[k])

# # print both the key and the value
# for k in jon_snow:
#     print("%s: %s" % (k, jon_snow[k]))


# print how many characters 
def charA(char_list):
    start_with_a = 0
    for person in char_list:
        if person['name'][0] == 'A':
            start_with_a += 1
    return start_with_a

print(charA(characters))

# How many characters names start with "Z"?
def charZ(char_list):
    start_with_z = 0
    for person in char_list:
        if person['name'][0] == 'Z':
            start_with_z += 1
    return start_with_z

print(charZ(characters))

# How many characters are dead?
def deadChar(char_list):
    dead_count = 0
    for person in char_list:
        if len(person['died']) > 0:
            dead_count += 1
    return dead_count

print(deadChar(characters))

# Who has the most titles?
def mostTitles(char_list):
    most_so_far = 0
    most_titles = ''
    for person in char_list:
        if len(person['titles']) > most_so_far:
            most_so_far = len(person['titles'])
            most_titles = person['name']
    return most_titles

print(mostTitles(characters))

# How many are Valyrian?
def areValyrian(char_list):
    valyrian = 0
    for person in char_list:
        if person['culture'] == 'Valyrian':
            valyrian += 1
    return valyrian

print(areValyrian(characters))

# What actor plays "Hot Pie" (and don't use IMDB)?
def hotPieActor(char_list):
    for person in char_list:
        if person['name'] == 'Hot Pie':
            return person['playedBy'][0]

print(hotPieActor(characters))

# How many characters are *not* in the tv show?
def notInShow(char_list):
    not_in_show = 0
    for person in char_list:
        if len(person['tvSeries'][0]) == 0:
            not_in_show += 1
    return not_in_show

print(notInShow(characters))

# Produce a list characters with the last name "Targaryen"
def Targaryens(char_list):
    targaryen_list = []
    for person in char_list:
        if 'Targaryen' in person['name']:
            targaryen_list.append(person['name'])
    return targaryen_list

print(Targaryens(characters))

# Create a histogram of the houses (it's the "allegiances" key)

# make a list of all house allegiances
def allegiances(char_list, house_list):
    alleg_list = []
    for person in char_list:
        if person["allegiances"] != []:
            alleg_list.append(person['allegiances'])

# makes a dictionary, counting the frequency of each house
    frequency = {}
    for a_house in alleg_list:
        for house in a_house:
            if (house in frequency):
                frequency[house] += 1
            else:
                frequency[house] = 1

# creates new dictionary replacing he URL key with the value from the api dictionary
    new_freq = {}
    for old_key in frequency:
        for key in houses:
            if old_key == key:
                new_freq[houses[key]] = frequency[old_key]
    return new_freq

print(allegiances(characters, houses))

