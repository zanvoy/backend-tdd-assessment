#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo
import subprocess


# Your test case class goes here
class TestEcho(unittest.TestCase):
    def setUp(self):
        self.parser = echo.create_parser()
    
    def test_no_option(self):
        args = ['hElLo WoRlD']
        ns = self.parser.parse_args(args)
        self.assertFalse(ns.upper)
        self.assertFalse(ns.lower)
        self.assertFalse(ns.title)
        actual = echo.main(args)
        excepted = 'hElLo WoRlD'
        self.assertEqual(actual, excepted)

    def test_all_options(self):
        args = ['-tlu', 'hElLo WoRlD']
        ns = self.parser.parse_args(args)
        self.assertTrue(ns.upper)
        self.assertTrue(ns.lower)
        self.assertTrue(ns.title)

        actual = echo.main(args)
        excepted = 'Hello World'
        self.assertEqual(actual, excepted)

    def test_upper_short(self):
        args = ['-u', 'hElLo WoRlD']
        ns = self.parser.parse_args(args)
        self.assertTrue(ns.upper)

        actual = echo.main(args)
        excepted = 'HELLO WORLD'
        self.assertEqual(actual, excepted)
    def test_lower_short(self):
        args = ['-l', 'hElLo WoRlD']
        ns = self.parser.parse_args(args)
        self.assertTrue(ns.lower)

        actual = echo.main(args)
        excepted = 'hello world'
        self.assertEqual(actual, excepted)
    def test_title_short(self):
        args = ['-t', 'hElLo WoRlD']
        ns = self.parser.parse_args(args)
        self.assertTrue(ns.title)

        actual = echo.main(args)
        excepted = 'Hello World'
        self.assertEqual(actual, excepted)
    def test_upper_long(self):
        args = ['--upper', 'hElLo WoRlD']
        ns = self.parser.parse_args(args)
        self.assertTrue(ns.upper)

        actual = echo.main(args)
        excepted = 'HELLO WORLD'
        self.assertEqual(actual, excepted)
    def test_lower_long(self):
        args = ['--lower', 'hElLo WoRlD']
        ns = self.parser.parse_args(args)
        self.assertTrue(ns.lower)

        actual = echo.main(args)
        excepted = 'hello world'
        self.assertEqual(actual, excepted)
    def test_title_long(self):
        args = ['--title', 'hElLo WoRlD']
        ns = self.parser.parse_args(args)
        self.assertTrue(ns.title)

        actual = echo.main(args)
        excepted = 'Hello World'
        self.assertEqual(actual, excepted)

    def test_help(self):
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        stdout = stdout.decode('utf8')
        with open("./USAGE") as f:
            usage = f.read()
            
        self.assertEquals(stdout, usage)
    


if __name__ == '__main__':
    unittest.main()
