import os

from dgs.game.docgen import ConfigClass, generate_docs, Info, dynamic_import

games = []
for entry in os.listdir('.'):
    if os.path.isdir(entry):
      if os.path.exists(f'{entry}/info.py'):
        games.append(entry)

for game in games:
  print("Building docs for", game)
  info = dynamic_import("info", f'{game}/info.py').info

  docs = generate_docs(game, info)

  with open(f"{game}/README.md", "w") as f:
    f.write(docs)