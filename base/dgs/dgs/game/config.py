import abc
import os
import typing

from dataclasses import dataclass

@dataclass
class VariableDocs:
  env_var: str
  config_option: str
  type_name: str
  description: str
  default: str

class Variable(abc.ABC):
  type_name = "Variable"

  def __init__(self, env_var: str, default: typing.Any = None, description: str = ""):
    self.description = description
    self.default = default
    self.env_var = env_var
  
  def _get_from_env(self) -> typing.Optional[str]:
    return os.environ.get(self.env_var)

  @abc.abstractmethod
  def get(self) -> typing.Optional[typing.Any]:
    return self._get_from_env()

class String(Variable):
  type_name = "string"

  def get(self) -> typing.Optional[str]:
    env_value = self._get_from_env()

    if not env_value: 
      if self.default is not None:
        return self.default
      return None
    
    return env_value
  
class Integer(Variable):
  type_name = "integer"

  def get(self) -> typing.Optional[int]:
    env_value = self._get_from_env()

    if not env_value:
      if self.default is not None:
        return self.default
      return None
    
    return int(env_value)

class Boolean(Variable):
  type_name = "boolean"

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
  
  def variable_docs(self) -> typing.List[VariableDocs]:
    docs: typing.List[VariableDocs] = []

    for attr, value in self.__iter__():
      docs.append(VariableDocs(value.env_var, attr, value.type_name, value.description, str(value.default)))
    
    return docs
  
  def read(self):
    data = {}
    for attr, value in self.__iter__():
      data[attr] = value.get()
    
    return data
