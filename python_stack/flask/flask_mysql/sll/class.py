class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        return self

    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next
        return self

    def add_to_back(self, val):
        if self.head == None:
            self.add_to_front(val)
            return self

        new_node = Node(val)
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = new_node
        return self

    def remove_from_front(self):
        old_head = self.head
        self.head = old_head.next
        return self

    def remove_from_back(self):
        runner = self.head
        while (runner.next != None):
            prev_val = runner
            runner = runner.next
        prev_val.next = None   
        return self

    def remove_val(self, val):
      
        if self.head.value == val:
            self.remove_from_front()
            return self
        
        else:
            runner = self.head 
            while (runner.value != val):
                prev_val = runner
                runner = runner.next
            if runner.next == None:
                self.remove_from_back()
            else:
                prev_val.next = runner.next
            return self

    def insert_at(self, val, n):
        if n == 0:
            self.add_to_front(val)
            return self
        else:
            runner = self.head
            iter = 0
            while (iter < n):
                if runner.next == None:
                    self.add_to_back(val)
                    return self
                else:
                    prev_val = runner
                    runner = runner.next
                    iter += 1
            new_node = Node(val)
            prev_val.next = new_node
            new_node.next = runner

        return self
        
class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

my_list = SList()	# create a new instance of a list
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!")

my_list.insert_at("Hi", 3).print_values()