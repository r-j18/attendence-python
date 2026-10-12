

class Subject:
    def __init__(self, name, present = 0, absent = 0):
        if(not isinstance(absent, int) or not isinstance(present, int)):
            raise TypeError("Enter an integer >= 0")
        if(not isinstance(name, str)):
            raise TypeError("Enter a valid name")       
        if(present <0 or absent <0):
            raise ValueError("Must be positive")
        if(name.strip() == ""):
            raise ValueError("Enter a name")
        self.name = name
        self.present = present
        self.absent = absent
    
    def mark_present(self):
        self.present += 1

    def mark_absent(self):
        self.absent += 1

    def percentage(self):
        if(self.present + self.absent <= 0):
            return 0
        return((self.present/ (self.present + self.absent) * 100))

