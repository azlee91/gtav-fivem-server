#!/bin/bash
docker run -dit --rm --name gta5_server -p 30120:30120/tcp -p 30120:30120/udp -v /srv/gta_server_files:/gtaV_server gta5server:latest
