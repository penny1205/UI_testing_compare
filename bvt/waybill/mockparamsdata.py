class MockParamsData(object):

    @classmethod
    def generate(cls,type1):
        if type1 == 1:
            return ['123456','123456','123456']
        else:
            return ['456789','456789','456789']