#!/usr/bin/env python
# Copyright 2018 Chathuranga Abeyrathna. All Rights Reserved.
# AWS OpsWorks deployment cli

# update custom cookbooks

import sys
import getopt
import boto3
import time
import modules.common_functions


def update_custom_cookbooks():
    try:
        opts, args = getopt.getopt(sys.argv[2:], 'r:s:l:i:h', [
            'region=', 'stack=', 'layer=', 'help'
        ])
    except getopt.GetoptError:
        modules.common_functions.update_custom_cookbooks_usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            modules.common_functions.update_custom_cookbooks_usage()
        elif opt in ('-r', '--region'):
            region = arg
        elif opt in ('-s', '--stack'):
            stack = arg
        elif opt in ('-l', '--layer'):
            layer = arg
        else:
            modules.common_functions.update_custom_cookbooks_usage()

    modules.common_functions.get_names(stack, layer, region, "update_custom_cookbooks")
    # initiate boto3 client
    client = boto3.client('opsworks', region_name=region)
    # calling deployment to specified stack layer
    run_update_custom_cookbooks = client.create_deployment(
        StackId=stack,
        LayerIds=[
            layer,
        ],
        Command={
            'Name': 'update_custom_cookbooks'
        },
        Comment='automated update_custom_cookbooks job'
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

    deploymentId = run_update_custom_cookbooks['DeploymentId']
    # sending describe command to get status"""  """
    modules.common_functions.get_status(deploymentId, region, instances)
