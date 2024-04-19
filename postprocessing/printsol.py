import sys
from itertools import combinations
from anytree import Node, RenderTree
from anytree.exporter import UniqueDotExporter



class PrintSol():
    LABELS = []
    DEPTH = {
        0: 0,
        1: 1,
        5: 2,
        9: 3,
        13: 4,
        17: 5,
        21: 6,
        25: 7
    }

    # dataset should never be an expanded dataset
    def __init__(self, sol, dataset, target):
        features = self.get_features(dataset)

        for f in features:
            self.LABELS.append(f)
        
        self.get_combinations(features)
        self.draw_tree(sol, target)


    def get_features(self, dataset):
        with open(dataset) as file:
            line = file.readline()
            features = [int(i) for i in line.split(" ")]
            features = [i for i in range(len(features))][1:]
        
        return features


    def get_combinations(self, features):
        for f1, f2 in combinations(features, 2):
            self.LABELS.append(f"{f1} or {f2}")
            self.LABELS.append(f"not {f1} or {f2}")
            self.LABELS.append(f"{f1} or not {f2}")
            self.LABELS.append(f"not {f1} or not {f2}")
            self.LABELS.append(f"{f1} xor {f2}")


    def draw_tree(self, sol, target):
        nodes = dict()
        last_depth = 0

        with open(sol) as f:
            for cnt, line in enumerate(f):
                if cnt != 0:
                    l = line.split(":")
                    depth = self.DEPTH[l[0].count(" ")]

                    try:
                        feature = self.LABELS[int(l[-1])]
                    
                    except:
                        feature = str(l[-1])
                    
                    if depth == 0:
                        root = Node(feature)
                        nodes[depth] = root
                    
                    elif depth > last_depth:
                        nodes[depth] = Node(feature, parent=nodes[last_depth])
                        last_depth = depth
                    
                    elif depth < last_depth:
                        nodes[depth] = Node(feature, parent=nodes[depth-1])
                        last_depth = depth
                    
                    else:
                        nodes[depth] = Node(feature, parent=nodes[depth-1])

        #for pre, fill, node in RenderTree(root):
        #    print("%s%s" % (pre, node.name))
        
        UniqueDotExporter(root).to_picture(target)



if __name__ == "__main__":
    sol = sys.argv[1]
    dataset = sys.argv[2]
    target = sys.argv[3]
    Sol = PrintSol(sol, dataset, target)
