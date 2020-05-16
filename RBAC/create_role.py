from __future__ import print_function
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint
from get_config import cluster_config
from parse_config import parse_config


class CreateRole:
    def __init__(self, path):
        self.path = path

    def create_role(self):
        config = parse_config(self.path)
        # create an instance of the API class
        api_instance = kubernetes.client.RbacAuthorizationV1Api(
            kubernetes.client.ApiClient(cluster_config(config['clustername'])))
        namespace = config['namespace']  # str | object name and auth scope, such as for teams and projects
        verbs = config['verbs']
        resources = config['resources']
        apiGroups = config['api_groups']
        body = kubernetes.client.V1Role(metadata=kubernetes.client.V1ObjectMeta(name=namespace), rules=[
            kubernetes.client.V1PolicyRule(verbs=verbs, resources=resources, api_groups=apiGroups)])  # V1Role |
        pretty = 'true'  # str | If 'true', then the output is pretty printed. (optional)
        try:
            api_response = api_instance.create_namespaced_role(namespace, body, pretty=pretty)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling RbacAuthorizationV1Api->create_namespaced_role: %s\n" % e)
