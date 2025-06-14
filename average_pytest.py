import pytest
import logging
import average as f

#Создание логирования
logger = logging.getLogger(__name__)

def test_empty_list(): #Тест для пустого списка
   res = f.calculate_average([])
   logger.info("Tested by Bulatov Andrey")
   assert res == None

def test_positive_list(): #Тест для списка из положительных элементов
   res = f.calculate_average([1, 2, 3, 4, 5])
   logger.info("Tested by Bulatov Andrey")
   assert res == 3.0

def test_negative_list(): #Тест для списка из отрицательных элементов
   res = f.calculate_average([-1, -2, -3, -4, -5])
   logger.info("Tested by Bulatov Andrey")
   assert res == -3.0
   