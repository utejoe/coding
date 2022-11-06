class MenuItem(object):
    ''' The class for one item on the menu. '''

    def __init__(self, title, cost, long_desc = '', short_desc = '', item_type='main'):
        '''sets up a Menuitem object. Title, long_desc, short_desc, and item_type should be strings. Cost should bee a float. '''
        self.title = title
        self.cost = cost
        self.long_desc = long_desc
        self.short_desc = short_desc
        self.item_type = item_type

    def change_item_type(self, item_type):
        ''' Changes the item type. Does not do any checking. '''
        self.item_type = item_type
