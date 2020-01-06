FROM fobbyal/wnameless-oracle-xe-11g
RUN apt-get update && apt-get install -y tzdata
ADD init/init.sh /
RUN mkdir /init
WORKDIR /init/
RUN chmod +x /init.sh
