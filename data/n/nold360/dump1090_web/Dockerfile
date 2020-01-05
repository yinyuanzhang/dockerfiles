FROM nginx

RUN apt-get update && \
    apt-get install -y --no-install-recommends git ca-certificates && \
	git clone --depth=1 https://github.com/mutability/dump1090 /app && \
	apt-get purge -y git ca-certificates && \
	apt-get autoremove -y --purge && apt-get clean && \
	rm -rf /var/lib/apt/lists/*

COPY nginx-default.conf /etc/nginx/conf.d/default.conf
