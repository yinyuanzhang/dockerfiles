FROM manorrock/debian
RUN apt update && \
    apt upgrade -y && \
    apt install -y curl gnupg2 ca-certificates lsb-release && \
    echo "deb http://nginx.org/packages/debian `lsb_release -cs` nginx" \
    | tee /etc/apt/sources.list.d/nginx.list && \
    curl -fsSL https://nginx.org/keys/nginx_signing.key | apt-key add - && \
    apt update && \
    apt install -y nginx && \
    rm -rf /var/lib/apt/lists/*
WORKDIR /mnt
CMD ["nginx", "-g", "daemon off;"]
