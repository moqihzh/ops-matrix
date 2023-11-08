import json
import sys

from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cdn.v20180606 import cdn_client, models



def refresh_tencent_cdn(domains):
    domains = str(domains).replace(',',' ').strip("']").strip("['").split(' ')
    try:
        secret_id=""
        secret_key=""
        cred = credential.Credential(secret_id, secret_key)
        httpProfile = HttpProfile()
        httpProfile.endpoint = "cdn.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = cdn_client.CdnClient(cred, "ap-shanghai", clientProfile)

        req = models.PurgePathCacheRequest()
        params = {
            "Paths": domains,
            "FlushType": "delete"
        }
        req.from_json_string(json.dumps(params))

        response = client.PurgePathCache(req)
        return response

    except TencentCloudSDKException as err:
        print(err)
        
if __name__ == '__main__':
    domains = sys.argv[1:]
    response = refresh_tencent_cdn(domains)
    print("refresh cdn success,task id {}".format(response))