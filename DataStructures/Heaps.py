''' Implementing a MinHeap '''

# Using an array
# Arr[(i-1)/2] returns parent node
# Arr[(2*i) + 1] returns left child node
# Arr[(2*i) + 2] return righ child node

class MinHeap:

    def __init__(self):
        self.heap = [None]
        self.size = 0

    def push(self, element):
        self.size = self.size + 1
        self.heap.append(element) # Places it at the end of the array
        i = self.size
        print("Item has been appended:  " + str(self.heap))
        # Upheap
        while i > 1 and self.heap[i] < self.heap[i//2]:
            temp = self.heap[i]
            self.heap[i] = self.heap[i // 2]
            self.heap[i // 2] = temp 
            i = i // 2
            print(self.heap)

        
    
    def pop(self):
        if self.size == 0:
            return None
        
        ret = self.heap[1]
        
        return


def main():
    li = [9,8,7,3,6,5,1,3,2,1,0]

    h = MinHeap()

    for item in li:
        h.push(item)
    
    print(h.heap)

if __name__ == "__main__":
    main()