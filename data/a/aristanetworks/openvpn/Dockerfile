# Copyright (c) 2017 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.
FROM aristanetworks/base:3.9.3
MAINTAINER Fabrice Rabaute fabrice@arista.com

# Install openvpn and iptables
RUN apk add --no-cache \
    iptables=1.6.2-r1 \
    openvpn=2.4.6-r4

ENTRYPOINT ["/usr/bin/dumb-init", "--", "openvpn"]
