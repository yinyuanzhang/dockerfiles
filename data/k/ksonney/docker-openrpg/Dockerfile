# To use:
#	docker run -v /tmp/.X11-unix:/tmp/.X11-unix \
#		-e DISPLAY=unix$DISPLAY \
#		ksonney/docker-openrpg
#

FROM ubuntu:trusty
LABEL maintainer "Kevin Sonney <kevin@sonney.com>"

RUN apt-get update
RUN apt-get install -y python python-wxversion python-wxgtk2.8
RUN apt-get install -y wget unzip
RUN mkdir /openrpg
RUN cd /openrpg && wget http://www.assembla.com/spaces/openrpg/documents/download/OpenRPG1.8.0.zip && unzip OpenRPG1.8.0.zip
RUN chmod +x /openrpg/start_client.py
COPY orpg_windows_patched.py /openrpg/orpg/orpg_windows.py
WORKDIR /openrpg 
ENTRYPOINT ["/openrpg/start_client.py"]
