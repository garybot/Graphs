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
        visited = set()
        paths = []

        while q.size():
            current = q.dequeue()

            if current[-1] not in visited:
                visited.add(current[-1])
                if graph.get(current[-1]):
                    for node in graph[current[-1]]:
                        q.enqueue(current + [node])
                else: paths.append(current)
                    
        paths.sort(key=lambda p : len(p))

        return paths[-1][-1]

        