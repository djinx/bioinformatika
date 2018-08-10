def is_connected(G):

    visited = {};
    for v in G:
        DFS(G,v,visited)
        break

    for v in G:
        if v not in visited:
            return False

    return True