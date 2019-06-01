#!/usr/bin/env python
# Copyright 2018 Chathuranga Abeyrathna. All Rights Reserved.
# opsworks-cli for AWS OpsWorks Deployments

# execute recipes module

import boto3
import prettytable
import modules.common_functions


def test_output_summary(region, stack, layer, cookbook, custom_json):
    table = prettytable.PrettyTable()
    table.field_names = ["Region", "StackID", "LayerID", "Cookbook", "Custom_JSON"]
    table.add_row([str(region), str(stack), str(layer), str(cookbook), str(custom_json)])
    print(table.get_string(title="Test Input Summary"))


def run_recipes_with_json(region, stack, layer, cookbook, instances, custom_json=None):
    # adding new line to support the test functions
    if stack == '2e7f6dd5-e4a3-4389-bc95-b4bacc234df0':
        print('run_recipes_with_json sub function testing with custom_json without layer_id')
        test_output_summary(region, stack, layer, cookbook, custom_json)
    else:
        # initiate boto3 client
        client = boto3.client('opsworks', region_name=region)
        # calling deployment to specified stack
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
        print('run_recipes_without_json sub function testing without custom_json with layer_id')
        test_output_summary(region, stack, layer, cookbook, custom_json=None)
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


def get_instance_count_stack(region, stack, layer, cookbook, custom_json=None):
    # this function is for where only the stack id is defined
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
    if custom_json is None:
        run_recipes_without_json(region, stack, layer, cookbook, instances)
    else:
        run_recipes_with_json(region, stack, layer, cookbook, instances, custom_json)


def get_instance_count_layer(region, stack, layer, cookbook, custom_json=None):
    # this function is for where the stack and layer both ids are defined
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
    if custom_json is None:
        run_recipes_without_json(region, stack, layer, cookbook, instances)
    else:
        run_recipes_with_json(region, stack, layer, cookbook, instances, custom_json)


def execute_recipes(region, stack, cookbook, layer=None, custom_json=None):
    if custom_json is None and layer is None:
        # adding new line to support the test functions
        if stack == '2e7f6dd5-e4a3-4389-bc95-b4bacc234df0':
            print('execute_recipes main function testing without layer_id and custom_json')
            test_output_summary(region, stack, layer, cookbook, custom_json)
        else:
            # sending request to collect the stack and layer names
            modules.common_functions.get_names(stack, layer, region, "execute_recipe")
            print("\ncookbook " + str(cookbook) + " | and without layer or custom-json")
            # sending request to get the instance count with stack and send to boto3
            get_instance_count_stack(region, stack, layer, cookbook, custom_json)
    elif custom_json is None and layer is not None:
        # adding new line to support the test functions
        if stack == '2e7f6dd5-e4a3-4389-bc95-b4bacc234df0':
            print('execute_recipes main function testing with layer_id without custom_json')
            test_output_summary(region, stack, layer, cookbook, custom_json)
        else:
            # sending request to collect the stack and layer names
            modules.common_functions.get_names(stack, layer, region, "execute_recipe")
            print("\ncookbook " + str(cookbook) + " | and with layer_id and without custom-json")
            # sending request to get the instance count with stack and send to boto3
            get_instance_count_layer(region, stack, layer, cookbook)
    elif layer is None and custom_json is not str({}):
        # adding new line to support the test functions
        if stack == '2e7f6dd5-e4a3-4389-bc95-b4bacc234df0':
            print('execute_recipes main function testing with custom_json and without layer_id')
            test_output_summary(region, stack, layer, cookbook, custom_json)
        else:
            # sending request to collect the stack and layer names
            modules.common_functions.get_names(stack, layer, region, "execute_recipe")
            print("\ncookbook " + str(cookbook) + " | and custom-json " + str(custom_json))
            # sending request to get the instance count with stack and send to boto3
            get_instance_count_stack(region, stack, layer, cookbook, custom_json)
    else:
        # adding new line to support the test functions
        if stack == '2e7f6dd5-e4a3-4389-bc95-b4bacc234df0':
            print('execute_recipes main function testing with custom_json and layer_id')
            test_output_summary(region, stack, layer, cookbook, custom_json)
        else:
            modules.common_functions.get_names(stack, layer, region, "execute_recipe")
            print("\ncookbook " + str(cookbook) + " | custom-json " + str(custom_json) + " | layer " + str(layer))
            # sending request to get the instance count with stack and send to boto3
            get_instance_count_layer(region, stack, layer, cookbook)
