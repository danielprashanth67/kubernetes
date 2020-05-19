from __future__ import print_function
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint
from get_config import cluster_config
from parse_config import parse_config
import json


class CreateRole:
    def __init__(self, path):
        self.path = path

    def create_role(self):
        data_config = parse_config(self.path)
        for config in data_config:
            clustername = config['clustername']
            api_instance = kubernetes.client.RbacAuthorizationV1Api(
                kubernetes.client.ApiClient(cluster_config(clustername)))
            namespace = config['namespace']
            name = config['User']['name'] + '-' + config['User']['email']
            name = name.split('@', 1)[0]  # str | object name and auth scope, such as for teams and projects
            verbs = config['verbs']
            resources = config['resources']
            apiGroups = config['api_groups']
            body = kubernetes.client.V1Role(metadata=kubernetes.client.V1ObjectMeta(name=name), rules=[
                kubernetes.client.V1PolicyRule(verbs=verbs, resources=resources, api_groups=apiGroups)])  # V1Role |
            pretty = 'true'  # str | If 'true', then the output is pretty printed. (optional)
            try:
                api_response = api_instance.create_namespaced_role(namespace, body, pretty=pretty)
                pprint(api_response)
            except ApiException as e:
                error = json.loads(e.body)
                print(error['message'])
