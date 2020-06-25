class Nodo():
    def __init__(self, valor, izquierda=None, derecha=None):
        self.izquierda = None
        self.derecha = None
        self.valor = valor

def en_orden(arbol):
    if arbol == None:
        return []
    return en_orden(arbol.izquierda) + [arbol.valor] + en_orden(arbol.derecha)


def pre_orden(arbol):
    if arbol == None:
        return []
    return [arbol.valor] + pre_orden(arbol.izquierda) + pre_orden(arbol.derecha)


def post_orden(arbol):
    if arbol == None:
        return []
    return post_orden(arbol.izquierda) + post_orden(arbol.derecha) + [arbol.valor]


def insertar(arbol, valor):
    if arbol == None:
        return Nodo(valor)
    if arbol.valor > valor:
        return Nodo(arbol.valor, insertar(arbol.izquierda,valor), arbol.derecha)
    return Nodo(arbol.valor, arbol.izquierda, insertar(arbol.derecha, valor))



arbol = Nodo(25, Nodo(15,None,Nodo(20)), Nodo(50))

print(en_orden(arbol))
print(pre_orden(arbol))
print(post_orden(arbol))
print(en_orden(insertar(arbol,5)))