from dgs.game.docgen import ConfigClass, generate_docs

with open("README.md", "w") as f:
  docs = generate_docs("7 Days To Die Server", [
    ConfigClass("start", "docker/start.py", "SevenDaysToDieConfig"),
  ])

  f.write(docs)
