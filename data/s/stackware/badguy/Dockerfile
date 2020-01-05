FROM fedora:latest

RUN mkdir -p /usr/app && mkdir -p /usr/wordlist
ADD rockyou.txt /usr/wordlist/rockyou.txt
ADD hydra.bin /usr/app/hydra
RUN chmod +x /usr/app/hydra

ADD badguy.sh /usr/app/badguy.sh
RUN chmod +x /usr/app/badguy.sh

ENTRYPOINT ["/usr/app/badguy.sh"]
CMD ["127.0.0.1","22"]
