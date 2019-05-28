#!/usr/bin/env python
# Copyright 2018 Chathuranga Abeyrathna. All Rights Reserved.
# AWS OpsWorks deployment cli - Unittest
# Ref - https://stackoverflow.com/questions/4219717/how-to-assert-output-with-nosetest-unittest-in-python

import sys
import unittest
import contextlib
from io import StringIO
import modules.execute_recipes
import modules.update_custom_cookbooks
import modules.deploy
import modules.setup
import modules.common_functions


class Case(unittest.TestCase):
    def test_execute_recipes(self):
        usage_stdout = StringIO()
        with contextlib.redirect_stdout(usage_stdout):
            modules.execute_recipes('eu-west-1', '2e7f6dd5-e4a3-4389-bc95-b4bacc234df0', 'ac0df176-104b-46ae-946e-7cf7367b816e', 'apache2::default')
        output = usage_stdout.getvalue().strip()
        self.assertIn('2e7f6dd5-e4a3-4389-bc95-b4bacc234df0', output)

    def test_execute_recipes_json(self):
        usage_stdout = StringIO()
        with contextlib.redirect_stdout(usage_stdout):
            modules.execute_recipes('eu-west-1', '2e7f6dd5-e4a3-4389-bc95-b4bacc234df0', 'ac0df176-104b-46ae-946e-7cf7367b816e', 'apache2::default', '{"sample": "sample"}')
        output = usage_stdout.getvalue().strip()
        self.assertIn('2e7f6dd5-e4a3-4389-bc95-b4bacc234df0', output)

    def test_run_recipes_without_json(self):
        usage_stdout = StringIO()
        with contextlib.redirect_stdout(usage_stdout):
            modules.run_recipes_without_json('eu-west-1', '2e7f6dd5-e4a3-4389-bc95-b4bacc234df0', 'ac0df176-104b-46ae-946e-7cf7367b816e', 'apache2::default', '2')
        output = usage_stdout.getvalue().strip()
        self.assertIn('2e7f6dd5-e4a3-4389-bc95-b4bacc234df0', output)

    def test_run_recipes_with_json(self):
        usage_stdout = StringIO()
        with contextlib.redirect_stdout(usage_stdout):
            modules.run_recipes_with_json('eu-west-1', '2e7f6dd5-e4a3-4389-bc95-b4bacc234df0', 'ac0df176-104b-46ae-946e-7cf7367b816e', 'apache2::default', '{"sample": "sample"}', '2')
        output = usage_stdout.getvalue().strip()
        self.assertIn('2e7f6dd5-e4a3-4389-bc95-b4bacc234df0', output)

    def test_run_update_custom_cookbook(self):
        usage_stdout = StringIO()
        with contextlib.redirect_stdout(usage_stdout):
            modules.update_custom_cookbooks('eu-west-1', '2e7f6dd5-e4a3-4389-bc95-b4bacc234df0', 'ac0df176-104b-46ae-946e-7cf7367b816e')
        output = usage_stdout.getvalue().strip()
        self.assertIn('2e7f6dd5-e4a3-4389-bc95-b4bacc234df0', output)

    def test_run_setup(self):
        usage_stdout = StringIO()
        with contextlib.redirect_stdout(usage_stdout):
            modules.setup('eu-west-1', '2e7f6dd5-e4a3-4389-bc95-b4bacc234df0', 'ac0df176-104b-46ae-946e-7cf7367b816e')
        output = usage_stdout.getvalue().strip()
        self.assertIn('2e7f6dd5-e4a3-4389-bc95-b4bacc234df0', output)

    def test_run_deploy(self):
        usage_stdout = StringIO()
        with contextlib.redirect_stdout(usage_stdout):
            modules.deploy('eu-west-1', '2e7f6dd5-e4a3-4389-bc95-b4bacc234df0', 'ac0df176-104b-46ae-946e-7cf7367b816e')
        output = usage_stdout.getvalue().strip()
        self.assertIn('2e7f6dd5-e4a3-4389-bc95-b4bacc234df0', output)

    def test_run_deploy_json(self):
        usage_stdout = StringIO()
        with contextlib.redirect_stdout(usage_stdout):
            modules.deploy('eu-west-1', '2e7f6dd5-e4a3-4389-bc95-b4bacc234df0', 'ac0df176-104b-46ae-946e-7cf7367b816e', '{"sample": "sample"}')
        output = usage_stdout.getvalue().strip()
        self.assertIn('2e7f6dd5-e4a3-4389-bc95-b4bacc234df0', output)

    def test_run_getnames(self):
        usage_stdout = StringIO()
        with contextlib.redirect_stdout(usage_stdout):
            modules.common_functions.get_names('2e7f6dd5-e4a3-4389-bc95-b4bacc234df0', 'ac0df176-104b-46ae-946e-7cf7367b816e', 'eu-west-1', 'setup')
        output = usage_stdout.getvalue().strip()
        self.assertIn('setup', output)

    def test_run_getstatus(self):
        usage_stdout = StringIO()
        with contextlib.redirect_stdout(usage_stdout):
            modules.common_functions.get_status('2e7f6dd5e4a34389bc95b4bacc234df0', 'eu-west-1', '2')
        output = usage_stdout.getvalue().strip()
        self.assertIn('2e7f6dd5e4a34389bc95b4bacc234df0', output)

    def test_summary(self):
        summary_stdout = StringIO()
        with contextlib.redirect_stdout(summary_stdout):
            modules.common_functions.summary(100, 50, 10)
        output = summary_stdout.getvalue().strip()
        self.assertIn('Success', output)


if __name__ == '__main__':
    unittest.main()
