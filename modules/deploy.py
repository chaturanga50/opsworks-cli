#!/usr/bin/env python
# Copyright 2018 Chathuranga Abeyrathna. All Rights Reserved.
# AWS OpsWorks deployment cli

# execute recipes

import sys
import getopt
import boto3
import time
from common_functions import deploy_usage
from common_functions import get_names
from common_functions import get_status


def deploy():
    try:
        opts, args = getopt.getopt(sys.argv[2:], 'r:s:l:h', [
            'region=', 'stack=', 'layer=', 'help'
        ])
    except getopt.GetoptError:
        deploy_usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            deploy_usage()
        elif opt in ('-r', '--region'):
            region = arg
        elif opt in ('-s', '--stack'):
            stack = arg
        elif opt in ('-l', '--layer'):
            layer = arg
        else:
            deploy_usage()
    try:
        custom_json
    except NameError:
        custom_json = str({})
    try:
        layer
    except NameError:
        layer = None
        get_names(stack, layer, region, "deploy")
        # initiate boto3 client
        client = boto3.client('opsworks', region_name=region)
        # calling deployment to specified stack layer
        run_recipes = client.create_deployment(
            StackId=stack,
            LayerIds=[
                layer,
            ],
            Command={
                'Name': 'deploy',
            },
            Comment='automated deploy job'
        )

        # calling aws api to get the instances within the layer
        get_intance_count = client.describe_instances(
            LayerId=layer
        )
        all_instance_IDs = []
        for instanceid in get_intance_count['Instances']:
            ec2id = instanceid['Ec2InstanceId']
            all_instance_IDs.append(ec2id)
        instances = len(all_instance_IDs)

    deploymentId = run_recipes['DeploymentId']
    # sending describe command to get status"""  """
    get_status(deploymentId, region, instances)