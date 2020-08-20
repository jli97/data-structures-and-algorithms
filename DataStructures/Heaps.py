''' Heaps using heapq '''
# Insert = O(logn) //worst case
# Pop = O(1)


import heapq


def main():
    li = [1,9,8,2,6,5,7,3]
    min_heap = []
    max_heap = []
    asc_order = []
    des_order = []

    heapq.heapify(min_heap)
    heapq.heapify(max_heap)

    for num in li:
        heapq.heappush(min_heap, num)
        heapq.heappush(max_heap, -num) #Max heap is done by making values negative
    
    for _ in range(len(li)):
        min_pop = heapq.heappop(min_heap)
        asc_order.append(min_pop)

        max_pop = heapq.heappop(max_heap)
        des_order.append(-max_pop) #Remember to reverse the value or store a key with the value as a tuple
    
    print(asc_order)
    print(des_order)
    

if __name__ == "__main__":
    main()