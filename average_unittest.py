import unittest
import logging
import average as f

#Конфигурация логирования
logger = logging.getLogger(__name__)
logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
    )

class AverageTestCase(unittest.TestCase):
    def test_empty_list(self): #Тест для пустого списка
        res = f.calculate_average([])
        self.assertEqual(res, None)
        logger.info("Tested by Bulatov Andrey")

    def test_multiple_values(self): #Тест для списка из положительных элементов
        res = f.calculate_average([1, 2, 3, 4, 5])
        self.assertEqual(res, 3.0)
        logger.info("Tested by Bulatov Andrey")

    def test_negative_values(self): #Тест для списка из отрицательных элементов
        res = f.calculate_average([-1, -2, -3])
        self.assertEqual(res, -2.0)
        logger.info("Tested by Bulatov Andrey")


