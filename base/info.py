from dgs.game.docgen import ConfigClass, generate_docs, Info, DockerInfo

info = Info("Base", config_classes=[
  ],
  docker=DockerInfo("dgs.scurry.io/base", "latest"),
  )