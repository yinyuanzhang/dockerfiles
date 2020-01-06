ARG centos=7
ARG buildrepo=php7build
ARG image=build

FROM aursu/${buildrepo}:${centos}-${image}

COPY SOURCES ${BUILD_TOPDIR}/SOURCES
COPY SPECS ${BUILD_TOPDIR}/SPECS

RUN chown -R $BUILD_USER ${BUILD_TOPDIR}/{SOURCES,SPECS}

USER $BUILD_USER

ENTRYPOINT ["/usr/bin/rpmbuild", "php7-pear.spec"]
CMD ["-ba"]
