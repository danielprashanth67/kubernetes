from __future__ import print_function
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint
from get_config import cluster_config


class CreateNamespace:

    def __init__(self, namespace, clustername):
        self.namespace = namespace
        self.clustername = clustername

    def create_namespace(self):
        api_instance = kubernetes.client.CoreV1Api(kubernetes.client.ApiClient(cluster_config(self.clustername)))
        body = kubernetes.client.V1Namespace(metadata=kubernetes.client.V1ObjectMeta(name=self.namespace))
        pretty = 'true'  # str | If 'true', then the output is pretty printed. (optional)
        try:
            api_response = api_instance.create_namespace(body, pretty=pretty)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CoreV1Api->create_namespace: %s\n" % e)
