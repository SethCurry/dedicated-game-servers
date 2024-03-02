FROM ubuntu:24.04

RUN apt-get update; apt-get install software-properties-common; add-apt-repository multiverse; dpkg --add-architecture i386; apt-get update; echo steam steam/question select "I AGREE" | debconf-set-selections && echo steam steam/license note '' | debconf-set-selections
RUN apt-get install -y steamcmd ca-certificates language-pack-en python3

COPY dgs /opt/dgs

RUN curl -sSL https://install.python-poetry.org | python3 -
RUN cd /opt/dgs; poetry install; poetry build; pip install dist/*.whl