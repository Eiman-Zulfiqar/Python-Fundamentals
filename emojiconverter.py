def  emoji_converter(message):
     words = message.split( " ")
     emojis = {
        ":)" : "😀",
        ":(" : "😞",
        "lol" : "😂",
        "sick":"😨",
        "happy": "😀",
        "mermaid": "🧜‍"
     }
     outcome = " "
     for word in words:
         outcome += emojis.get(word, word) + " "
     return output


Msg = input  (“>”)
print(emoji_converter(msg))
