class IntrinsicExpr:
    def __init__(self, intrinsic_op):
        self.intrinsic_op = intrinsic_op

class BinExpr:
    def __init__(self, op_name, ty, op1, op2):
        self.op_name = op_name
        self.ty = ty
        self.op1 = op1
        self.op2 = op2

class FnCallExpr:
    def __init__(self, fn_id, args, rets):
        self.fn_id = fn_id
        self.args = args
        self.rets = rets

class FFICallExpr:
    def __init__(self, fn_id, args, rets):
        self.fn_id = fn_id
        self.args = args
        self.rets = rets
