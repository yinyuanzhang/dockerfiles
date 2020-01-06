# LICENSE
# -------
# Copyright 2018 Apostolos Benisis
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# DESCRIPTION
# ----------
# This is the Dockerfile for Oracle Database 11g Release 2 Express Edition
#
# PREREQUISITES
# ----------------------------------
# [*] Docker 1.17.05 and above
# [*] oracle-xe-11.2.0-1.0.x86_64.rpm.zip
#     You can download Oracle Database 11g Release 2 Express Edition for Linux x64
#     from http://www.oracle.com/technetwork/database/database-technologies/express-edition/downloads/index.html
# [*] runOracle.sh, checkDBstatus.sh, setPassword.sh, xe.rsp
#     Get the various script files including this dockerfile from
#     git clone https://apostolosbenisis@bitbucket.org/apostolosbenisis/oracle-database-11.2.0.2-xe.git
#
# HOW TO BUILD THIS IMAGE
# -----------------------
# Put the downloaded files in the same directory as this Dockerfile
# Run:
#      $ docker build --force-rm=true --no-cache=true -t apostolosbenisis/oracle11g-11.2.0.2-xe -f Dockerfile .
#
# Optionally you can pass the uid for the oracle user and the guid for the dba group as arguments, for example run:
#      $ docker build --build-arg ORACLE_USERID=<custom oracle user id> --build-arg DBA_GROUPID=<custom dba group id> --force-rm=true --no-cache=true -t apostolosbenisis/oracle11g-11.2.0.2-xe -f Dockerfile .
#
# IMPORTANT
# ---------
# Oracle XE uses shared memory for MEMORY_TARGET and needs at least 1 GB.

# Default values for the arguments
# Use the --build-arg flag to override the values
# The uid for the oracle user and the gid of the dba group used in the container.
ARG ORACLE_USERID=1973
ARG	DBA_GROUPID=1973

# Pull base image
# ---------------
FROM oraclelinux:7-slim

# Maintainer
# ----------
MAINTAINER Apostolos Benisis <info@brokenrhythm.blog>

# Use the --build-arg flag to override the values
# The uid for the oracle user and the gid of the dba group used in the container.
ARG ORACLE_USERID
ARG	DBA_GROUPID

# Environment variables required for this build (do NOT change)
# -------------------------------------------------------------
ENV ORACLE_BASE=/u01/app/oracle \
    ORACLE_HOME=/u01/app/oracle/product/11.2.0/xe \
    ORACLE_SID=XE \
    INSTALL_FILE_1="oracle-xe-11.2.0-1.0.x86_64.rpm.zip" \
    INSTALL_DIR="$HOME/install" \
    CONFIG_RSP="xe.rsp" \
    RUN_FILE="runOracle.sh" \
    PWD_FILE="setPassword.sh" \
    CHECK_HEALTH_FILE="checkHealth.sh"


# Use second ENV so that variable get substituted
ENV PATH=$ORACLE_HOME/bin:$PATH

# Copy binaries
# -------------
COPY $INSTALL_FILE_1 $CONFIG_RSP $RUN_FILE $PWD_FILE $CHECK_HEALTH_FILE $INSTALL_DIR/

# Install Oracle Express Edition
# ------------------------------

RUN echo oracle uid:$ORACLE_USERID dba guid:$DBA_GROUPID && \
	mkdir -p /u01/app/ && \
	groupadd -g $DBA_GROUPID dba && \
	useradd -u $ORACLE_USERID -g dba -d $ORACLE_BASE -s /bin/bash oracle && \
	yum -y install unzip libaio bc initscripts net-tools openssl && \
    rm -rf /var/cache/yum && \
    cd $INSTALL_DIR && \
    unzip $INSTALL_FILE_1 && \
    rm $INSTALL_FILE_1 &&    \
    cat() { declare -A PROC=(["/proc/sys/kernel/shmmax"]=4294967295 ["/proc/sys/kernel/shmmni"]=4096 ["/proc/sys/kernel/shmall"]=2097152 ["/proc/sys/fs/file-max"]=6815744); [[ ${PROC[$1]} == "" ]] && /usr/bin/cat $* || echo ${PROC[$1]}; } && \
    free() { echo "Swap: 2048 0 2048"; } && \
    export -f cat free && \
    rpm -i Disk1/*.rpm &&    \
    unset -f cat free && \
    mkdir -p $ORACLE_BASE/scripts/setup && \
    mkdir $ORACLE_BASE/scripts/startup && \
    ln -s $ORACLE_BASE/scripts /docker-entrypoint-initdb.d && \
    mkdir $ORACLE_BASE/oradata && \
    chown -R oracle:dba $ORACLE_BASE && \
    mv $INSTALL_DIR/$CONFIG_RSP $ORACLE_BASE/ && \
    mv $INSTALL_DIR/$RUN_FILE $ORACLE_BASE/ && \
    mv $INSTALL_DIR/$PWD_FILE $ORACLE_BASE/ && \
    mv $INSTALL_DIR/$CHECK_HEALTH_FILE $ORACLE_BASE/ && \
    ln -s $ORACLE_BASE/$PWD_FILE / && \
    cd $HOME && \
    rm -rf $INSTALL_DIR && \
    chmod ug+x $ORACLE_BASE/*.sh

VOLUME ["$ORACLE_BASE/oradata"]
EXPOSE 1521 8080
HEALTHCHECK --interval=1m --start-period=5m \
   	CMD "$ORACLE_BASE/$CHECK_HEALTH_FILE" >/dev/null || exit 1

CMD exec $ORACLE_BASE/$RUN_FILE
