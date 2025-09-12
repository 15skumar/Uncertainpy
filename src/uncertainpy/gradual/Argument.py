from .Arguable import Arguable

class Argument(Arguable):
    """
    A class representing an argument in an argumentation framework.
    """

    def __init__(self, name: str, initial_weight: float, strength: float=None, attackers=None, supporters=None):
        super().__init__(name=name, initial_weight=initial_weight, strength=strength, attackers=attackers, supporters=supporters)

    def __repr__(self) -> str:
        return f"Argument {self.name}: initial weight {self.initial_weight}, strength {self.strength}, attackers {self.attackers}, supporters {self.supporters}"

    def __str__(self) -> str:
        return f"Argument(name={self.name}, weight={self.initial_weight}, strength={self.strength})"
