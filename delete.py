class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.pre = None

n1 = Node(10)
head = n1
n2 = Node(20)
# n2.pre = n1
n1.next = n2
n3 = Node(30)
# n3.pre = n2
n2.next = n3
n4 = Node(40)
# n4.pre = n3
n3.next = n4
n5 = Node(50)
# n5.pre = n4
n4.next = n5
n6 = Node(60)
# n6.pre = n5
n5.next = n6
tail = n6

h = head

while h is not None:
    print(h.data)
    h = h.next

head = head.next


print('\n')
h = head
while h is not None:
    print(h.data)
    h = h.next

#End
n5.next = None    
tail = n5

print('\n')
h = head
while h is not None:
    print(h.data)
    h = h.next

#between
n3.next = n3.next.next
print('\n')
h = head
while h is not None:
    print(h.data)
    h = h.next