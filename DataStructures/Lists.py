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