FROM centos:7
LABEL maintainer "Chen Di <di.chen16@outlook.com>"

RUN yum -y groupinstall "Development Tools"
RUN yum -y install unixODBC unixODBC-devel wxBase wxGTK SDL wxGTK-gl
RUN yum -y install gcc glibc-devel make ncurses-devel openssl-devel xmlto perl wget

WORKDIR /app

RUN wget https://pocoproject.org/releases/poco-1.9.2/poco-1.9.2-all.tar.gz && \
		tar xvf poco-1.9.2-all.tar.gz && \
        cd poco-1.9.2-all/ && \
        ./configure --omit=Data/ODBC,Data/MySQL && \
        make && make install && \
        cd ../ && rm -rf poco-1.9.2-all/ && \
	rm -rf  poco-1.9.2-all.tar.gz
