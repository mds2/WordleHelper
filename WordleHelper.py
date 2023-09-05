
class WordleHelper:
    """
    To use:
    import WordleHelper
    w = WordleHelper.WordleHelper()
    w.suggest_guesses()
    w.guess("atone", "....y")
    """
    class Scorer:
        def __init__(self):
            self.chrs = "etaoinshrdlucmfwyp"
            self.chr_map = {}
            for i in range(len(self.chrs)):
                self.chr_map[self.chrs[i]] = 1.0 / (1 + i)
            self.default = 1.0 / (1 + len(self.chrs))
        def score(self, w):
            return -sum([self.chr_map.get(c, self.default) for c in
                         "".join(set(w))])
    def __init__(self, copyFrom=None):
        if copyFrom:
            from copy import deepcopy
            self.cands = deepcopy(copyFrom.cands)
            if copyFrom.cands2:
                self.cands2 = deepcopy(copyFrom.cands2)
            else:
                self.cands2 = None
            self.known = deepcopy(copyFrom.known)
            self.present = deepcopy(copyFrom.present)
            self.max_counts = deepcopy(copyFrom.max_counts)
            self.elim = deepcopy(copyFrom.elim)
            self.blocking = deepcopy(copyFrom.blocking)
            self.tree_search_cutoff = deepcopy(copyFrom.tree_search_cutoff)
            self.scorer = WordleHelper.Scorer()
        else:
            try:
                self.resetRealDict()
            except:
                print("Cannot find wordle dictionaries in folder wordle-words!")
                from nltk.corpus import words as words
                self.reset(list(set([w.lower() for w in words.words()
                                     if len(w) == 5] + ["disco", "donut"])))
    def resetRealDict(self):
        self.reset([x.replace("\n", "") for x in
                    open("wordle-words/wordle-La.txt").readlines()],
                   possible_words =
                   [x.replace("\n", "") for x in
                    open("wordle-words/wordle-Ta.txt").readlines()])
    def reset(self, words, possible_words=None):
        self.cands = words
        self.cands2 = possible_words
        self.known = [None for i in range(5)]
        self.present = ""
        self.max_counts = {}
        self.elim = ""
        self.blocking = [[] for i in range(5)]
        self.tree_search_cutoff = 2000
        self.scorer = WordleHelper.Scorer()
    def guess(self, guess, result):
        maxed = set()
        max_count = {}
        for i in range(5):
            if result[i] in 'gG':
                self.known[i] = guess[i]
                self.present += guess[i]
                self.elim = "".join([c for c in self.elim if c != guess[i]])
                max_count[guess[i]] = max_count.get(guess[i], 0) + 1
            elif result[i] in 'yY':
                self.present += guess[i]
                self.blocking[i].append(guess[i])
                self.elim = "".join([c for c in self.elim if c != guess[i]])
                max_count[guess[i]] = max_count.get(guess[i], 0) + 1
            else:
                maxed.add(guess[i])
                if not guess[i] in self.present:
                    self.elim += guess[i]
        for m in maxed:
            if m in max_count:
                self.max_counts[m] = max_count[m]
        self.filter_cands()
    def cautious_guesses(self):
        from absurdle_search import do_search
        for depth in range(1,5):
            sols = do_search(initial_game_state=WordleHelper(copyFrom=self),
                             target_depth = depth)
            if len(sols) > 0:
                return (depth, list(set([s[0] for s in sols])))
        return []
    def suggest_guesses(self, broad=False, num=30, force_new=False,
                        by_worst_case=False):
        unsorted = self.cands
        if broad and self.cands2:
            unsorted = unsorted + self.cands2
        guesses = sorted(unsorted, key = self.scorer.score)
        sort_key = lambda g: self.expected_remaining(g)
        if by_worst_case:
            sort_key = lambda g: self.worst_case_remaining(g)
        if len(self.cands) < self.tree_search_cutoff or force_new:
            print("Using new branch of code")
            guesses = sorted(guesses, key = sort_key)
        return guesses[:num]
    def strat_summary(self, num=5):
        cautions = self.cautious_guesses()
        broad = len(self.cands) > 10
        guess_lists = {
            "cautious": cautions[1],
            "worst_case": self.suggest_guesses(broad=broad, num=num,
                                               force_new=True,
                                               by_worst_case=True),
            "expected": self.suggest_guesses(broad=broad, num=num,
                                             force_new=True,
                                             by_worst_case=False)}
        def summarize(label, data):
            print(label)
            for word in data:
                print(str((word, self.expected_remaining(word),
                           self.likely_colors(word)[:2],
                           (word in cautions[1]),
                           word in self.cands)))
        for k in guess_lists:
            summarize(k, guess_lists[k])
    def good_starting_words(self):
        return ['tarie', 'raise', 'serai', 'nares', 'tarse', 'rasen', 'saite',
                'laser', 'reina', 'seral', 'taler', 'taise', 'laine', 'aries',
                'leora', 'sinae', 'ariel', 'retia', 'arise', 'ratel', 'solea',
                'later', 'serta', 'marie', 'terna', 'strae', 'artie', 'snare',
                'teras', 'slare']
    def broad_starting_gambles(self):
        return ['reina', 'irena', 'erian', 'norie', 'oared', 'irone', 'redia',
                'ocrea', 'manei', 'aider', 'kioea', 'heiau', 'oread', 'paeon',
                'opera', 'oaken', 'niepa', 'cameo', 'eniac', 'ocean', 'kenai',
                'genoa', 'idean', 'vinea', 'bohea', 'xenia', 'neoza', 'howea',
                'obeah', 'ozena']
    def interesting_starting_gambles(self):
        return ['noria', 'arion', 'cairo', 'oaric', 'haori', 'radio', 'doria',
                'nahor', 'norah', 'iroha', 'aroid', 'rohan', 'naomi', 'danio',
                'doina', 'donia', 'acoin', 'oncia', 'gonia', 'omina', 'konia',
                'inoma', 'adion', 'nogai', 'amino', 'audio', 'ikona', 'iowan',
                'honda', 'axion']
    def riskier_starting_gambles(self):
        return ['corin', 'morin', 'noric', 'irony', 'minor', 'curio', 'biron',
                'curin', 'robin', 'groin', 'yourn', 'cornu', 'runic', 'burin',
                'doric', 'mourn', 'corny', 'bruin', 'round', 'horny', 'crony',
                'goric', 'rundi', 'coiny', 'bourn', 'corgi', 'myron', 'drony',
                'duroc', 'cordy']
    def filter_cands(self):
        self.cands = [c for c in self.cands if self.plausible(c)]
        if self.cands2:
            self.cands2 = [c for c in self.cands2 if self.plausible(c)]
    def likely_colors(self, guess):
        counts = {}
        for w in self.cands:
            s = WordleHelper.what_if(w, guess)
            counts[s] = counts.get(s, 0) + 1
        ks = sorted(counts.keys(), key = lambda k: -counts[k])
        return [ (k, counts[k]) for k in ks]
    def expected_remaining(self, guess):
        results = {}
        total = 0
        for truth in self.cands:
            k = WordleHelper.what_if(truth, guess)
            results[k] = results.get(k, 0) + 1
            total += 1
        return sum([results[k] * results[k] for k in results]) / total
    def win_ratio(self, guess1, guess2):
        cols1 = dict(self.likely_colors(guess1))
        cols2 = dict(self.likely_colors(guess2))
        wins = 0
        losses = 0
        for truth in self.cands:
            c1 = WordleHelper.what_if(truth, guess1)
            c2 = WordleHelper.what_if(truth, guess2)
            wins += (cols1[c1] < cols2[c2])
            losses += (cols2[c2] < cols1[c1])
        if wins + losses == 0:
            return 0.5
        return wins / (wins + losses)
    def best_start_against(self, guess='slate'):
        """
        Good candidates against 'slate' include
        ('alert', 0.452755905511811)
        ('orate', 0.4469763365468887)
        """
        best_w = "loser"
        best_score = 1.0
        for g2 in self.cands + (self.cands2 or []):
            if g2 == guess:
                continue
            score = self.win_ratio(guess, g2)
            if score < best_score:
                best_w = g2
                best_score = score
                print((best_w, best_score))
        return (best_w, best_score)
    def worst_case_remaining(self, guess):
        results = {}
        worst_score = 0
        for truth in self.cands:
            k = WordleHelper.what_if(truth, guess)
            results[k] = results.get(k, 0) + 1
            if results[k] > worst_score:
                worst_score = results[k]
        return worst_score
    def plausible(self, word):
        for i in range(5):
            if self.known[i] and self.known[i] != word[i]:
                return False
            if word[i] in self.blocking[i]:
                return False
        for c in self.present:
            if not c in word:
                return False
        for c in self.elim:
            if c in word:
                return False
        histo = {}
        for c in word:
            histo[c] = histo.get(c, 0) + 1
        for c in histo:
            if c in self.max_counts and histo[c] != self.max_counts[c]:
                return False
        return True
    def count_in(word, letter):
        return len([c for c in word if c == letter])
    def what_if(truth, guess):
        """
        Returns what sequence of colors Worlde would give
        if the true word were truth, and the guess were guess
        """
        accum = []
        seen = {}
        for i in range(5):
            if truth[i] == guess[i]:
                accum += "g"
                seen[guess[i]] = seen.get(guess[i], 0) + 1
            elif not guess[i] in truth:
                accum += "."
            else:
                accum += "y" # incorrect, but I'll leave it
                seen[guess[i]] = seen.get(guess[i], 0) + 1
        for c in seen:
            cap = WordleHelper.count_in(truth, c)
            if cap < seen[c]:
                count = 0
                for i in range(5):
                    if guess[i] == c and accum[i] == "g":
                        count += 1
                for i in range(5):
                    if guess[i] == c and accum[i] == "y":
                        if count < cap:
                            count += 1
                        else:
                            accum[i] = "."
        return "".join(accum)

