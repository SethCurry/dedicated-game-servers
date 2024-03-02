import argparse
import subprocess
import os
import sys

from dgs.game.build import build_docker, save_docker
from dgs.game.docgen import dynamic_import

parser  = argparse.ArgumentParser(description='Build and upload Docker containers to hosts')

parser.add_argument('-s', '--server', help='Server to upload the container to', required=True)
parser.add_argument('-u', '--user', help='User to upload the container as', default='root')
parser.add_argument('-r', '--runtime', help='Runtime to use for the container', default='ctr')
parser.add_argument('-g', '--games', help="Comma-separated list of games to build")
parser.add_argument('-t', '--temp', help="Temporary directory to store the Docker image", default="/tmp")
parser.add_argument('-d', '--delete', action='store_true', help="Delete the Docker image after uploading it")

args = parser.parse_args()

games = []

if args.games:
  games = args.games.split(',')
else:
  for entry in os.listdir('.'):
    if os.path.isdir(entry):
      if os.path.exists(f'{entry}/info.py'):
        games.append(entry)

for game in games:
  print("Building", game)
  info = dynamic_import("info", f'{game}/info.py').info
  build_docker(info, path=f"{game}/docker")

  image_path = save_docker(info, path=f"/tmp")

  print("Syncing", image_path, "to", f"{args.user}@{args.server}:{image_path}")
  subprocess.run(["rsync", "-avHSP", image_path, f"{args.user}@{args.server}:{image_path}"], stdout=sys.stdout, stderr=sys.stderr)
  print("Importing image on", args.server)
  subprocess.run(["ssh", f"{args.user}@{args.server}", f"{args.runtime} -n k8s.io images import {image_path}"], stdout=sys.stdout, stderr=sys.stderr)

  if args.delete:
    print("Removing cached image on", args.server)
    subprocess.run(["ssh", f"{args.user}@{args.server}", f"rm {image_path}"], stdout=sys.stdout, stderr=sys.stderr)
