import sys
print("\nsys.base_exec_prefix:")
print(sys.base_exec_prefix)

print("\nsys.base_prefix:")
print(sys.base_prefix)

print("\nByteorder")
print(sys.byteorder)

print("\nLength of incoming argument-list (sys.argv):")
print(len(sys.argv))

print("\nDatatype of sys.argv")
print(type(sys.argv))

print("\nPrint all Arguments that were passed from the command line:")
print(sys.argv)

print("\nName of the file:")
print(sys.argv[0])

# add some args
argv_len = len(sys.argv)
for i in range(argv_len, argv_len + 8):
    sys.argv.append(i)

print("\n___________")
print("After adding:")
print(sys.argv)
