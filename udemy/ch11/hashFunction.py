class Robot:
    def __init__(self, name, age, address):
        self.name=name
        self.age=age
        self.address=address
    
    # define a private function
    def __key(self):
        return (self.name, self.age, self.address)
 
    def __hash__(self):
        return hash(self.__key())
    
    def __eq__(self, other):
        if isinstance(other, Robot):
            return self.__key() == other.__key()
        return NotImplemented
    
    
 
robot = Robot("Wilson", 25, "Hawaii")
robot2 = Robot("Wilson", 25, "Hawaii")
robot3 = Robot("Duncan", 30, "Hawaii")
dictionary = {robot: "W robot"}
print(dictionary[robot]) #return W robot
print(robot == robot2)