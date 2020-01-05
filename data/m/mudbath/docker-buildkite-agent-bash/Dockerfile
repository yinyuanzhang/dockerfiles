FROM buildkite/agent:3.0

RUN apk --no-cache add gawk sed grep bc coreutils \
	groff less python && \
	mkdir -p /aws && \
	pip install awscli
