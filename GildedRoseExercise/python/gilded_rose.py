# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue
            if item.name == 'Backstage passes to a TAFKAL80ETC concert':
                item.quality += 1
                if item.name == "Backstage passes to a TAFKAL80ETC concert":
                    if item.sell_in < 6:
                        item.quality += 2
                    elif item.sell_in < 11:
                        item.quality += 1
            if item.sell_in < 1:
                if item.name == "Backstage passes to a TAFKAL80ETC concert":
                    item.quality = 0
            if item.name == 'generic_item':
                item = self._update_quality(item)
            elif item.name == 'Aged Brie':
                item = self._update_quality(item)
            item.sell_in -= 1
            item.quality = min(item.quality, 50)
            item.quality = max(item.quality, 0)
    
    def _update_quality(self,item):
        if item.name == 'generic_item':
            item = self._update_generic_item_quality(item)
        elif item.name == 'Aged Brie':
            item = self._update_aged_brie_quality(item)
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






class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
