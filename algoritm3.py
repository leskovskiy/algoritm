class Node:
    def __init__(self, data):
        self.data  = data
        self.next = None


    def __str__(self):
        return f"[{self.data}]->{self.next}"
    
class LinkedList:
    def _init_(self):
        self.head = None

    def _str_(self):
        return str(self.head)
    

class Solution:
    def reverse(self,head:LinkedList) -> LinkedList:
        if not head:
            return head


        temp = head
        tail = LinkedList(val=head.val)
        while temp.next:
            temp = temp.next
            tail = LinkedList(val=temp.val, next=tail)
            return tail
