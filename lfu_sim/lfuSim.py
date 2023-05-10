import math

class Heap:
    def __init__(self,list):
        if list == None: 
            self._A = []
        else:
            self._A = list
            self.buildHeap()
    def insert(self,x):
        self._A.append(x) #마지막 노드에 x 추가
        self.percolateUP(len(self._A)-1) #마지막 노드 인덱스에 접근해서 제자리로 스며오르기
    def deleteMin(self):
        minimum = self._A[0] #max값에 1번째 노드 값 저장
        self._A[0] = self._A.pop() #마지막 값을 pop해서 1번째 노드에 저장
        self.percolateDown(0) #1번째 노드부터 시작해서 제자리로 스며내리기
        return minimum
    def min(self):
        return self._A[0] #1번째 노드의 값을 반환함
    def buildHeap(self):
        for i in range((len(self._A)-2)//2, -1, -1): #마지막 노드의 부모 노드에서부터 0번째 노드까지 스며내리기를 진행하기
            self.percolateDown(i) #재귀적 호출
    def size(self):
        return len(self._A) #길이를 반환
    def isEmpty(self):
        return len(self._A) == 0
    def clear(self):
        self._A = list
    def percolateUP(self, i:int):
        parent = (i-1)//2 #i번째 노드의 부모 노드 인덱스
        if i > 0 and self._A[i] < self._A[parent]:
            self._A[i], self._A[parent] = self._A[parent], self._A[i]
            self.percolateUP(parent)
    def percolateDown(self, i:int):
        child = 2*i + 1 #i번째 노드의 왼쪽 자식
        right_child = 2*i + 2 #i번째 노드의 오른쪽 자식
        if child < len(self._A)-1: #왼쪽 자식이 존재할 경우
            if right_child <= len(self._A)-1 and self._A[child] > self._A[right_child]: #왼쪽 자식이 오른쪽 자식보다 작을 경우
                child = right_child
            if self._A[child] < self._A[i]: #자식이 부모인 i번째 노드보타 클 경우
                self._A[child], self._A[i] = self._A[i], self._A[child] #서로 교체
                self.percolateDown(child) # 스며내리기 재반복
    def print_heap(self):
        print(self._A) #배열 보여줌
        print(self._A[0]) #배열의 0번째 노드 출력
        for i in range(1, len(self._A)): #1번째 노트부터 마지막 노드까지
            if math.log2(i+2) == int(math.log2(i+2)): #각 depth+2 가 2의 거듭제곱일 경우
                print(self._A[i], end = ' ') #출력하고
                print() #개행문자 삽입하기
            else:
                print(self._A[i], end = ' ')
        print()
class LfuHeap(Heap):
    
    def __init__(self, list, cache_slots):
        if list == None: 
            self._A = []
        else:
            self._A = []
            self.buildHeap()
        self.length = cache_slots
        
    def isFull(self):
        return self.size() == self.length
    
    def increase(self, index):
        self._A[index][1] += 1
        
    
    def insert(self, lpn, frequency):
        self._A.append([lpn, frequency]) #마지막 노드에 x 추가
        self.percolateUP(len(self._A)-1)
        
    def deleteMin(self):
        minimum = self._A[0] #max값에 1번째 노드 값 저장
        self._A[0] = self._A[-1]
        self._A.pop()#마지막 값을 pop해서 1번째 노드에 저장
        self.percolateDown(0) #1번째 노드부터 시작해서 제자리로 스며내리기
        return minimum
    
    def percolateUP(self, i:int):
        parent = (i-1)//2 #i번째 노드의 부모 노드 인덱스
        if i > 0 and self._A[i][1] < self._A[parent][1]:
            self._A[i], self._A[parent] = self._A[parent], self._A[i]
            self.percolateUP(parent)
    def percolateDown(self, i:int):
        child = 2*i + 1 #i번째 노드의 왼쪽 자식
        right_child = 2*i + 2 #i번째 노드의 오른쪽 자식
        if child <= len(self._A)-1: #왼쪽 자식이 존재할 경우
            if right_child <= len(self._A)-1 and self._A[child][1] > self._A[right_child][1]: #왼쪽 자식이 오른쪽 자식보다 작을 경우
                child = right_child
            if self._A[child][1] < self._A[i][1]: #자식이 부모인 i번째 노드보타 작을 경우
                self._A[child], self._A[i] = self._A[i], self._A[child] #서로 교체
                self.percolateDown(child) # 스며내리기 재반복
    def search(self, x):
        if not self.isEmpty():
            #print(list(zip(*self._A))[0])
            for i, v in enumerate(list(zip(*self._A))[0]):
                if x == v:
                    return i
        return False
                
        
        
        
def lfu_sim(cache_slots):
    cache_hit = 0
    tot_cnt = 0

    data_file = open("linkbench.trc")

    cache_table = dict()
    cache_heap = LfuHeap([],cache_slots)

    # for line in data_file.readlines():
    #     lpn = line.split()[0]
    #     if lpn not in cache_table.keys():
    #         cache_table[lpn] = 1
    #     if not cache_heap.search(lpn):
    #         if cache_heap.isFull():
    #             evicted = cache_heap.deleteMin()
    #             cache_table[evicted[0]] = evicted[1]
    #         cache_heap.insert(lpn, cache_table[lpn])
    #     else:
    #         index = cache_heap.search(lpn)
    #         cache_heap[index][1] += 1
    #         cache_heap.percolateUP(index)
    #         cache_hit += 1
    #     tot_cnt += 1
    
    #디버깅
    for line in data_file.readlines():
        lpn = line.split()[0]
        if lpn not in cache_table.keys():
            cache_table[lpn] = 1
        if not cache_heap.search(lpn):
            if cache_heap.isFull():
                evicted = cache_heap.deleteMin()
                cache_table[evicted[0]] = evicted[1]
            cache_heap.insert(lpn, cache_table[lpn])
        else:
            index = cache_heap.search(lpn)
            cache_heap.increase(index)
            cache_heap.percolateUP(index)
            cache_hit += 1
        tot_cnt += 1
        # cache_heap.print_heap()
    
    
    
    
    # Program here 

    print("cache_slot = ", cache_slots, "cache_hit = ", cache_hit, "hit ratio = ", cache_hit / tot_cnt, tot_cnt)

if __name__ == "__main__":
    test = LfuHeap([],10)
   
    for cache_slots in range(100, 1000, 100):
        lfu_sim(cache_slots)



