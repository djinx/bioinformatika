def bypass(G, u, v, w):
    G_p = copy.deepcopy(G)
    G_p[u].remove(v)
    G_p[v].remove(w)
    G_p[u].append(v+"'")  #v'
    G_p[v+"'"] = [w]
    return G_p