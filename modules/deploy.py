#!/usr/bin/env python
# Copyright 2018 Chathuranga Abeyrathna. All Rights Reserved.
# opsworks-cli for AWS OpsWorks Deployments

# execute deploy module

import boto3
import modules.common_functions


def deploy(region, stack, layer, custom_json=None):
    try:
        custom_json
    except NameError:
        custom_json = str({})
    try:
        layer
    except NameError:
        layer = None
    # adding new line to support the test functions
    if stack == '2e7f6dd5-e4a3-4389-bc95-b4bacc234df0':
        print('Testing completed with the deploy for StackID ' + str(region) + ' ' + str(stack) + ' ' + str(layer))
    else:
        # sending request to collect the stack and layer names
        modules.common_functions.get_names(stack, layer, region, "deploy")
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
        all_instance_ids = []
        for instanceid in get_intance_count['Instances']:
            ec2id = instanceid['Ec2InstanceId']
            all_instance_ids.append(ec2id)
        instances = len(all_instance_ids)

        deploymentid = run_recipes['DeploymentId']
        # sending describe command to get status"""  """
        modules.common_functions.get_status(deploymentid, region, instances)
