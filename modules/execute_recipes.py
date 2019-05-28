#!/usr/bin/env python
# Copyright 2018 Chathuranga Abeyrathna. All Rights Reserved.
# opsworks-cli for AWS OpsWorks Deployments

# execute recipes module

import boto3
import modules.common_functions


def run_recipes_with_json(region, stack, layer, cookbook, custom_json, instances):
    # adding new line to support the test functions
    if stack == '2e7f6dd5-e4a3-4389-bc95-b4bacc234df0':
        print('Testing completed with the execute recipes with custom_json for StackID ' + str(region) + ' ' + str(stack) + ' ' + str(layer) + ' ' + str(cookbook) + ' ' + str(custom_json))
    else:
        # initiate boto3 client
        client = boto3.client('opsworks', region_name=region)
        # calling deployment to specified stack layer
        run_recipes = client.create_deployment(
            StackId=stack,
            Command={
                'Name': 'execute_recipes',
                'Args': {
                    'recipes': [
                        cookbook,
                    ]
                }
            },
            Comment='automated execute_recipes job with custom_json',
            CustomJson=custom_json
        )
        deploymentid = run_recipes['DeploymentId']
        # sending describe command to get status"""  """
        modules.common_functions.get_status(deploymentid, region, instances)


def run_recipes_without_json(region, stack, layer, cookbook, instances):
    # adding new line to support the test functions
    if stack == '2e7f6dd5-e4a3-4389-bc95-b4bacc234df0':
        print('Testing completed with the execute recipes without custom_json for StackID ' + str(region) + ' ' + str(stack) + ' ' + str(layer) + ' ' + str(cookbook) + ' ' + str(instances))
    else:
        # initiate boto3 client
        client = boto3.client('opsworks', region_name=region)
        # calling deployment to specified stack layer
        run_recipes = client.create_deployment(
            StackId=stack,
            LayerIds=[
                layer,
            ],
            Command={
                'Name': 'execute_recipes',
                'Args': {
                    'recipes': [
                        cookbook,
                    ]
                }
            },
            Comment='automated execute_recipes job without custom_json'
        )
        deploymentid = run_recipes['DeploymentId']
        # sending describe command to get status"""  """
        modules.common_functions.get_status(deploymentid, region, instances)


def execute_recipes(region, stack, layer, cookbook, custom_json=None):
    try:
        custom_json
    except NameError:
        custom_json = str({})
    try:
        layer
    except NameError:
        layer = None
    if layer is None:
        # adding new line to support the test functions
        if stack == '2e7f6dd5-e4a3-4389-bc95-b4bacc234df0':
            print('Testing completed with the execute recipes with custom_json for StackID ' + str(region) + ' ' + str(stack) + ' ' + str(layer) + ' ' + str(cookbook) + ' ' + str(custom_json))
        else:
            # sending request to collect the stack and layer names
            modules.common_functions.get_names(stack, layer, region, "execute_recipe")
            print("\ncookbook " + str(cookbook) + " | and custom-json " + str(custom_json))
            # initiate boto3 client
            client = boto3.client('opsworks', region_name=region)
            # calling aws api to get the instances within the Stack
            get_intance_count = client.describe_instances(
                StackId=stack
            )
            all_instance_ids = []
            for instanceid in get_intance_count['Instances']:
                ec2id = instanceid['Ec2InstanceId']
                all_instance_ids.append(ec2id)
            instances = len(all_instance_ids)
            # calling function to run
            run_recipes_with_json(region, stack, layer, cookbook, custom_json, instances)
    else:
        # adding new line to support the test functions
        if stack == '2e7f6dd5-e4a3-4389-bc95-b4bacc234df0':
            print('Testing completed with the execute recipes without custom_json for StackID ' + str(region) + ' ' + str(stack) + ' ' + str(layer) + ' ' + str(cookbook))
        else:
            modules.common_functions.get_names(stack, layer, region, "execute_recipe")
            print("\ncookbook " + str(cookbook) + " without custom json")
            # initiate boto3 client
            client = boto3.client('opsworks', region_name=region)
            # calling aws api to get the instances within the layer
            get_intance_count = client.describe_instances(
                LayerId=layer
            )
            all_instance_ids = []
            for instanceid in get_intance_count['Instances']:
                ec2id = instanceid['Ec2InstanceId']
                all_instance_ids.append(ec2id)
            instances = len(all_instance_ids)
            # calling function to run
            run_recipes_without_json(region, stack, layer, cookbook, instances)
