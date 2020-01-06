FROM alpine:3.10.3

# ----------------------------------------------------------------------------------------------- */
# Base packages
# ----------------------------------------------------------------------------------------------- */

RUN set -xe; \
	apk add --no-cache \
		ca-certificates \
		git \
		rsync \
		sudo \
		shadow \
		openssh-client

# ----------------------------------------------------------------------------------------------- */
# Create regular user & group
# ----------------------------------------------------------------------------------------------- */

USER root
RUN set -xe; \
	addgroup -g 1000 -S deployer \
	&& adduser -s /bin/sh -u 1000 -S deployer -G deployer \
	&& echo "deployer ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/deployer \
    && chmod 0440 /etc/sudoers.d/deployer

# ----------------------------------------------------------------------------------------------- */
# Change to regular user and set working directory
# ----------------------------------------------------------------------------------------------- */

USER deployer

WORKDIR /home/deployer

CMD ["/bin/sh"]