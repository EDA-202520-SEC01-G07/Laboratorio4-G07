from DataStructures.List import single_linked_list as sl
def new_stack():
    pila = sl.new_list()
    return pila
def pop(stack):
    if sl.is_empty(stack):
        raise Exception("EmptyStructureError: queue is empty")
    else:
        elemento = sl.last_element(stack)
        sl.remove_last(stack)
        return elemento
def push(pila, elemento):
    sl.add_last(pila, elemento)
    return pila
def is_empty(pila):
    x = sl.is_empty(pila)
    return x
def top(pila):
    if not sl.is_empty(pila):
        return sl.last_element(pila)
    else:
        raise Exception("EmptyStructureError: queue is empty" )