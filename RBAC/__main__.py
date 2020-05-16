import argparse
from create_namespace import CreateNamespace
from create_service_account import CreateServiceAccount
from create_role import CreateRole
from create_rolebinding import CreateRoleBinding


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--clustername', dest='clustername')
    parser.add_argument('--namespace', dest='namespace')
    args = parser.parse_args()
    a = CreateNamespace(args.namespace, args.clustername)
    a.create_namespace()
    b = CreateServiceAccount(args.namespace, args.clustername)
    b.create_service_account()
    c = CreateRole(args.namespace, args.clustername)
    c.create_role()
    d = CreateRoleBinding(args.namespace, args.clustername)
    d.create_role_binding()


if __name__ == "__main__":
    main()
