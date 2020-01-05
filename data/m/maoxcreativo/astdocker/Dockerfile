FROM centos:latest
MAINTAINER Maoxcreativo "maoxcreativo@gmail.com"
RUN yum -y update
RUN yum -y install vim tar htop gcc gcc-c++ make wget subversion libxml2-devel ncurses-devel openssl-devel sqlite-devel libuuid-devel vim-enhanced jansson-devel unixODBC unixODBC-devel libtool-ltdl libtool-ltdl-devel subversion speex-devel mysql-devel
WORKDIR /usr/src
RUN svn co http://svn.pjsip.org/repos/pjproject/trunk/ pjproject-trunk
WORKDIR /usr/src/pjproject-trunk
RUN ./configure --libdir=/usr/lib64 --prefix=/usr --enable-shared --disable-sound --disable-resample --disable-video --disable-opencore-amr CFLAGS='-O2 -DNDEBUG'
RUN make dep
RUN make
RUN make install
RUN ldconfig
RUN ldconfig -p | grep pj
WORKDIR /usr/src
RUN wget http://downloads.asterisk.org/pub/telephony/certified-asterisk/asterisk-certified-13.8-current.tar.gz
RUN tar -zxvf asterisk-certified-13.8-current.tar.gz
WORKDIR /usr/src/asterisk-certified-13.8-cert2
RUN sh /usr/src/asterisk-certified-13.8-cert2/contrib/scripts/get_mp3_source.sh
RUN sh /usr/src/asterisk-certified-13.8-cert2/contrib/scripts/install_prereq install
RUN ./configure CFLAGS='-g -O2 -mtune=native' --libdir=/usr/lib64
RUN make
RUN make install
RUN make samples
RUN printf "[simpletrans] \n\
type=transport \n\
protocol=udp \n\
bind=0.0.0.0 \n\
 
[6001] \n\
type = endpoint \n\
transport = simpletrans \n\
context = default \n\
disallow = all \n\
allow = ulaw \n\
aors = 6001 \n\
auth = auth6001 \n\
 
[6001] \n\
type = aor \n\
max_contacts = 1 \n\
 
[auth6001] \n\
type=auth \n\
auth_type=userpass \n\
password=1234 \n\
username=6001 \n\
 
[6002] \n\
type = endpoint \n\
transport = simpletrans \n\
context = default \n\
disallow = all \n\
allow = ulaw \n\
aors = 6002 \n\
auth = auth6002 \n\
 
[6002] \n\
type = aor \n\
max_contacts = 1 \n\
 
[auth6002] \n\
type=auth \n\
auth_type=userpass \n\
password=1234 \n\
username=6001 \n" \ 
> /etc/asterisk/pjsip.conf

RUN printf "[general] \n\
; RTP start and RTP end configure start and end addresses \n\
; \n\
; Defaults are rtpstart=5000 and rtpend=31000 \n\
; \n\
rtpstart=10000 \n\
rtpend=10008 \n" \
> /etc/asterisk/rtp.conf



WORKDIR /root
CMD ["/usr/sbin/asterisk", "-cvvvvvvv"]
