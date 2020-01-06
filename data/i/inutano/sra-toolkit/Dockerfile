FROM ubuntu:18.10
RUN apt-get update -y && apt-get install -y wget && \
    apt-get clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/* && \
    wget -P /usr/bin "https://raw.githubusercontent.com/inutano/pfastq-dump/master/bin/pfastq-dump" && \
    chmod +x /usr/bin/pfastq-dump && \
    wget -P / "http://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/2.9.2/sratoolkit.2.9.2-ubuntu64.tar.gz" && \
    tar zxf /sratoolkit.2.9.2-ubuntu64.tar.gz && \
    cp -r /sratoolkit.2.9.2-ubuntu64/bin/* /usr/bin && \
    rm -fr /sratoolkit.2.9.2-ubuntu64*
