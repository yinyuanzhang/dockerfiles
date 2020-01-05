FROM nginx:1.10.1-alpine

COPY build/ /usr/share/nginx/html/

# Override the nginx start from the base container
COPY start.sh /start.sh
RUN chmod +x /start.sh

# Expose the app port
EXPOSE 80

ENTRYPOINT ["/start.sh"]


