class InvalidDepositError(BaseException):
    def __init__(self,msg):
        self.msg = msg

class InvalidWithdrawError(Exception):
    def __init__(self,msg):
        self.msg = msg

class InSuffAmtError(BaseException): pass

class LimitExceed(BaseException):
    def __init__(self,msg):
        self.msg = msg