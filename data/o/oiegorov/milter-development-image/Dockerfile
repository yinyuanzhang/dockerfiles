from centos:6
# Install all development and library packages for milters
RUN yum groupinstall -y Development tools && yum install -y sendmail-milter sendmail-devel sendmail-milter mysql-devel db4-devel valgrind gdb strace rsyslog
RUN curl -O http://dl.fedoraproject.org/pub/epel/6/x86_64/Packages/g/GeoIP-1.6.5-1.el6.x86_64.rpm -O http://dl.fedoraproject.org/pub/epel/6/x86_64/Packages/g/GeoIP-devel-1.6.5-1.el6.x86_64.rpm -O http://dl.fedoraproject.org/pub/epel/6/x86_64/Packages/g/GeoIP-GeoLite-data-2018.04-1.el6.noarch.rpm -O http://dl.fedoraproject.org/pub/epel/6/x86_64/Packages/g/GeoIP-GeoLite-data-extra-2018.04-1.el6.noarch.rpm -O http://dl.fedoraproject.org/pub/epel/6/x86_64/Packages/g/geoipupdate-2.2.1-2.el6.x86_64.rpm -O http://dl.fedoraproject.org/pub/epel/6/x86_64/Packages/l/libmaxminddb-devel-1.1.1-5.el6.x86_64.rpm -O http://dl.fedoraproject.org/pub/epel/6/x86_64/Packages/l/libmaxminddb-1.1.1-5.el6.x86_64.rpm -O http://rpms.remirepo.net/enterprise/6/remi/x86_64//hiredis-last-devel-0.13.3-1.el6.remi.x86_64.rpm -O http://rpms.remirepo.net/enterprise/6/remi/x86_64//hiredis-last-0.13.3-1.el6.remi.x86_64.rpm -O http://dl.fedoraproject.org/pub/epel/6/x86_64/Packages/l/libspf2-1.2.10-5.20150405gitd57d79fd.el6.x86_64.rpm -O http://dl.fedoraproject.org/pub/epel/6/x86_64/Packages/l/libspf2-devel-1.2.10-5.20150405gitd57d79fd.el6.x86_64.rpm
RUN yum localinstall -y GeoIP-1.6.5-1.el6.x86_64.rpm GeoIP-devel-1.6.5-1.el6.x86_64.rpm GeoIP-GeoLite-data-2018.04-1.el6.noarch.rpm GeoIP-GeoLite-data-extra-2018.04-1.el6.noarch.rpm geoipupdate-2.2.1-2.el6.x86_64.rpm libmaxminddb-devel-1.1.1-5.el6.x86_64.rpm libmaxminddb-1.1.1-5.el6.x86_64.rpm hiredis-last-devel-0.13.3-1.el6.remi.x86_64.rpm hiredis-last-0.13.3-1.el6.remi.x86_64.rpm libspf2-1.2.10-5.20150405gitd57d79fd.el6.x86_64.rpm libspf2-devel-1.2.10-5.20150405gitd57d79fd.el6.x86_64.rpm
RUN git clone https://github.com/DaveGamble/cJSON.git && cd cJSON && make && make install
# Now install repo for milter-manager, nice suite with milter-test-server utility
COPY milter-manager_repo_setup.rpm.sh ./ 
RUN ./milter-manager_repo_setup.rpm.sh
RUN yum install -y milter-manager
RUN yum install -y vim gdb-gdbserver
# Define a deploy key in order to avoid sensitive information being stored in a github. I can simply type it in during docker run
ENV deploy_key_token=nodefaultvalue
ENV SHELL=/bin/bash
# post-cmfilter needs to examine this library path for several of its libraries: libcidr and libcjson if I am not mistaken
ENV LD_LIBRARY_PATH=/usr/local/lib/
# Set up entry point : compile milter, start rsyslogd, milter, bash shell
COPY docker-entrypoint.sh /usr/local/bin/ 
RUN ln -sf usr/local/bin/docker-entrypoint.sh / # backwards compat
ENTRYPOINT ["./docker-entrypoint.sh"]
