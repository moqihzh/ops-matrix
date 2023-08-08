import json
import sys

from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cdn.v20180606 import cdn_client, models


if __name__ == '__main__':
    domains = sys.argv[1:]
    domains = str(domains).replace(',',' ').strip("']").strip("['").split(' ')
    try:
        cred = credential.Credential("", "")
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

        resp = client.PurgePathCache(req)
        print(resp)
        print('refresh cdn success')

    except TencentCloudSDKException as err:
        print(err)