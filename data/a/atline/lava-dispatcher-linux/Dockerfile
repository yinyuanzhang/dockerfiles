ARG build_from

FROM lavasoftware/lava-dispatcher:$build_from

COPY ["lava-coordinator.conf", "/etc/lava-coordinator/lava-coordinator.conf"]

RUN sed -i '/\/etc\/lava-dispatcher\/lava-slave/i\set +e\ngrep "export http_proxy=\$http_proxy" /etc/lava-dispatcher/lava-slave\nrc=$?\nset -e\nif [ $rc -ne 0 ]; then\necho "export http_proxy=\$http_proxy" >> /etc/lava-dispatcher/lava-slave\nfi\nsed -i "s/\\"coordinator_hostname\\": .*/\\"coordinator_hostname\\": \\"$master\\"/g" /etc/lava-coordinator/lava-coordinator.conf' /root/entrypoint.sh;\
sed -i '/\/usr\/bin\/lava-slave/i\service tftpd-hpa start\nrpcbind\nservice nfs-kernel-server start\nservice ser2net start' /root/entrypoint.sh;\
sed -i '/killproc -p/a\rm -f \$PIDFILE || true' /etc/init.d/ser2net;\
apt-get update;\
apt-get install -y python3-pip --no-install-recommends;\
apt-get install -y lavacli;\
apt-get install -y vim --no-install-recommends;\
rm -rf /var/lib/apt/lists/*;\
pip3 install pyserial;

ENV TINI_VERSION v0.18.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini
ENTRYPOINT ["/tini", "--"]
CMD ["/root/entrypoint.sh"]
