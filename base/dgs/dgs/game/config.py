import abc
import os
import typing

class Variable(abc.ABC):
  def __init__(self, env_var: str, default: typing.Any = None):
    self.default = default
    self.env_var = env_var
  
  def _get_from_env(self) -> typing.Optional[str]:
    return os.environ.get(self.env_var)

  @abc.abstractmethod
  def get(self) -> typing.Optional[typing.Any]:
    return self._get_from_env()

class String(Variable):
  def get(self) -> typing.Optional[str]:
    env_value = self._get_from_env()

    if not env_value: 
      if self.default is not None:
        return self.default
      return None
    
    return env_value
  
class Integer(Variable):
  def get(self) -> typing.Optional[int]:
    env_value = self._get_from_env()

    if not env_value:
      if self.default is not None:
        return self.default
      return None
    
    return int(env_value)

class Boolean(Variable):
  def get(self) -> typing.Optional[bool]:
    env_value = self._get_from_env()

    if not env_value:
      if self.default is not None:
        return self.default
      return None
    
    return env_value.lower() == "true"

class Config:
  def __iter__(self):
    for attr_name in dir(self):
      attr = getattr(self, attr_name)

      if callable(attr):
        continue

      if isinstance(attr, Variable):
        yield attr_name, attr
      
    for attr, value in vars(self):
      if isinstance(value, Variable):
        yield attr, value
  
  def read(self):
    data = {}
    for attr, value in self.__iter__():
      data[attr] = value.get()
    
    return data
