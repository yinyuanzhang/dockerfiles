#TO BUILD: docker build --build-arg un=???YOUR USER??? --build-arg uid=???YOUR USER ID??? . -t uol/cs/co3090/ecp_jee_gf:4.1.2
#TO RUN: docker run --name ecp_jee_gf --rm -it -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v ???HOST PATH??? :home/???YOUR USER ID???/workspace -p 4848:4848 -p 8080:8080 uol/cs/co3090/ecp_jee_gf:4.1.2 ./eclipse/eclipse
FROM openjdk:8 as ecpjee
ARG un=ecpjeegf
ARG uid=1000
RUN echo $uid $un
ENV HOME /home/$un 
ENV USER $un 
ENV UID $uid 
ENV ECP_URL=http://www.mirrorservice.org/sites/download.eclipse.org/eclipseMirror/technology/epp/downloads/release/oxygen/2/ 
ENV ECP_PKG=eclipse-jee-oxygen-2-linux-gtk-x86_64.tar.gz   
ENV GF_HOME=/glassfish4
#ENV GF_IMG=


RUN apt-get update && apt-get install -y \
	# For eclipse            
	libx11-6 libxext-dev libxrender-dev libxtst-dev libcanberra-gtk-module \ 
        --no-install-recommends \ 
	&& apt-get clean \  
	&& rm -rf /var/lib/apt/lists/*

#Change number to user id of the host to avoid problems
RUN useradd -u $UID -ms /bin/bash $USER

WORKDIR $HOME

#Eclipse JEE
RUN wget "$ECP_URL$ECP_PKG" \
&& tar -xvf $ECP_PKG \
&& rm $ECP_PKG \
&& mkdir -p $HOME/workspace \
&& chown -R $USER:$USER $HOME \
&& sed -i 's/"-Dswing.defaultlaf=com.sun.java.swing.plaf.gtk.GTKLookAndFeel"//g' $HOME/eclipse/eclipse


#For Glassfish
COPY --from=oracle/glassfish:4.1.2 $GF_HOME $GF_HOME
RUN chown -R $USER:$USER $GF_HOME 

# Ports being exposed 
EXPOSE 4848 8080 8181

USER $USER 
