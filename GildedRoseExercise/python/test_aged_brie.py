import unittest

from gilded_rose import Item, GildedRose


class AgedBrieTest(unittest.TestCase):

    def test_should_increase_quality_by_2_when_quality_starts_at_20_and_item_is_aged_brie(self):
        
        items = [Item("Aged Brie", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(22, items[0].quality)

    def test_should_increase_quality_by_1_when_quality_starts_at_49_and_item_is_aged_brie(self):
        
        items = [Item("Aged Brie", 0, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_should_increase_quality_by_0_when_quality_starts_at_50_and_item_is_aged_brie(self):
        
        items = [Item("Aged Brie", 0, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_should_increase_quality_by_2_when_quality_starts_at_20_and_sell_in_date_is_negative_1_and_item_is_aged_brie(self):
        
        items = [Item("Aged Brie", -1, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(22, items[0].quality)

    def test_should_increase_quality_by_1_when_quality_starts_at_49_and_sell_in_date_is_negative_1_and_item_is_aged_brie(self):
        
        items = [Item("Aged Brie", -1, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_should_increase_quality_by_0_when_quality_starts_at_50_and_sell_in_date_is_negative_1_and_item_is_aged_brie(self):
        
        items = [Item("Aged Brie", -1, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)