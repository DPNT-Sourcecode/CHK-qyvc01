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

    def test_chk_alpha(self):
        assert checkout_solution.checkout("AAAEeB") == -1

    def test_chk_char(self):
        assert checkout_solution.checkout("&") == -1

    def test_chk_f(self):
        assert checkout_solution.checkout("F") == 10

    def test_chk_h5(self):
        assert checkout_solution.checkout("HHHHH") == 45

    def test_chk_h5(self):
        assert checkout_solution.checkout("HHHHHHHHHHHHHHH") == 125

