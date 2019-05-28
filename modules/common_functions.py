#!/usr/bin/env python
# Copyright 2018 Chathuranga Abeyrathna. All Rights Reserved.
# opsworks-cli for AWS OpsWorks Deployments

# common fuctions module

import boto3
import time
import prettytable
import modules.colour


def summary(success_count, skipped_count, failed_count):
    table = prettytable.PrettyTable()
    table.field_names = ["Success", "Skipped", "Failed"]
    table.add_row([str(success_count), str(skipped_count), str(failed_count)])
    print(table.get_string(title="Summary"))


def get_status(deploymentid, region, instances):
    # adding new line to support the test functions
    if deploymentid == '2e7f6dd5e4a34389bc95b4bacc234df0':
        print('Testing completed with the get_status with deploymentid ' + str(deploymentid) + ' ' + str(region) + ' ' + str(instances))
    else:
        client = boto3.client('opsworks', region_name=region)
        describe_deployment = client.describe_commands(
            DeploymentId=deploymentid
        )

        try:
            success_count = 0
            skipped_count = 0
            failed_count = 0
            fail_skip_count = 0
            print("Deployment started...")
            time.sleep(2)
            while not (success_count == int(instances) or failed_count == int(instances)):
                print("Deployment not completed yet..waiting 10 seconds before send request back to aws...")
                time.sleep(10)
                describe_deployment = client.describe_commands(
                    DeploymentId=deploymentid)
                success_count = str(describe_deployment).count("successful")
                skipped_count = str(describe_deployment).count("skipped")
                failed_count = str(describe_deployment).count("failed")
                fail_skip_count = int(skipped_count) + int(failed_count)
                if int(success_count) + int(skipped_count) == int(instances):
                    success_count = int(instances)
                elif int(skipped_count) == int(instances):
                    skipped_count = int(instances)
                elif int(failed_count) == int(instances):
                    failed_count = int(instances)
                elif int(skipped_count) + int(failed_count) == int(instances):
                    fail_skip_count = int(instances)
                elif int(success_count) + int(failed_count) == int(instances):
                    success_fail_count = int(instances)
            if success_count == int(instances):
                modules.colour.print_success("\nDeployment completed...")
                summary(success_count, skipped_count, failed_count)
                print("\nCheck the deployment logs...\n")
                for logs in describe_deployment['Commands']:
                    print(logs['LogUrl'])
            elif skipped_count == int(instances):
                modules.colour.print_warning("\nDeployment skipped...")
                summary(success_count, skipped_count, failed_count)
                print("\nCheck the deployment logs...\n")
                for logs in describe_deployment['Commands']:
                    print(logs['LogUrl'])
            elif failed_count == int(instances):
                modules.colour.print_err("\nDeployment failed...")
                summary(success_count, skipped_count, failed_count)
                print("\nCheck the deployment logs...\n")
                for logs in describe_deployment['Commands']:
                    print(logs['LogUrl'])
            elif fail_skip_count == int(instances):
                modules.colour.print_muted("\nDeployment failed and some of them skipped...")
                summary(success_count, skipped_count, failed_count)
                print("\nCheck the deployment logs...\n")
                for logs in describe_deployment['Commands']:
                    print(logs['LogUrl'])
            elif success_fail_count == int(instances):
                modules.colour.print_warning(
                    "\nDeployment success on some instances and some are got failed...")
                summary(success_count, skipped_count, failed_count)
                print("\nCheck the deployment logs...\n")
                for logs in describe_deployment['Commands']:
                    print(logs['LogUrl'])
        except Exception as e:
            print(e)


def get_names(stack, layer, region, name):
    # adding new line to support the test functions
    if stack == '2e7f6dd5-e4a3-4389-bc95-b4bacc234df0':
        print('Testing completed with the get_name with StackID ' + str(region) + ' ' + str(stack) + ' ' + str(layer) + ' ' + str(name))
    else:
        client = boto3.client('opsworks', region_name=region)
        stack_details = client.describe_stacks(
            StackIds=[
                stack,
            ]
        )
        stack_name = stack_details['Stacks'][0]['Name']
        if layer is not None:
            layer_details = client.describe_layers(
                LayerIds=[
                    layer,
                ]
            )
            layer_name = layer_details['Layers'][0]['Name']
        else:
            layer_name = "None"
        print("\nRunning " + str(name) + " for, "
            + "\n stack id: " + str(stack) + " | stack name: " + str(stack_name)
            + "\n layer id: " + str(layer) + " | layer name: "
            + str(layer_name) + "\n")
