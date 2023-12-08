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
        features = features[1:]

        for line in data:
            for f1, f2 in combinations(features, 2):
                x_or_y = line[f1] or line[f2]
                notx_or_y = not line[f1] or line[f2]
                x_or_noty = line[f1] or not line[f2]
                x_xor_y = line[f1] ^ line[f2]
                line.append(int(x_or_y))
                line.append(int(notx_or_y))
                line.append(int(x_or_noty))
                line.append(int(x_xor_y))
        
        return data



if __name__ == "__main__":
    file_name = sys.argv[1]
    new_file_name = sys.argv[2]
    ExpandFeatures(file_name, new_file_name)
    