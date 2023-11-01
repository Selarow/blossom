import sys
from itertools import combinations



class ExpandFeatures():
    def __init__(self, file, new_file):
        self.file = file
        self.new_file = new_file
        data = self.parse_file(self.file)
        data = self.expand_features(data)
        self.write_file(self.new_file, data)


    def parse_file(self, file):
        data = []
        f = open(file, "r")

        for line in f.readlines():
            data.append([int(x) for x in line.split(" ")])
        
        f.close()

        return data


    def write_file(self, new_file, data):
        f = open(new_file, "a")

        for line in data:
            f.write(" ".join(map(str, line))+"\n")
        
        f.close()


    def expand_features(self, data):
        features = [i for i in range(len(data[0]))]

        for line in data:
            for f1, f2 in combinations(features, 2):
                cnf = line[f1] or line[f2]
                line.append(cnf)
        
        return data



if __name__ == "__main__":
    file_name = sys.argv[1]
    new_file_name = sys.argv[2]
    ExpandFeatures(file_name, new_file_name)
    