
def info():
    info = """
        Program oblicza stopnie podanych wierzcholkow oraz podaje
    stopien grafu. Foramat podawania danych:

    Przyklad: 'A B E X T' wiercholek glowny to A (pierwszy element na liscie),
    reszta to wierzcholki z nim polaczone. Program modyfikuje dane tak aby
    powstal graf prosty.

    !!!!!ABY ZAKOŃCZYĆ WPROWADZANIE DANYCH NALEZY NACISNAC DWA RAZY
    ENTER PO WPROWADZENIU DANYCH!!!!!
    """
    return print(info)


def get_date():
    """
    Funkcja pobiera dane z standardowego
    wejscia i umieszcza je w liscie
    ."""
    lista_v = []
    while True:
        get_V_and_E = input().split()
        try:
            if get_V_and_E[0] == '':
                break
        except IndexError:
            break
        if get_V_and_E is not '':
            lista_v.append(get_V_and_E)
    return lista_v


def add_to_dict(lista):
    """
    Funkcja przenosi dane do slownika (graph). Lista[0] jest wieszcholkiem
    a lista[1:] to wierzcholki z ktorymi jest polaczony. Jeżeli wieszlek
    jest juz w grafie dodaje do niego wierzcholki. Przyjmowane dane są
    modyfikowane aby w wartościach poszczegulnych kluczy nie powstawaly
    powtorzenia
    ."""
    graph = {}
    for date in lista:
        date_list = list(date)
        if date_list[0] in graph.keys():
            lista_V = graph[date_list[0]]
            lista_V_2 = date[1:]
            lista_V.extend(lista_V_2)
            # nie powiela takich samych nazw wieszcholkow w value
            graph[date_list[0]] = list(set(lista_V))
        else:
            graph[date_list[0]] = list(set(date[1:]))
    return graph


def simple_graph(graph):
    """
    Usuwa multikrawdzie z grafu
    ."""
    lis_of_key = [key for key in graph.keys()]
    for key, value in graph.items():
        for v in value:
            if v in lis_of_key:
                list_value = graph[v]
                if key in list_value:
                    list_value.remove(key)
    return graph


def create_graph():
    return simple_graph(add_to_dict(get_date()))


def deg(graph):
    """
    Funkcaja zwraca slownik z wierzcholkami i jego stopniami
    ."""
    deg_V = {}
    #petla tworzy liste wszytkich wierzcholkow
    list_V = [key for key in graph.keys()]
    for value in graph.values():
        list_V.extend(value)
    #lista wierzcholkow z value slownika
    list_value = []
    for value in graph.values():
        list_value.extend(value)
    for v in list_V:
        if v in graph.keys():
            deg_V[v] = len(graph[v]) + list_value.count(v)
        elif v in list_value:
            deg_V[v] = list_value.count(v)
    return deg_V


def show_results(deg_V):
    max = 0
    while deg_V:
        for key, value in deg_V.items():
            print('Wierzcholek ' + key + ' jest stopnia ' + str(value))
            if max < value:
                max = deg_V[key]
        print('\nStopien grafu wynosi ' + str(max))
        break
    else:
        print('Nie wprowadzono zadnych wierzcholkow')


if __name__ == '__main__':
    info()
    g = create_graph()
    show_results(deg(g))
