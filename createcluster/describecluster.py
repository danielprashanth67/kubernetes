import boto3
import json

client = boto3.client('eks')


class DescribeCluster:
    def __init__(self, cluster_name):
        self.cluster_name = cluster_name

    def describe_cluster(self):
        response = client.describe_cluster(
            name=self.cluster_name)
        return response['cluster']['status']
