class SquaredProductAggregation:
    def __init__(self) -> None:
        pass

    def aggregate_strength(self, attackers, supporters, state):
        support_value = 1
        for a in attackers:
            support_value *= (1-state[a])**2

        attack_value = 1
        for s in supporters:
            attack_value *= (1-state[s])**2

        return support_value - attack_value

    def __str__(self) -> str:
        return __class__.__name__
