

""" The virus detail will be prompts to enter manualy

                _____Attributes______

mortality_rate: death mortality
"""
class Virus(object):
    def __init__(self,name,mortality_rate,contagious_rate):
        self.mortality_rate = mortality_rate
        self.name = name
        self.contagious_rate = contagious_rate
        pass
