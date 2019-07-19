#!/usr/bin/env python
# Copyright 2018 Chathuranga Abeyrathna. All Rights Reserved.
# opsworks-cli for AWS OpsWorks Deployments

# update custom cookbooks module

import boto3
import prettytable
import modules.common_functions


def test_output_summary(region, stack, layer):
    table = prettytable.PrettyTable()
    table.field_names = ["Region", "StackID", "LayerID"]
    table.add_row([str(region), str(stack), str(layer)])
    print(table.get_string(title="Test Input Summary"))


def update_custom_cookbooks_with_layer(region, stack, layer):
    # adding new line to support the test functions
    if stack == '2e7f6dd5-e4a3-4389-bc95-b4bacc234df0':
        print('update_custom_cookbooks_with_layer sub function testing')
        test_output_summary(region, stack, layer)
    else:
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
        all_instance_status = []
        for instancestatus in get_intance_count['Instances']:
            ec2status = instancestatus['Status']
            all_instance_status.append(ec2status)
        instances = len(all_instance_status)

        deploymentid = run_update_custom_cookbooks['DeploymentId']
        # sending describe command to get status"""  """
        modules.common_functions.get_status(deploymentid, region, instances)


def update_custom_cookbooks_without_layer(region, stack):
    # adding new line to support the test functions
    if stack == '2e7f6dd5-e4a3-4389-bc95-b4bacc234df0':
        print('update_custom_cookbooks_without_layer sub function testing')
        layer = None
        test_output_summary(region, stack, layer)
    else:
        # initiate boto3 client
        client = boto3.client('opsworks', region_name=region)
        # calling deployment to specified stack
        run_update_custom_cookbooks = client.create_deployment(
            StackId=stack,
            Command={
                'Name': 'update_custom_cookbooks'
            },
            Comment='automated update_custom_cookbooks job'
        )

        # calling aws api to get the instances within the layer
        get_intance_count = client.describe_instances(
            StackId=stack
        )
        all_instance_status = []
        for instancestatus in get_intance_count['Instances']:
            ec2status = instancestatus['Status']
            all_instance_status.append(ec2status)
        instances = len(all_instance_status)

        deploymentid = run_update_custom_cookbooks['DeploymentId']
        # sending describe command to get status"""  """
        modules.common_functions.get_status(deploymentid, region, instances)


def update_custom_cookbooks(region, stack, layer):
    # adding new line to support the test functions
    if stack == '2e7f6dd5-e4a3-4389-bc95-b4bacc234df0':
        print('update_custom_cookbooks main function testing')
        test_output_summary(region, stack, layer)
    else:
        # sending request to collect the stack and layer names
        modules.common_functions.get_names(stack, layer, region, "update_custom_cookbooks")
        if layer is None:
            update_custom_cookbooks_without_layer(region, stack)
        else:
            update_custom_cookbooks_with_layer(region, stack, layer)
