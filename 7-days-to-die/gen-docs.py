import importlib.util

start_spec = importlib.util.spec_from_file_location("start", "docker/start.py")
start = importlib.util.module_from_spec(start_spec)
start_spec.loader.exec_module(start)

game_config = start.SevenDaysToDieConfig()

with open("config.md", "w") as f:
  f.write("# 7 Days To Die Server Configuration\n")
  f.write("## Environment Variables\n")

  f.write("| Environment Variable | Config Option | Type | Description | Default |\n")
  f.write("| --- | --- | --- | --- | --- |\n")

  for var_doc in game_config.variable_docs():
    f.write(f"| {var_doc.env_var} | {var_doc.config_option} | {var_doc.type_name} | {var_doc.description} | {var_doc.default} |\n")