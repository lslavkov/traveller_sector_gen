class Star:
    def __init__(self, spectral_type: str, size: str):
        self.spectral_type = spectral_type  # O, B, A, F, G, K, M
        self.size = size  # I, II, III, IV, V, VI, D, BD

    def __str__(self):
        return f"Star: {self.spectral_type}{self.size}"
