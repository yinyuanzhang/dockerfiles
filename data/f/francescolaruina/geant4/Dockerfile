FROM 	fedora as builder
RUN 	dnf install -y cmake gcc make g++ expat-devel
RUN	mkdir -p /opt/geant4/{src,build} && \
	curl http://geant4-data.web.cern.ch/geant4-data/releases/geant4.10.05.p01.tar.gz | tar xz -C /opt/geant4/src --strip 1
WORKDIR /opt/geant4/build
RUN 	cmake -DCMAKE_INSTALL_PREFIX=/opt/geant4/install -DGEANT4_BUILD_MULTITHREADED=ON /opt/geant4/src && \
	make -j $(nproc) && \
	make install

FROM 	fedora
RUN 	dnf install -y cmake gcc make g++ expat-devel && dnf clean all 
COPY	--from=builder /opt/geant4/install /opt/geant4/install
COPY 	entrypoint.sh /entrypoint.sh
WORKDIR /data
ENTRYPOINT ["/entrypoint.sh"]
CMD ["/bin/bash"]
