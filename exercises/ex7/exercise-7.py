def upper_lower(string, command):
    if command == "up":
        return string.upper()
    elif command == "lo":
        return string.lower()
    else:
        return "sorry, no valid commad"


print(upper_lower("string", "up"))
print(upper_lower("string", "lo"))
