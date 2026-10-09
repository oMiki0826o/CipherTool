"""Test the registry dispatch interface used by the GUI."""

import unittest

from cipher_tool.registry import run_tool


class RegistryTest(unittest.TestCase):
    """Verify registered tools dispatch to their public module APIs."""

    def test_dispatches_cipher_with_parameters(self) -> None:
        """Registry passes string GUI parameters to Caesar correctly."""
        self.assertEqual(run_tool("caesar", "encrypt", "ABC", {"shift": "3"}), "DEF")

    def test_dispatches_number_conversion(self) -> None:
        """Registry keeps numeric base conversion separate from text hex."""
        self.assertEqual(run_tool("number_base", "convert", "255", {"from_base": "10", "to_base": "16"}), "FF")

    def test_dispatches_scytale_with_column_parameter(self) -> None:
        """Registry converts the Scytale column entry to an integer."""
        ciphertext = run_tool("scytale", "encrypt", "MEETMEATNOON", {"columns": "4"})
        self.assertEqual(run_tool("scytale", "decrypt", ciphertext, {"columns": "4"}), "MEETMEATNOON")

    def test_dispatches_integrity_tool(self) -> None:
        """Registry exposes checksum calculations to the GUI."""
        self.assertEqual(run_tool("crc3", "calculate", "A", {}), "3")

    def test_rejects_unknown_tool(self) -> None:
        """Unknown tool identifiers do not silently fall through."""
        with self.assertRaises(ValueError):
            run_tool("unknown", "encode", "text", {})


if __name__ == "__main__":
    unittest.main()
