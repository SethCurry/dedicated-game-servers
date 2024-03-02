FROM dgs.scurry.io/base:latest

RUN /usr/games/steamcmd +force_install_dir /srv/7-days-to-die +login anonymous +app_update 294420 +quit
COPY ./start.py /srv/7-days-to-die/start.py

WORKDIR /srv/7-days-to-die

CMD ["/srv/7-days-to-die/start.py"]
