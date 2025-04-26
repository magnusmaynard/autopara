FROM osrf/ros:jazzy-desktop-full

ARG USERNAME=ubuntu
ARG USER_ID=1000
ARG GROUP_ID=1000

USER root

RUN apt-get update && \
    apt-get install -y sudo && \
    echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME && \
    chmod 0440 /etc/sudoers.d/$USERNAME

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    tmux

ENV ROS_WS=/home/${USERNAME}/ws
RUN mkdir -p ${ROS_WS}/src

SHELL ["/bin/bash", "-c"]
RUN echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc


WORKDIR ${ROS_WS}
USER $USERNAME

CMD ["bash"]