FROM centos:7
MAINTAINER Genaro Contreras

ENV NESSUS_VERSION="8.5.1"


RUN set -x \
  && touch /var/log/nessus-install.log \
  && echo "Updating packages" >> /var/log/nessus-install.log \
  && yum update -y \
  \
  && echo "Find the download-id" >> /var/log/nessus-install.log \
  && DOWNLOAD_PAGE=$(curl -ssl -o - "https://www.tenable.com/downloads/nessus" | grep -w $NESSUS_VERSION"-es7.x86_64.rpm" |  sed -n -e 's/.*data-page-id="\([0-9]*\)".*data-download-id="\([0-9]*\)".*".*/\1:\2/p' ) \
   && PAGE_ID=${DOWNLOAD_PAGE%:*} \
  && DOWNLOAD_ID=${DOWNLOAD_PAGE#*:} \
  \
  && echo "Import Tanable's GPG key" >> /var/log/nessus-install.log \
  && rpm --import https://static.tenable.com/marketing/RPM-GPG-KEY-Tenable \
  \
  && echo "Fetch the rpm with license agreement and follow redirect " >> /var/log/nessus-install.log \
  && curl -ssL -L -o /tmp/Nessus-${NESSUS_VERSION}-es7.x86_64.rpm \
    "https://www.tenable.com/downloads/pages/${PAGE_ID}/downloads/${DOWNLOAD_ID}/download_file?utf8=%E2%9C%93&i_agree_to_tenable_license_agreement=true&commit=I+Agree" \
  \
  && echo "Install the rpm" >> /var/log/nessus-install.log \
  && rpm -ivh /tmp/Nessus-${NESSUS_VERSION}-es7.x86_64.rpm \
  \
  && echo "Redirect logs to stdout" >> /var/log/nessus-install.log \
  && for lf in backend.log nessusd.messages www_server.log; do \
     ln -s /dev/stdout /opt/nessus/var/nessus/logs/${lf}; done \
  \
  && echo "Cleanup" >> /var/log/nessus-install.log \
  && rm /tmp/Nessus-${NESSUS_VERSION}-es7.x86_64.rpm \
  && yum clean all \
  && rm -rf /var/cache/yum \
  && rm -rf /opt/nessus/var/nessus/{uuid,*.db*,master.key} \
  && echo "Starting Nessus Service" >> /var/log/nessus-install.log 

EXPOSE 8834
CMD ["/opt/nessus/sbin/nessus-service"]
