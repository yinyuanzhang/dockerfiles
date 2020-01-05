FROM ubuntu

RUN apt-get update && \
    apt-get install apg && \
    rm -rf /var/lib/apt/lists/*

CMD sh -c 'apg -n 20 -x 10 -M LCNs -t -E 0O1I\|'
