import random
# TODO: Import the virus clase
import uuid
from randomUser import Create_user
import pdb

'''
    Person objects will populate the simulation.

    _____Attributes______:

    _id: Int.  A unique ID assigned to each person.

    is_vaccinated: Bool.  Determines whether the person object is vaccinated against
        the disease in the simulation.

    is_alive: Bool. All person objects begin alive (value set to true).  Changed
        to false if person object dies from an infection.

    infection:  None/Virus object.  Set to None for people that are not infected.
        If a person is infected, will instead be set to the virus object the person
        is infected with.

    _____Methods_____:

    __init__(self, _id, is_vaccinated, infected=False):
        - self.alive should be automatically set to true during instantiation.
        - all other attributes for self should be set to their corresponding parameter
            passed during instantiation.
        - If person is chosen to be infected for first round of simulation, then
            the object should create a Virus object and set it as the value for
            self.infection.  Otherwise, self.infection should be set to None.

    did_survive_infection(self):
        - Only called if infection attribute is not None.
        - Takes no inputs.
        - Generates a random number between 0 and 1.
        - Compares random number to mortality_rate attribute stored in person's infection
            attribute.
            - If random number is smaller, person has died from disease.
                is_alive is changed to false.
            - If random number is larger, person has survived disease.  Person's
            is_vaccinated attribute is changed to True, and set self.infected to None.
    '''
class Person(object):
    def __init__(self, is_vaccinated=False, infected=False, virus = None):
        # TODO:  Finish this method.  Follow the instructions in the class documentation
        # to set the corret values for the following attributes.
        self._id = uuid.uuid4().hex[:10]
        self.is_vaccinated = is_vaccinated
        self.is_alive = True
        self.survive = False
        self.infected = infected #virus type object
        self.virus = virus
        self.interacted = False
        user_obj = Create_user()
        user = user_obj.create()
        self.name = ('%s %s' %(user.first_name,user.last_name))
        #pdb.set_trace()


    def did_survive_infection(self):
        # TODO:  Finish this method. Follow the instructions in the class documentation
        # for resolve_infection.  If person dies, set is_alive to False and return False.
        # If person lives, set is_vaccinated = True, infected = None, return True.
        if self.infected is not None:
            chance_to_survive =  random.uniform(0.0,1.0)
            if chance_to_survive > self.virus.mortality_rate:
                self.is_alive = True
                self.is_vaccinated = True
                self.infected = False
                return True
            else:
                self.is_alive = False
                self.infected = False
                return False
        pass

    #def resolve_infection():

        #chance_to_survice
