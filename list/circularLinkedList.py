from list.listNode import ListNode


class CircularLinkedList:
    def __init__(self):
        self.__tail = ListNode("dummy", None)
        self.__tail.next = self.__tail
        self.__numItems = 0
    
    def __getNode(self, i):
        curr = self.__tail.next
        for k in range(i+1):
            curr = curr.next
        return curr
    
    def append(self,x):
        newItem = ListNode(x, self.__tail.next)
        self.__tail.next = newItem
        self.__tail = newItem
        self.__numItems += 1
    
    def insert(self, i, x):
        if i < 0  or i > self.__numItems:
            return -1
        if i == self.__numItems-1:
            self.append(x)
        else:
            prev = self.__getNode(i-1)
            newNode = ListNode(x, prev.next)
            prev.next = newNode
        self.__numItems += 1
        
    def numItems(self, cnt):
        if cnt != 0 and self.__tail.next.item == "dummy":
            return cnt-1
        else:
            self.__tail = self.__tail.next
            cnt += 1
            return self.numItems(cnt)
        
        
    def pop(self, *args):
        if self.isEmpty():
            return None
        if len(args) != 0:
            i = args[0]
        if len(args) == 0 or args[0] == -1:
            i = self.__numItems-1
        if( i >= 0 and i <= self.__numItems-1):
            prev = self.__getNode(i-1)
            curr = prev.next.item
            prev.next = prev.next.next
            if i == self.__numItems -1:
                self.__tail = prev
            self.__numItems -= 1
            return curr
        else:
            return None

    def remove(self, x):
        (prev,curr) = self.__findNode(x)
        if curr != None:
            prev.next = curr.next
            if curr == self.__tail:
                self.tail = prev
            self.__numItems -= 1
        else:
            return None
            
    
    def __findNode(self, x):
        prev = self.__tail.next
        curr = prev.next
        while curr != None:
            if curr.item == x:
                return (prev, curr)
            else:
                prev = curr
                curr = curr.next
        return (None, None)
    
    def get(self, *args):
        if len(args) != 0:
            i = args[0]
        if len(args) == 0 or i == -1:
            i = self.__numItems -1
        if (i >= 0 and i <= self.__numItems -1):
            curr = self.__getNode(i)
        return curr.item

    def index(self, x):
        cnt = 0
        curr = self.__tail.next.next
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
        self.__tail = ListNode("dummy", None)
        self.__tail.next = self.__tail
        self.__numItems = 0
        
    def count(self,x):
        cnt = 0
        for i in self:
            cnt += 1
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
        a = CircularLinkedList()
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
       
         
    def __iter__(self):
        return CircularLinkedListIterator(self)
    
    
class CircularLinkedListIterator:
    
    def __init__(self, alist):
        self.__head = alist.getNode(-1)
        self.iterPosition = self.__head.next
    def __next__(self):
        if self.iterPosition == self.__head:
            raise StopIteration
        else:
            item = self.iterPosition.item
            self.iterPosition = self.iterPosition.next
            return item


            