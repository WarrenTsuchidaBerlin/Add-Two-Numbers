#https://leetcode.com/problems/add-two-numbers/description/
#This defines a class Solution with a method addTwoNumbers, which takes two linked lists l1 and l2 as input and returns a linked list.
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #Creates a dummy head node that will make it easier to handle the head node of ListNode (our output list).
        dummyHead = ListNode(0)
        #Creates a tail pointer, down a few lines it gets updated to always point at the last node in the results list. 
        #Of course, it initially points to the head node as it is the only node at the beginning (i.e. both first and last).
        tail = dummyHead
        #We need this variable to keep track of any carry-over that results from summing digits.
        carry = 0

        #while loop that continues as long as we have more nodes to processn in either l1 or l2 or if there is carry-over.
        while l1 is not None or l2 is not None or carry != 0:
            #The next two lines of code are what extract the current digit from l1 or l2.
            #0 is utilized once end of list has been reached.
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            #calculating the sum of the two digits extracted above + carry-over is calculated.
            sum = digit1 + digit2 + carry
            #extracting last digit of sum by taking the modulo 10 of sum.
            digit = sum % 10
            #Carry-over for the next sum is calculate by performing interger division of the sum by 10.
            carry = sum // 10

            #Here we build our output/answer. 
            #A new node is created with the value of digit that was assigned on line 23.
            newNode = ListNode(digit)
            #Here we are building our output list. We append newNode to the output list.
            tail.next = newNode
            #Update the tail pointer we made earlier to the new node (i.e. the new tail).
            tail = tail.next

            #Here we "keep the ball rolling" and advance the pointers in l1 and l2 to the next node.
            #Set to None if the end is reached.
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        #Here we return our answer:
        #result will store the head of our answer list.
        #Remember, dummyHead was a placeholder node we created at the beginning to make building the list easier. 
        #The actual answer list starts with the node right after dummyHead, which is what dummyHead.next is pointing to.
        result = dummyHead.next
        #"Good practice" code to prevent memory leak by breaking the link between dummyhead and actual first node.
        dummyHead.next = None
        #provide the answer back to the caller. 
        #Here, we are returning the head of the answer list to whoever called the addTwoNumbers function. 
        #This allows the caller to access the entire answer list via this head node, as the rest of the list can be traversed starting from this node.
        return result
