FROM cpswarm/gazebo-em-ex-deps:latest

ENV TURTLEBOT_3D_SENSOR=no3d \
    TURTLEBOT_TOP_PLATE_DEVICE=rplidar

COPY . $HOME

## chmod a+x for all bash scripts
RUN $INST_SCRIPTS/set_user_permission.sh $HOME $HOME/ws

WORKDIR $HOME/ws/

RUN catkin init --workspace .

RUN /bin/bash build.sh

RUN echo "source $HOME/ws/devel/setup.bash" >> ~/.bashrc \
	 && echo "source $HOME/ws/global_variables.env" >> ~/.bashrc

WORKDIR $HOME

RUN mkdir cpswarm

ENV JAVA_HOME /usr/lib/jvm/java-1.8.0-openjdk-amd64/

RUN keytool -noprompt -importcert -trustcacerts \
    -file pert-demoenergy-virtus.ismb.polito.it.pem -alias pert-demoenergy-virtus.ismb.polito.it \
    -storepass changeit -keystore -J-Duser.language=en $JAVA_HOME/jre/lib/security/cacerts

USER 1000

ENTRYPOINT ["/home/vncStartup/vnc_startup.sh"]
CMD ["--wait"]


