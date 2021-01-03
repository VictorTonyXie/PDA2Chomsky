class CFG:
    variables: list[str] = []
    terminals: list[str] = []
    start_variable: str
    production_rules: dict[str, list[list[str]]] = {}

    def __init__(self, variables: list[str], terminals: list[str], start_variable):
        self.variables = variables.copy()
        self.terminals = terminals.copy()
        self.start_variable = start_variable
        for v in self.variables:
            self.production_rules[v] = []

    def isTerminal(self, ident: str):
        return ident in self.terminals

    def isNonTerminal(self, ident: str):
        return ident in self.variables

    def addRule(self, left: str, right: list[str]):
        self.production_rules[left].append(right.copy())

    def __str__(self, epsilon="ε"):
        ret = "\n".join([f"{nont} -> {' | '.join([' '.join(single_rule) if len(single_rule) > 0 else epsilon for single_rule in self.production_rules[nont]])}" for nont in self.production_rules])
        return ret


if __name__ == "__main__":
    cfg = CFG(["S", "A", "B", "C"], ["a", "b"], "S")
    cfg.addRule("S", ["A", "a", "B"])
    cfg.addRule("A", ["a", "A"])
    cfg.addRule("A", [])
    cfg.addRule("B", ["b", "B"])
    cfg.addRule("B", [])
    print(cfg)
