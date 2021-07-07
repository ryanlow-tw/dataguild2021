# -*- coding: utf-8 -*-
from update_item_quality import UpdateItemQuality

class GildedRose(object):

    def __init__(self, items):
        self.items = items
        self.update_item_quality = UpdateItemQuality() 
        self.legendary_items = ['Sulfuras, Hand of Ragnaros']

    def update_quality(self):
        for item in self.items:
            if item.name not in self.legendary_items:
                item = self._update_item_quality(item)
    
    def _update_item_quality(self,item):
        if item.name == 'Aged Brie':
            item = self.update_item_quality.update_aged_brie_quality(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            item = self.update_item_quality.update_concert_ticket_quality(item)
        elif item.name == 'Conjured Item':
            item = self.update_item_quality.update_conjured_item_quality(item)
        else:
            item = self.update_item_quality.update_generic_item_quality(item)
        item.sell_in -= 1
        item.quality = max(min(item.quality, 50),0)
        return item
        

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
