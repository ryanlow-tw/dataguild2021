# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GenericItemTest(unittest.TestCase):
    def test_should_reduce_quality_by_0_when_quality_starts_at_0_and_item_is_generic_item(self):
        items = [Item("generic_item", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)

    def test_should_reduce_quality_by_2_when_quality_starts_at_2_and_item_is_generic_item(self):
        items = [Item("generic_item", 0, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)

    def test_should_reduce_quality_by_1_when_quality_starts_at_1_and_item_is_generic_item(self):
        items = [Item("generic_item", 0, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)

    def test_should_reduce_quality_by_2_when_quality_starts_at_20_and_item_is_generic_item(self):
        items = [Item("generic_item", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(18, items[0].quality)
    
#TODO: Bug to be fixed - able to create item with more than 50 quality
#TODO: Bug to be fixed - should not be able to create an item with negative quality  
#TODO: Bug to be fixed - quality reduction should double when sell in date passed

if __name__ == '__main__':
    unittest.main()
