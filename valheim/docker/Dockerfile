FROM dgs.scurry.io/base:latest

RUN /usr/games/steamcmd +force_install_dir /srv/valheim +login anonymous +app_update 896660 +quit
COPY ./start.py /srv/valheim/start.py

WORKDIR /srv/valheim

CMD ["/srv/valheim/start.py"]
