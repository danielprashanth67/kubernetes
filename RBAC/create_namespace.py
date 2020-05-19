from __future__ import print_function
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint
from get_config import cluster_config
from parse_config import parse_config
import json


class CreateNamespace:

    def __init__(self, path):
        self.path = path

    def create_namespace(self):
        data_config = parse_config(self.path)
        for config in data_config:
            clustername = config['clustername']
            api_instance = kubernetes.client.CoreV1Api(kubernetes.client.ApiClient(cluster_config(clustername)))
            namespace = config['namespace']
            body = kubernetes.client.V1Namespace(metadata=kubernetes.client.V1ObjectMeta(name=namespace))
            pretty = 'true'  # str | If 'true', then the output is pretty printed. (optional)
            try:
                api_response = api_instance.create_namespace(body, pretty=pretty)
                pprint(api_response)
            except ApiException as e:
                error = json.loads(e.body)
                print(error['message'])
