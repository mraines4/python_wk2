# Dictionaries
# aka Hash, HashMap, HashTables, Map, Object

places = {
    'farm burger': '1234 piedmont, atlanta',
    'naan stop': '1235 piedmont, atlanta'
}

# what is the address of farm burger?
places['farm burger']
# go get me the thing with 'farm burger' on the left hand side of the column

friends = {
    'Europe': {
        'Paris': ['frankie', 'grace'],
        'Berlin': ['bobbie']
    },
    'Asia': ['my cousin', 'my other cousin', 'their friend'],
    'US': {
        'angela': {
            'pets': {
                'oakley': {
                    'toys': [
                        'everything'
                    ]
                },
                'milla': {
                    'hobbies': [
                        'drooling'
                    ]
                }
            }
        }
    }
}

# friends in the us
friends['US']
# friends in berlin inside europe
friends['Europe']['Berlin']
# will give you back frankie
friends['Europe']['Paris'][0]
#how do you access oakleys toys?
toys = friends['US']['angela']['pets']['oakley']['toys']
# print toys
for item in toys:
    print("%s is one of oakley's fav toys" % item)