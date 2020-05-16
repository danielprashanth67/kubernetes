from get_token import get_token
import kubernetes.client


def cluster_config(clustername):
    # create an instance of the API class
    # Configure API key authorization: BearerToken
    configuration = kubernetes.client.Configuration()
    configuration.api_key['authorization'] = get_token(clustername)
    configuration.host = 'https://584852762EFDA04D84B11B551DA2AFBA.yl4.us-east-2.eks.amazonaws.com'
    configuration.verify_ssl = False
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    configuration.api_key_prefix['authorization'] = 'Bearer'
    return configuration
