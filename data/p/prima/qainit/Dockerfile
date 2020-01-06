FROM prima/ruby:2.4.3-9

RUN apt-get update && \
	apt-get install -qqy cmake rsync locales && \
	apt-get install -qqy git curl tar gzip wget zip && \
	gem install prima-twig && \
	echo "LC_ALL=en_US.UTF-8" >> /etc/environment && \
	echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \
	echo "LANG=en_US.UTF-8" > /etc/locale.conf && \
	locale-gen en_US.UTF-8

ENV PYTHONUNBUFFERED=1 \
    DOCKER_API_VERSION=1.27 \
    TZ=:/etc/localtime

RUN pip install --upgrade awscli docker==2.6.1 pyyaml 'docker-compose==1.15.0' && \
    curl -L "https://get.docker.com/builds/Linux/x86_64/docker-17.03.1-ce.tgz" -o /opt/docker-17.03.1-ce.tgz && \
    cd /opt && tar xzvf docker-17.03.1-ce.tgz && \
    chmod +x docker/* && \
    mv docker/* /usr/bin/ && \
    rm -rf /opt/docker*

COPY files/twig_setup.sh /usr/bin/twig_setup
COPY files/prepare-docker-compose.py /usr/bin/prepare-docker-compose
COPY files/qainit-to-s3.py /usr/bin/qainit-to-s3
COPY files/qainit-from-s3.py /usr/bin/qainit-from-s3

RUN chmod 755 /usr/bin/twig_setup && \
	chmod 755 /usr/bin/prepare-docker-compose && \
	chmod 755 /usr/bin/qainit-to-s3 && \
	chmod 755 /usr/bin/qainit-from-s3

ENTRYPOINT ["/bin/bash"]
