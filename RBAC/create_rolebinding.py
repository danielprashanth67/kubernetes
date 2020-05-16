from __future__ import print_function
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint
from get_config import cluster_config


class CreateRoleBinding:
    def __init__(self, namespace, clustername):
        self.namespace = namespace
        self.clustername = clustername

    def create_role_binding(self):
        # create an instance of the API class
        api_instance = kubernetes.client.RbacAuthorizationV1Api(
            kubernetes.client.ApiClient(cluster_config(self.clustername)))
        namespace = self.namespace  # str | object name and auth scope, such as for teams and projects
        body = kubernetes.client.V1RoleBinding(metadata=kubernetes.client.V1ObjectMeta(name=self.namespace),
                                               role_ref=kubernetes.client.V1RoleRef(
                                                   api_group='rbac.authorization.k8s.io', kind='Role',
                                                   name='self.namespace'))  # V1Role |
        pretty = 'true'  # str | If 'true', then the output is pretty printed. (optional)
        try:
            api_response = api_instance.create_namespaced_role_binding(namespace, body, pretty=pretty)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling RbacAuthorizationV1Api->create_namespaced_role: %s\n" % e)
