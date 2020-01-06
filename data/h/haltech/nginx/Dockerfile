FROM nginx:1.17.6-alpine

LABEL maintainer="HAL Tech <support@haltech.io>"

# Add config files
ADD config/default.conf /etc/nginx/conf.d/default.conf

# Simlink logs to standard out and standard error
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

ENV PORT 80
EXPOSE 80

# Run nginx
CMD ["nginx", "-g", "daemon off;"]
