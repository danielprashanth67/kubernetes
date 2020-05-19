import socket

import kubernetes.client
from kubernetes.client.rest import ApiException
from parse_config import parse_config
from get_config import cluster_config
import json
import smtplib


class SendCredentials:

    def __init__(self, clustername):
        self.exact = True
        self.export = True
        self.clustername = clustername
        self.api_instance = kubernetes.client.CoreV1Api(
            kubernetes.client.ApiClient(cluster_config(self.clustername)))

    def jdefault(self, o):
        return o.__dict__

    def get_secret(self, name, namespace):
        # create an instance of the API class
        secret_token = []
        pretty = 'true'
        api_response = self.api_instance.read_namespaced_service_account(name, namespace,
                                                                         pretty=pretty, exact=self.exact,
                                                                         export=self.export)
        data = json.dumps(api_response, default=self.jdefault)
        json_data = json.loads(data)
        secrets = json_data['_secrets']
        for secret in secrets:
            secret_token.append(secret['_name'])
        return str(secret_token).strip('[]').split('u', 1)[1].strip('\"').strip('\'')

    def get_credentials(self, secret, namespace):
        pretty = 'true'
        api_response = self.api_instance.read_namespaced_secret(secret, namespace,
                                                                pretty=pretty, exact=self.exact,
                                                                export=self.export)
        data = json.dumps(api_response, default=self.jdefault)
        json_data = json.loads(data)
        return json_data

    def send_credentials(self, json_data, recipient):
        gmail_user = 'danielprashanth67@gmail.com'
        gmail_password = 'xxxxxx'
        sent_from = gmail_user

        recipient = recipient.split('-', 1)[1] + '@gmail.com'
        to = recipient
        subject = 'Credentials for your namespace'
        body = json_data
        email_text = """\
        From: %s
        To: %s
        Subject: %s

        %s
        """ % (sent_from, ", ".join(to), subject, body)

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(sent_from, to, email_text)
            server.close()
            print 'Email sent!'
        except:
            print 'Something went wrong...'
