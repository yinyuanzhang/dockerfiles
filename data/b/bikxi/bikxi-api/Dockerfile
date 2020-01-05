FROM ruby:2.5.0

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && \
	apt-get install -y nodejs && \
	apt-get clean

WORKDIR /build

CMD ["bash"]
