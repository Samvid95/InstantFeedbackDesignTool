from metroidvania.game import Simulator

global prev
prev = {}

def analyze(design):
    prev.clear()

    sim =  Simulator(design)
    init = sim.get_initial_state()
    moves = sim.get_moves()

    queue = []
    queue.append(init)
    prev[init] = None

    while queue:
        current_state = queue.pop(0)
        for move in moves:
            next_state = sim.get_next_state(current_state,move)
            if next_state!= None and next_state not in prev:
                queue.append(next_state)
                prev[next_state] = current_state

    return prev

def inspect(result, coord, draw_line):
    x,y = coord
    current_state= None
    for state in result:
        print(state)
        coord = state[0]
        if coord == (x,y):
            current_state = state
            previous_state = result[current_state]
            while previous_state != None:
                draw_line(current_state[0], previous_state[0],state,previous_state[1])
                current_state = previous_state
                previous_state = result[current_state]



