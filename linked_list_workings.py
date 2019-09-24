class LinkedList:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def append(self, item):
        head_ptr = LinkedList(0)
        cur_ptr = head_ptr
        for nums in item:
            cur_ptr.next = LinkedList(nums)
            cur_ptr = cur_ptr.next
        cur_ptr = head_ptr.next
        self.len_list(cur_ptr)
"""
    def display(self, node):
        while node and node.next:
            print(str(node.val) + "->", end='')
            node = node.next
        if node:
            print(node.val)
        else:
            print("Empty LinkedList")
"""
    def len_list(self, l_list):
        head_ptr = LinkedList(0)
        temp_ptr = head_ptr
        temp_ptr.next = l_list
        #print(vars(temp_ptr.next))
        cntr = 1
        
        while temp_ptr.next != None:
            cntr = cntr + 1
            temp_ptr = temp_ptr.next
        print(cntr)

n = int(input())
ls = list(map(int,input().strip().split()))
SolutionObj = Solution()
SolutionObj.append(ls)

