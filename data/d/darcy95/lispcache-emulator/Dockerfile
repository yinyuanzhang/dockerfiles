FROM perl:5
WORKDIR /usr/src/lisp
VOLUME logs
COPY LICENSE /usr/src/lisp/
COPY lispcache-emulator.pl /usr/src/lisp/
COPY lisp-database /usr/src/lisp/
COPY README /usr/src/lisp/
COPY bootstrap-data.sh /usr/src/lisp/
COPY xTR.sh /usr/src/lisp/
RUN ["cpanm", "Socket6"]
RUN ["cpanm", "Net::Patricia"]
RUN ["git", "clone", "https://github.com/kohler/ipsumdump.git"]
WORKDIR /usr/src/lisp/ipsumdump
RUN ["./bootstrap.sh"]
RUN ["./configure"]
RUN ["make"]
RUN ["make", "install"]
WORKDIR /usr/src/lisp
