# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class ConjuredItemTest(unittest.TestCase):
    def test_should_reduce_quality_by_2_when_quality_starts_at_20_and_sell_in_date_is_not_0_and_item_is_conjured_item(self):
        items = [Item("Conjured Item", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(18, items[0].quality)

    def test_should_reduce_quality_by_4_when_quality_starts_at_0_and_sell_in_date_is_not_0_and_item_is_conjured_item(self):
        items = [Item("Conjured Item", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(16, items[0].quality)

    def test_should_reduce_quality_by_2_when_quality_starts_at_2_and_sell_in_date_is_not_0_and_item_is_conjured_item(self):
        items = [Item("Conjured Item", 0, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)
  
if __name__ == '__main__':
    unittest.main()
