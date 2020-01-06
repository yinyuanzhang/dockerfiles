FROM kinetica/kinetica-intel:latest

WORKDIR /usr/local/kinetica/

ENV LICENSE_KEY Empty

RUN yum install -y wget && \
    wget http://files.kinetica.com/zwu/rpm/jdk-8u192-linux-x64.rpm && \
    yum localinstall -y jdk-8u192-linux-x64.rpm && rm jdk-8u192-linux-x64.rpm &&  \
	echo '2' | update-alternatives --config java

COPY resources/gpudb.conf /opt/gpudb/core/etc/gpudb.conf 

EXPOSE 2003 4000-4019 5552 5553 6555-6575 8080 8081 8082 8088 8181 9001 9002 9191-9211 9292 9300

CMD ["/bin/sh","-c","chown gpudb:gpudb /opt/gpudb/core/etc/gpudb.conf && sed -i \"s|license_key =|license_key = ${LICENSE_KEY}|g\" /opt/gpudb/core/etc/gpudb.conf && ldconfig && /etc/init.d/gpudb_host_manager start && while /opt/gpudb/core/bin/gpudb host-manager-status >/dev/null 2>&1 ; do sleep 20; done"]
