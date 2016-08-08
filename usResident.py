class Person(object):
    def __init__(self, name):
        self.name = name
        try:
            firstBlank = name.rindex(' ')
            self.lastName = name[firstBlank+1:]
        except:
            self.lastName = name
        self.age = None
    def getLastName(self):
        return self.lastName
    def setAge(self, age):
        self.age = age
    def getAge(self):
        if self.age == None:
            raise ValueError
        return self.age
    def __lt__(self, other):
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    def __str__(self):
        return self.name
        
class USResident(Person):

    def __init__(self, name, status):

        Person.__init__(self, name)
        if status in ["citizen", "legal_resident", "illegal_resident"]:
            self.status = status
        else:
            raise ValueError
        
    def getStatus(self):

        return self.status
