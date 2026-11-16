
import unittest
from unittest.mock import Mock

from llm_client import LLMClient, LLMResult


class TestLLMClient(unittest.TestCase):

    def setUp(self):
        self.provider = Mock()
        self.provider.provider_name = "TestProvider"

        self.logger = Mock()

        self.client = LLMClient(
            provider=self.provider,
            usage_logger=self.logger
        )

    def test_successful_generation(self):
        self.provider.generate.return_value = LLMResult(
            text="VS Code is a code editor.",
            input_tokens=10,
            output_tokens=8
        )

        result = self.client.generate("What is VS Code?")

        self.assertEqual(result, "VS Code is a code editor.")
        self.provider.generate.assert_called_once()
        self.logger.log_call.assert_called_once()

    def test_failed_generation(self):
        self.provider.generate.side_effect = Exception("Test error")

        with self.assertRaises(Exception):
            self.client.generate("Test prompt")

        self.logger.log_call.assert_called_once()


if __name__ == "__main__":
    unittest.main()
