class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        print("New Node Created with data %d" % (data))


class Circular_Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def __len__(self):
        temp = self.head
        if temp is None:
            return 1
        length = 1
        while 1:
            length += 1
            temp = temp.next
            if temp == self.head:
                break
        return length

    def get_pre_position(self, position):
        temp = self.head
        position -= 1
        while position:
            position -= 1
            temp = temp.next
        return temp

    def insert_at_beginning(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.next = new_node
            self.head, self.tail = new_node, new_node
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head, self.tail.next = new_node, new_node

    def insert_at_end(self, data):
        if self.tail == None:
            if self.head:
                print("Some error in the program")
                return None
            else:
                self.insert_at_beginning(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.tail.next, self.tail = new_node, new_node

    def insert(self, data, /, end=False, position=None):
        if self.head is None:
            length = 0
        else:
            length = len(self)
        if position != None and (position < 0 or position > length):
            print(
                "Position should be greater than or equal 0 and less that or equal to %d "
                % (length)
            )
        elif end is False:
            if position is None:
                self.insert_at_beginning(data)
            else:
                if position == 0:
                    self.insert_at_beginning(data)
                elif position == len(self):
                    self.insert_at_end(data)
                else:
                    temp = self.get_pre_position(position)
                    new_node = Node(data)
                    temp.next, new_node.next = new_node, temp.next
        else:
            if position is None:
                self.insert_at_end(data)
            else:
                if position == 0:
                    self.insert_at_end(data)
                elif position == length:
                    self.insert_at_beginning(data)
                else:
                    position = length - position
                    temp = self.get_pre_position(position)
                    new_node = Node(data)
                    temp.next, new_node.next = new_node, temp.next
        return self

    def delete_at_end(self):
        if self.head == None:
            print("No Node to delete")
            return None
        if self.head == self.tail:
            print("Node is deleted at the EnD")
            return
        temp = self.head
        while temp.next != self.tail:
            temp = temp.next
        print("Node with teh data %d at the end is deleted" % (temp.next.data))
        temp.next = temp.next.next
        self.tail = temp

    def delete(self, /, data=None, end=False, position=None, all=False):
        if data is None:
            if end is False:
                if position is None:
                    if all is False:
                        self.delete_at_end()
                    else:
                        self.head,self.tail=None,None
                        print("List is cleared")
                else:
                    if all is False:
                        
        pass

    def display(self):
        """
        Display:
            if head is none:
                list is empty
                reterns the self of this class
            started displaying the nodes
            temp is assigned t head of the node list
            temp is traveled till the end of the list
                by displaying the values in each node
            returns the self of this class
        """
        if self.head == None:
            print("No Nodes to display")
            return self
        print("Nodes are: ", end=" ")
        temp = self.head
        while temp != self.tail:
            print(temp.data, end=" ")
            temp = temp.next
        print(temp.data)
        return self


if __name__ == "__main__":
    head = Circular_Linked_List()
    head.insert(4).insert(3).insert(2).insert(1, position=0)
    head.display()
    # head.delete(data=5).display()
    # head.delete().display()
    # head.delete(end=True).display()
    # head.delete(data=6, end=True, all=True).display()
