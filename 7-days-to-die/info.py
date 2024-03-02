from dgs.game.docgen import ConfigClass, generate_docs, Info, DockerInfo

info = Info("7 Days to Die", config_classes=[
    ConfigClass("start", "docker/start.py", "SevenDaysToDieConfig"),
  ],
  docker=DockerInfo("dgs.scurry.io/7-days-to-die", "latest"),
)