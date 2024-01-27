import os, sys, psutil
from itertools import combinations



class ExpandFeatures():
    NUM_CNF = 5

    def __init__(self, cnfs, file, new_file):
        self.cnfs = [cnf for cnf in map(int, str(cnfs))]
        if len(self.cnfs) != self.NUM_CNF:
            raise Exception("Invalid cnfs") 
        
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
        print("\nWriting...")
        f = open(new_file, "a")

        for line in data:
            f.write(" ".join(map(str, line))+"\n")
        
        f.close()
        print("Done")
        file_size = "{:.2f}".format(os.stat(new_file).st_size/1024 ** 2)
        print(f"New file: {new_file} of size {file_size} MB")


    def expand_features(self, data):
        n, p = len(data), len(data[0])
        process = psutil.Process()
        features = [i for i in range(p)][1:]
        print("Progress = 0%", end="")
        cpt = 0

        for line in data:
            for f1, f2 in combinations(features, 2):
                if self.cnfs[0] == 1:
                    x_or_y = line[f1] or line[f2]
                    line.append(int(x_or_y))
                
                if self.cnfs[1] == 1:
                    notx_or_y = not line[f1] or line[f2]
                    line.append(int(notx_or_y))
                
                if self.cnfs[2] == 1:
                    x_or_noty = line[f1] or not line[f2]
                    line.append(int(x_or_noty))
                
                if self.cnfs[3] == 1:
                    notx_or_noty = not line[f1] or not line[f2]
                    line.append(int(notx_or_noty))
                
                if self.cnfs[4] == 1:
                    x_xor_y = line[f1] ^ line[f2]
                    line.append(int(x_xor_y))
            
            cpt+=1
            mem = int(process.memory_info().rss/1024 ** 2)
            print(f"\rProgress = {int((cpt/n)%100 * 100)}% | Using: {mem} MB", end="", flush=True)
        
        return data



if __name__ == "__main__":
    cnfs = sys.argv[1]
    file_name = sys.argv[2]
    new_file_name = sys.argv[3]
    ExpandFeatures(cnfs, file_name, new_file_name)
    