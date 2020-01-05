FROM melihsavdert/oel7-systemd
MAINTAINER Melih Savdert

ENV ORA_MOUNT_PATH /u01
ENV ORA_ORACLE_BASE /u01/app/oracle
ENV ORA_ORACLE_HOME /u01/app/oracle/product/18.3.0.0/dbhome_1
ENV GRID_ORACLE_BASE /u01/app/grid
ENV GRID_ORACLE_HOME /u01/app/18.3.0.0/grid
ENV ORAINVENTORY /u01/app/oraInventory
ENV TZ Europe/Istanbul

# Update the operating system
RUN ["yum", "-y", "update"]

RUN yum-config-manager \
    --add-repo \
    http://public-yum.oracle.com/public-yum-ol7.repo

# Install necessary packages
RUN ["yum", "-y", "install", \
       "oracle-database-preinstall-18c", \
       "vim", \
       "screen", \
       "net-tools", \
       "wget", \
       "ntp"]

RUN yum install -y binutils compat-libstdc++-33 compat-libstdc++-33.i686 gcc gcc-c++ glibc glibc.i686 glibc-devel glibc-devel.i686 ksh libgcc libgcc.i686 libstdc++ libstdc++.i686 libstdc++-devel libstdc++-devel.i686 libaio libaio.i686 libaio-devel libaio-devel.i686 libXext libXext.i686 libXtst libXtst.i686 libX11 libX11.i686 libXau libXau.i686 libxcb libxcb.i686 libXi libXi.i686 make sysstat unixODBC unixODBC-devel zlib-devel zlib-devel.i686

# Clean the yum cache
RUN ["yum", "clean", "all"]

##  Users and Groups
RUN userdel -r oracle
RUN groupdel oinstall
RUN groupdel dba
RUN groupdel oper
RUN groupdel backupdba
RUN groupdel dgdba
RUN groupdel kmdba
RUN groupdel racdba
RUN groupadd -g 54421 oinstall
RUN groupadd -g 54329 asmadmin
RUN groupadd -g 54327 asmdba
RUN groupadd -g 54328 asmoper
RUN groupadd -g 54322 dba
RUN groupadd -g 54323 oper
RUN groupadd -g 54324 backupdba
RUN groupadd -g 54325 dgdba
RUN groupadd -g 54326 kmdba
RUN groupadd -g 54330 racdba
RUN useradd -u 54321 -g oinstall -G dba,asmdba,backupdba,dgdba,kmdba,racdba,oper oracle
RUN useradd -u 54322 -g oinstall -G asmadmin,asmdba,racdba,asmoper,dba grid

# Give root, grid and oracle users passwords
RUN echo "oracle:Qazxsw123" | chpasswd
RUN echo "root:Qazxsw123" | chpasswd
RUN echo "grid:Qazxsw123" | chpasswd

# Disable SELinux
RUN sed -i 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/selinux/config

# Add ulimits configuration file for grid user
# oracle user ulimits configuration file already added by oracle-rdbms-server-xx.x-preinstall
RUN echo -e "oracle   soft   nofile    1024\n\
oracle   hard   nofile    65536\n\
oracle   soft   nproc    16384\n\
oracle   hard   nproc    16384\n\
oracle   soft   stack    10240\n\
oracle   hard   stack    32768\n\
oracle   hard   memlock    134217728\n\
oracle   soft   memlock    134217728\n\
grid     soft   nofile    1024\n\
grid     hard   nofile    65536\n\
grid     soft   nproc    16384\n\
grid     hard   nproc    16384\n\
grid     soft   stack    10240\n\
grid     hard   stack    32768\n\
grid     hard   memlock    134217728\n\
grid     soft   memlock    134217728\n\
" >> /etc/security/limits.conf

RUN echo -e "if [ \$USER = \"oracle\" ] || [ \$USER = \"grid\" ]; then\n\
    if [ \$SHELL = \"/bin/ksh\" ]; then\n\
        ulimit -p 16384\n\
        ulimit -n 65536\n\
    else\n\
        ulimit -u 16384 -n 65536\n\
    fi\n\
    umask 022\n\
fi" >> /etc/profile

##  SSH Shared Keys
# Create SSH shared key directory for the oracle user
RUN ["mkdir", "-p", "-m", "0700", "/home/oracle/.ssh/"]

# Generate SSH shared keys for the oracle user
RUN ssh-keygen -q -C '' -N '' -f /home/oracle/.ssh/id_rsa

# Create the authorized_keys file for the oracle user
RUN cat /home/oracle/.ssh/id_rsa.pub > /home/oracle/.ssh/authorized_keys

# Change ownership of the SSH shared key files for the oracle user
RUN chown -R oracle:oinstall /home/oracle/.ssh

# Change permissions of the authorized_keys file for the oracle user
RUN ["chmod", "0640", "/home/oracle/.ssh/authorized_keys"]

# Create SSH shared key directory for the grid user
RUN ["mkdir", "-p", "-m", "0700", "/home/grid/.ssh/"]

# Generate SSH shared keys for the grid user
RUN ssh-keygen -q -C '' -N '' -f /home/grid/.ssh/id_rsa

# Create the authorized_keys file for the grid user
RUN cat /home/grid/.ssh/id_rsa.pub > /home/grid/.ssh/authorized_keys

# Change ownership of the SSH shared key files for the grid user
RUN chown -R grid:oinstall /home/grid/.ssh

# Change permissions of the authorized_keys file for the grid user
RUN ["chmod", "0640", "/home/grid/.ssh/authorized_keys"]

# Generate SSH host ECDSA shared keys
RUN ssh-keygen -q -C '' -N '' -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key

# Create the ssh_known_hosts file
RUN for NODE in ora1 ora2; do (echo -n "$NODE " && cat /etc/ssh/ssh_host_ecdsa_key.pub) >> /etc/ssh/ssh_known_hosts; done

## .bash_profile ###
RUN echo -e "#this is for oracle install#\n\
if [ -t 0 ]; then\n\
        stty intr ^C\n\
fi" >> /home/oracle/.bashrc && \
echo -e "#this is for oracle install#\n\
if [ -t 0 ]; then\n\
        stty intr ^C\n\
fi" >> /home/grid/.bashrc
## .bash_profile ###
RUN echo -e "### for oracle install ####\n\
export ORACLE_BASE=${ORA_ORACLE_BASE}\n\
export GRID_BASE=${GRID_ORACLE_BASE}\n\
export ORACLE_HOME=${ORA_ORACLE_HOME}\n\
export ORACLE_HOSTNAME=\`hostname\`\n\
" >> /home/oracle/.bash_profile
RUN echo -e "export TMPDIR=/tmp\n\
export TEMP=/tmp\n\
export TZ=${TZ}\n\
export PATH=\$ORACLE_HOME/bin:\$ORACLE_HOME/OPatch/:/usr/sbin:\$PATH\n\
export LD_LIBRARY_PATH=\$ORACLE_HOME/lib:/usr/lib\n\
export CLASSPATH=\$ORACLE_HOME/jlib:\$ORACLE_HOME/rdbms/jlib\n\
alias cdob='cd \$ORACLE_BASE'\n\
alias cdoh='cd \$ORACLE_HOME'\n\
alias tns='cd \$ORACLE_HOME/network/admin'\n\
alias envo='env | grep ORACLE'\n\
alias sqla='sqlplus / as sysdba'\n\
alias psf='ps -fe | grep pmon'\n\
alias taila='tail -200f \$ORACLE_BASE/diag/rdbms/\${ORACLE_UNQNAME,,}/\${ORACLE_SID}/trace/alert_\${ORACLE_SID}.log'\n\
alias crsalert='tail -200f \$GRID_BASE/diag/crs/\`hostname -s\`/crs/trace/alert.log'\n\
" >> /home/oracle/.bash_profile
RUN echo -e "### for oracle install ####\n\
export ORACLE_BASE=${GRID_ORACLE_BASE}\n\
export GRID_BASE=\$ORACLE_BASE\n\
export ORACLE_HOME=${GRID_ORACLE_HOME}\n\
export ORACLE_HOSTNAME=\`hostname\`\n\
" >> /home/grid/.bash_profile
RUN echo -e "export TMPDIR=/tmp\n\
export TEMP=/tmp\n\
export TZ=${TZ}\n\
export PATH=\$ORACLE_HOME/bin:\$ORACLE_HOME/OPatch/:/usr/sbin:\$PATH\n\
export LD_LIBRARY_PATH=\$ORACLE_HOME/lib:/usr/lib\n\
export CLASSPATH=\$ORACLE_HOME/jlib:\$ORACLE_HOME/rdbms/jlib\n\
alias cdob='cd \$ORACLE_BASE'\n\
alias cdoh='cd \$ORACLE_HOME'\n\
alias tns='cd \$ORACLE_HOME/network/admin'\n\
alias envo='env | grep ORACLE'\n\
alias sqla='sqlplus / as sysdba'\n\
alias psf='ps -fe | grep pmon'\n\
alias asmalert='tail -200f \$GRID_BASE/diag/asm/\${ORACLE_SID,,}/\${ORACLE_SID}/trace/alert_\${ORACLE_SID}.log'\n\
alias crsalert='tail -200f \$GRID_BASE/diag/crs/\`hostname -s\`/crs/trace/alert.log'\n\
" >> /home/grid/.bash_profile

## create oraclehome
RUN  mkdir ${ORA_MOUNT_PATH} && \
     mkdir -p ${ORA_ORACLE_HOME} && \
     mkdir -p ${GRID_ORACLE_BASE} && \
     mkdir -p ${GRID_ORACLE_HOME} && \
     chown -R grid:oinstall ${ORA_MOUNT_PATH} && \
     mkdir -p ${ORA_ORACLE_BASE} && \
     chown -R oracle:oinstall ${ORA_ORACLE_BASE} && \
     chmod -R 775 ${ORA_MOUNT_PATH}

RUN mkdir -p /u01/software
RUN chown -R oracle:oinstall /u01/software
RUN chmod -R g+w /u01/software/

# Hide/disable the ttyS0 serial console service
RUN ["systemctl", "mask", "serial-getty@ttyS0.service"]

# Set timezone Europe/Istanbul
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN systemctl disable firewalld
RUN systemctl enable sshd
RUN systemctl enable ntpd
RUN rm -rf /run/nologin

EXPOSE 1521 1158 5500 7803 7102 9803

CMD ["/usr/sbin/init"]
