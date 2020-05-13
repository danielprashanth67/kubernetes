import boto3

client = boto3.client('eks')


class CreateCluster:

    def __init__(self, cluster_name):
        self.cluster_name = cluster_name

    def create_cluster(self):
        response = client.create_cluster(
            version='1.15',
            name=self.cluster_name,
            resourcesVpcConfig={
                'securityGroupIds': [
                    'sg-dc7488b8'
                ],
                'subnetIds': [
                    'subnet-5028732a',
                    'subnet-cd62e181',
                ],
            },
            roleArn='arn:aws:iam::889849497923:role/eksClusterRole',
        )
        return response
