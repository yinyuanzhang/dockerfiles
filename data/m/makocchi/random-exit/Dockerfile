FROM busybox:1.30.1

# a percentage of success
ENV SUCCESS=50

CMD ["sh", "-c", "test $(($RANDOM % 100)) -lt $SUCCESS; exit $?"]
