from WordleHelper import *
import heapq

global_count = 0
depth_exp = 3
branching = 5

def make_node(gamestate, depth, guess_list):
    global global_count, depth_exp
    global_count += 1
    return (len(gamestate.cands) * (depth_exp ** depth), depth, global_count, gamestate, guess_list)

def make_start_node(initial_game_state = None):
    if initial_game_state is not None:
        return make_node(initial_game_state, 0, [])
    w = WordleHelper()
    w.resetRealDict()
    return make_node(w, 0, [])

def do_search(initial_game_state = None, target_depth = 4):
    global branching
    h = [make_start_node(initial_game_state)]
    solutions = []
    while len(h) != 0:
        _pri, depth, _ties, w, guesses = heapq.heappop(h)
        if depth < target_depth and len(w.cands) == 1:
            sol_output = guesses + w.cands
            print(sol_output)
            solutions.append(sol_output)
            continue
        if depth >= target_depth - 1:
            continue
        candidate_guesses = []
        if depth == 0 and len(w.cands) > 2000:
            candidate_guesses = ['arise', 'raise', 'aesir', 'reais', 'serai',
                                 'aiery', 'ayrie', 'ariel', 'raile', 'aloes',
                                 'realo']
        else:
            candidate_guesses = w.suggest_guesses(force_new=True, broad=True, by_worst_case=True)[:branching]
        for guess in candidate_guesses:
            w2 = WordleHelper(copyFrom=w)
            colors = w2.likely_colors(guess)
            for color in [x[0] for x in colors if x[1] == colors[0][1]]:
                w3 = WordleHelper(copyFrom=w2)
                w3.guess(guess, color)
                heapq.heappush(h, make_node(w3, depth + 1, guesses + [guess,color]))
    return solutions

if __name__ == "__main__":
    solutions = do_search()
    print("".join(["=" for i in range(80)]))
    print("SOLUTIONS")
    print("".join(["=" for i in range(80)]))
    for s in sorted(solutions):
        print(",".join(s))
