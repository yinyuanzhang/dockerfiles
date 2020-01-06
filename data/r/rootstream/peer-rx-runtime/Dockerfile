################################################################################
#                                                                              #
#                     VIRTULABS / ROOTSTREAM CONFIDENTIAL                      #
#      Copyright (c) 2017 RootStream project authors. All Rights Reserved      #
# ____________________________________________________________________________ #
#                                                                              #
# NOTICE: All information contained herein is, and remains the property of     #
# VirtuLabs/RootStream and its suppliers, if any. The intellectual and         #
# technical concepts contained herein are proprietary to VirtuLabs/RootStream  #
# and its suppliers and may be covered by U.S. and Foreign Patents, patents in #
# process, and are protected by trade secret or copyright law. Dissemination   #
# of this information or reproduction of this material is strictly forbidden   #
# unless prior written permission is obtained from VirtuLabs/RootStream.       #
# ____________________________________________________________________________ #

FROM ubuntu:bionic

ENV \
  DEBIAN_FRONTEND=noninteractive, \
  GST_PLUGIN_PATH=/usr/share/gst-plugins-custom \
  LD_LIBRARY_PATH=/usr/local/lib:/usr/share/gst-plugins-custom

ADD build.sh .
RUN bash build.sh && rm build.sh

ENTRYPOINT ["/usr/bin/dumb-init", "--"]
