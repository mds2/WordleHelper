from WordleHelper import *
from expected_search import *
from multiprocessing import Pool
import argparse

def explore(word_and_colors):
    print(f"Exploring {word_and_colors}")
    word, colors = word_and_colors
    w = WordleHelper()
    w.guess(word, colors)
    result = best_expected_guess(w)
    print(f"{((word, colors))}: {result}")
    return [((word, colors)), result]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--guess', '-g',
                        type=str,
                        required=True
                        )
    parser.add_argument('--skip', '-s',
                        type=int,
                        default=0,
                        )
    parser.add_argument('--multiprocess', '-m',
                        action='store_true')
    args = parser.parse_args()
    w = WordleHelper()
    to_try = w.likely_colors(args.guess)
    to_try = [t for t in to_try if t[1] >= 30]
    to_try = to_try[args.skip:]
    print(f"Likely colors are {to_try}")
    if args.multiprocess:
        with Pool(3) as pool:
            print(pool.map(explore,
                           [(args.guess, colors[0]) for colors in to_try]))
    else:
        print([explore(guess) for guess in
               [(args.guess, colors[0]) for colors in to_try]])
    print("Done")
