import os

import jenkins
from config.config import (
    JENKINS_URL,
    JENKINS_USERNAME,
    JENKINS_PASSWORD,
    JENKINS_TOKEN,
    DEFAULT_TEST_MODEL,
    DEFAULT_TEST_FEATURE
)

if __name__ == '__main__':

    try:
        test_models = os.environ['test_model']
    except KeyError:
        test_models = DEFAULT_TEST_MODEL

    try:
        test_features = os.environ['test_feature']
    except KeyError:
        test_features = DEFAULT_TEST_FEATURE

    jenkins_server = jenkins.Jenkins(
        JENKINS_URL,
        JENKINS_USERNAME,
        JENKINS_PASSWORD
    )

    test_env = [
        '生产环境_gzvip1',
        '生产环境_main',
        '生产环境_vip0',
        '生产环境_vip1',
        '生产环境_vip2',
        '生产环境_vip3',
        '生产环境_vip4',
        '生产环境_vip5',
        '生产环境_vip6',
        '生产环境_gzmain',
        '生产环境_gzvip0'
    ]

    for _ in test_env:
        params = {
            'test_env': _,
            'test_model': test_models,
            'test_feature': test_features
        }

        jenkins_server.build_job('autotest', params, JENKINS_TOKEN)
