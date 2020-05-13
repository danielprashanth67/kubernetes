import boto3

client = boto3.client('eks')


class CreateNode:
    def __init__(self, node_name, cluster_name):
        self.node_name = node_name
        self.cluster_name = cluster_name

    def create_node(self):
        response = client.create_nodegroup(
            clusterName=self.cluster_name,
            nodegroupName=self.node_name,
            scalingConfig={
                'minSize': 1,
                'maxSize': 2,
                'desiredSize': 1
            },
            diskSize=4,
            subnets=[
                'subnet-5028732a',
                'subnet-cd62e181',
            ],
            instanceTypes=[
                't2.micro',
            ],
            amiType='AL2_x86_64',
            remoteAccess={
                'ec2SshKey': 'eks-node',
            },
            nodeRole='arn:aws:iam::889849497923:role/NodeInstanceRole',
            labels={
                'test': 'test'
            },
            tags={
                'test': 'test'
            },
        )
        return response
