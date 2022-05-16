FROM ubuntu:latest

EXPOSE 30120

RUN useradd -u 1000 fivem

RUN apt update \
    && apt upgrade -y \
    && apt install -y xz-utils vim


ADD . /home/fivem/gtaV_server
WORKDIR /home/fivem/gtaV_server
RUN chown -R 1000:1000 /home/fivem
USER 1000

# Extract server files
RUN tar xvf fx.tar.xz \
    && chmod 777 run_server.sh \
    && mv server.cfg vendor/server-data \
    && mkdir -p vendor/server-data/resources/\[local\] \
    && mv local_resources/* vendor/server-data/resources/\[local\]

CMD  /home/fivem/gtaV_server/run_server.sh
