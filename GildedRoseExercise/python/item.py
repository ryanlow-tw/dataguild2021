class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GenericItem(Item):

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def __update_item_quality(self):
        if self.sell_in < 1:
            self.quality -= 2
        else:
            self.quality -= 1

        self.quality = min(50, max(0, self.quality))

    def _update_item_sell_in(self):
        self.sell_in -= 1

    def update_item(self):
        self.__update_item_quality()
        self._update_item_sell_in()


class LegendaryItem(GenericItem):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_item(self):
        pass


class AgedBrie(GenericItem):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def __update_item_quality(self):
        self.quality += 2
        self.quality = min(50, max(0, self.quality))

    def update_item(self):
        self.__update_item_quality()
        self._update_item_sell_in()


class ConcertTicket(GenericItem):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def __update_item_quality(self):
        if self.sell_in <= 0:
            self.quality = 0
        elif self.sell_in <= 5:
            self.quality += 3
        elif self.sell_in <= 10:
            self.quality += 2
        else:
            self.quality += 1
        self.quality = min(50, max(0, self.quality))

    def update_item(self):
        self.__update_item_quality()
        self._update_item_sell_in()


class ConjuredItem(GenericItem):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def __update_item_quality(self):
        if self.sell_in < 1:
            self.quality -= 4
        else:
            self.quality -= 2
        self.quality = min(50, max(0, self.quality))

    def update_item(self):
        self.__update_item_quality()
        self._update_item_sell_in()
