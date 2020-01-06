# level 1b

# Security has tightened - I've had to make this container look more real.
# It contains a miniature operating system (alpine) that uses busybox,
# can run a real /bin/sh, and has a flag file that contains real data.
#
# The transit inspectors will start the container to check the flag data
# before export like this:
# $ sudo docker run --rm -it level1b
#
# Hopefully you can find the real key.
#
# - Bumblebear

FROM alpine

# First we put the flag in root
COPY flag.txt /

# Now we'll replace the 'cat' program with a fake
RUN rm /bin/cat && \
touch /bin/cat && \
chmod +x /bin/cat && \
echo -e '#!/bin/sh\necho "[This is an empty flag that the recipient will return through customs]"' > /bin/cat

# Set the command to print the flag when our container is run by security agents
CMD cat /flag.txt
