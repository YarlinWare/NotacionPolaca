def notacion_polaca(operacion):
    operador = ['+', '-', '/', '*','^']
    d = ''
    pila = []
    aux = []
    '''
    A partir de funciones anónimas realizamos
    el proceso de separación de carácteres
    '''
    expresion =  (lambda fun: lambda arg: fun(arg)) (lambda a: list(a))(operacion)
    print('La expresión en lista: {}'.format(expresion))

    '''
    A partir de la teoría sobre árboles y notación polaca
    procedemos a realizar la operación para generar la nueva
    organización de los elementos
    '''
    for caracter in expresion:
        if (caracter not in operador) and (caracter != ')') and (caracter != '('):
            pila.append(caracter)
        elif (caracter in operador) and (caracter != ')') and (caracter != '('):
            if len(aux) != 0:
                if aux[-1] == '(':
                    d = aux.pop()
                if (len(aux) != 0) and (operador.index(caracter) <= operador.index(aux[-1])):
                    c = aux.pop()
                    pila.append(c)
                elif (len(aux) != 0) and (operador.index(caracter) >= operador.index(aux[-1])):
                    pila.append(caracter)
                if d == '(':
                    aux.append(d)
            aux.append(caracter)
            if pila[-1] == aux[-1]:
                aux.pop()
        elif caracter == '(':
            aux.append(caracter)
        elif caracter == ')':
            if len(aux) == 0:
                pass
            else:
                while aux[-1] != '(':
                    c = aux.pop()
                    pila.append(c)
            aux.pop()
    while len(aux) > 0:
        if aux[-1] in pila:
            aux.pop()
        else:
            c = aux.pop()
            pila.append(c)
    pila.reverse()
    print('La pila creada en forma de lista: {}'.format(pila))
    print('Expresión final: {}'.format(''.join(pila)))

