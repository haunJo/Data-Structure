from listNode import *

class LinkedListbasic:
    def __init__(self):
        self.__head = ListNode("dummy", None)
        self.__numItems = 0
    
    def __getNode(self, i):
        if i < 0 or i >= self.__numItems:
            return -1
        curr = self.__head
        for k in range(i+1):
            curr = curr.next
        return curr
    
    def append(self,x):
        newItem = ListNode(x, self.__head)
        prev = self.__getNode(self.__numItems-1)
        prev.next = newItem
        self.__numItems += 1
    
    def insert(self, i, x):
        if i < 0  or i > self.__numItems:
            return -1
        prev = self.__getNode(i-1)
        newItem = ListNode(x, prev.next)
        prev.next = newItem
        self.__numItems += 1
        
    def pop(self, i):
        if i < 0  or i > self.__numItems:
            return None
        prev = self.__getNode(i-1).item
        curr = prev.next
        prev.next = curr.next
        self.__numItems -= 1
        return curr.item

    def remove(self, x):
        (prev, curr) = self.__findNode(x)
        if curr:
            prev.next = curr.next
            self.__numItems -= 1
    
    def __findNode(self, x):
        curr = self.__head.next
        prev = self.__head
        while curr != None:
            if curr.itme == x:
                return (prev, curr)
            else:
                prev = curr
                curr = curr.next
        return (None, None)
    
    def get(self, i):
        if i < 0 or i > self.__numItems-1:
            return None
        curr = self.__getNode(i)
        return curr.item
    
    def index(self, x):
        cnt = 0
        curr = self.__head.next
        for i in range(self.__numItems):
            if curr.item == x:
                return cnt
            else:
                cnt += 1
                curr = curr.next
        return -12345
    
    def isEmpty(self):
        return self.__numItems == 0
    
    def size(self):
        return self.__numItems
    
    def clear(self):
        self.__head = ListNode("dummy", None)
        self.__numItems = 0
        
    def count(self,x):
        cnt = 0
        prev = self.__head
        curr = prev.next
        while curr != None:
            if curr.item == x:
                cnt += 1
            curr = curr.next
        return cnt
    
    def extend(self, a):
        for i in range(a.size()):
            self.append(a.get(i))
    
    def copy(self):
        a = ListNode("dummy", None)
        for i in range(self.__numItems):
            a.append(self.get(i))
        return a
    
    def reverse(self):
        a = LinkedListbasic()
        for i in range(self.__numItems()):
            a.append(self.get(i))
        self.clear()
        while a.__numItems != 0:
            self.append(a.pop())

    def sort(self):
        a = []
        for i in range(self.__numItems):
            a.append(self.get(i))
        a.sort()
        self.clear()
        for i in range(len(a)):
            self.append(a[i])
            
    