import unittest
from llm_ops.manager import LLMManager

class TestLLMManager(unittest.TestCase):
    def test_deploy(self):
        mgr = LLMManager()
        self.assertTrue(mgr.deploy("test-model").startswith("dep-"))
