class BidirectNode:
    def __init__(self, newitem, prevNode = "bidirect", nextNode = "bidirect"):
        self.item = newitem
        self.prev = prevNode
        self.next = nextNode