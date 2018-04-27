import queue


def deg_v(a):
    liczba_degv = {}
    checkd = []
    for i in a:
        if i not in checkd:
            liczba_degv[i] = a.count(i)
            checkd.append(i)
    return liczba_degv


def pary(a):
    v = a[::2]
    v_2 = a[1::2]
    end_v = []
    for i in range(0, len(v)):
        temp = []
        temp.append(str(v[i]))
        temp.append(str(v_2[i]))
        end_v.append(temp)
    return end_v


def brakujace_v(graph):
    g = {}
    for v in graph.values():
        for i in v:
            if i not in graph.keys():
                g[i] = []
    graph.update(g)
    return graph


def add_to_dict(lista):
    """
    Funkcja przenosi dane do slownika (graph).
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
    return brakujace_v(graph)


def DFS(graph, poczatek):
    kolejka = queue.LifoQueue()
    odwiedzone = []
    kolejka.put(poczatek)
    while not kolejka.empty():
        poczatek = kolejka.get()
        if poczatek not in odwiedzone:
            odwiedzone.append(poczatek)
            for v in graph[poczatek]:
                if v not in odwiedzone:
                    kolejka.put(v)
    return odwiedzone


def przeszukiwanie(graph):
    start = list(graph.keys())[0]
    return DFS(graph, start)


def get_date():
    dane = input()
    return list(dane)


def graf_elulerowski(deg):
    nie_parz = []
    for value in deg.values():
        if value % 2 == 0:
            continue
        else:
            nie_parz.append(value)
            if len(nie_parz) > 2:
                return ('\nie jest grafem eulerowskim,\nnie jest grafem poleulerowskim')
    if len(nie_parz) == 0:
        return('\njest eulerowski oraz poleulerowski')
    elif len(nie_parz) == 2:
        return ('jest grafem poleulerowskim')


def jaki_to_graf():
    date = get_date()
    w = add_to_dict(pary(date))
    if len(przeszukiwanie(w)) == len(list(w.keys())):
        print('Graf:\njest spójny')
        print(graf_elulerowski(deg_v(date)))
    else:
        print('Graf:\n nie jest spojny,\nnie jest eulerowski,\nnie jest poleulerowski')


if __name__ == '__main__':
    jaki_to_graf()
