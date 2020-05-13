from createcluster import CreateCluster
from nodes import CreateNode
from describecluster import DescribeCluster
from describenodegroup import DescribeNodeGroup
import time
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--nodename', dest='nodename')
    parser.add_argument('--clustername', dest='clustername')
    args = parser.parse_args()
    nodename = args.nodename
    clustername = args.clustername
    a = CreateCluster(clustername)
    a.create_cluster()
    print('------------------Cluster creation has started-------------------')
    x = DescribeCluster(clustername)
    cluster_status = x.describe_cluster()
    while cluster_status != 'ACTIVE':
        time.sleep(30)
        cluster_status = x.describe_cluster()
        print('-----------------Cluster Status is ' + cluster_status + ' -----------------')
        if cluster_status == 'ACTIVE':
            break
        elif cluster_status == 'FAILED':
            raise ValueError('Cluster creation has failed')
        else:
            continue

    b = CreateNode(nodename, clustername)
    b.create_node()
    print('------------------nodegroup creation has started-------------------')
    k = DescribeNodeGroup(nodename, clustername)
    node_status = k.describe_nodegroup()
    while node_status != 'ACTIVE':
        time.sleep(30)
        node_status = k.describe_nodegroup()
        print('-----------------nodegroup Status is ' + node_status + ' -----------------')
        if node_status == 'ACTIVE':
            break
        elif node_status == 'FAILED':
            raise ValueError('nodegroup creation has failed')
        else:
            continue


if __name__ == "__main__":
    main()
