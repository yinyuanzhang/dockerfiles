FROM alpine:latest
LABEL maintainer="Vincent FRICOU <vincent@fricouv.eu>"

COPY ./jobs/runners/ /jobs/runners

RUN \
  apk -U upgrade && \
  apk add curl && \
  mkdir -p /jobs/1min && \
  mkdir -p /jobs/5min && \
  mkdir -p /jobs/15min && \
  mkdir -p /jobs/hourly && \
  mkdir -p /jobs/daily && \
  mkdir -p /jobs/weekly && \
  mkdir -p /jobs/monthly && \
  printf "*/1\t*\t*\t*\t*\tsh /jobs/runners/run-1min.sh\n" >> /etc/crontabs/root && \
  printf "*/5\t*\t*\t*\t*\tsh /jobs/runners/run-5min.sh\n" >> /etc/crontabs/root && \
  printf "*/15\t*\t*\t*\t*\tsh /jobs/runners/run-15min.sh\n" >> /etc/crontabs/root && \
  printf "00\t*\t*\t*\t*\tsh /jobs/runners/run-hourly.sh\n" >> /etc/crontabs/root && \
  printf "00\t12\t*\t*\t*\tsh /jobs/runners/run-daily.sh\n" >> /etc/crontabs/root && \
  printf "00\t12\t*\t*\t1\tsh /jobs/runners/run-weekly.sh\n" >> /etc/crontabs/root && \
  printf "00\t12\t1\t*\t*\tsh /jobs/runners/run-monthly.sh\n" >> /etc/crontabs/root && \
  find /jobs -type f -exec chmod +x {} \;

CMD [ "/usr/sbin/crond","-f","-d","7" ]