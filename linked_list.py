class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head=None

    def append(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self,data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insertion_in_between(self,prev,data):
        if not prev:
            print("Element not in list")
            return

        new_node = Node(data)
        new_node.next = prev.next
        prev.next = new_node

    def print_linked_list(self):
        cur_node = self.head
        while cur_node.next is not None:
            print(cur_node.data)
            cur_node = cur_node.next
        print (cur_node.data)


    def del_node(self,data):
        cur_node = self.head

        if cur_node and cur_node.data==data:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        while cur_node and cur_node.data!=data:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None

    def del_node_at_pos(self,pos):
        cur_node = self.head
        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        count = 1
        while cur_node and count!=pos:
            prev= cur_node
            cur_node = cur_node.next
            count+=1

        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None

    def len_iterative(self):
        count=0
        cur_node=self.head

        while cur_node:
            count+=1
            cur_node = cur_node.next
        print(count)
        return

    def len_rec(self,node):
        if node is None:
            return 0
        return 1 + self.len_rec(node.next)

    def swap_nodes(self,key_1,key_2):

        if key_1 == key_2:
            return

        prev_1 = None
        prev_2 = None
        curr_1 = self.head
        curr_2 = self.head

        while curr_1 is not None and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        while curr_2 is not None and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        if not curr_1 or not curr_2:
         return

        if prev_1 is not None:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2 is not None:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next


    def remove_duplicates(self):
        cur = self.head
        prev = None
        dup_values = dict()
        while cur:
            if cur.data in dup_values:
                prev.next = cur.next
                cur = None
            else:
                dup_values[cur.data]=1
                prev = cur
            cur = prev.next

# l1 = LinkedList()
# l1.append("A")
# l1.append("B")
# l1.append("C")
# l1.append("D")
# l1.append("E")
# l1.print_linked_list()
# print("*********")
# l1.prepend("S")
# l1.print_linked_list()
# print("*******")
# l1.insertion_in_between(l1.head.next.next,"G")
# l1.print_linked_list()
# print("*******")
# l1.del_node("G")
# print("*******")
# l1.print_linked_list()
# print("*******")
# l1.del_node_at_pos(3)
# l1.print_linked_list()
# l1.len_iterative()
# print(l1.len_rec(l1.head))
# print("*******")
# print("*******")
# l1.print_linked_list()
# l1.swap_nodes('S','A')
# print("*******")
# print("*******")
# print("*******")
# print("*******")
# l1.print_linked_list()
l2 = LinkedList()
l2.append("A")
l2.append("B")
l2.append("C")
l2.append("D")
l2.append("B")
l2.append("D")
l2.append("D")
l2.append("E")
l2.print_linked_list()
l2.remove_duplicates()
print("*******")
l2.print_linked_list()