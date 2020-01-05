FROM       ubuntu:16.04
MAINTAINER Felix Kazyua

# Umgebungsvariablen
ENV TERM xterm
ENV DEBIAN_FRONTEND noninteractive

#Date of Build
RUN echo "Built at" $(date) > /etc/built_at

# Portfreigaben

# Dateien reinkopieren

# Anwendungen
RUN apt-get update
RUN apt-get -yq install -y --no-install-recommends software-properties-common 
RUN apt-add-repository ppa:ansible/ansible
RUN apt-get update
RUN apt-get -yq upgrade #Pfui, macht man nicht, aber ich will alles aktuell haben
RUN apt-get -yq install -y --no-install-recommends python-yaml python-jinja2 python-httplib2 python-keyczar python-paramiko python-setuptools python-pkg-resources git python-pip htop tree nano vim wget curl supervisor perl ttf-dejavu procps openssl xmlstarlet gzip


# Startbefehl
# Combining ENTRYPOINT and CMD allows you to specify the default executable for your image while also providing default arguments to that executable which may be overridden by the user.
# When both an ENTRYPOINT and CMD are specified, the CMD string(s) will be appended to the ENTRYPOINT in order to generate the container's command string. Remember that the CMD value can be easily overridden by supplying one or more arguments to `docker run` after the name of the image.
# Entrypoint explizit override needed
# Entrypoint needs new value for each argument ["/bin/ping","-c","4"]
# CMD Overwrite by arguments after run (same as Entrypoint ["localhost"])
CMD [ "cat", "/etc/built_at" ]
