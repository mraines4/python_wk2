letters = 'abcdefghijklmnopqrstuvwxyz '

def translate(a_letter, master):
    return master.index(a_letter)


def map_over(collection, master, do_translation):
    result = []
    for letter in collection:
        result.append(do_translation(letter, master))

    return result


#################

message = input('please enter a secret: ')

def encode(entered_message, master_list):
    return map_over(entered_message, master_list, translate)


print(encode(message, letters))
