#!/usr/bin/env python
# Copyright 2018 Chathuranga Abeyrathna. All Rights Reserved.
# AWS OpsWorks deployment cli - Unittest for python2

import unittest
import logging
import sys
import modules.execute_recipes

if sys.version_info < (3, 3):
    import StringIO

region = 'us-west-2'
stack = '6f210730-19ec-4369-b1dc-0148480d5a56'
layer = '0d5e11ed-36d4-42d0-a353-fbf7d6c80410'
app = '2da891ea-1809-480d-a799-cb2c08746115'
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
