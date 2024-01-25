import argparse
import base64

parser = argparse.ArgumentParser(description ="My first CLI Python pgrogram for homework 11.")
parser.add_argument("-i", "--input", help ="input file", required=True)
#parser.add_argument("-o", "--output", help ="output file", required=True)
parser.add_argument("--optional", help ="Uncreative optional argument", action="store_true")
parser.add_argument("--operation", help="The options for text editing are:\n"
                                        "\"capital\": to print everything in capital letters\n"
                                        "\"replace\": to replace all \"e\"s with 3s\n"
                                        "\"base64\": to decode the text into binary code\n"
                                        "\"caesars_cipher\" to decode the text to Caesar\'s cipher\n"
                                        "\"animal\": to write elephant after every third word")

def action(input_text, optional, operation):
    result = input_text
    if operation == "capital": 
        result = input_text.upper()
    elif operation == "replace":
        result = input_text.replace("e", "3")
    elif operation == "base64":
        result = base64.b64encode(input_text.encode())
    elif operation == "caesars_cipher":
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        caesars_cipher_alphabet= "XYZABCDEFGHIJKLMNOPQRSTUVW"
        alphabets_dictionary = dict(zip(alphabet, caesars_cipher_alphabet))
        result =  "".join(alphabets_dictionary.get(character, character) for character in input_text)
    elif operation == "animal":
        words = input_text.split()
        for i in range(2, len(words), 4):
            words.insert(i, "elephant")
            result = " ".join(words)
    
    if optional:
        print("An uncreative optional action.")

    return result

args = parser.parse_args()

with open(args.input, encoding="utf-8") as poem_file:
    input_text = poem_file.read()

output_text = action(input_text, args.optional, args.operation)

with open("output.txt", "w", encoding="utf-8") as output_file:
    output_file.write(output_text) 