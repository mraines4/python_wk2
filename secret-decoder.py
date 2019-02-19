
letters = 'abcdefghijklmnopqrstuvwxyz'

secret = [1, 0, 3] # "bad"

def translate(index, master):
    return master[index]

def map_over(collection, master, how):
    result = ''
    for item in collection:
        result += how(item, master)

    return result

# give your funciton "verb" names
def decode(number_list, master_list):
    return map_over(number_list, master_list, translate)
    # configuration came in as arguments
    # result = ''
    # count = 0

    # do the translation
    # for each item in number_list
    # for item in number_list:
        # find that index in master_list
        # letter = master_list[item]

        # put that character in result
        # result is result + letter
        # result += letter

        # result += master_list[item]
        # result += translate(item, master_list)

    # return the result
    # return result

decoded_message = decode(secret, letters)
print(decoded_message)
# print(decode(secret, letters))

def decode_while(number_list, master_list):
    result = ''
    count = 0
    max_length = len(number_list)
    while count < max_length:
        result += master_list[number_list[count]]
        count += 1
    return result

print(decode_while(secret, letters))




print(map_over(secret, letters, translate))