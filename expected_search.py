from WordleHelper import *

def get_cached_results():
    """
    Sometimes this stuff takes a long time to run.
    """
    return {(('orate', '..g.g')): ('spale', 3.119047619047619),
            (('orate', '..g.y')): ('leash', 'leach', 2.272727272727273),
            (('orate', '..gyy')): ('leant', 2.4166666666666665),
            (('orate', '.g..y')): ('cried', 2.68),
            (('orate', '.g.y.')): ('trips', 2.3125)
            (('orate', '.yyy.')): ('satyr', 'strap', 'sprat', 'tarry',
                                   'tayra', 2.111111111111111)}

def best_expected_guess(w):
    best_score = 100
    best_cand = ""
    cands = w.suggest_guesses(broad=True, num=30, force_new=True, by_worst_case=False)
    for cand in cands:
        score = expected_depth(w, cand)
        if score < best_score:
            best_score = score
            best_cand = cand
    return (best_cand, best_score)

def expected_depth(w, guess):
    count = 0
    scoresum = 0
    if len(w.cands) < 2:
        if guess in w.cands:
            return 1
        return 2
    buckets = w.likely_colors(guess)
    for bucket in buckets:
        if bucket[1] == 1:
            count += 1
            scoresum += 2
        elif bucket[1] == 2:
            count += 2
            scoresum += 2 * (1 + 1.5)
        else:
            w2 = WordleHelper(copyFrom=w)
            w2.guess(guess, bucket[0])
            _, score = best_expected_guess(w2)
            count += bucket[1]
            scoresum += bucket[1] * (1 + score)
    return scoresum/max(count, 1)
