class TestHTMLToCSVExtraction(unittest.TestCase):

    def test_table_with_multiple_rows_and_columns(self):
        test_case_html = """
        <table class="waffle">
            <tbody>
                <tr><td>Cell 1</td><td>Cell 2</td></tr>
                <tr><td>Cell 3</td><td>Cell 4</td></tr>
            </tbody>
        </table>
        """
        expected = [["Cell 1", "Cell 2"], ["Cell 3", "Cell 4"]]
        self.assertEqual(extract_csv_data_from_html(test_case_html), expected)

    def test_table_with_empty_cells(self):
        test_case_html = """
        <table class="waffle">
            <tbody>
                <tr><td>Cell 1</td><td></td></tr>
                <tr><td></td><td>Cell 4</td></tr>
            </tbody>
        </table>
        """
        expected = [["Cell 1", ""], ["", "Cell 4"]]
        self.assertEqual(extract_csv_data_from_html(test_case_html), expected)

    def test_table_with_only_one_row(self):
        test_case_html = """
        <table class="waffle">
            <tbody>
                <tr><td>Single Cell 1</td><td>Single Cell 2</td></tr>
            </tbody>
        </table>
        """
        expected = [["Single Cell 1", "Single Cell 2"]]
        self.assertEqual(extract_csv_data_from_html(test_case_html), expected)

    def test_table_with_only_one_column(self):
        test_case_html = """
        <table class="waffle">
            <tbody>
                <tr><td>Column Cell 1</td></tr>
                <tr><td>Column Cell 2</td></tr>
            </tbody>
        </table>
        """
        expected = [["Column Cell 1"], ["Column Cell 2"]]
        self.assertEqual(extract_csv_data_from_html(test_case_html), expected)

    def test_no_table_with_class_waffle_present(self):
        test_case_html = """
        <div>
            <p>No table here!</p>
        </div>
        """
        expected = []
        self.assertEqual(extract_csv_data_from_html(test_case_html), expected)
