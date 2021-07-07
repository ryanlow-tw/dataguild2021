# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue
            else:
                item = self._update_quality_handler(item)
            item.sell_in -= 1
            item.quality = min(item.quality, 50)
            item.quality = max(item.quality, 0)
    
    def _update_quality_handler(self,item):
        if item.name == 'Generic Item':
            item = self._update_generic_item_quality(item)
        elif item.name == 'Aged Brie':
            item = self._update_aged_brie_quality(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            item = self._update_concert_ticket_quality(item)
        elif item.name == 'Conjured Item':
            item = self._update_conjured_item_quality(item)
        return item
            
    def _update_generic_item_quality(self, item):
        if item.sell_in < 1:
            item.quality -= 2
        else:
            item.quality -= 1
        return item
    
    def _update_aged_brie_quality(self,item):
        item.quality += 2
        return item

    def _update_concert_ticket_quality(self,item):
        if item.sell_in <= 0:
            item.quality = 0
        elif item.sell_in <= 5:
            item.quality += 3
        elif item.sell_in <= 10:
            item.quality += 2
        else:
            item.quality += 1
        return item

    def _update_conjured_item_quality(self,item):
        if item.sell_in < 1:
            item.quality -= 4
        else:
            item.quality -= 2
        return item







class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
