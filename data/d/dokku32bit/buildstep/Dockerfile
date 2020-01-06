FROM dokku32bit/cedarish32bit:cedar14

RUN curl https://raw.githubusercontent.com/dokku32bit/herokuish_32bit/dist/release/herokuish_0.3.0_linux_i686.tgz \
		--silent -L | tar -xzC /bin

# install herokuish supported buildpacks and entrypoints
RUN /bin/herokuish buildpack install \
	&& ln -s /bin/herokuish /build \
	&& ln -s /bin/herokuish /start \
	&& ln -s /bin/herokuish /exec

# backwards compatibility
ADD ./rootfs /
