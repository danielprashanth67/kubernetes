import argparse
from create_namespace import CreateNamespace
from create_service_account import CreateServiceAccount
from create_role import CreateRole
from create_rolebinding import CreateRoleBinding
from send_credentials import SendCredentials


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--user_config_path', dest='path')
    args = parser.parse_args()
    a = CreateNamespace(args.path)
    a.create_namespace()
    b = CreateServiceAccount(args.path)
    b.create_service_account()
    c = CreateRole(args.path)
    c.create_role()
    d = CreateRoleBinding(args.path)
    d.create_role_binding()


if __name__ == "__main__":
    main()
