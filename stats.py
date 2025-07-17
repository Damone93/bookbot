def sort_dict(word_dict):
        keyvalue = []
        for key, value in word_dict.items():
            some_new_dict = { "char": key, "num": value }
            keyvalue.append(some_new_dict)

        def get_char_count(char_dict):
            return char_dict["num"]
            
        keyvalue.sort(reverse=True, key=get_char_count)
        return keyvalue