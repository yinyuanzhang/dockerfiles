FROM perl:5.30

WORKDIR /
RUN git clone https://github.com/OpenKore/openkore.git

WORKDIR /openkore
RUN 	sed -i 's\master\master International - iRO: Ymir/Yggdrasil/Valkyrie\g' control/config.txt && \
	sed -i 's\server\server 0\g' control/config.txt && \
	./openkore.pl --no-connect

COPY entrypoint.sh /
RUN chmod +x -v /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]