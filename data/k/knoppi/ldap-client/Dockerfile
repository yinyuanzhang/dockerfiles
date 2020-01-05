FROM debian:jessie 

MAINTAINER Jan Bundesmann <jan.bundesmann@gmx.de>

# runs as user openldap(104), group openldap(107) 

RUN apt-get update \ 
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends ldap-utils curl\ 
    && apt-get clean && rm -rf /var/lib/apt/lists/* 

COPY search_all.sh /root/search_all.sh
COPY add_base.sh /root/add_base.sh
    
CMD tailf /dev/null

