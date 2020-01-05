FROM mono:latest
ARG source
WORKDIR ./
COPY ${source:-bin} .
ENTRYPOINT ["mono", "Host.exe", "./projects/kicking-the-mic-2019.xml"]
# ENTRYPOINT ["mono", "Host.exe", "kicking-the-mic-2019.xml", "-v", "Emphasized"]
