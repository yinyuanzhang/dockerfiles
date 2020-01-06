FROM ubuntu:18.04

RUN apt-get update && apt-get install -y curl

# Use uid 100 for hive user
RUN usermod -u 103 _apt
RUN groupadd -r -g 65533 hive 
RUN useradd -r -u 100 -g 65533 hive

USER hive

ADD entrypoint.sh /bin/entrypoint.sh

ENTRYPOINT ["/bin/entrypoint.sh"]
