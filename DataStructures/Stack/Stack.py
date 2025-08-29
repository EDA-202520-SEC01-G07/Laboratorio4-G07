from DataStructures.List import single_linked_list as sl
def new_stack():
    pila = sl.new_list()
    return pila

def push(pila, elemento):
    sl.add_last(pila, elemento)
    return pila