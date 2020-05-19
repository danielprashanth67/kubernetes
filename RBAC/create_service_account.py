from __future__ import print_function

import json
from pprint import pprint

import kubernetes.client
from kubernetes.client.rest import ApiException

from get_config import cluster_config
from parse_config import parse_config

import send_credentials


class CreateServiceAccount:

    def __init__(self, path):
        self.path = path

    def create_service_account(self):
        # create an instance of the API class
        data_config = parse_config(self.path)
        for config in data_config:
            namespace = config['namespace']
            name = config['User']['name'] + '-' + config['User'][
                'email']
            name = name.split('@', 1)[0]  # str | object name and auth scope, such as for teams and projects
            clustername = config['clustername']
            a = send_credentials.SendCredentials(clustername)
            api_instance = kubernetes.client.CoreV1Api(kubernetes.client.ApiClient(cluster_config(clustername)))
            body = kubernetes.client.V1ServiceAccount(
                metadata=kubernetes.client.V1ObjectMeta(name=name))
            pretty = 'pretty_example'  # str | If 'true', then the output is pretty printed. (optional)
            field_manager = config['namespace']

            try:
                api_response = api_instance.create_namespaced_service_account(namespace, body, pretty=pretty,
                                                                              field_manager=field_manager)
                secret = a.get_secret(name, namespace)
                credential = a.get_credentials(secret, namespace)
                a.send_credentials(credential, name)
                pprint(api_response)
            except ApiException as e:
                error = json.loads(e.body)
                print(error['message'])
