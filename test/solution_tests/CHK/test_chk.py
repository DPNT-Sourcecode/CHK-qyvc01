from solutions.CHK import checkout_solution

class TestCHK():
    def test_chk_e(self):
        assert checkout_solution.checkout("ABCEEE") == 220

    def test_chk_a5(self):
        assert checkout_solution.checkout("AAAAAAA") == 250

    def test_chk_a3(self):
        assert checkout_solution.checkout("AAAA") == 180

    def test_chk_e2(self):
        assert checkout_solution.checkout("AAAEEB") == 210

