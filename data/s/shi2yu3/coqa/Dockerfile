FROM msranni/nni

# install fuser-dfs

RUN wget --quiet http://archive.cloudera.com/cdh5/one-click-install/trusty/amd64/cdh5-repository_1.0_all.deb && \
    dpkg -i cdh5-repository_1.0_all.deb

#ENV KERNEL=4.15.0-1031-azure
ENV KERNEL=4.15.0-*-azure

RUN apt-get update \
    && apt-get install -y --allow-unauthenticated \
       module-init-tools \
       linux-image-$KERNEL \
       default-jre \
       hadoop-hdfs-fuse \
    && rm -rf /var/lib/apt/lists/*

RUN ln -s /usr/lib/jvm/java-8-openjdk-amd64/jre/lib/amd64/server/libjvm.so /lib/libjvm.so

# mount hdfs

#RUN mkdir -p hdfs && \
#    hadoop-fuse-dfs dfs://10.0.0.4:9000 hdfs

# install python packages

RUN pip install hdfs boto3 tqdm memory_profiler

#WORKDIR /root
