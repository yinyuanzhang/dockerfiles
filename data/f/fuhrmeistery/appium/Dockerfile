From beevelop/ionic:v4.1.2

LABEL maintainer="yannikfuhrmeister@web.de"

RUN apt-get update && \
    apt-get install -y python && \
    apt-get install -y build-essential && \
    apt-get install -y libglib2.0-dev && \
    apt-get install -y libnss3 && \
    apt-get clean && \
    npm i -g npm && \
    PATH=$PATH:$JAVA_HOME/bin
	
