#!/usr/bin/env python3
import os
import sys
import subprocess
from pathlib import Path

def main():
    subprocess.run(["xhost", "+local:"], check=True)
    image = "autopara:latest"
    network_mode = "host"
    container_name = "autopara-dev"
    ws_path = os.path.expanduser(f"{Path.home()}/github/autopara/ws")
    
    if not os.path.exists(ws_path):
        print(f"Creating ROS2 workspace directory: {ws_path}")
        os.makedirs(ws_path, exist_ok=True)
    
    docker_cmd = [
        "docker", "run", "-it", "--rm",
        "--name", container_name,
        "--hostname", "autopara-dev",
        "--gpus", "all",
        "--runtime=nvidia",
        "-e", "NVIDIA_VISIBLE_DEVICES=all",
        "-e", "NVIDIA_DRIVER_CAPABILITIES=all",
        "-e", f"DISPLAY={os.environ['DISPLAY']}",
        "-e", "__NV_PRIME_RENDER_OFFLOAD=1",
        "-e", "__GLX_VENDOR_LIBRARY_NAME=nvidia",
        "-v", "/tmp/.X11-unix:/tmp/.X11-unix",
        "-v", f"{ws_path}:/home/ubuntu/ws",
        image,
        "/bin/bash"
    ]
    
    try:
        subprocess.run(docker_cmd)
    except KeyboardInterrupt:
        print("\nStopping container...")
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
