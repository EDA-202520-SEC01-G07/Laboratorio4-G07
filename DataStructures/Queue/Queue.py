from DataStructures.List import array_list as lt

def new_queue():
    cola = lt.new_list()
    return cola
def enqueue(cola, elemento):
    lt.add_last(cola, elemento)
    return cola

def dequeue(cola):
    lt.remove_first(cola)
    return cola

def is_empty(cola):
    x = lt.is_empty(cola)
    return x
def peek(cola):
    if not lt.is_empty(cola):
        return lt.get_element(cola, 1)
    else:
        raise Exception("EmptyStructureError: queue is empty")

def size(cola):
    return lt.size(cola)