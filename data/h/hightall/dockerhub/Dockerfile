FROM alpine/git as git

RUN cd /tmp && git clone https://github.com/HaitaoYue/dockerhub.git && \
	cd dockerhub && lastTag=$(git describe --tags `git rev-list --tags --max-count=1`) && \
	echo $lastTag && git checkout -b $lastTag $lastTag

FROM ubuntu:16.04
COPY --from=git /tmp/dockerhub /tmp/
