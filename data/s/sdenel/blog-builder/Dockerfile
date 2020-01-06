# If you want to build this image by yourself, try: docker build . -t sdenel/blog-builder
FROM ubuntu:latest
ENV PYTHONIOENCODING=utf-8
COPY setup.sh /opt/setup.sh
RUN chmod +x /opt/setup.sh && /opt/setup.sh

