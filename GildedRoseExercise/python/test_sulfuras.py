# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_should_reduce_quality_by_0_when_quality_starts_at_20_and_item_is_sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(20, items[0].quality)

    def test_should_reduce_quality_by_0_when_quality_starts_at_0_and_item_is_sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)

    def test_should_reduce_quality_by_0_when_quality_starts_at_1_and_item_is_sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(1, items[0].quality)

    def test_should_reduce_quality_by_0_when_quality_starts_at_negative_1_and_item_is_sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, -1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(-1, items[0].quality)

    def test_should_reduce_sell_in_by_0_when_sell_in_starts_at_1_and_item_is_sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 1, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(1, items[0].sell_in)

    def test_should_reduce_sell_in_by_0_when_sell_in_starts_at_negative_1_and_item_is_sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", -1, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(-1, items[0].sell_in)

    def test_should_reduce_sell_in_by_0_when_sell_in_starts_at_0_and_item_is_sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", -1, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(-1, items[0].sell_in)


if __name__ == '__main__':
    unittest.main()