# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        while len(lists) > 1:
            tempList = []
            
            for i in range(0,len(lists),2):
                l1 = lists[i]
                if i + 1 < len(lists):
                    l2 = lists[i+1]
                else:
                    l2= None
                tempList.append(self.merge(l1,l2))
            lists = tempList
        
        return lists[0]
    
    
    def merge(self,list1,list2):
        newNode = ListNode()
        tail  = newNode
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        
        return newNode.next
            