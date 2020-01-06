FROM jenda1/testovadlo

#
# Initialization
#
RUN pip3 install dateparser
ADD https://github.com/jplag/jplag/releases/download/v2.11.9-SNAPSHOT/jplag-2.11.9-SNAPSHOT-jar-with-dependencies.jar /lib/jplag.jar

RUN mkdir -p /output
COPY tasks/* /tasks/


#
# Tests
#
RUN ln -s /tasks/unpack /test.d/01-unpack_arg0; \
	ln -s /tasks/compile /test.d/10-compile; \
	ln -s /tasks/checkstyle /test.d/11-checkstyle; \
	ln -s /tasks/history /test.d/19-history; \
	ln -s /tasks/jplag /test.d/20-jplag; \
	ln -s /tasks/test_main /test.d/40-test_main; \
	ln -s /tasks/jarfile /test.d/41-jarfile

COPY test /test.d/50-test

