# Test uchun oddiy funksiyalar
import unittest
import functions


class TestMyFuncs(unittest.TestCase):
    example_list = ["Odam", "BOBO", "HaYot", "Sog'lik"]

    def test_listUpperCase(self):
        self.assertEqual(functions.listUpperCase(TestMyFuncs.example_list), [
                         'ODAM', 'BOBO', 'HAYOT', "SOG'LIK"])

    def test_listTitleCase(self):
        self.assertEqual(functions.listTitleCase(TestMyFuncs.example_list), [
                         'Odam', 'Bobo', 'Hayot', "Sog'Lik"])

    def test_listLowerCase(self):
        self.assertEqual(functions.listLowerCase(TestMyFuncs.example_list), [
                         'odam', 'bobo', 'hayot', "sog'lik"])

    def test_getArea(self):
        self.assertAlmostEqual(functions.getArea(
            3), 28.27, 2)  # javobi 28.27431

    def test_getPerimeter(self):
        self.assertAlmostEqual(functions.getPerimeter(
            3), 18.8495, 2)  # javobi 18.849539


class TestTransleter(unittest.TestCase):
    def test_krl_to_lotin(self):
        self.assertEqual(functions.translater("Salom dunyo"), "Салом дунё")

    def test_lotin_to_krl(self):
        self.assertEqual(functions.translater(
            "Dunyoni faqat mehr qutqaradi !"), "Дунёни фақат меҳр қутқаради !")


class CheckAdmin(unittest.TestCase):
    def test_is_admin(self):
        self.assertTrue(functions.is_admin(
            login="EngKattaAdmin", password="Parol123321"))
        self.assertFalse(functions.is_admin(
            login="Adminman", password="brootforce"))


if __name__ == "__main__":
    unittest.main()
