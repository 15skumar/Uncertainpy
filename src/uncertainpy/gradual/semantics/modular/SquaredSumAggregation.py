class SquaredSumAggregation:
    def __init__(self) -> None:
        pass

    def aggregate_strength(self, attackers, supporters, state):
        aggregate = 0
        for a in attackers:
            attack_weight = attackers[a]
            aggregate -= state[a]**2 * attack_weight

        for s in supporters:
            support_weight = supporters[s]
            aggregate += state[s]**2 * support_weight

        return aggregate
    
    def __str__(self) -> str:
        return __class__.__name__
