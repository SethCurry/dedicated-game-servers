from dgs.game.docgen import ConfigClass, generate_docs, Info, DockerInfo

info = Info("Valheim", config_classes=[
    ConfigClass("start", "docker/start.py", "ValheimConfig"),
  ],
  docker=DockerInfo("dgs.scurry.io/valheim", "latest"),
  )