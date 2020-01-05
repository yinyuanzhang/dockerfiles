FROM pshouse/squeak-base

RUN apt-get install -yq subversion

RUN groupadd -g 1234 openqwaq && useradd -g 1234 -G 1234 -u 1234 -c "OpenQwaq service user" -d /home/openqwaq -m -s /bin/bash openqwaq

USER openqwaq

WORKDIR /home/openqwaq

RUN svn co http://openqwaq.googlecode.com/svn/trunk/server && cp /home/openqwaq/server/conf/server.conf.in /home/openqwaq/server/conf/server.conf

ENV serverDir /home/openqwaq/server

CMD ${serverDir}/bin/forums/RunServer.sh ${serverDir}/conf/server.conf -vncPort: 5999 -startServiceProvider
