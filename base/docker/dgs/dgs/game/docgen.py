import importlib.util
import typing

from dataclasses import dataclass

def dynamic_import(module_name: str, path: str):
  spec = importlib.util.spec_from_file_location(module_name, path)
  module = importlib.util.module_from_spec(spec)
  spec.loader.exec_module(module)
  return module

@dataclass
class ConfigClass:
  module_name: str
  path: str
  class_name: str

@dataclass
class DockerInfo:
  image: str
  tag: str

@dataclass
class Info:
  name: str
  docker: DockerInfo
  config_classes: typing.List[ConfigClass]


def __generate_config_docs(path: str, info: Info) -> str:
  docs = "## Configuration\n"
  docs += "### Environment Variables\n"
  docs += "| Environment Variable | Config Option | Type | Description | Default |\n"
  docs += "| --- | --- | --- | --- | --- |\n"

  for config_class in info.config_classes:
    module = dynamic_import(config_class.module_name, path + "/"+config_class.path)

    cfgcls = getattr(module, config_class.class_name)

    inst = cfgcls()

    for var_doc in inst.variable_docs():
      docs += f"| {var_doc.env_var} | {var_doc.config_option} | {var_doc.type_name} | {var_doc.description} | {var_doc.default} |\n"
  return docs


def generate_docs(path: str, info: Info) -> str:
  docs = f"# {info.name} Configuration\n"

  docs += "## Building\n"

  docs += "First, you will need to build the base Docker image.  See the [README](../base/README.md) for instructions on how to do this.\n"
  docs += "\n"
  docs += "\n"
  docs += "Once you have done that, you can build the game server image with this command:\n"
  docs += "\n"
  docs += "```bash\n"
  docs += f"docker build -t {info.docker.image}:{info.docker.tag} .\n"
  docs += "```\n"

  docs += __generate_config_docs(path, info)

  return docs
