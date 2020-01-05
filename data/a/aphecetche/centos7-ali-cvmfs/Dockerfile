FROM aphecetche/centos7-ali-core

RUN mkdir -p /cvmfs/alice.cern.ch /cvmfs/alice-ocdb.cern.ch /cvmfs/alice-nightlies.cern.ch

ENTRYPOINT ["/cvmfs-startup.sh"]

CMD ["GCC-Toolchain/v6.2.0-alice1-4"]
