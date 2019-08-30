from solutions.CHK import checkout_solution

class TestCHK():
    def test_chk_e1(self):
        assert checkout_solution.checkout("ABCEEE") == 190

    def test_chk_a1(self):
        assert checkout_solution.checkout("AAAAAAA") == 300

    def test_chk_a2(self):
        assert checkout_solution.checkout("AAAA") == 180

    def test_chk_e2(self):
        assert checkout_solution.checkout("AAAEEB") == 210


