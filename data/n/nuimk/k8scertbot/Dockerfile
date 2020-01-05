FROM certbot/certbot

COPY letsencrypt-* /usr/local/bin/

ENTRYPOINT []
WORKDIR /root
CMD ["python", "-m", "SimpleHTTPServer", "80"]
