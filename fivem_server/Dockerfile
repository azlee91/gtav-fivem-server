FROM ubuntu:latest

EXPOSE 30120

RUN apt update \
    && apt upgrade -y \
    && apt install -y xz-utils vim

ADD . /gtaV_server

# Extract server files
WORKDIR /gtaV_server
RUN tar xf fx.tar.xz \
    && chmod 777 run_server.sh \
    && mv server.cfg vendor/server-data \
    && mkdir -p vendor/server-data/resources/\[local\] \
    && mv local_resources/* vendor/server-data/resources/\[local\]

CMD  /gtaV_server/run_server.sh
