# level 1a

# I'm going to ship you an empty container so it clears export control.
# You'll need to uncover the original data.
#
# - Bumblebear

FROM scratch

# Put in a small portable go program (and source) that prints the flag
# Hopefully security agents waste their time inspecting this binary 
COPY catflag/catflag /

# Set the cmd to our portable printer
CMD ["/catflag"]

# Put the flag in the container, then erase the secret before transport
# so the container appears clean
COPY flag.txt /
COPY empty.txt /flag.txt
