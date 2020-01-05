FROM kanapi/kanapi-bbs
MAINTAINER Jacek Danecki <jacek.m.danecki@gmail.com>
RUN git clone https://github.com/jdanecki/kanapi.git /kanapi_build/kanapi; /kanapi_build/kanapi/kanapi_system/docker/configure; \
	cd /kanapi_build/kanapi/kanapi_system/x86_64 && ./install t_compression verbose  && ./install t_system verbose  && \
	./install devel verbose  && ./install vim verbose  && ./install bc verbose  && \
	/kanapi_build/kanapi/kanapi_system/docker/strip_binaries && \
	 rm -rf ${HOME}/src && mkdir ${HOME}/src && rm -rf ${HOME}/.ccache && rm -rf /kanapi_build/kanapi
CMD ["/bin/bash"]

