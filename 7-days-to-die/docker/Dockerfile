FROM dgs.scurry.io/base:latest

RUN /usr/games/steamcmd +force_install_dir /srv/7-days-to-die +login anonymous +app_update 294420 +quit
COPY ./start.sh /srv/7-days-to-die/start.sh
COPY ./docker.xml /srv/7-days-to-die/docker.xml

CMD ["/srv/7-days-to-die/start.sh"]
