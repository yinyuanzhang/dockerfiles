FROM base/archlinux

# Update system
RUN yes | pacman -Syu

# install hledger
RUN yes | pacman -Sy hledger hledger-api hledger-web

# creaty empty journal file
RUN touch /root/.hledger.journal

