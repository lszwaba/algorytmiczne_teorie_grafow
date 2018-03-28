def info():
    info = """
        Program oblicza stopnie podanych wierzcholkow oraz podaje
    najwyzszy stopien wieszcholka. Foramta podawania danych:Przyklad
    'A B E X T' wiercholek glowny to A (pierwszy element na liscie), reszta
    to wierzcholki z nim polaczone.

    !!!!!ABY ZAKOŃCZYĆ WPROWADZANIE DANYCH NALEZY NAPISAC 'quit'!!!!!
    """
    print(info)


def get_date(lista):
    """
    Funkcja pobiera dane z standardowego
    wejscia i umieszcza je w liscie
    ."""
    while True:
        get_V_and_E = input().split()
        try:
            if get_V_and_E[0] == 'quit':
                break
        except IndexError:
            print('Nie wprowadzono danych')
        else:
            lista.append(get_V_and_E)


def add_to_dict(graph, lista):
    """
    Funkcja przenosi dane do slownika (graph). Lista[0] jest wieszcholkiem
    a lista[1:] to wierzcholki z ktorymi jest polaczony. Jeżeli wieszlek
    jest juz w grafie dodaje do niego wierzcholki
    ."""
    roboczy_dic = {}
    for date in lista:
        date_list = list(date)
        if date_list[0] in graph.keys():
            print(graph[date_list[0]])
            lista_V = graph[date_list[0]]
            lista_V_2 = date[1:]
            lista_V.extend(lista_V_2)
            print(type(lista_V_2))
            roboczy_dic[date_list[0]] = lista_V
        else:
            graph[date_list[0]] = list(date[1:])


def create_graph(graph, lista):
    get_date(lista)
    add_to_dict(graph, lista)
    print(graph)


if __name__ == '__main__':
    graph = {}
    lista = []
    info()
    create_graph(graph, lista)
