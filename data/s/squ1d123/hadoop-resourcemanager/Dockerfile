FROM squ1d123/hadoop:2.8.4

RUN apt-get update \
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends  python3 \
&& rm -rf /var/lib/apt/lists/*

ENV PYSPARK_PYTHON=python3
ADD run.sh /run.sh
RUN chmod a+x /run.sh

CMD ["/run.sh"]
