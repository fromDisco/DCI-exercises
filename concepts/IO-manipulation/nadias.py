import os



def sed(pattern, replacement,file, file2):
    #if os.path.isfile(file):
        f = open(file,'r')

        file_content = f.readlines()

        f2 = open(file2, 'a')
        f2.write(str(file_content))
        print(f2)
        for i in f:
            if pattern in i:
                f2.replace(pattern, replacement)
                return f2
sed('ok','am','n.txt','s.txt')