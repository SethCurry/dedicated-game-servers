import subprocess
import sys

from .docgen import Info

def build_docker(info: Info, path: str = "."):
  subprocess.run(["docker", "build", "-t", f"{info.docker.image}:{info.docker.tag}", "."], cwd=path, stdout=sys.stdout, stderr=sys.stderr)

def save_docker(info: Info, path: str = ".") -> str:
  outpath = f"{path}/{info.docker.image.replace('/', '_')}-{info.docker.tag}.tar"
  subprocess.run(["docker", "save", f"{info.docker.image}:{info.docker.tag}", "-o", outpath], cwd=path, stdout=sys.stderr, stderr=sys.stderr)
  return outpath
