from solutions.CHK import checkout_solution

class TestCHK():
    def test_chk_e(self):
        assert checkout_solution.checkout("ABCEEE") == 220

    def test_chk_a5(self):
        assert checkout_solution.checkout("AAAAAA") == 200

    def test_chk_a3(self):
        assert checkout_solution.checkout("AAA") == 130
