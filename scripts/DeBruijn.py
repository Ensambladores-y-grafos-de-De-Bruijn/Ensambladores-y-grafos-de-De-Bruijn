import random, copy
from graphviz import Digraph

def clona(obj):
    """ Atajo para crear copias de objetos recursivamente. """
    return copy.deepcopy(obj)

class Vertice:
    
    def __init__(self, k_mer):
        self.k_mer = k_mer
        self.exvecinos = []
        self.invecinos = []
    
    def agrega_flecha(self, v):
        """
        Método que agrega la flecha que va de este vértice al vértice v.
        """
        self.exvecinos.append(v.k_mer)
        v.invecinos.append(self.k_mer)
    
    def es_balanceado(self):
        """
        Método que regresa True syss el exgrado y el ingrado del vértice son iguales
        """
        return self.balance() == 0
    
    def es_semibalanceado(self):
        """
        Método que regresa True syss el exgrado y el ingrado del vértice difieren en 1
        """
        return abs(self.balance()) == 1

    # Definimos el balance de un vértice como su exgrado menos su ingrado
    def balance(self):
        return len(self.exvecinos) - len(self.invecinos)

    def __str__(self) -> str:
        return self.k_mer
    
    __repr__ = __str__


class GraficaDeDeBuijn:
    """
    Clase para representar gráficas de Debruijn.
    """

    def __init__(self, cadena, k):
        # Atributos de una gráfica
        self.vertices = {}
        self.vertice_inicial = None # Vértice de donde se comenzará el recorrido
        self.paseo_euleriano = [] # Donde guardaremos nuestro paseo euleriano

        # Obtenemos nuestros k-mers
        k_mers = [cadena[i: j] for i in range(len(cadena)) for j in range(i + 1, len(cadena) + 1) if len(cadena[i:j]) == k]
        
        # Creamos nuatra gráfica
        for k_mer in k_mers:
            # Obtenemos el prefijo y el sufijo del k-mer
            der = k_mer[1:]
            izq = k_mer[:-1]
            # Agregamos los vértices a nuestra gráfica si no se encuentran
            if der not in self.vertices:
                self.vertices[der] = Vertice(der)
            if izq not in self.vertices:
                self.vertices[izq] = Vertice(izq)
            # Agregamos la flecha que va del vértice izquierdo (prefijo) al vértice derecho (sufijo)
            self.vertices[izq].agrega_flecha(self.vertices[der])
       
        # Checamos que nuestra gráfica sea euleriana
        no_balanceados = []
        # vértices inicial y final en caso de que existan vértices balanceados
        vertice_inicial = None
        vertice_final = None
        for vertice in self.vertices.values():
            if not vertice.es_balanceado():
                if vertice.es_semibalanceado():
                    no_balanceados.append(vertice)
                    # Si el balance es 1, entonces aquí debe iniciar el paseo euleriano
                    if vertice.balance() == 1:
                        vertice_inicial = vertice
                    # En otro caso, el balance es -1 y por tanto aquí debe terminar el paseo euleriano
                    else:
                        vertice_final = vertice
       
        for v in self.vertices.values():
            print('Vértice: {}      Exvecinos: {}       Invecinos: {}'.format(v.k_mer,v.exvecinos, v.invecinos))
       
        # Si tenemos más de dos vértices que son semibalanceados, o no tenemos vértice de inicio o fin, entonces no tenemos
        # una digráfica euleriana
        assert len(no_balanceados) == 2 or not vertice_inicial or not vertice_final, 'La digráfica no es euleriana'
        
        # En caso de no tener un vértice inicial, escogemos uno al azar
        if not vertice_inicial:
            k_mer = random.choice(k_mers)
            if random.randint(0,1):
                self.vertice_inicial = self.vertices[k_mer[1:]]
            else:
                self.vertice_inicial = self.vertices[k_mer[:-1]]
        else:
            self.vertice_inicial = vertice_inicial
        
    def construye_secuencia_original(self):
        """
        Método que intenta recuperar la secuencia original dado el paseo euleriano.
        """
        paseo = self.get_paseo_euleriano()
        original = ''.join(vertice.k_mer[-1] for vertice in paseo[1:])
        original = paseo[0].k_mer + original
        return original
        
    def dibuja_digrafica(self, nombre):
        """
        Método que crea la representación gráfica de la digráfica de De Bruijn."""
        d = Digraph(name=nombre)
        for llave, valor in self.vertices.items():
            for exvecino in valor.exvecinos:
                d.edge(llave,exvecino)
        d.view(nombre)

    def get_paseo_euleriano(self):
        """
        Método que devuelve un paseo hamiltoniano de la digráfica
        """
        # Si ya creamos el paseo euleriano, simplemente lo devolvemos
        if self.paseo_euleriano:
            return self.paseo_euleriano
        # En otro caso lo creamos y lo devolvemos
        H = clona(self)
        self.crea_paseo_euleriano(H)
        return self.paseo_euleriano

    # Método auxiliar que crea el paseo euleriano
    def crea_paseo_euleriano(self, H):
        stack = [H.vertice_inicial]
        while stack:
            actual = stack[-1]
            # Si el vértice ya no tiene exvecinos lo sacamos del satck y lo agregamos a nuestra respuesta
            if not actual.exvecinos:
                self.paseo_euleriano.insert(0,stack.pop())
            # En otro, nos movemos a alguno de sus exvecinos por alguna flecha, eliminamos dicha flecha
            # y agregamos el vértice al que nos movimos al stack
            else:
                siguiente = H.vertices[actual.exvecinos.pop()]
                stack.append(siguiente)

s = ("GATTTCAAAAGCATTCTGTTGTTCTTTGAGGTCAGCAACCTGACCAATAAAA"
    "ACTTCAGCACTTGTATCAAGTACCAAGACATCTTGGGTCAGTAGATCATCTTGACTATTTCATTACTGTTTTCT"
    "TCGGGCTGCCCTTCACCTCTTTGCTTCCAGTATTATAGCCCCCTTCTGCCGGTTGGCTATCATTAGACATGGGA"
    "GCATCCGATTGTTGATTATGCTGAAGTCCTGAACTCTGGGTTTGCCTTTCAGCATGAGTGTTTGCTGGAGCAAT"
    "ACTGCGTAATTGAGATATGAAATGCTTCTCTACTGCTTATGCGATAATGATAGGCTAACTACTCCCTTGTGGTT"
    "ACCCATCATCAAAATCAAAATTCGAAACTGGCCTTCTCAATTTGCAGCCTGTATTGGAACATTCATTTCATGGG"
    "GTGGATTGTAATGAAAACTAATCTCAATCCCAGCTATGGCAGCGTCCTCACTCGATATCGTTTTCTCCATATTC"
    "TAGAACGGAGCAACAAACCCTCAAAGGCTCCTTGGGATCAGACTTAGGAGACTGTCTTTCAAGAACATGAATGC"
    "TAGCAATTTTGATAAGTTGTGACATTGCATCTGAGCCTTTTGGAAAGTGAGTTTTGAAAGGACTTCAAAGTAGA"
    "ATTCTGAACTGCAATGTAATGAGCATGACAGCCTTGGAAGTCTTATTAGAAGAAGCTCAAATTTCCTCCATTGG"
    "AGCATTAGCCTCGAATACAACAACTTTCGGATTAGTTGACTCAAATTCGAGAAAATCGTAATCCTCAACTTCCC"
    "AAGCCTCAAATTCAACAACTTCTTGATTCTTCAGAAGGGGTACCCTCATCACTAGAGTTTTCCAACTGGATGAA"
    "ATAAGAGGATCGACCTTTACTCGTCCATCTGTCTTACTTTCAGAAGTGATAAATTGTCTAGTAGGGCCATTATT"
    "GAGGTGAACTGACTCAGGAATATTTTCACTAACATATGCAGGAATTTCGAATGGAATCAA")

g = GraficaDeDeBuijn(s, 10)
print(g.get_paseo_euleriano())
print(g.construye_secuencia_original())

print(g.construye_secuencia_original() == s)

print('Original:\n{}'.format(s))
print('Resultado:\n{}'.format(g.construye_secuencia_original()))

g.dibuja_digrafica('digráfica1')

"""g = GraficaDeDeBuijn('Hola_como_como_como_estas', 4)
print(g.get_paseo_euleriano())
print(g.construye_secuencia_original())
g.dibuja_digrafica('digráfica2')"""