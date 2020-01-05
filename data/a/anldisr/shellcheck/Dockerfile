FROM debian:buster-slim

LABEL maintainer "Rogier"

RUN apt-get update && apt-get install -y \
	file \
	--no-install-recommends \
	&& rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y \
    shellcheck \
	--no-install-recommends \
	&& rm -rf /var/lib/apt/lists/*

CMD ["shellcheck"]