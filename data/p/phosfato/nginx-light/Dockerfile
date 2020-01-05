FROM ubuntu

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update -yq && \
    apt-get upgrade -yq &&  \
    apt-get install -yq nginx-light && \
    # remove files left by `apt-get update`
    rm -rf /var/lib/apt/lists/* && \
    # nginx-light uses these files as output, redirect them to stdout/stderr
    ln -sf /dev/stdout /var/log/nginx/access.log && \
    ln -sf /dev/stderr /var/log/nginx/error.log

COPY ./nginx.conf /etc/nginx/nginx.conf

# The nginx-light documentation says to use SIGQUIT for a "graceful shutdown"
# but there's a bug in the way that SIGQUIT is handled by nginx-light so use
# SIGTERM intead.
#
# References:
# - http://nginx.org/en/docs/control.html
# - https://github.com/nginxinc/docker-nginx/issues/167
# - https://trac.nginx.org/nginx/ticket/753
#
# The default STOPSIGNAL used by Docker is already SIGTERM but we will keep
# this directive in as a reminder, if the nginx-light situation changes back to
# SIGQUIT we have to update this.
STOPSIGNAL SIGTERM

EXPOSE 80

CMD ["nginx"]