from collections import defaultdict, deque

def parse_input(file):
    with open(file, 'r') as f:
        data = f.read().strip().split('\n\n')
    
    rules = data[0].split('\n')
    updates = [update.split(',') for update in data[1].split('\n')]
    return rules, updates

def build_graph(rules):
    graph = defaultdict(list)
    for rule in rules:
        x, y = rule.split('|')
        graph[x].append(y)
    return graph

def valid(update, graph):
    index = {page: i for i, page in enumerate(update)}
    for i in update:
        for j in graph[i]:
            if j in index and index[i] > index[j]:
                return False
    return True

def middle_page(update):
    return update[len(update) // 2]

def make_sum(file):
    rules, updates = parse_input(file)
    graph = build_graph(rules)

    valid_updates = [update for update in updates if valid(update, graph)]
    middle_pages = [int(middle_page(update)) for update in valid_updates]
    return sum(middle_pages)

def reorder(update, graph):
    index = {page: i for i, page in enumerate(update)}
    in_degree = {page: 0 for page in update}
    for i in update:
        for j in graph[i]:
            if j in index:
                in_degree[j] += 1

    queue = deque([page for page in update if in_degree[page] == 0])
    ordered_update = []

    while queue:
        node = queue.popleft()
        ordered_update.append(node)
        for neighbor in graph[node]:
            if neighbor in index:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

    return ordered_update

def make_sum_incorrect(file):
    rules, updates = parse_input(file)
    graph = build_graph(rules)

    invalid_updates = [update for update in updates if not valid(update, graph)]
    reordered_updates = [reorder(update, graph) for update in invalid_updates]
    middle_pages = [int(middle_page(update)) for update in reordered_updates]
    return sum(middle_pages)


file = 'day5/input.txt' 
print(make_sum_incorrect(file))