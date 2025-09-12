class Arguable:
    """
    A superclass for objects that can be attacked or supported in an argumentation framework.
    """

    def __init__(self, name: str, initial_weight: float, strength: float=None, attackers=None, supporters=None):
        """
        Initializes an instance of the Arguable class.
        :param name: The name of the arguable entity.
        :param initial_weight: The initial weight of the arguable entity.
        :param strength: The current strength of the arguable entity. If None, it defaults to initial_weight.
        :param attackers: A list of attackers. If None, it defaults to an empty dictionary.
        :param supporters: A list of supporters. If None, it defaults to an empty dictionary.
        """
        self.name = name
        self.initial_weight = initial_weight
        self.strength = initial_weight
        self.attackers = attackers if attackers is not None else {}
        self.supporters = supporters if supporters is not None else {}


    def get_name(self):
        return self.name

    def add_attacker(self, attacker, attack_weight=1):
        self.attackers[attacker] = attack_weight

    def add_supporter(self, supporter, support_weight=1):
        self.supporters[supporter] = support_weight

    def get_initial_weight(self):
        return self.initial_weight
        
    def reset_initial_weight(self, weight):
        self.initial_weight = weight


    def __str__(self):
        return f"Arguable({self.name}, initial_weight={self.initial_weight})"

    def __repr__(self):
        return self.__str__()