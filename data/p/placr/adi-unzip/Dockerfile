FROM    python:2.7

ENV     INCOMING_ZIPFILE_PATH  "/home/sftpuser/data/ToLoad"
ENV     PROCESSED_ZIPFILE_PATH "/home/sftpuser/data/Loaded"
ENV     FAILED_ZIPFILE_PATH    "/home/sftpuser/data/Failed"

# Use identical group as the sftp/adi-unzip one, in case the folders are shared with host. 
RUN     addgroup --gid 30100 adiunzipgroup
RUN     useradd -u 30102 -M -N -g adiunzipgroup adiunzipuser

# Add the ADI extraction script
RUN 	mkdir -p /opt/adi_unzip
ADD 	src/adi_unzip.py /opt/adi_unzip/adi_unzip.py

COPY    docker-entrypoint.sh /

# Map the data volume also for other components.
VOLUME  /var/cisdata

ENTRYPOINT ["/docker-entrypoint.sh"]

WORKDIR /opt/adi_unzip

CMD 	[ "/opt/adi_unzip/adi_unzip.py" ]