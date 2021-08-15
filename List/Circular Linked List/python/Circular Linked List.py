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
        length = 1
        temp = self.head
        while 1:
            length += 1
            temp = temp.next
            if temp == self.head:
                break
        return length

    def get_pre_position(self, position):
        length = self.len(self.head)
        if position > length:
            return None
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
        if position != None and position < 0:
            print("Position should be greater than or equal 0")
        if end is False:
            if position is None:
                self.insert_at_beginning(data)
            else:
                if position == 0:
                    self.insert_at_beginning(data)
                elif position == len(self.head):
                    self.insert_at_end(data)
                    pass
                else:
                    # at sep position
                    pass
        else:
            if position is None:
                if self.head is None:
                    # new node
                    pass
                else:
                    # insert at end
                    pass
            else:
                length = len(self.head)

                if position == 0:
                    # insert at end
                    pass
                else:
                    # chnage the postion form last to first to first to last
                    # at sep position
                    pass
            pass

        return self

    """
        def get_pre_position(self, position):
            length=self.len()
            if position >=  length or (position < 0 and -position > length):
                return None
            if position<0:
                position=length+position
                pass
            temp = self.head
            position -= 1
            while position:
                position -= 1
                temp = temp.next
            return temp
            
        def insert(self, data, /, end=False,position=None):

            if end is False:
                if position is None:
                    new_node = Node(data)
                    if self.head==None:
                        new_node.next = new_node
                        self.tail=new_node
                        self.head=new_node
                    else:
                        new_node.next = self.head
                        self.tail.next=new_node
                        self.head=new_node
                    print("New Node Inserted with data %d at the Beginning" % (data))
                elif position == 0:
                    new_node = Node(data)
                    self.head, new_node.next ,self.tail.next= new_node, self.head,new_node
                else:
                    temp = self.get_pre_position(position)
                    if temp == None:
                        print("Position is too Long")
                    else:
                        new_node = Node(data)
                        temp.next, new_node.next = new_node, temp.next
                return self

            else:
                if position is None:
                    if self.head == None:
                        self.head = Node(data)
                        print("New Node Inserted with data %d at the End" % (data))
                    else:
                        temp = self.head
                        while temp.next:
                            temp = temp.next
                        temp.next = Node(data)
                        print("New Node Inserted with data %d at the End" % (data))
                else:
                    if position>0:
                        position=-position
                    temp = self.get_pre_position(position)
                    if temp == None:
                        print("Position is too Long")
                    else:
                        new_node = Node(data)
                        temp.next, new_node.next = new_node, temp.next
            return self

        '''
            Delete:
            Data:  optional
            end:   optional
            all:   optional
            if all is True: (deleting all the occurance of teh data)
                if data is None:
                    error => No data is given to delete in the list
                    returns the self of this class
                head is assigned to temp 
                passing the temp in while till next node of exist
                    if the data in next node of the temp then
                        (deleting the node)
                        next node of the next node of the temp is 
                        assigned to
                        next node of the temp
                    next node of the temp is assigned to temp
            if end is None: (deleting at the beginning)
                if data is None: (deleting at the beginning)
                    if head is None:
                        No data to delete from the list
                    else:
                        next node of head is assigned to head
                        ( if next node of head is null 
                        it shows that list have only one 
                        node so that node is deleted
                        by assigned next node of the head(null) to the head
                        )
                if data is not None:(delete a node whose data is matching with the given data)
                    if head is not None:
                        head have no data to delete
                    if head have only one node to delete
                        and that node have the given data:
                            assigned next node of the head(null) to the head
                    else:
                        head is assigned to temp
                        passing the temp in while till next node of exist
                            if data of next node of temp is givendata:
                                deleting the node
                                and then breaking the while loop
                            next node of temp is assigned to temp
            else:
                if data is None:
                    if head is None:
                        no data to delete
                    if head have only one node:
                        next node of head is assigned to head
                        ( if next node of head is null 
                        it shows that list have only one 
                        node so that node is deleted
                        by assigned next node of the head(null) to the head
                        )
                    else:
                        head is assigned to temp
                        passing the temp in while till next node of exist
                            next node of temp is assigned to temp
                        (temp is traveled to previous node of last node in the list)
                        and that node is deleted
                else:
                    if head is None:
                        no data to delete
                    else: (deleting the last occurance of data)
                        previous, temp_previous,valid set all to None
                        head is assigned to temp
                        passing the temp in while till next node of exist
                            if data in temp is matching to the given data:
                                store the previous to temp_previous and
                                True to valid
                            store temp to previous
                        if temp_previous is None:
                            if valid is True:(last occurance of data is found on the first node)
                                store next node of head to head
                        else:
                            store next node of next node of temp_pre to next node of temp_pre
            returns the self of this class
        '''
        def delete(self, *, data=None, end=None,all=False):
            if all:
                if data == None:
                    print("No data is given")
                    return self
                temp = self.head
                while temp.next:
                    if temp.next.data == data:
                        temp.next = temp.next.next
                        if temp.next == None:
                            break
                    temp = temp.next
                print("All the Node with Data%d is deleted" % (data))
            elif end is None:
                if data == None:
                    if self.head == None:
                        print("No Node to delete")
                    else:
                        self.head = self.head.next
                        print("Node is Deleted at the Beginning")
                else:
                    if self.head == None:
                        print("No Node to delete")
                    elif self.head.next == None:
                        if self.head.data == data:
                            self.head = self.head.next
                            print(
                                "Node with data %d is Deleted at the Beginning" % (data))
                    else:
                        temp = self.head
                        while temp.next:
                            if temp.next.data == data:
                                temp.next = temp.next.next
                                print(
                                    "Node with data %d is Deleted at the Beginning" % (data))
                                break
                            temp = temp.next
            else:
                if data == None:
                    if self.head == None:
                        print("No data to delete")
                    elif self.head.next == None:
                        self.head = self.head.next
                        print("Node is Deleted at the End")
                    else:
                        temp = self.head
                        while temp.next.next:
                            temp = temp.next
                        temp.next = temp.next.next
                        print("Node is Deleted at the End")
                else:
                    if self.head == None:
                        print("No data to delete")
                        return self
                    else:
                        pre = temp_pre = valid = None
                        temp = self.head
                        while temp:
                            if temp.data == data:
                                temp_pre = pre
                                valid = True
                            pre = temp
                            temp = temp.next
                        if temp_pre == None:
                            if valid:
                                self.head = self.head.next
                        else:
                            temp_pre.next = temp_pre.next.next
                        print("Node with data %d is Deleted at the End" % (data))
            return self

        def replace(self, old_data, new_data):
            temp = self.head
            while temp:
                if temp.data == old_data:
                    temp.data = new_data
                    print("%d is Replaced with %d" % (old_data, new_data))
                    break
                temp = temp.next
            return self

        def replace_all(self, old_data, new_data):
            temp = self.head
            while temp:
                if temp.data == old_data:
                    temp.data = new_data
                temp = temp.next
            print("All the instances of %d is replaced with %d" % (old_data, new_data))
            return self

        def __len__(self):
            length = 0
            temp = self.head
            while temp:
                length += 1
                temp = temp.next
            return length

        def rotate(self, times):
            if self.head == None or self.head.next ==None:
                return self
            length = len(self)
            times %= length
            tail = self.head
            while tail.next:
                tail = tail.next
            while times:
                times -= 1
                tail.next = self.head
                tail = tail.next
                self.head = self.head.next
                tail.next = None
            print("Nodes are rotated")
            return self
    """

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
