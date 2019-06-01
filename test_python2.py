#!/usr/bin/env python
# Copyright 2018 Chathuranga Abeyrathna. All Rights Reserved.
# AWS OpsWorks deployment cli - Unittest for python2

import unittest
import logging
import sys
import modules.execute_recipes

if sys.version_info < (3, 4):
    import StringIO

region = 'eu-west-1'
stack = '2e7f6dd5-e4a3-4389-bc95-b4bacc234df0'
layer = 'ac0df176-104b-46ae-946e-7cf7367b816e'
cookbook = 'apache2::default'
custom_json = '{"default": "version"}'
instances = 2


class Case2(unittest.TestCase):
    if sys.version_info < (3, 4):
        def test_execute_recipes1(self):
            stdout = sys.stdout
            s = StringIO.StringIO()
            sys.stdout = s
            modules.execute_recipes(region=region, stack=stack, cookbook=cookbook)
            sys.stdout = stdout
            s.seek(0)
            self.assertIn('execute_recipes main function testing without layer_id and custom_json', s.read())

        def test_execute_recipes2(self):
            stdout = sys.stdout
            s = StringIO.StringIO()
            sys.stdout = s
            modules.execute_recipes(region=region, stack=stack, cookbook=cookbook, layer=layer)
            sys.stdout = stdout
            s.seek(0)
            self.assertIn('execute_recipes main function testing with layer_id without custom_json', s.read())

        def test_execute_recipes3(self):
            stdout = sys.stdout
            s = StringIO.StringIO()
            sys.stdout = s
            modules.execute_recipes(region=region, stack=stack, cookbook=cookbook, custom_json=custom_json)
            sys.stdout = stdout
            s.seek(0)
            self.assertIn('execute_recipes main function testing with custom_json and without layer_id', s.read())

        def test_execute_recipes4(self):
            stdout = sys.stdout
            s = StringIO.StringIO()
            sys.stdout = s
            modules.execute_recipes(region=region, stack=stack, cookbook=cookbook, layer=layer, custom_json=custom_json)
            sys.stdout = stdout
            s.seek(0)
            self.assertIn('execute_recipes main function testing with custom_json and layer_id', s.read())

        def test_run_recipes_without_json(self):
            stdout = sys.stdout
            s = StringIO.StringIO()
            sys.stdout = s
            modules.run_recipes_without_json(region=region, stack=stack, cookbook=cookbook, layer=layer, instances=instances)
            sys.stdout = stdout
            s.seek(0)
            self.assertIn('run_recipes_without_json sub function testing without custom_json with layer_id', s.read())

        def test_run_recipes_with_json(self):
            stdout = sys.stdout
            s = StringIO.StringIO()
            sys.stdout = s
            modules.run_recipes_with_json(region=region, stack=stack, layer=layer, cookbook=cookbook, instances=instances, custom_json=custom_json)
            sys.stdout = stdout
            s.seek(0)
            self.assertIn('run_recipes_with_json sub function testing with custom_json without layer_id', s.read())
    else:
        print('python version is higher than 3.4')


if __name__ == '__main__':
    unittest.main()
