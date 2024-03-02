import subprocess

from .docgen import Info

def build_docker(info: Info, path: str = "."):
  subprocess.run(["docker", "build", "-t", f"{info.docker.image}:{info.docker.tag}", "."], cwd=path, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def save_docker(info: Info, path: str = "."):
  subprocess.run(["docker", "save", f"{info.docker.image}:{info.docker.tag}", "-o", f"{info.docker.image}-{info.docker.tag}.tar"], cwd=path, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
