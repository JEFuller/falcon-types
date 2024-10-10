import unittest

from falcon.testing.client import TestClient


class TestCase(unittest.TestCase, TestClient):
    ...
