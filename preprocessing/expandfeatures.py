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
        data = dict()
        f = open(file, "r")
        cnt = 0

        for line in f.readlines():
            data[cnt] = [int(x) for x in line.split(" ")]
            cnt+=1
        
        f.close()

        return data


    def write_file(self, new_file, data):
        print("\n")
        f = open(new_file, "a")

        for i, line in data.items():
            f.write(" ".join(map(str, line))+"\n")
            print(f"\rWriting...: {int(((i+1)/len(data))%100 * 100)}%", end=" ", flush=True)
        
        f.close()
        print("Done")
        file_size = "{:.2f}".format(os.stat(new_file).st_size/1024 ** 2)
        print(f"New file: {new_file} of size {file_size} MB")


    def expand_features(self, data):
        n, p = len(data), len(data[0])
        process = psutil.Process()
        features = [i for i in range(p)][1:]
        print("Progress = 0%", end="")

        for i, line in data.items():
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
            
            mem = int(process.memory_info().rss/1024 ** 2)
            print(f"\rProgress: {int(((i+1)/n)%100 * 100)}% | Mem usage: {mem} MB", end="", flush=True)
        
        return data



if __name__ == "__main__":
    cnfs = sys.argv[1]
    file_name = sys.argv[2]
    new_file_name = sys.argv[3]
    ExpandFeatures(cnfs, file_name, new_file_name)
    