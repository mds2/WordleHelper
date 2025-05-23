from WordleHelper import *

def get_cached_results():
    """
    Sometimes this stuff takes a long time to run.
    """
    return {(('orate', '..g.g'),): ('spale', 'slake', 3.119047619047619),
            (('orate', '..g.y'),): ('leash', 'leach', 2.272727272727273),
            (('orate', '..gyy'),): ('leant', 2.4166666666666665),
            (('orate', '.g..y'),): ('cried', 2.68),
            (('orate', '.g.y.'),): ('trips', 2.3125),
            (('orate', '.yyy.'),): ('satyr', 'strap', 'sprat', 'tarry',
                                   'tayra', 2.111111111111111),
            (('orate', '....y'),): ('sewel', 'bleep', 'sleep', 'heels', 'sheel',
                                    'speel', 2.7452830188679247),
            (('orate', 'yy.y.'),): ('horst', 2.5),
            (('orate', '....g'),): ('since', 'singe', 2.8313253012048194),
            (('orate', 'y....'),): ('colds', 2.9166666666666665),
            (('orate', '..yy.'),): ('tauld', 'tical', 3.0),
            (('orate', 'y...g'),): ('close', 'scone', 2.8),
            (('orate', '.y..y'),): ('reels', 3.0510204081632653),
            (('orate', '..yyy'),): ('cleat', 2.6),
            (('orate', '..gy.'),): ('plait', 'clast', 2.5652173913043477),
            (('orate', 'y.y..'),): ('macon', 2.5416666666666665),
            (('orate', '.yg..'),): ('chard', 2.5789473684210527),
            (('orate', '..g..'),): ('clans', 2.7746478873239435),
            (('orate', '...yg'),): ('thine, tuile', 2.3529411764705883),
            (('orate', '...yy'),): ('sleet', 2.5357142857142856),
            (('orate', '.....'),): ('slink', 2.8923076923076922),
            (('orate', '...y.'),): ('snift', 2.6984126984126986),
            (('orate', 'y..y.'),): ('point', 2.7083333333333335),
            (('orate', '.gg.g'),): ('crave', 3.066666666666667),
            (('orate', '..y..'),): ('canal', 2.7410714285714284),
            (('orate', '.yg.y'),): ('leary', 2.3),
            (('orate', '..yg.'),): ('tacts', 2.7777777777777777),
            (('orate', '.yy..'),): ('carpi', 2.630434782608696),
            (('orate', '.y.y.'),): ('shirt', 'hurst', 2.0),
            (('orate', '..y.g'),): ('angle', 2.8666666666666667),
            (('orate', 'y..yg'),): ('stone', 'toile', 'stole', 'thole', 'stoke', 'stove', 'tonne', 2.8),
            (('orate', '.yy.g'),): ('carse', 2.2),
            (('roate', '...y.'),): ('snift', 2.6984126984126986),
            (('roate', 'g...y'),): ('repin', 2.5238095238095237),
            (('roate', '....y'),): ('sewel', 2.7452830188679247),
            (('roate', '.....'),): ('slink', 2.8923076923076922),
            (('roate', '..y.g'),): ('angle', 2.8666666666666667),
            (('roate', '...yy'),): ('sleet', 2.5357142857142856),
            (('roate', 'yy...'),): ('crown', 2.8947368421052633),
            (('roate', 'y...g'),): ('perse', 2.769230769230769),
            (('roate', 'y.yyy'),): ('artel', 2.8823529411764706),
            (('roate', '..g.g'),): ('spale', 'slake', 3.119047619047619),
            (('roate', 'y...y'),): ('defer', 3.0294117647058822),
            (('roate', '..yg.'),): ('tacts', 2.7777777777777777),
            (('roate', 'y.y..'),): ('marcs', 2.5142857142857142),
            (('roate', '.yyy.'),): ('bloat', 2.176470588235294),
            (('roate', '..gy.'),): ('clast', 'plait', 2.5652173913043477),
            (('roate', '..g..'),): ('clans', 2.7746478873239435),
            (('roate', '..yy.'),): ('tauld', 'tical', 3.0),
            (('roate', 'y.gy.'),): ('scart', 2.55),
            (('slate', '.....'),): ('courd', 2.914027149321267),
            (('slate', '....y'),): ('diner', 2.981818181818182),
            (('slate', '..y..'),): ('maron', 2.7794117647058822),
            (('slate', '....g'),): ('drone', 2.9065420560747666),
            (('slate', '.y...'),): ('drily', 'could', 2.8505747126436782),
            (('slate', '...y.'),): ('tronc', 2.7209302325581395),
            (('slate', '...yy'),): ('deter', 'toter', 'treed', 2.7083333333333335),
            (('slate', '..y.y'),): ('macer', 2.80327868852459),
            (('slate', '.y..y'),): ('liner', 2.7868852459016393),
            (('slate', '.yy..'),): ('moral', 2.6724137931034484),
            (('slate', 'g....'),): ('spunk', 2.6785714285714284),
            (('slate', '..yy.'),): ('tabid', 2.803921568627451),
            (('slate', '..g..'),): ('drawn', 2.6875),
            (('slate', 'y....'),): ('mirks', 2.5238095238095237),
            (('slate', '.g...'),): ('flunk', 2.58974358974359),
            (('slate', 'g..y.'),): ('stunk', 2.7948717948717947),
            (('slate', '...g.'),): ('north', 2.72972972972973),
            (('slate', 'g...g'),): ('shine', 2.75),
            (('slate', '..y.g'),): ('range', 'marge', 'ragde', 2.7419354838709675),
            (('slate', '.yy.y'),): ('pedal', 2.6451612903225805),
            (('slate', '..g.g'),): ('crave', 2.857142857142857),
            (('slate', '.g..g'),): ('eloge', 'globe', 'glove', 2.6153846153846154),
            (('slate', 'y.g..'),): ('crags', 2.230769230769231),
            (('slate', 'y...y'),): ('rohes', 'roues', 2.263157894736842),
            (('slate', '.y.yy'),): ('tweel', 2.2),
            (('slate', 'g.y.y'),): ('sneap', 'spean', 'spear', 'speak', 'sewan', 2.5),
            (('slate', 'g...y'),): ('speer', 'sheer', 'spier', 'sheen', 2.5357142857142856),
            (('slate', 'y..y.'),): ('trois', 'frost', 2.4583333333333335),
            (('slate', 'g.g..'),): ('scamp', 2.608695652173913),
            (('slate', '..yyy'),): ('acted', 2.72),
            (('slate', 'g.gy.'),): ('starn', 'stank', 'stark', 'stand', 'scart', 2.7857142857142856),
            (('slate', '.yy.g'),): ('pagle', 2.5625),
            (('slate', 'y...g'),): ('nurse', 'purse', 2.7037037037037037),
            (('slate', 'g.g.g'),): ('spare', 'spade', 3.1538461538461537),
            (('ayrie', 'y....'),): ('clans', 2.953216374269006),
            (('ayrie', '.....'),): ('sculp', 2.8518518518518516),
            (('ayrie', '....y'),): ('sleet', 2.786764705882353),
            (('ayrie', '...y.'),): ('snift', 2.888888888888889),
            (('ayrie', '..y..'),): ('crust', 2.8461538461538463),
            (('ayrie', 'y...y'),): ('leman', 'leapt', 2.825),
            (('ayrie', 'y.y..'),): ('scart', 2.953488372093023),
            (('ayrie', '....g'),): ('close', 'stone', 2.957894736842105),
            (('ayrie', '...yg'),): ('snipe', 'spine', 3.0153846153846153),
            (('ayrie', '...yy'),): ('pined', 'lined', 2.5),
            (('ayrie', '...g.'),): ('colin', 'cutin', 'uplit', 2.6458333333333335),
            (('ayrie', 'y..g.'),): ('cabin', 'panic', 'patin', 2.566666666666667),
            (('ayrie', 'yyg..'),): ('party', 2.4166666666666665),
            (('ayrie', '..yy.'),): ('skirt', 'spirt', 2.727272727272727),
            (('ayrie', '.y..y'),): ('onely', 'yelts', 2.823529411764706),
            (('ayrie', '..y.g'),): ('trope', 2.85),
            (('ayrie', 'y...g'),): ('stale', 'scale', 3.1666666666666665),
            (('ayrie', '.y.y.'),): ('shily', 3.0377358490566038),
            (('ayrie', 'yy...'),): ('talcy', 'patly', 3.1323529411764706),
            (('ayrie', '..y.y'),): ('reest', 3.1964285714285716),
            (('ayrie', '.y...'),): ('godly', 3.0833333333333335),
            (('ayrie', 'y.y.y'),): ('recal', 3.2419354838709675),
            (('ayrie', '..yyy'),): ('riped', 3.1777777777777776),
            (('ayrie', 'y.y.g'),): ('crate', 'trace', 3.1785714285714284),
            (('ayrie', '..g.g'),): ('serve', 'verse', 'scree', 'spree', 'perse', 'herse', 2.76),
            (('plate', '.....'),): ('coirs', 2.9137254901960783),
            (('plate', '....y'),): ('diner', 3.011173184357542),
            (('plate', '..y..'),): ('caron', 2.7891156462585034),
            (('plate', '....g'),): ('drone', 2.945736434108527),
            (('plate', '...y.'),): ('horst', 2.8515625),
            (('plate', '.y...'),): ('dills', 2.851063829787234),
            (('plate', '...yy'),): ('reest', 2.7241379310344827),
            (('plate', '..g..'),): ('crans', 'chars', 2.7681159420289854),
            (('plate', '.yy..'),): ('salol', 2.75),
            (('plate', '..y.y'),): ('amber', 2.819672131147541),
            (('plate', '.y..y'),): ('wheel', 'lowed', 2.7966101694915255),
            (('plate', '..yy.'),): ('habit', 2.888888888888889),
            (('plate', '.g...'),): ('flocs', 2.739130434782609),
            (('plate', '...g.'),): ('north', 'broth', 2.8636363636363638),
            (('plate', '..y.g'),): ('carse', 2.7435897435897436),
            (('plate', '..g.g'),): ('crave', 3.1052631578947367),
            (('plate', 'y....'),): ('crisp', 2.4473684210526314),
            (('plate', '..gy.'),): ('scart', 2.4705882352941178),
            (('plate', '.y..g'),): ('bilge', 'liege', 'bugle', 'bulse', 'belie', 'ruble', 2.56),
            }

def best_expected_guess(w, use_cached=True):
    best_score = 100
    best_cand = [""]
    if use_cached and len(w.guess_history) < 2:
        book = get_cached_results()
        if tuple(w.guess_history) in book:
            return book[tuple(w.guess_history)]
    cands = w.suggest_guesses(broad=True, num=30, force_new=True, by_worst_case=False)
    for cand in cands:
        score = expected_depth(w, cand)
        if score < best_score:
            best_score = score
            best_cand = [cand]
        elif score == best_score:
            best_cand.append(cand)
    return tuple(best_cand + [best_score])

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
            guess_results = best_expected_guess(w2)
            score = guess_results[-1]
            count += bucket[1]
            scoresum += bucket[1] * (1 + score)
    return scoresum/max(count, 1)
