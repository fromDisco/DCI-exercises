import re
import os

document = """Hey Mr. Bezos,

I hope its okay I message you in this unsecure email program. Sry about that!
Here the list of extremely confidential clients and close coworkers of you who actually visited Epsteins island. Oh boy how I hope no random Python Students extract this sensitive list with some kind of regular expressions! 

therealjeffbezos@bossnet.com
markzuckerbergtheman@facebookormetaidkmail.com
donaldtothatrump@getthatcapitolmail.com
2pacaintdeadandnowchillinonwrongislands@mail.com

Kind regards,
Tanisha"""


def search_file():
    txt_files = []

    dir_path = os.path.dirname(os.path.realpath(__file__))
    folder_content = os.listdir(dir_path)
    txt_pattern = r"[a-zA-Z0-9]+.txt"

    for file in folder_content:
        try:
            txt_files.append(re.match(txt_pattern, file).group())
        except:
            continue

    return txt_files
    

def read_adress(document):
    pattern = r"[A-Za-z0-9.-]+@[A-Za-z]{3,}\.[a-z]{2,}"
    collection = re.findall(pattern, document)
    return collection


def parse_result(adresses):
    for adress in adresses: 
        print(adress)


def main():
    files = search_file()
    for file in files:
        with open(file) as text:
            file_content = text.read()
            adresses = read_adress(file_content)
            parse_result(adresses)

    adresses = read_adress(document)
    print("Here we go:")
    parse_result(adresses)


main()


