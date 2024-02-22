class TypedList(list):
    def __init__(self, example_element, initial_list):
        self.type = type(example_element)
        if not isinstance(initial_list, list):
            raise TypeError("Second argument of TypesList must be a list.")
        for element in initial_list:
            self.__check(element)
        super().__init__(initial_list)

    def __check(self, element):
        if type(element) != self.type:
            raise TypeError("Attempted to add an element of incorrect type to a TypesList.")
        
    def __setitem__(self, i, element):
        self.__check(element)
        super().__setitem__(i, element)

    def __getitem__(self, i):
        return super().__getitem__(i)
    
x = TypedList("exampleType", ["some", "original"])    
y = TypedList("", [""] * 5)
print(x + y)
