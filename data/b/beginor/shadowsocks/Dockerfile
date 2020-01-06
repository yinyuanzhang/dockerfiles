FROM mritd/shadowsocks:latest

ENV SS_MODULE="ss-server"
ENV SS_CONFIG="-s 0.0.0.0 -p 6478 -k z7TFyJ6mAev1 -m aes-256-gcm -u"
ENV KCP_FLAG="true"
ENV KCP_MODULE="kcpserver"
ENV KCP_CONFIG="-l :6907 -t 127.0.0.1:6478 --crypt none --mtu 1200 --nocomp --mode normal --dscp 46"

EXPOSE 6478 6907
