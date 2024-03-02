#!/usr/bin/env python3

import subprocess
import sys

from dgs.game.config import Config, String, Integer

class ValheimConfig(Config):
  name = String("NAME", default="Valheim Server")
  port = Integer("PORT", default=2456)
  world = String("WORLD", default="MyWorld")
  password = String("PASSWORD")
  public = Integer("PUBLIC", default=1)
  savedir = String("SAVE_DIR")
  logFile = String("LOG_FILE")

  def generate_command(self):
    command = ["bash", "-c", "./valheim_server.x86_64"]

    for attr, value in self.read().items():
      if value is not None:
        command.append(f"-{attr.lower()}")
        command.append(str(value))
    
    return command

print(ValheimConfig().generate_command())

config = ValheimConfig()

command = config.generate_command()

subprocess.run(command,
               stdout=sys.stdout,
               stderr=sys.stderr,
               )