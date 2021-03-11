def EmojiConverter(message):
    words = message.split(' ')
    emojis = { #map to emoji's on windows use windows key + . to bring up emoji's
        ":)" : "\U0001F600", #convert to unicode of the emoji's
        ":(" : "\U0001F622",
        ":|" : "\U0001F937",
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output

message = input(">")
print(EmojiConverter(message))
