FROM nginx:alpine


#RUN apk update && \
RUN apk add --no-cache \
        git && \
    mkdir -p /usr/src && \
    cd /usr/src && \
    git clone https://github.com/jgraph/drawio.git && \
    rm -rf /usr/src/drawio/.git && \
    rm -rf /usr/share/nginx/html && \
    ln -s /usr/src/drawio/src/main/webapp /usr/share/nginx/html && \
    apk del git

# Starting nginx in foreground mode
CMD ["/usr/sbin/nginx", "-g", "daemon off;"]

# Expose the ports for nginx
EXPOSE 80
