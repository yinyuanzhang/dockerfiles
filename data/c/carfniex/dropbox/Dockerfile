FROM debian:stretch
# thank you matt for doing basically all the work i am bad at computers
#MAINTAINER Matt Bentley <mbentley@mbentley.net>

# install prereqs
RUN (apt-get update &&\
  apt-get install -y jq libglib2.0-0 python wget git build-essential locales &&\
  rm -rf /var/lib/apt/lists/*)

# grab the fs fix and make it
RUN cd / \
  && git clone https://github.com/dark/dropbox-filesystem-fix.git \
  && cd /dropbox-filesystem-fix \
  && make \
  && cp -R /dropbox-filesystem-fix /opt/dropbox-filesystem-fix \
  && chmod +x /opt/dropbox-filesystem-fix/dropbox_start.py

# install dropbox
RUN (mkdir /opt/dropbox &&\
  cd /opt/dropbox &&\
  wget -O - "https://www.dropbox.com/download?plat=lnx.x86_64" | tar xzf -)


# install dropbox.py
RUN (wget -O /usr/local/bin/dropbox.py "https://www.dropbox.com/download?dl=packages/dropbox.py" &&\
  chmod +x /usr/local/bin/dropbox.py)

# install tini
RUN (TINI_VER="$(wget -q -O - https://api.github.com/repos/krallin/tini/releases/latest | jq -r .tag_name)" &&\
  wget "https://github.com/krallin/tini/releases/download/${TINI_VER}/tini-amd64" -O /tini &&\
  chmod +x /tini)

# install gosu
RUN (wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/1.10/gosu-amd64" &&\
  wget -O /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/1.10/gosu-amd64.asc" &&\
  chmod +x /usr/local/bin/gosu)

RUN locale-gen en_US.UTF-8
ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["start"]
