FROM cockroachdb/cockroach:v19.1.1

#RUN rm -f /etc/apt/sources.list
#RUN echo "deb http://archive.debian.org/debian/ jessie main" >> /etc/apt/sources.list
#RUN echo "deb-src http://archive.debian.org/debian/ jessie main" >> /etc/apt/sources.list
#RUN echo "deb http://security.debian.org jessie/updates main" >> /etc/apt/sources.list
#RUN echo "deb-src http://security.debian.org jessie/updates main" >> /etc/apt/sources.list

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl wget unzip python3-pip python3-setuptools && \
    apt-get clean

RUN pip3 install awscli --upgrade

RUN wget -O kubernetes-client-linux-amd64.tar.gz  https://dl.k8s.io/v1.12.6/kubernetes-client-linux-amd64.tar.gz && \
    tar xzvf kubernetes-client-linux-amd64.tar.gz -C /usr/local/bin --strip-components=3 && \
    rm kubernetes-client-linux-amd64.tar.gz

COPY generate-certs.sh /usr/local/bin/ 
RUN  chmod a+x /usr/local/bin/generate-certs.sh

WORKDIR /cockroach

ENTRYPOINT ["/bin/bash", "-ecx"] 

CMD ["/usr/local/bin/generate-certs.sh"]
