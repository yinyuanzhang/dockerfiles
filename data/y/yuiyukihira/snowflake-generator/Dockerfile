FROM ubuntu:latest
LABEL maintainer="Yui Yukihira (yuiyukihira@pm.me)"
EXPOSE 8080
COPY setup.sh /src/
RUN sh /src/setup.sh
COPY snowflake.py /src/
ENTRYPOINT ["python3.7"]
CMD ["/src/snowflake.py", "&"]
ARG epoch=1546300800
ENV EPOCH=$epoch
ARG debug=0
ENV DEBUG=$debug
