#DIANA QUINTANA GAMBOA
#DEF. DE FUNCIONES 
def f_dictionary(text):
    dictionary = dict()
    for i in range(len(text)):
        if dictionary.has_key(text[i]):
            print "Ingrese Probabilidad",text[i]
            dictionary[text[i]] = float(raw_input("- "))
        else:
            print "Ingrese Probabilidad",text[i]
            dictionary[text[i]] = float(raw_input("- "))
    return dictionary

class Node:
    def __init__(self, char, fre, izq=None, der=None):
        self.char = char
        self.fre = fre
        self.izq = izq
        self.der = der
        self.father = None
        self.bit = None

def cr_tres(dictionary):
    dictionary = sorted(dictionary.iteritems(), key=lambda value: value[1])
    nodes = list()
    for char, fre in dictionary:
        nodes.append(Node(char, fre))

    while len(nodes) > 1:
        node1 = nodes[0]
        del nodes[0]
        node2 = nodes[0]
        del nodes[0]

        sum_fre = node1.fre + node2.fre
        sum_char = node1.char + node2.char
        father = Node(sum_char, sum_fre, node1, node2)

        node1.father = father
        node2.father = father

        nodes.append(father)
        nodes = sorted(nodes, key=lambda value: value.fre)
    return father

def g_codes(code, node, bits):
    if len(node.char) != 1:
        g_codes(code, node.izq, bits + '0')
        g_codes(code, node.der, bits + '1')
    else:
        code = bits
        codes[node.char] = code
        fordecodes[code] = node.char


def main():
    print "ALGORITMO DE HUFFMAN"
    text = str(raw_input("Ingrese los caracteres como una cadena: "))
    dictionary = f_dictionary(text)
    print 'PROBABILIDAD:', dictionary
    tres = cr_tres(dictionary)
    g_codes('', tres, '')
    print 'CODEWORD:', codes
    
#PROGRAMA PRINCIAPL
if __name__ == '__main__':
    codes = dict()
    fordecodes = dict()
    main()

