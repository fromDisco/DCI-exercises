def repl(num_str):
    binary = num_str
    for i in range(9 + 1):
        if i < 5:
            binary = binary.replace(str(i), "0")
        else:
            binary = binary.replace(str(i), "1")
        
    return binary


print(repl("2839838934701432"))