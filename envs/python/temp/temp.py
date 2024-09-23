class Colors:
    # ANSI escape codes for different colors
    RED = '\033[31m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    YELLOW = '\033[33m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    RESET = '\033[0m'  # Resets the color to default

    @staticmethod
    def red(text):
        """text in red color"""
        return f"{Colors.RED}{text}{Colors.RESET}"

    @staticmethod
    def green(text):
        """text in green color"""
        return f"{Colors.GREEN}{text}{Colors.RESET}"

    @staticmethod
    def blue(text):
        """text in blue color"""
        return f"{Colors.BLUE}{text}{Colors.RESET}"

    @staticmethod
    def yellow(text):
        """text in yellow color"""
        return f"{Colors.YELLOW}{text}{Colors.RESET}"

    @staticmethod
    def magenta(text):
        """text in magenta color"""
        return f"{Colors.MAGENTA}{text}{Colors.RESET}"

    @staticmethod
    def cyan(text):
        """text in cyan color"""
        return f"{Colors.CYAN}{text}{Colors.RESET}"

import unittest

class TestColors(unittest.TestCase):

    def test_red(self):
        # Test that the red method returns a string formatted with red color
        self.assertEqual(Colors.red("hello"), '\033[31mhello\033[0m')

    def test_green(self):
        # Test that the green method returns a string formatted with green color
        self.assertEqual(Colors.green("hello"), '\033[32mhello\033[0m')

    def test_blue(self):
        # Test that the blue method returns a string formatted with blue color
        self.assertEqual(Colors.blue("hello"), '\033[34mhello\033[0m')

    def test_yellow(self):
        # Test that the yellow method returns a string formatted with yellow color
        self.assertEqual(Colors.yellow("hello"), '\033[33mhello\033[0m')

    def test_magenta(self):
        # Test that the magenta method returns a string formatted with magenta color
        self.assertEqual(Colors.magenta("hello"), '\033[35mhello\033[0m')

    def test_cyan(self):
        # Test that the cyan method returns a string formatted with cyan color
        self.assertEqual(Colors.cyan("hello"), '\033[36mhello\033[0m')

if __name__ == '__main__':    unittest.main()