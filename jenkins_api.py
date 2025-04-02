import requests


if __name__ == '__main__':
    req=requests.post(
        url='http://172.20.184.42:8080/job/autotest/buildWithParameters?token=rlxfhhPAWRQILval&test_env=生产环境_gzvip1&test_model=仅执行菜单遍历'
    )
    print(req.text)
