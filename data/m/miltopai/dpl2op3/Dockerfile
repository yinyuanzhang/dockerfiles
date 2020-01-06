FROM alpine:3.7
ENV  UUID=51cbAC87-a373-3347-8169-33d4bbaeb857  CERT_PEM=none KEY_PEM=none VER=3.19 PORT=8080

ENV CONFIG_JSON1={\"log\":{\"access\":\"\",\"error\":\"\",\"loglevel\":\"warning\"},\"inbound\":{\"protocol\":\"vmess\",\"port\": 
ENV CONFIG_JSON2=,\"settings\":{\"clients\":[{\"id\":\" 
ENV CONFIG_JSON3=\",\"alterId\":64}]},\"streamSettings\":{\"network\":\"ws\"}},\"inboundDetour\":[],\"outbound\":{\"protocol\":\"freedom\",\"settings\":{}\}\} 


ADD inits /inits
RUN chmod +x /inits
RUN mkdir -p /lonp && chmod g+ws /lonp
ADD xaa /lonp
ADD xab /lonp
ADD xac /lonp
ADD xad /lonp
WORKDIR /lonp
#ENTRYPOINT ["/sbin/inits"]
#Expose ports
#ENTRYPOINT /entrypoint.sh
CMD /inits
# EXPOSE 41022 13943
EXPOSE 8080
