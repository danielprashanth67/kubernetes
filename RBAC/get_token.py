import subprocess
import json


def get_token(clustername):
    args = ("aws", "eks", "get-token", "--cluster-name", clustername)
    popen = subprocess.Popen(args, stdout=subprocess.PIPE)
    popen.wait()
    response = popen.stdout.read()
    response = json.loads(response)
    return response['status']['token']
