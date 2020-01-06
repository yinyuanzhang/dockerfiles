FROM kinetica/kinetica-intel:latest

CMD usermod -a -G fuse gpudb_proc ; chgrp fuse /dev/fuse ; ldconfig && /opt/gpudb-docker-start.sh
