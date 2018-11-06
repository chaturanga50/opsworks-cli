#!/usr/bin/env python
# Copyright 2018 Chathuranga Abeyrathna. All Rights Reserved.
# AWS OpsWorks deployment cli

# common help

import sys
import getopt
import boto3
import time


def usage():
    print 'usage: aws-opsworks [options] <command> <subcommand> [<subcommand> ...] [parameters]\n'
    print 'To see help text, you can run: \n' + \
          sys.argv[0] + ' --help \n' + \
          sys.argv[0] + ' [options] --help \n'
    print 'available options:\n - execute-recipes\n - update-custom-cookbooks\n - setup\n'
    exit(0)


def execute_recipes_usage():
    print 'usage: \n' + \
        sys.argv[1] + ' --region [region] --stack [opsworks_stack_id] --layer [opsworks_layer_id] --instances [opsworks_layer_instance_count] --cookbook [cookbook] --custom-json [custom-json]'
    exit(0)


def update_custom_cookbooks_usage():
    print 'usage: \n' + \
        sys.argv[1] + ' --region [region] --stack [opsworks_stack_id] --layer [opsworks_layer_id] --instances [opsworks_layer_instance_count]\n'
    exit(0)


def setup_usage():
    print 'usage: \n' + \
        sys.argv[1] + ' --region [region] --stack [opsworks_stack_id] --layer [opsworks_layer_id] --instances [opsworks_layer_instance_count]'
    exit(0)


def get_status(deploymentId, region, instances):
    client = boto3.client('opsworks', region_name=region)
    describe_deployment = client.describe_commands(
        DeploymentId=deploymentId
    )

    try:
        success_count = 0
        skipped_count = 0
        failed_count = 0
        fail_skip_count = 0
        while success_count is not int(instances):
            print "Deployment not completed yet..waiting 10 seconds before send request back to aws..."
            time.sleep(10)
            describe_deployment = client.describe_commands(
                DeploymentId=deploymentId)
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
        if success_count == int(instances):
            print "\nDeployment completed..."
            print "Summary: \n success instances: " + \
                str(success_count) + "\n skipped instances: " + \
                str(skipped_count) + "\n failed instances: " + \
                str(failed_count) + "\n"
            print "Check the deployment logs...\n"
            for logs in describe_deployment['Commands']:
                print logs['LogUrl']
        elif skipped_count == int(instances):
            print "\nDeployment skipped..."
            print "Summary: \n success instances: " + \
                str(success_count) + "\n skipped instances: " + \
                str(skipped_count) + "\n failed instances: " + \
                str(failed_count) + "\n"
            print "Check the deployment logs...\n"
            for logs in describe_deployment['Commands']:
                print logs['LogUrl']
        elif failed_count == int(instances):
            print "\nDeployment failed..."
            print "Summary: \n success instances: " + \
                str(success_count) + "\n skipped instances: " + \
                str(skipped_count) + "\n failed instances: " + \
                str(failed_count) + "\n"
            print "Check the deployment logs...\n"
            for logs in describe_deployment['Commands']:
                print logs['LogUrl']
        elif fail_skip_count == int(instances):
            print "\nDeployment failed and some of them skipped..."
            print "Summary: \n success instances: " + \
                str(success_count) + "\n skipped instances: " + \
                str(skipped_count) + "\n failed instances: " + \
                str(failed_count) + "\n"
            print "Check the deployment logs...\n"
            for logs in describe_deployment['Commands']:
                print logs['LogUrl']
    except Exception, e:
        print e


def get_names(stack, layer, region, name):
    client = boto3.client('opsworks', region_name=region)
    stack_details = client.describe_stacks(
        StackIds=[
            stack,
        ]
    )
    stack_name = stack_details['Stacks'][0]['Name']
    layer_details = client.describe_layers(
        LayerIds=[
            layer,
        ]
    )
    layer_name = layer_details['Layers'][0]['Name']
    print "\nrunning " + str(name) + " started for, " + \
        "\n stack id: " + str(stack) + " | stack name: " + str(stack_name) + \
        "\n layer id: " + str(layer) + " | layer name: " + str(layer_name) + "\n"


def version():
    print '0.4.5'
    exit(0)
