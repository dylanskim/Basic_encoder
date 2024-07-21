import random
user_in = input("Press enter to decode or type raw text here: ")
if not user_in == "":
    multi = random.randint(2, 9)
    join_delimiter = str(random.randint(1000, 9999))

    text_ascii = map(str, list(map(ord, user_in)))
    spaced_text_ascii = int(join_delimiter.join(text_ascii))
    output_encoded = str(multi * spaced_text_ascii)
    print(hex(int(output_encoded + join_delimiter + str(multi))))

else:
    user_hex = input("Type encoded text here: ")
    user_code = str(int(user_hex,0))
    code_decode = str(int(user_code[0:-5]) // int(user_code[-1]))
    code_delimiter = user_code[-5:-1]
    code_translate = [int(i) for i in code_decode.split(code_delimiter)]
    translate_output = [chr(i) for i in code_translate]
    print("".join(translate_output))
