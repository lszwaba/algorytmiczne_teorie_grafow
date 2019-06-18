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

def add_to_dict(lista):
    """
    Funkcja przenosi dane do slownika (graph).
    ."""
    graph = {}
    for date in lista:
        if date[0] not in graph.keys():
            graph[date[0]] = [date[1]]
            if date[1] not in graph.keys():
                graph[date[1]] = []
        elif date[0] in graph.keys():
            w = list(graph[date[0]])
            w.extend([date[1]])
            graph[date[0]] = w
            if date[1] not in graph.keys():
                graph[date[1]] = []

    return graph


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


def przeszukiwanie(graph, date):
    start = date[0]
    return DFS(graph, start)


def get_date():
    dane = []
    while True:
        try:
            d = input().split()
            dane.extend(d)
        except EOFError:
            break
    return list(dane)


def graf_elulerowski(deg):
    nie_parz = []
    for value in deg.values():
        if value % 2 == 0:
            continue
        else:
            nie_parz.append(value)
            if len(nie_parz) > 2:
                return ('\nnie jest grafem eulerowskim,\nnie jest grafem poleulerowskim\n')
    if len(nie_parz) == 0:
        return('\njest eulerowski oraz poleulerowski\n')
    elif len(nie_parz) == 2:
        return ('jest grafem poleulerowskim\n')


def jaki_to_graf():
    date = get_date()
    w = add_to_dict(pary(date))
    if len(przeszukiwanie(w, date)) == len(list(w.keys())):
        print('\nGraf:\njest spojny')
        print(graf_elulerowski(deg_v(date)))
    else:
        print('Graf:\nnie jest spojny,\nnie jest eulerowski,\nnie jest poleulerowski\n')


if __name__ == '__main__':
    jaki_to_graf()
