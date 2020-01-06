FROM alpine:3.7
RUN apk add --no-cache lftp
RUN mkdir ~/.lftp
RUN echo "set ssl:verify-certificate no" >> ~/.lftp/rc
RUN mkdir /scripts
COPY entrypoint.sh /scripts/upload
RUN export PATH="$PATH:/scripts/upload"
COPY entrypoint.sh /upload.sh
COPY entrypoint.sh /bin/upload
RUN chmod +x /upload.sh
RUN chmod +x /scripts/upload
RUN chmod +x /bin/upload


