from dgs.game.docgen import ConfigClass, generate_docs

with open("README.md", "w") as f:
  docs = generate_docs("Valheim Server", [
    ConfigClass("start", "docker/start.py", "ValheimConfig"),
  ])

  f.write(docs)
