FROM openjdk:8
WORKDIR /
COPY build.sh /build/build.sh
RUN chmod a+x /build/build.sh && /build/build.sh
CMD ["java","-Dcom.mojang.eula.agree=true","-Djline.terminal=jline.UnsupportedTerminal","-jar","spigot.jar","nogui"]
