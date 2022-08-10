# please fill the two lists with the data from the "emails" list. Use string slicing and methods for extracting what you need
#example:
#  test@mail.com
# usernames = ["test"]
# email_provider = ["mail.com"]

emails = [
        "123whatever@gmail.com",
        "456idontcare@gmail.com",
        "789istilldontmind@hotmail.de",
        "forrealbruvwhatever@gmx.de"
        ]

usernames = []
email_provider = []
array_index = 3

theAt = emails[array_index].index("@")
username = emails[array_index][:theAt]
usernames.append(username)

provider = emails[array_index][theAt + 1:]
email_provider.append(provider)

print(usernames)
print(email_provider)
        
