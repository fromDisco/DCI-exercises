names = ['peter doe', 'peer doe', 'mary doe', 'tom doe', 'john doe']

cap = [n.title() for n in names if not "p" in n]

print(cap)