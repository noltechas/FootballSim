class Field:
    def __init__(self, color_1=(0, 255, 0), color_2=(0, 255, 255), symmetrical=True, endzone_font_path=None, yard_number_font_path=None,
                 endzone_font_size=50, yard_number_font_size=50, endzone_1_text=None, endzone_2_text=None, yard_number_color=(255, 255, 255),
                 yard_numbers_spaced=False, endzone_text_offset=0, midfield_logo_size=150):
        self.field_color_1 = color_1
        self.field_color_2 = color_2
        self.symmetrical = symmetrical
        self.endzone_font_path = endzone_font_path
        self.yard_number_font_path = yard_number_font_path
        self.yard_number_font_size = yard_number_font_size
        self.endzone_font_size = endzone_font_size
        self.endzone_1_text = endzone_1_text
        self.endzone_2_text = endzone_2_text
        self.yard_number_color = yard_number_color
        self.yard_numbers_spaced = yard_numbers_spaced
        self.endzone_text_offset = endzone_text_offset
        self.midfield_logo_size = midfield_logo_size