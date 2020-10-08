from util import Stack, Queue  # These may come in handy

def earliest_ancestor(ancestors, starting_node):
    graph = {}
    for rel in ancestors:
        if rel[1] in graph:
            graph[rel[1]].add(rel[0])
        else:
            graph[rel[1]] = {rel[0]}

    if starting_node not in graph:
        return -1

    else:
        q = Queue()
        q.enqueue([starting_node])
        paths = []

        while q.size():
            current = q.dequeue()

            if graph.get(current[-1]):
                for node in graph[current[-1]]:
                    q.enqueue(current + [node])
            else: paths.append(current)
            
        ## Will the longest path always be last?
        # paths.sort(key=lambda p : len(p))

        return paths[-1][-1]



# def dft_recursive(table, node, distance):
#     parents = table[node]

#     for parent in parents:
#         dft_recursive(ancestors, parent, distance+1)



# def earliest_ancestor(ancestors, starting_node, distance=0):
#     table = {}
#     for rel in ancestors:
#         if rel[1] in table:
#             table[rel[1]].add(rel[0])
#         else:
#             table[rel[1]] = {rel[0]}

#     if starting_node not in table:
#         return -1

#     dft_recursive(table, starting_node, distance)