# Pronalazenje maksimalnih nerazgranatih putanja u grafu
def maximal_non_branching_paths(G):
    paths = []
    visited = {}

    for v in G:
        (v_in_deg, v_out_deg) = degree(G, v)
        if v_in_deg != 1 or v_out_deg != 1:
            visited[v] = True

            if v_out_deg > 0:
                for w in G[v]:
                    non_branching_path = [(v,w)]
                    visited[w] = True
                    (w_in_deg, w_out_deg) = degree(G, w)

                    while w_in_deg == 1 and w_out_deg == 1:
                        u = G[w][0]
                        non_branching_path.append((w,u))
                        w = u
                        visited[w] = True
                        (w_in_deg, w_out_deg) = degree(G, w)

                    paths.append(non_branching_path)
	
    for v in G:
        if v not in visited:
            c = isolated_cycle(G, v)
            if c != None:
                paths.append(c)

    return paths