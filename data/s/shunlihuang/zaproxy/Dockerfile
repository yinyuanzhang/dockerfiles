FROM owasp/zap2docker-stable
LABEL maintainer="shunli.huang.wistron@gmail.com"

USER root

RUN apt-get update && apt-get install -q -y --fix-missing \
	jq \
	python3-csvkit \
	vim
RUN pip install csvkit
#RUN pip3 install csvkit
RUN apt-get clean && \
	rm -rf /var/lib/apt/lists/*

#RUN rm -rf /var/lib/dpkg/lock && rm -rf /var/cache/apt/archives/lock && /var/lib/apt/lists/lock && apt-get update && apt-get upgrade -Y
WORKDIR /zap

#Change to the zap user so things get done as the right person (apart from copy)
USER zap
