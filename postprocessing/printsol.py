import sys
from copy import deepcopy
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
    P_ATOM = 1/2
    P_AND = 1/4
    P_OR = 3/4
    P_XOR = 1/2

    # Dataset should never be an expanded dataset
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
            features = [i-1 for i in range(len(features))][1:]
        
        return features


    def get_combinations(self, features):
        for f1, f2 in combinations(features, 2):
            self.LABELS.append(f"x{f1} or x{f2}")
            self.LABELS.append(f"not x{f1} or x{f2}")
            self.LABELS.append(f"x{f1} or not x{f2}")
            self.LABELS.append(f"not x{f1} or not x{f2}")
            self.LABELS.append(f"x{f1} xor x{f2}")


    def draw_tree(self, sol, target):
        nodes = dict()
        last_depth = 0

        with open(sol) as f:
            for cnt, line in enumerate(f):
                if cnt != 0:
                    l = line.split(":")
                    depth = self.DEPTH[l[0].count(" ")]

                    if "yes" in l[0]:
                        tag = "yes"
                    
                    else:
                        tag = "no"

                    try:
                        feature = str(self.LABELS[int(l[-1])])
                    
                    except:
                        feature = str(l[-1])
                    
                    if depth == 0:
                        self.root = Node(feature, tag="root")
                        nodes[depth] = self.root
                    
                    elif depth > last_depth:
                        nodes[depth] = Node(feature, parent=nodes[last_depth], tag=tag)
                        last_depth = depth
                    
                    elif depth < last_depth:
                        nodes[depth] = Node(feature, parent=nodes[depth-1], tag=tag)
                        last_depth = depth
                    
                    else:
                        nodes[depth] = Node(feature, parent=nodes[depth-1], tag=tag)
        
        UniqueDotExporter(self.root).to_picture(target)


    def traverse(self, current_node, path, paths):
        path.append([current_node.tag, current_node.name])

        if not current_node.children:
            paths.append(self.rotate(list(path)))
        
        else:
            for child in current_node.children:
                self.traverse(child, path, paths)
        
        path.pop()


    def rotate(self, path):
        first_elements = [sublist[0] for sublist in path]
        first_elements = first_elements[1:] + first_elements[:1]
        updated_path = deepcopy(path)

        for i in range(len(updated_path)):
            updated_path[i][0] = first_elements[i]
        
        return updated_path


    def get_all_paths(self, node):
        paths = []
        self.traverse(node, [], paths)

        return paths


    def avg_len_axp(self):
        all_paths = self.get_all_paths(self.root)
        avg_len_axp = 0

        for path in all_paths:
            len_axp = 0
            P_axp = 1

            for type,cond in path[:-1]:
                if "xor" in cond:
                    len_axp += 2
                    P_axp = P_axp * self.P_XOR
                
                elif ("or" in cond and type == "yes") or ("and" in cond and type == "no"):
                    len_axp += 1
                    P_axp = P_axp * self.P_OR
                
                elif ("and" in cond and type == "yes") or ("or" in cond and type == "no"):
                    len_axp += 2
                    P_axp = P_axp * self.P_AND

                else:
                    len_axp += 1
                    P_axp = P_axp * self.P_ATOM
            
            avg_len_axp += len_axp * P_axp

        return avg_len_axp



if __name__ == "__main__":
    sol = sys.argv[1]
    dataset = sys.argv[2]
    target = sys.argv[3]
    Sol = PrintSol(sol, dataset, target)
    avg = Sol.avg_len_axp()
    print("AVERAGE AXP LENGTH =", avg)
