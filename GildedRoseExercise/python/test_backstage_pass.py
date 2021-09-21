# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class BackstagePassTest(unittest.TestCase):
    def test_should_increase_quality_by_1_when_quality_starts_at_20_and_sell_in_date_is_11_item_is_backstage_pass(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(21, items[0].quality)

    def test_should_increase_quality_by_0_when_quality_starts_at_50_and_sell_in_date_is_11_item_is_backstage_pass(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_should_increase_quality_by_2_when_quality_starts_at_20_and_sell_in_date_is_10_item_is_backstage_pass(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(22, items[0].quality)

    def test_should_increase_quality_by_1_when_quality_starts_at_49_and_sell_in_date_is_10_item_is_backstage_pass(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_should_increase_quality_by_0_when_quality_starts_at_50_and_sell_in_date_is_10_item_is_backstage_pass(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_should_increase_quality_by_2_when_quality_starts_at_20_and_sell_in_date_is_6_item_is_backstage_pass(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 6, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(22, items[0].quality)

    def test_should_increase_quality_by_3_when_quality_starts_at_20_and_sell_in_date_is_5_item_is_backstage_pass(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(23, items[0].quality)

    def test_should_increase_quality_by_2_when_quality_starts_at_48_and_sell_in_date_is_5_item_is_backstage_pass(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 48)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_should_increase_quality_by_1_when_quality_starts_at_49_and_sell_in_date_is_5_item_is_backstage_pass(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_should_increase_quality_by_0_when_quality_starts_at_50_and_sell_in_date_is_5_item_is_backstage_pass(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_quality_should_be_0_when_sell_in_date_is_negative_1_and_item_is_backstage_pass(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", -1, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_quality_should_be_0_when_sell_in_date_is_0_and_item_is_backstage_pass(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)



