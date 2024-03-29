#!/usr/bin/env python3

import subprocess
import sys

from dgs.game.config import Config, String, Integer

class ValheimConfig(Config):
  name = String("NAME", default="Valheim Server", description="The name of the server")
  port = Integer("PORT", default=2456, description="The port the server will listen on")
  world = String("WORLD", default="MyWorld", description="The name of the world")
  password = String("PASSWORD", default="not-yo-cheese", description="The password for the server")
  public = Integer("PUBLIC", default=1, description="Whether the server is public (1) or not (0)")
  savedir = String("SAVE_DIR", description="The directory to save the world to")
  logFile = String("LOG_FILE", description="The file to log to")

  def generate_command(self):
    server_cmd = "./valheim_server.x86_64"
    for attr, value in self.read().items():
      if value is not None:
        server_cmd += f" -{attr.lower()} "

        if isinstance(value, int):
          server_cmd += str(value)
        else:
          server_cmd += '"' + str(value) + '"'
    
    return ["bash", "-c", server_cmd]

if __name__ == "__main__":
  config = ValheimConfig()
  command = config.generate_command()
  print("Running", command)
  subprocess.run(command,
                 env={
                   'LD_LIBRARY_PATH': './linux64',
                 },
               stdout=sys.stdout,
               stderr=sys.stderr,
               )