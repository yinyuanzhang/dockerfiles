FROM            mbitz/alpinebase:e340
MAINTAINER      Howard Mei      <howardmei@mubiic.com>
ENV             TIMEZONE        Asia/Singapore

# Add apk repository mirror list and user local bin
COPY            entrypoint      /entrypoint
COPY            root            /root

RUN 			chmod 0755 /entrypoint && NewPackages="bash" && \
				apk-install ${NewPackages} && set-timezone ${TIMEZONE} && apk-cleanup
				
# Define the Entry Point and/or Default Command
ENTRYPOINT      ["/entrypoint"]

