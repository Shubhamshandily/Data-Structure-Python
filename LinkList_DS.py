print('*****************LINKED LIST***********************\n')

class Node(object):
    def __init__(self,data=None, next_node=None):
        self.data =data
        self.next_node=next_node,

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self,new_next):
        self.next_node=new_next

class LinkedList(object):
    def __init__(self, head=None):
        self.head= head

    def insert(self, data):
        new_node =Node(data)
        new_node.set_next(self.head)
        self.head =new_node

    def size(self):
        current =self.head
        count=0
        while current:
            count += 1
            print(current.get_data())
            current=current.get_next()
        print('The size of linkedlist: ',count)

    def search(self,data):
        current= self.head
        found=False
        while current and found is False:
            if current.get_data()==data:
                found=True
            else:
                current=current.get_next()
        if current is None:
            raise ValueError('Item not found')
        return found
    def delete(self, data):
        current=self.head
        previous=None
        found=False
        while current and found is False:
            if current.get_data()==data:
                found=True
            else:
                previous= current
                current =current.get_next()
        if current is None:
            raise ValueError('Item not found')
        if previous is None:
            self.head=current.get_next()
        else:
            previous.set_next(current.get_next())

ll=LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.size()
val=ll.search(2)
if val:
    print('Item found is: ',val)
ll.delete(3)
ll.size()

print('\n---------------******************GRAPH*******************-----------------\n')
from collections import defaultdict
graph=defaultdict(list)

def addEdge(graph, u,v):
    graph[u].append(v)

def generate_edges(graph):
    edges=[]
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node,neighbour))
    return edges

addEdge(graph, 'a', 'c')
addEdge(graph, 'b', 'c')
addEdge(graph, 'b', 'e')
addEdge(graph, 'c', 'd')
addEdge(graph, 'c', 'e')
addEdge(graph, 'c', 'a')
addEdge(graph, 'c', 'b')
addEdge(graph, 'e', 'b')
addEdge(graph, 'd', 'c')
addEdge(graph, 'e', 'c')

print(generate_edges(graph))
