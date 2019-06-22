import copy

# Setting class object, wasn't working without "(object)"
class School:
    
# Initializing name and roster method
    def __init__(self, name): 
        self.name = name
        self._roster = {}

# Setting roster method
    def roster(self):
        return self._roster

# Adding student including name and grade method
    def add_student(self, name, grade):
        if grade in self._roster:
            self._roster[grade].append(name)  
        else: 
            self._roster[grade] = [name]
        return self._roster

#Grade method
    def grade(self,grade):
        return self._roster[grade]

#Sorting roster method
    def sort_roster(self):
        new_dict = copy.deepcopy(self._roster)
       
        for key in new_dict:
            new_dict[key].sort()
            
        return new_dict
        
    
        