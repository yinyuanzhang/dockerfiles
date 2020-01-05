FROM mono

MAINTAINER Erich Ellsworth <kg5key@kg5key.com>

RUN apt update && apt install -y \
    python3 \
    git \
    wget

RUN wget https://raw.githubusercontent.com/Ellsworth/terraria-docker/master/tshock_server/tshock-download.py
RUN python3 tshock-download.py

WORKDIR /TShock

# run TShock
ENTRYPOINT ["mono", "--server", "--gc=sgen", "-O=all", "TerrariaServer.exe", "-configpath", "/terraria", "-worldpath", "/terraria", "-logpath", "/logs"]
