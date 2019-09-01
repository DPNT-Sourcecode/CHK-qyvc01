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

    def test_chk_h15(self):
        assert checkout_solution.checkout("HHHHHHHHHHHHHHH") == 125

    def test_chk_k2(self):
        assert checkout_solution.checkout("KK") == 150

    def test_chk_nbogof(self):
        assert checkout_solution.checkout("NNNM") == 120

    def test_chk_p5(self):
        assert checkout_solution.checkout("PPPPP") == 200


    def test_chk_q3(self):
        assert checkout_solution.checkout("QQQ") == 80

    def test_chk_rbogof(self):
        assert checkout_solution.checkout("RRRQQ") == 180

    def test_chk_u3(self):
        assert checkout_solution.checkout("UUU") == 120

    def test_chk_u4(self):
        assert checkout_solution.checkout("UUUU") == 120

    def test_chk_u8(self):
        assert checkout_solution.checkout("UUUUUUUU") == 240

    def test_chk_v2(self):
        assert checkout_solution.checkout("VV") == 90

    def test_chk_v3(self):
        assert checkout_solution.checkout("VVV") == 130


    def test_chk_group(self):
        assert checkout_solution.checkout("ZZZ") == 150


