import pprint
b = {'1': ['30', '5', '3'],
     '5': ['75', '1'],
     '3': ['1', '5', '3'],
     '4': ['1']
     }
la = [1, 3 ,45 ,5]


def simple_graph(d):
    """
    Usuwa multikrawdzi oraz petle
    ."""
    lis_of_key = [key for key in d.keys()]
    for key, value in d.items():
        for v in value:
            if v in lis_of_key:
                list_value = d[v]
                if key in list_value:
                    list_value.remove(key)
    return d



def deg(graph):
    deg_V = {}
    #petla tworzy liste wszytkich wierzcholkow
    list_V = [key for key in graph.keys()]
    #lista wierzcholkow z value slownika
    list_value = []
    for value in graph.values():
        list_value.extend(value)
    for value in graph.values():
        list_V.extend(value)
    uniq_list_v = list(set(list_V))
    print(list_V)
    for v in uniq_list_v:
        if v in graph.keys() and v in list_value:
            deg_V[v] = len(graph[v]) + list_value.count(v)
        elif v in list_value:
            deg_V[v] = list_value.count(v)
    return deg_V



simple_graph(b)
deg(simple_graph(b))
