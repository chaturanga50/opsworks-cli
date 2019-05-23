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
    def test_usage_output(self):
        usage_stdout = StringIO()
        with contextlib.redirect_stdout(usage_stdout):
            modules.common_functions.usage()
        output = usage_stdout.getvalue().strip()
        self.assertIn('usage:', output)
    

    def test_version_output(self):
        version_stdout = StringIO()
        with contextlib.redirect_stdout(version_stdout):
            modules.common_functions.version()
        output = version_stdout.getvalue().strip()
        self.assertEqual(output, '0.4.9')
    

    def test_execute_recipes_usage_output(self):
        execute_recipes_stdout = StringIO()
        with contextlib.redirect_stdout(execute_recipes_stdout):
            modules.common_functions.execute_recipes_usage()
        output = execute_recipes_stdout.getvalue().strip()
        self.assertIn('execute-recipes', output)


    def test_deploy_usage(self):
        deploy_stdout = StringIO()
        with contextlib.redirect_stdout(deploy_stdout):
            modules.common_functions.deploy_usage()
        output = deploy_stdout.getvalue().strip()
        self.assertIn('deploy', output)


    def test_setup_usage(self):
        setup_stdout = StringIO()
        with contextlib.redirect_stdout(setup_stdout):
            modules.common_functions.setup_usage()
        output = setup_stdout.getvalue().strip()
        self.assertIn('setup', output)


    def test_update_custom_cookbooks_usage(self):
        update_custom_cookbooks_stdout = StringIO()
        with contextlib.redirect_stdout(update_custom_cookbooks_stdout):
            modules.common_functions.update_custom_cookbooks_usage()
        output = update_custom_cookbooks_stdout.getvalue().strip()
        self.assertIn('update-custom-cookbooks', output)


    def test_summary(self):
        summary_stdout = StringIO()
        with contextlib.redirect_stdout(summary_stdout):
            modules.common_functions.summary(100,50,10)
        output = summary_stdout.getvalue().strip()
        self.assertIn('Success', output)


if __name__ == '__main__':
#    assert not hasattr(sys.stdout, "getvalue")
#    unittest.main(module=__name__, buffer=True, exit=False)
    unittest.main()