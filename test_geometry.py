import unittest
import math
from circle import area as circle_area
from circle import perimeter as circle_perimeter
from rectangle import area as rectangle_area
from rectangle import perimeter as rectangle_perimeter
from square import area as square_area
from square import perimeter as square_perimeter
from triangle import area as triangle_area
from triangle import perimeter as triangle_perimeter

import unittest
import math

class GeometryTestCase(unittest.TestCase):
   
    # === ТЕСТЫ ДЛЯ КРУГА ===
    
    def test_circle_area_zero(self):
        res = circle_area(0)
        self.assertEqual(res, 0)
        
    def test_circle_area_normal(self):
        res = circle_area(10)
        self.assertEqual(res, 100 * math.pi)
        
    def test_circle_perimeter_zero(self):
        res = circle_perimeter(0)
        self.assertEqual(res, 0)
        
    def test_circle_perimeter_normal(self):
        res = circle_perimeter(10)
        self.assertEqual(res, 20 * math.pi)
    
    # === ТЕСТЫ ДЛЯ ПРЯМОУГОЛЬНИКА ===
    
    def test_rectangle_area_zero(self):
        res = rectangle_area(10, 0)
        self.assertEqual(res, 0)
        
    def test_rectangle_area_square(self):
        res = rectangle_area(10, 10)
        self.assertEqual(res, 100)
        
    def test_rectangle_area_normal(self):
        res = rectangle_area(5, 3)
        self.assertEqual(res, 15)
        
    def test_rectangle_perimeter_zero(self):
        res = rectangle_perimeter(10, 0)
        self.assertEqual(res, 20)
        
    def test_rectangle_perimeter_square(self):
        res = rectangle_perimeter(10, 10)
        self.assertEqual(res, 40)
        
    def test_rectangle_perimeter_normal(self):
        res = rectangle_perimeter(5, 3)
        self.assertEqual(res, 16)
    
    # === ТЕСТЫ ДЛЯ КВАДРАТА ===
    
    def test_square_area_zero(self):
        res = square_area(0)
        self.assertEqual(res, 0)
        
    def test_square_area_normal(self):
        res = square_area(10)
        self.assertEqual(res, 100)
        
    def test_square_perimeter_zero(self):
        res = square_perimeter(0)
        self.assertEqual(res, 0)
        
    def test_square_perimeter_normal(self):
        res = square_perimeter(10)
        self.assertEqual(res, 40)
    
    # === ТЕСТЫ ДЛЯ ТРЕУГОЛЬНИКА ===
    
    def test_triangle_area_zero_base(self):
        res = triangle_area(0, 5)
        self.assertEqual(res, 0)
        
    def test_triangle_area_zero_height(self):
        res = triangle_area(5, 0)
        self.assertEqual(res, 0)
        
    def test_triangle_area_normal(self):
        res = triangle_area(4, 3)
        self.assertEqual(res, 6.0)
        
    def test_triangle_perimeter_zero(self):
        res = triangle_perimeter(0, 4, 5)
        self.assertEqual(res, 9)
        
    def test_triangle_perimeter_equilateral(self):
        res = triangle_perimeter(5, 5, 5)
        self.assertEqual(res, 15)
        
    def test_triangle_perimeter_normal(self):
        res = triangle_perimeter(3, 4, 5)
        self.assertEqual(res, 12)

if __name__ == '__main__':
    unittest.main()