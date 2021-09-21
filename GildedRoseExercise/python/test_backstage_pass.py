# -*- coding: utf-8 -*-
import unittest
from item import ConcertTicket
from gilded_rose import GildedRose


class BackstagePassTest(unittest.TestCase):
    def test_should_increase_quality_by_1_when_sell_in_date_is_more_than_10(self):
        items = [ConcertTicket("Backstage passes to a TAFKAL80ETC concert", sell_in=11, quality=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].quality)

    def test_should_not_increase_quality_when_quality_is_50(self):
        items = [ConcertTicket("Backstage passes to a TAFKAL80ETC concert", 11, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_should_increase_quality_by_2_when_sell_in_date_is_less_than_equal_to_10(self):
        items = [ConcertTicket("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(22, items[0].quality)

    def test_should_not_increase_quality_above_50_when_quality_is_49_and_sell_in_date_is_less_than_equal_to_10(self):
        items = [ConcertTicket("Backstage passes to a TAFKAL80ETC concert", 10, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_should_increase_quality_by_2_when_sell_in_date_is_more_than_5(self):
        items = [ConcertTicket("Backstage passes to a TAFKAL80ETC concert", 6, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(22, items[0].quality)

    def test_should_increase_quality_by_3_when_sell_in_date_is_less_than_equal_to_5(self):
        items = [ConcertTicket("Backstage passes to a TAFKAL80ETC concert", 5, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(23, items[0].quality)

    def test_should_not_increase_quality_above_50_when_quality_is_48_and_sell_in_date_is_less_than_equal_to_5(self):
        items = [ConcertTicket("Backstage passes to a TAFKAL80ETC concert", 5, 48)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_should_not_increase_quality_above_50_when_quality_is_49_and_sell_in_date_is_less_than_equal_to_5(self):
        items = [ConcertTicket("Backstage passes to a TAFKAL80ETC concert", 5, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_should_not_increase_quality_above_50_when_quality_is_50_and_sell_in_date_is_less_than_equal_to_5(self):
        items = [ConcertTicket("Backstage passes to a TAFKAL80ETC concert", 5, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_quality_should_be_0_when_sell_in_date_is_less_than_0(self):
        items = [ConcertTicket("Backstage passes to a TAFKAL80ETC concert", -1, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_quality_should_be_0_when_sell_in_date_is_0(self):
        items = [ConcertTicket("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)



