FROM fusioned/rhodecode-rccontrol:1.18.0.1700
LABEL maintainer="cyrill.kulka@gmail.com"

ENV RC_APP		Community
ENV RC_VERSION	4.12.4

# Install RhodeCode Community Edition
RUN .rccontrol-profile/bin/rccontrol	\
		install $RC_APP					\
		--version $RC_VERSION			\
		--accept-license				\
		'{"host": "0.0.0.0", "port": 5000, "username": "admin", "password": "ilovecookies", "email": "adalovelace@example.com", "repo_dir": "/data", "database": "sqlite"}'

# fix for hardcoded hooks URI
ENV DEFAULT_RC_HOOKS_HOST 127.0.0.1
COPY files .

# enable celery
RUN .rccontrol-profile/bin/rccontrol enable-module celery community-1

EXPOSE 5000
CMD bash ./patched-start.sh
