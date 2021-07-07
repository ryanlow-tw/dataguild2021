class UpdateItemQuality():
    def __init__(self):
        pass

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