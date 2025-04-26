#!/usr/bin/env python3

import os
import subprocess


def build():
    image_name = "autopara:latest"
    user_id = os.getuid()
    group_id = os.getgid()

    try:
        cmd = [
            "docker",
            "build",
            "--build-arg", f"USER_ID={user_id}",
            "--build-arg", f"GROUP_ID={group_id}",
            "--progress=plain",
            "-t",
            image_name,
            ".",
        ]

        result = subprocess.run(cmd, check=True)
        return result.returncode
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return e.returncode
    except Exception as e:
        print(f"Unexpected error: {e}")
        return 1


if __name__ == "__main__":
    build()
