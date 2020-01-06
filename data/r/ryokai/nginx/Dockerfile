from solita/ubuntu-systemd
RUN apt-get update;apt-get install -y nginx;systemctl enable nginx.service
# RUN systemctl start nginx.service
ENTRYPOINT ["/sbin/init"]
