from __future__ import print_function
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint
from get_config import cluster_config


class CreateServiceAccount:
    def __init__(self, namespace, clustername):
        self.namespace = namespace
        self.clustername = clustername

    def create_service_account(self):
        # create an instance of the API class
        api_instance = kubernetes.client.CoreV1Api(kubernetes.client.ApiClient(cluster_config(self.clustername)))
        namespace = self.namespace  # str | object name and auth scope, such as for teams and projects
        body = kubernetes.client.V1ServiceAccount(metadata=kubernetes.client.V1ObjectMeta(name=self.namespace))
        pretty = 'pretty_example'  # str | If 'true', then the output is pretty printed. (optional)
        field_manager = self.namespace

        try:
            api_response = api_instance.create_namespaced_service_account(namespace, body, pretty=pretty,
                                                                          field_manager=field_manager)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CoreV1Api->create_namespaced_service_account: %s\n" % e)
