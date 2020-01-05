FROM openshift/origin-haproxy-router:v3.9
RUN sed -i 's/iptables -L/iptables -nL/g' /var/lib/haproxy/reload-haproxy
