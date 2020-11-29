class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
def createLinkedList(arr: list, head: ListNode): #Array to LinkedList
    for val in arr:
        newNode = ListNode(val)
        head.next = newNode
        head = head.next
        '''
        DO NOT DO
            newNode = ListNode(val)
            head = newNode
            head = head.next

        When you reference head, you lose the reference of your previous node
        '''
def reverseListRecursive(self, head: ListNode) -> ListNode:
    if head is None or head.next is None: 
        return head
    
    p = self.reverseList(head.next) #Head node of reversed list
    head.next.next = head # After the first recurisve call ends, head is the 
    head.next = None      # second last node due to the base case above
    return p

def reverseListIteratively(self, head: ListNode) -> ListNode:
    prev = None
    while head:
        next = head.next
        head.next = prev
        prev = head
        head = next
                
    return prev

def printLinkedList(head: ListNode):
    ret = []
    while head != None:
        ret.append(head.val)
        head = head.next
    
    print(ret)

def main():
    arr = [1,2,3,4,5,6,7]
    dummyHead = ListNode()
    createLinkedList(arr, dummyHead)

    printLinkedList(dummyHead)

if __name__ == "__main__":
    main()