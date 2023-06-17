import heapq
import sys
inf = sys.maxsize

class FindShortestPath:
    def __init__(self):
        print("Bellmanford")
        self.input = []
        self.path = dict()
        self.vertexs = 0
        self.costs = []
        
        
    def load_data(self, filename):
        print("load_data ...", filename)
        with open(filename, 'r') as f:
            for item in f.readlines():
                li = item.strip().split(",")
                self.input.append([int(i) for i in li])


    def initialize(self):
        print("initialize ...")
        self.vertexs = max(next(zip(*self.input))) + 1
        print("정점의 개수 : ", self.vertexs)
    
    def find_path(self, r):
        print("find_path ...")
        for i in range(self.vertexs):
            self.path[i] = []
        self.path[r].append(r)
        cost = [inf]*self.vertexs
        cost[r] = 0
        
        for _ in range(self.vertexs-1):
            for prev, curr, costs in self.input:
                if cost[prev] != inf and costs + cost[prev] < cost[curr]:
                    cost[curr] = costs + cost[prev]
                    self.path[curr] = [i for i in self.path[prev]]
                    self.path[curr].append(curr)


        for prev, curr, costs in self.input:
            if cost[prev] != inf and costs + cost[prev] < cost[curr]:
                print("negative cycle detected")
                return
        
        self.costs = cost
        
    def print_path(self, r):
        print("print_path ...")
        for i in range(self.vertexs):
            print(f"[{i}] : {self.path[i]} : {self.costs[i]}")
            
if __name__ == '__main__':
    test = FindShortestPath()
    test.load_data('graph_pos.txt')
    test.initialize()
    test.find_path(0)
    test.print_path(0)