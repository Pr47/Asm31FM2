class AssignInsc:
    def __init__(self, assignee, expr):
        self.assignee = assignee
        self.expr = expr

class GotoInsc:
    def __init__(self, dest):
        self.dest = dest

class IfGotoInsc:
    def __init__(self, condition, dest):
        self.condition = condition
        self.dest = dest

class RetInsc:
    def __init__(self, ret_items):
        self.ret_items = ret_items

class RaiseInsc:
    def __init__(self, raise_item):
        self.raise_item = raise_item
