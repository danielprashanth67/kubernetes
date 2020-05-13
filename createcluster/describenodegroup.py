import boto3
import json

client = boto3.client('eks')


class DescribeNodeGroup:
    def __init__(self, node_name, cluster_name):
        self.node_name = node_name
        self.cluster_name = cluster_name

    def describe_nodegroup(self):
        response = client.describe_nodegroup(
            clusterName=self.cluster_name,
            nodegroupName=self.node_name
        )
        return response['nodegroup']['status']
