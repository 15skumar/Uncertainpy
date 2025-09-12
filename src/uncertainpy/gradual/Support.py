from .Arguable import Arguable

class Support(Arguable):
    def __init__(self, source, target, weight=1) -> None:
        super().__init__(name=f"Sup({source},{target})", initial_weight=weight)
        self.source = source
        self.target = target

    def get_source(self):
        return self.source

    def get_target(self):
        return self.target

    def get_initial_weight(self):
        return self.initial_weight

    def __repr__(self) -> str:
        return f"Support({self.source}, {self.target}, weight={self.initial_weight})"

    def __str__(self) -> str:
        return (
            f"Support by {self.source} to {self.target} with weight {self.initial_weight}"
        )
