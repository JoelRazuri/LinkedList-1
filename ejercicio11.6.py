""" 
    Ejercicio 11.6. Implementar el método __str__ de ListaEnlazada, para que se genere una salida legible de lo que contiene la lista, similar a las listas de python.
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.first = None
        self.size = 0

    def append(self, value):
        my_node = Node(value)

        if self.size == 0:
            self.first = my_node
        else:
            current = self.first
            while current.next != None:
                current = current.next
            current.next = my_node
        
        self.size+=1
        
        return my_node

    def remove(self, value):
        if self.size == 0:
            return False
        else:
            current = self.first
            try:
                if current.value == value:
                    deleted_node = current
                    self.first = deleted_node.next
                    current = self.first
                    self.size-=1
                    return deleted_node
                    
                while current.next.value != value:
                    if current.next == None:
                        return False
                    current = current.next
                
                deleted_node = current.next
                current.next = deleted_node.next
            except AttributeError:
                return False
        self.size-=1
        
        return deleted_node

    def __len__(self):
        return self.size

    # Ejercicio 11.6.
    def __str__(self):
        string = "["
        current = self.first
        
        for i in range(len(self)):
            string += str(current)
            if i != len(self) - 1:
                string += str(", ")
            current = current.next
        
        string +="]"

        return string


my_list1 = LinkedList()


my_list1.append(1)
my_list1.append(2)
my_list1.append(3)
my_list1.append(4)
my_list1.append(5)
my_list1.append(6)
my_list1.append(5)
my_list1.append(7)


print(f"Lista 1 : {my_list1}")


