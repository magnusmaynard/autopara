#!/usr/bin/env python3

import subprocess

def build():
    image_name = "autopara:latest"
    try:
        result = subprocess.run(["docker", "build", "-t", image_name, "."], check=True)
        return result.returncode
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return e.returncode
    except Exception as e:
        print(f"Unexpected error: {e}")
        return 1

if __name__ == "__main__":
    build()