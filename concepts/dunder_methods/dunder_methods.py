class softwares:
    names = []
    versions = {}


    def __init__(self, names):
        if names:
            self.names = names.copy()
            for name in names:
                self.versions[name] = 1
        else:                 
            print("Wrong")


    def __str__(self):
        output = "List of programs and their version:\n"
        for key, val in self.versions.items():
            output += f"{key}: {val}\n"
        
        return output


    def __setitem__(self, name, version):
        if name in self.versions:
            self.versions[name] = version

    
    def __getitem__(self, name):
        if name in self.versions:
            return self.versions[name]




p = softwares(['S1','S2','S3'])
p["S1"] = 2
print(p.versions)
p1 = softwares([])
print(p["S2"])

