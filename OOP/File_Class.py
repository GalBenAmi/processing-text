import string
import os

class FileP:
    def __init__(self, file_path, actions,file_output_path=None):
        self._path = file_path
        self._actions = actions
        self._output_path=file_output_path
        self._name = None
        self._type = None
        self._def_name = None
        self._processed = None
        
        self.initialize() 
    def initialize(self):
        process_file_path(self)
        defult_filename(self)  
    # Getter for _path
    def get_path(self):
        return self._path
    # Getter and setter for actions
    def get_actions(self):
        return self._actions
    def set_actions(self, value):
        self._actions = value
        # Getter and setter for output_path
    def get__output_path(self):
        return self._output_path
    def set_output_path(self, value):
        self._output_path = value
    
    # Getter and setter for name
    def get_name(self):
        return self._name
    def set_name(self, value):
        self._name = value
    # Getter and setter for type
    def get_type(self):
        return self._type
    def set_type(self, value):
        self._type = value
    # Getter and setter for def_name
    def get_def_name(self):
        return self._def_name
    def set_def_name(self, value):
        self._def_name = value
    # Getter and setter for processed
    def get_processed(self):
        return self._processed
    def set_processed(self, value):
        self._processed = value
    
    
    # Define properties to access attributes using getters and setters
    _path = property(get_path)
    _actions = property(get_actions, set_actions)
    _name = property(get_name, set_name)
    _type = property(get_type, set_type)
    _def_name = property(get_def_name, set_def_name)
    _processed = property(get_processed, set_processed)


## DO I WANT TO GET ACTIONS ASS WELL ?
    ## MAYBE I CAN MAKE IT MORE MOUDULAR BY VERSIONS
#setting _def_name : name='example' actions[t,t,t,t,t] -> get_def_name='example_Reversed_Filterd by-+( suffix[action[i]=t])
def defult_filename(file:FileP):
    name=file.get_name()+"_Filterd by-"
    suffix={0:"Reversed",1:"HebrewChar",2:"EnglishChar",3:"Common",4:"Custom"}
    arr=file.get_actions
    for t in [i for i, x in enumerate(arr) if x]:
        if(t==0):
            name=file.get_name()+"_"+suffix[t]+"_Filterd by-"
            continue
        name+=f" {suffix[t]}"
    file.set_def_name= name

#setting _name and _type and _def_name from _path path: C:\Users\YourUsername\Documents\example.txt -> file.get_name='example' file.get_type='txt' 
def process_file_path(file:FileP):
    result=os.path.splitext(os.path.basename(file.get_path()))
    file.set_name(result[0])
    file.set_type(result[1]) 

        
