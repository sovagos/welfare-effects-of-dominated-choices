class Program:
    """A class representing a program."""
    def __init__(self, program_id, contracts = []):
        self.program_id = program_id
        self.contracts = contracts[:]
        self.state_funded = None
        self.self_funded = None

        for c in contracts:
            if c.state_funded == 1:
                self.state_funded = c
            elif c.state_funded == 0:
                self.self_funded = c