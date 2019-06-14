#!/usr/bin/env python
# Copyright 2018 Chathuranga Abeyrathna. All Rights Reserved.
# AWS OpsWorks deployment cli - Unittest for python2

import unittest
import logging
import sys
import modules.execute_recipes

if sys.version_info < (3, 3):
    import StringIO

region = 'eu-west-1'
stack = '2e7f6dd5-e4a3-4389-bc95-b4bacc234df0'
layer = 'ac0df176-104b-46ae-946e-7cf7367b816e'
cookbook = 'apache2::default'
custom_json = '{"default": "version"}'
instances = 2


class Case2(unittest.TestCase):
    if sys.version_info < (3, 3):
        def test_execute_recipes1(self):
            stdout = sys.stdout
            s = StringIO.StringIO()
            sys.stdout = s
            modules.execute_recipes(region=region, stack=stack, cookbook=cookbook)
            sys.stdout = stdout
            s.seek(0)
            self.assertIn('execute_recipes main function testing', s.read())

        def test_execute_recipes2(self):
            stdout = sys.stdout
            s = StringIO.StringIO()
            sys.stdout = s
            modules.execute_recipes(region=region, stack=stack, cookbook=cookbook, layer=layer)
            sys.stdout = stdout
            s.seek(0)
            self.assertIn('execute_recipes main function testing', s.read())

        def test_execute_recipes3(self):
            stdout = sys.stdout
            s = StringIO.StringIO()
            sys.stdout = s
            modules.execute_recipes(region=region, stack=stack, cookbook=cookbook, custom_json=custom_json)
            sys.stdout = stdout
            s.seek(0)
            self.assertIn('execute_recipes main function testing', s.read())

        def test_execute_recipes4(self):
            stdout = sys.stdout
            s = StringIO.StringIO()
            sys.stdout = s
            modules.execute_recipes(region=region, stack=stack, cookbook=cookbook, layer=layer, custom_json=custom_json)
            sys.stdout = stdout
            s.seek(0)
            self.assertIn('execute_recipes main function testing', s.read())

        def test_run_recipes_without_layer(self):
            stdout = sys.stdout
            s = StringIO.StringIO()
            sys.stdout = s
            modules.run_recipes_without_layer(region=region, stack=stack, cookbook=cookbook, custom_json=custom_json)
            sys.stdout = stdout
            s.seek(0)
            self.assertIn('run_recipes_without_layer sub function', s.read())

        def test_run_recipes_without_layer2(self):
            stdout = sys.stdout
            s = StringIO.StringIO()
            sys.stdout = s
            modules.run_recipes_without_layer(region=region, stack=stack, cookbook=cookbook)
            sys.stdout = stdout
            s.seek(0)
            self.assertIn('run_recipes_without_layer sub function', s.read())

        def run_recipes_with_layer(self):
            stdout = sys.stdout
            s = StringIO.StringIO()
            sys.stdout = s
            modules.run_recipes_with_layer(region=region, stack=stack, layer=layer, cookbook=cookbook, custom_json=custom_json)
            sys.stdout = stdout
            s.seek(0)
            self.assertIn('run_recipes_with_layer sub function', s.read())

        def run_recipes_with_layer2(self):
            stdout = sys.stdout
            s = StringIO.StringIO()
            sys.stdout = s
            modules.run_recipes_with_layer(region=region, stack=stack, layer=layer, cookbook=cookbook)
            sys.stdout = stdout
            s.seek(0)
            self.assertIn('run_recipes_with_layer sub function', s.read())
    else:
        print('python version is higher than 3.4')


if __name__ == '__main__':
    unittest.main()
