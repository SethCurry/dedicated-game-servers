import importlib.util
import typing

from dataclasses import dataclass

def __dynamic_import(module_name: str, path: str):
  spec = importlib.util.spec_from_file_location(module_name, path)
  module = importlib.util.module_from_spec(spec)
  spec.loader.exec_module(module)
  return module

@dataclass
class ConfigClass:
  module_name: str
  path: str
  class_name: str

def __generate_config_docs(config_classes: typing.List[ConfigClass]):
  docs = "## Configuration\n"
  docs += "### Environment Variables\n"
  docs += "| Environment Variable | Config Option | Type | Description | Default |\n"
  docs += "| --- | --- | --- | --- | --- |\n"

  for config_class in config_classes:
    module = __dynamic_import(config_class.module_name, config_class.path)

    cfgcls = getattr(module, config_class.class_name)

    inst = cfgcls()

    for var_doc in inst.variable_docs():
      docs += f"| {var_doc.env_var} | {var_doc.config_option} | {var_doc.type_name} | {var_doc.description} | {var_doc.default} |\n"
  return docs

def generate_docs(game_name: str, config_classes: typing.List[ConfigClass] = list()) -> str:
  docs = f"# {game_name} Server Configuration\n"

  docs += __generate_config_docs(config_classes)

  return docs