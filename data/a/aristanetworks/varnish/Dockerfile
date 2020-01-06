# Copyright (c) 2019 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

FROM aristanetworks/base:2.3
LABEL maintainer="Krishnanand Thommandra kthommandra@arista.com"

RUN apk update && apk upgrade && \
    apk add --no-cache \
	varnish=6.0.2-r0 \
	dumb-init

ENTRYPOINT [ "dumb-init", "--" ]
CMD [ "sleep", "100000000" ]
