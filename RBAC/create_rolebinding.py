from __future__ import print_function
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint
from get_config import cluster_config
from parse_config import parse_config
import json


class CreateRoleBinding:
    def __init__(self, path):
        self.path = path

    def create_role_binding(self):

        data_config = parse_config(self.path)
        for config in data_config:
            namespace = config['namespace']  # str | object name and auth scope, such as for teams and projects
            name = config['User']['name'] + '-' + config['User']['email']
            clustername = config['clustername']
            api_instance = kubernetes.client.RbacAuthorizationV1Api(
                kubernetes.client.ApiClient(cluster_config(clustername)))
            name = name.split('@', 1)[0]
            body = kubernetes.client.V1RoleBinding(metadata=kubernetes.client.V1ObjectMeta(name=name),
                                                   role_ref=kubernetes.client.V1RoleRef(
                                                       api_group='rbac.authorization.k8s.io', kind='Role',
                                                       name=name), subjects=[
                    kubernetes.client.V1Subject(name=name, kind='ServiceAccount',
                                                namespace=namespace)])  # V1Role |
            pretty = 'true'  # str | If 'true', then the output is pretty printed. (optional)
            try:
                api_response = api_instance.create_namespaced_role_binding(namespace, body, pretty=pretty)
                pprint(api_response)
            except ApiException as e:
                error = json.loads(e.body)
                print(error['message'])
