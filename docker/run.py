#!/usr/bin/env python3

import os
import sys
import subprocess
from pathlib import Path


def main():
    image = "autopara:latest"
    network_mode = "host"
    ws_path = os.path.expanduser(f"{Path.home()}/github/autopara/ws")
    
    if not os.path.exists(ws_path):
        print(f"Creating ROS2 workspace directory: {ws_path}")
        os.makedirs(ws_path, exist_ok=True)
    
    docker_cmd = [
        "docker", "run", "-it", "--rm",
        "--network", network_mode,
        "-e", "DISPLAY",
        "-v", "/tmp/.X11-unix:/tmp/.X11-unix",
        "-e", "XAUTHORITY=/tmp/.Xauthority",
        "-v", f"{os.environ.get('XAUTHORITY', os.path.expanduser('~/.Xauthority'))}:/tmp/.Xauthority:ro",
        "-e", "QT_X11_NO_MITSHM=1",
        "-v", "/run/user/$(id -u)/pulse:/run/user/1000/pulse",
        "-e", "PULSE_SERVER=unix:/run/user/1000/pulse/native",
        "-v", f"{ws_path}:/root/ws",
        image,
        "/bin/bash"
    ]
    
    print("Starting ROS2 Docker container with GUI support...")
    print(" ".join(docker_cmd))
    
    try:
        subprocess.run(docker_cmd)
    except KeyboardInterrupt:
        print("\nStopping container...")
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    try:
        subprocess.run(["xhost", "+local:"], check=True)
    except subprocess.CalledProcessError:
        print("Warning: Could not set xhost permissions. GUI might not work.")
    
    sys.exit(main())