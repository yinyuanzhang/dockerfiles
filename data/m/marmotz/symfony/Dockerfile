FROM marmotz/apache:php70

USER root

ADD init_symfony.sh /

USER nonrootuser

CMD ["/init_symfony.sh"]
