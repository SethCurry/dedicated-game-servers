import abc
import os

class Variable(abc.ABC):
  def __init__(self, env_var: str):
    self.env_var = env_var
  
  def __get_from_env(self) -> str:
    return os.environ.get(self.env_var)
  
  @abc.abstractmethod
  def get(self) -> str:
    return self.__get_from_env()

class String(Variable):
  def __init__(self, env_var: str):
    super().__init__(self, env_var)
  
  def get(self) -> str:
    return self.__get_from_env()

class Config:
  def __init__(self):
    return
  
  def __iter__(self):
    for attr, value in self.__dict__.iteritems():
      if isinstance(value, Variable):
        yield attr, value
  
  def read(self):
    obj = object()
    for attr, value in self:
      setattr(obj, attr, value.get())
    
    return obj
