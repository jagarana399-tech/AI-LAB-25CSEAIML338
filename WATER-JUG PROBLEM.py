from collections import deque
def water_jug(capacity1, capacity2, target):
    visited = set()
    queue = deque([(0, 0, [])])
    while queue:
        jug1, jug2, path = queue.popleft()
        if (jug1, jug2) in visited:
            continue
        visited.add((jug1, jug2))
        path= path + [(jug1, jug2)]
        if jug1 == target or jug2 == target:
            return path
        next_states = [
            (capacity1, jug2),  # Fill jug 1
            (jug1, capacity2),  # Fill jug 2
            (0, jug2),          # Empty jug 1
            (jug1, 0),          # Empty jug 2
            (jug1 - min(jug1, capacity2 - jug2),
             jug2 + min(jug1, capacity2 - jug2)),
            (jug1 + min(jug2, capacity1 - jug1),
             jug2 - min(jug2, capacity1 - jug1))
        ]
        for state in next_states:
            if state not in visited:
                queue.append((state[0], state[1], path))
    return None
# Main program
capacity1 = int(input("Enter capacity of jug 1: "))
capacity2 = int(input("Enter capacity of jug 2: "))
target = int(input("Enter target amount: "))
result = water_jug(capacity1, capacity2, target)
if result:
    print("Solution path:")
    for state in result:
        print(state)
else:
    print("No solution exists")
