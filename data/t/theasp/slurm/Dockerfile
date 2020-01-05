FROM debian:unstable

RUN set -ex; \
  apt-get -qy update; \
  apt-get -qy install slurm-wlm slurm-wlm-basic-plugins slurmctld slurmd slurmdbd munge gettext-base supervisor; \
  apt-get -qy clean; \
  rm -f /etc/slurm-llnl/slurm.conf; \
  rm -f /etc/munge/munge.key; \
  rm -rf /var/lib/apt/lists/*

COPY app/ /app/
CMD ["/app/start.bash"]
