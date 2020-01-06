FROM euskadi31/gentoo-portage:latest

MAINTAINER Axel Etcheverry <axel@etcheverry.biz>

RUN echo "app-misc/sphinx ~amd64" >> /etc/portage/package.keywords
RUN echo "app-misc/sphinx id64 mysql postgres" >> /etc/portage/package.use
RUN emerge app-misc/sphinx

EXPOSE 9306 9312

CMD ["searchd", "--nodetach"]
