FROM osrf/ros:jazzy-desktop-full

ENV DEBIAN_FRONTEND=noninteractive

# Install tools
RUN apt-get update && apt-get install -y
    # build-essential

ENV ROS_WS=/root/ws
RUN mkdir -p ${ROS_WS}/src

SHELL ["/bin/bash", "-c"]
RUN echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc

WORKDIR ${ROS_WS}

CMD ["bash"]