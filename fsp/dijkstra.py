import heapq
import sys
inf = sys.maxsize
class FindShortestPath:
    def __init__(self):
        print("Dijkstra")
        self.graph = dict()
        self.input = []
        self.path = dict()
        self.vertexs = 0
        self.costs = []

    def load_data(self, filename):
        print("load_data ...", filename)
        with open(filename, 'r') as f:
            for item in f.readlines():
                self.input.append(item.strip().split(","))
        
        
    def initialize(self):
        print("initialize ...")
        for i in self.input:
            if int(i[0]) not in self.graph.keys():
                self.graph[int(i[0])] = []
            self.graph[int(i[0])].append([int(i[2]),int(i[0]), int(i[1])]) 
            #ex) dict[0] = [[10,0,1]] 이는 0번 노드에서 1번 노드가 연결되어 있으며 cost가 10이라는 뜻
        self.vertexs = len(self.graph.keys())
        
    def find_path(self, r):
        print("find_path ...")
        for i in range(self.vertexs):
            self.path[i] = []
        self.path[r].append(r)
        cost = [inf]*self.vertexs
        cost[r] = 0
        heap = []
        for val in self.graph[r]:
            heapq.heappush(heap, [val[0], val[1], val[2]])
        while heap:
            min = heapq.heappop(heap)
            if cost[min[1]] + min[0] < cost[min[2]]:
                cost[min[2]] = cost[min[1]]+ min[0] 
                self.path[min[2]] = [i for i in self.path[min[1]]]
                self.path[min[2]].append(min[2])
                for edge in self.graph[min[2]]:
                    heapq.heappush(heap, [edge[0], edge[1], edge[2]])
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