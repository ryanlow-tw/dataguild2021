# -*- coding: utf-8 -*-
from update_item_quality import UpdateItemQuality

class GildedRose(object, UpdateItemQuality):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue
            else:
                item = self._update_quality_handler(item)
    
    def _update_quality_handler(self,item):
        if item.name == 'Generic Item':
            item = self._update_generic_item_quality(item)
        elif item.name == 'Aged Brie':
            item = self._update_aged_brie_quality(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            item = self._update_concert_ticket_quality(item)
        elif item.name == 'Conjured Item':
            item = self._update_conjured_item_quality(item)
        item.sell_in -= 1
        item.quality = min(item.quality, 50)
        item.quality = max(item.quality, 0)
        return item
        

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
