FROM lakowske/k8s-keys

MAINTAINER Seth Lakowske <lakowske@gmail.com>

RUN mkdir /config-drive

RUN mkdir /iso

RUN apk add --update cdrkit gettext curl && rm -rf /var/cache/apk/*

RUN curl https://raw.githubusercontent.com/coreos/coreos-kubernetes/master/multi-node/generic/worker-install.sh > /worker-install.sh

RUN curl https://raw.githubusercontent.com/coreos/coreos-kubernetes/master/multi-node/generic/controller-install.sh > /controller-install.sh

ADD ./create-config-drive /

ADD ./setup-node.sh /

ADD ./user_data /

RUN chmod 755 /create-config-drive

ENTRYPOINT ["/create-config-drive"]
CMD /create-config-drive
