FROM node:slim
			
# install packages
RUN apt-get update -y && \
    apt-get install --no-install-recommends -y \
                nano \
		wget \
		unzip \
		procps \
		libpython2.7 \
		net-tools \
		python-apsw \
		python-lxml \
		python-m2crypto \
		python-pkg-resources && \
# install proxy
wget -o - https://github.com/xelaok/acey/archive/master.zip -O aceproxy.zip && \
unzip aceproxy.zip -d /opt/ && \
rm -rf aceproxy.zip && \
cd /opt/acey-master/ && \
npm install -g npm && \
npm i && \
npm run dist && \

# install acestream
mkdir -p /opt/acestream && \
wget -o - http://acestream.org/downloads/linux/acestream_3.1.49_debian_9.9_x86_64.tar.gz && \
tar -zxvf acestream_3.1.49_debian_9.9_x86_64.tar.gz -C /opt/acestream && \

# clean up
apt-get clean && \
apt autoremove -y && \
rm --force --recursive /var/lib/apt/lists && \
rm -rf /tmp/* /opt/acestream/data/plugins/*

# add services
ADD channel-groups-map.yaml /opt/acey-master/config/channel-groups-map.yaml
ADD channel-groups.yaml /opt/acey-master/config/channel-groups.yaml
ADD main.yaml /opt/acey-master/config/main.yaml
ADD ace-hls7.yaml /opt/acey-master/config/playlists/ace-hls7.yaml
ADD ace.yaml /opt/acey-master/config/channel-sources/ace.yaml
COPY root/ /
RUN chmod +x /opt/start.sh
