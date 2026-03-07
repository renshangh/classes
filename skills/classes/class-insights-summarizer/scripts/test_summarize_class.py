#!/usr/bin/env python3
import unittest
import os
import tempfile
import json
import shutil
from summarize_class import summarize_class

class TestSummarizeClass(unittest.TestCase):
    def setUp(self):
        # Create a temporary mock repository structure
        self.test_dir = tempfile.mkdtemp()
        self.class_id = "class-test"
        self.mock_repo_path = os.path.join(self.test_dir, "classes", "openclaw-beginner-class", "classes", self.class_id)
        os.makedirs(self.mock_repo_path)

    def tearDown(self):
        # Clean up temporary directory
        shutil.rmtree(self.test_dir)

    def test_summarize_success(self):
        # Test valid directory
        result = summarize_class(self.test_dir, self.class_id)
        self.assertIn("class_id", result)
        self.assertEqual(result["class_id"], self.class_id)
        self.assertIn("checkpoints", result)
        self.assertEqual(len(result["checkpoints"]), 2)
        self.assertTrue(result["metadata"]["path_verified"])

    def test_summarize_not_found(self):
        # Test invalid class_id
        result = summarize_class(self.test_dir, "non-existent")
        self.assertIn("error", result)
        self.assertTrue("not found" in result["error"].lower())

    def test_summarize_invalid_repo(self):
        # Test invalid repo_path
        result = summarize_class("/tmp/non/existent/path", self.class_id)
        self.assertIn("error", result)

if __name__ == "__main__":
    unittest.main()
