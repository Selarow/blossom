import os, sys
from itertools import combinations



class ExpandFeatures():
    NUM_CNF = 5

    def __init__(self, cnfs, file, file_ex):
        cnfs = [cnf for cnf in map(int, str(cnfs))]

        if len(cnfs) != self.NUM_CNF:
            raise Exception("Invalid cnfs") 
        
        self.cnfs = dict()
        self.cnfs["x_or_y"] = cnfs[0]
        self.cnfs["notx_or_y"] = cnfs[1]
        self.cnfs["x_or_noty"] = cnfs[2]
        self.cnfs["notx_or_noty"] = cnfs[3]
        self.cnfs["x_xor_y"] = cnfs[4]
        self.expand_features(file, file_ex)


    def rawcount(self, file):
        f = open(file, "rb")
        lines = 0
        buf_size = 1024 * 1024
        read_f = f.raw.read
        buf = read_f(buf_size)

        while buf:
            lines += buf.count(b"\n")
            buf = read_f(buf_size)

        return lines


    def expand_features(self, file, file_ex):
        fex = open(file_ex, "a")
        num_lines = self.rawcount(file)

        with open(file, "r") as f:
            for cnt, line in enumerate(f):
                line = [int(i) for i in line.split(" ")]

                if cnt == 0:
                    line_size = len(line)
                    features = [i for i in range(line_size)][1:]

                for f1, f2 in combinations(features, 2):
                    if self.cnfs["x_or_y"]:
                        x_or_y = line[f1] or line[f2]
                        line.append(int(x_or_y))
                    
                    if self.cnfs["notx_or_y"]:
                        notx_or_y = not line[f1] or line[f2]
                        line.append(int(notx_or_y))
                    
                    if self.cnfs["x_or_noty"]:
                        x_or_noty = line[f1] or not line[f2]
                        line.append(int(x_or_noty))
                    
                    if self.cnfs["notx_or_noty"]:
                        notx_or_noty = not line[f1] or not line[f2]
                        line.append(int(notx_or_noty))
                    
                    if self.cnfs["x_xor_y"]:
                        x_xor_y = line[f1] ^ line[f2]
                        line.append(int(x_xor_y))

                fex.write(" ".join(map(str, line))+"\n")
                file_size = "{:.2f}".format(os.stat(file_ex).st_size/1024 ** 2)
                print(f"\rProgress: {int(((cnt+1)/num_lines)%100 * 100)}% | File size: {file_size} MiB", end="", flush=True)

        fex.close()



if __name__ == "__main__":
    cnfs = sys.argv[1]
    file = sys.argv[2]
    file_ex = sys.argv[3]
    ExpandFeatures(cnfs, file, file_ex)
    