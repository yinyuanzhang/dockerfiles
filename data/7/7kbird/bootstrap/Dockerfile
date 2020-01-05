FROM nginx:1.9

ENV BOOTSTRAP_VERSION 3.3.6
ENV BOOTSTRAP_MD5 229936b042baadfc9f167244575ffe12

RUN build_deps='curl unzip' \
	&& apt-get update && apt-get install -y ${build_deps} --no-install-recommends \
	&& curl -SL "https://github.com/twbs/bootstrap/releases/download/v${BOOTSTRAP_VERSION}/bootstrap-${BOOTSTRAP_VERSION}-dist.zip" -o bootstrap.zip \
	&& echo "${BOOTSTRAP_MD5} bootstrap.zip" | md5sum -c \
	&& temp=$(mktemp -d) && unzip -d "$temp" "bootstrap.zip" \
	&& dest='/usr/share/nginx/html/bootstrap' && mkdir -p "$dest" && mv "$temp"/*/* "$dest" \
	&& rmdir "$temp"/* "$temp" && rm bootstrap.zip \
	&& apt-get purge -y --auto-remove $buildDep && rm -rf /var/lib/apt/lists/*
