class Matrix:
    def __init__(self):
        self._matrix = ((  0, 393, 288, 290, 498, 193, 552, 560, 572, 194, 588, 439, 556, 636, 532),
                        (393,   0, 123, 136, 234, 481, 266, 293, 312, 377, 753, 588, 447, 633, 255),
                        (288, 123,   0, 157, 353, 477, 376, 417, 429, 396, 791, 610, 498, 655, 386),
                        (290, 136, 157,   0, 214, 367, 267, 278, 290, 262, 632, 466, 354, 512, 247),
                        (498, 234, 353, 214,   0, 516,  54,  70,  91, 417, 606, 441, 226, 418,  35),
                        (193, 481, 477, 367, 516,   0, 583, 581, 574, 120, 459, 313, 465, 510, 547),
                        (552, 266, 376, 267,  54, 583,   0,  30,  69, 472, 634, 469, 251, 426,  24),
                        (560, 293, 417, 278,  70, 581,  30,   0,  44, 482, 611, 446, 228, 403,  37),
                        (572, 312, 429, 290,  91, 574,  69,  44,   0, 494, 575, 410, 192, 368,  70),
                        (194, 377, 396, 262, 417, 120, 472, 482, 494,   0, 429, 283, 396, 477, 449),
                        (588, 753, 791, 632, 606, 459, 634, 611, 575, 429,   0, 166, 392, 221, 634),
                        (439, 588, 610, 466, 441, 313, 469, 446, 410, 283, 166,   0, 225, 208, 467),
                        (556, 447, 498, 354, 226, 465, 251, 228, 192, 396, 392, 225,   0, 204, 252),
                        (636, 633, 655, 512, 418, 510, 426, 403, 368, 477, 221, 208, 204,   0, 427),
                        (532, 255, 386, 247,  35, 547,  24,  37,  70, 449, 634, 467, 252, 427,   0))
        self._cities = ['Berlin', 'Bremen', 'Hamburg', 'Hannover', 'Dortmund', 'Dresden', 'Duisburg', 'Dusseldorf',
                        'Koln', 'Leipzig', 'Munchen', 'Nurnberg', 'Frankfurt am Main', 'Stuttgart', 'Essen']

        self._right_cities = ('Berlin', 'Hamburg', 'Bremen', 'Hannover', 'Dortmund', 'Essen', 'Duisburg', 'Dusseldorf',
                              'Koln', 'Frankfurt am Main', 'Stuttgart', 'Munchen', 'Nurnberg', 'Leipzig', 'Dresden')
        self._right_indexes = [self._cities.index(city) for city in self._right_cities]
        self._right_distance = self.path_len(self._right_indexes)

    @property
    def cities_count(self):
        return len(self._matrix)

    @property
    def right_cities(self):
        return self._right_cities

    @property
    def right_distance(self):
        return self._right_distance

    def get_names(self, indexes):
        return [self._cities[i] for i in indexes]

    def path_len(self, seq):
        path = 0
        for i, from_ in enumerate(seq[:-1]):
            to_ = seq[i + 1]
            path += self._matrix[from_][to_]
        path += self._matrix[-1][0]
        return path

    def score(self, seq):
        path_len = self.path_len(seq)
        score = self._right_distance / path_len
        return score

