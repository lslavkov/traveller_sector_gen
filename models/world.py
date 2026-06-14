from core.ehex import ehex_to_int


class World:
    def __init__(self, name: str, uwp: str):
        self.name = name
        self.uwp = uwp

        # UWP world info based on rules
        self.size = uwp[0]
        self.atmosphere = uwp[1]
        self.hydrographics = uwp[2]
        self.population = uwp[3]
        self.government = uwp[4]
        self.law_level = uwp[5]
        self.tech_level = uwp[6]

    def get_tl(self) -> int:
        return ehex_to_int(self.tech_level)

    def __str__(self) -> str:
        return f"{self.name} | UWP: {self.uwp} | TL: {self.tech_level}"
