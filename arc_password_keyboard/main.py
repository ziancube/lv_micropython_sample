import lvgl as lv
lv.init()
# Register SDL display driver.

from display_driver_utils import driver, ORIENT_LANDSCAPE
drv = driver(width=480, height=800, orientation=ORIENT_LANDSCAPE)

class StyleWrapper(lv.style_t):
    def __init__(self):
        super().__init__()

    def radius(self, radius) -> "StyleWrapper":
        self.set_radius(radius)
        return self

    def align(self, align) -> "StyleWrapper":
        self.set_align(align)
        return self

    def text_color(self, text_color) -> "StyleWrapper":
        self.set_text_color(text_color)
        return self

    def text_opa(self, text_opa) -> "StyleWrapper":
        self.set_text_opa(text_opa)
        return self

    def text_align(self, text_align) -> "StyleWrapper":
        self.set_text_align(text_align)
        return self

    def text_align_right(self) -> "StyleWrapper":
        self.set_text_align(lv.TEXT_ALIGN.RIGHT)
        return self

    def text_align_left(self) -> "StyleWrapper":
        self.set_text_align(lv.TEXT_ALIGN.LEFT)
        return self

    def text_align_center(self) -> "StyleWrapper":
        self.set_text_align(lv.TEXT_ALIGN.CENTER)
        return self

    def text_font(self, text_font) -> "StyleWrapper":
        self.set_text_font(text_font)
        return self

    def bg_color(self, bg_color) -> "StyleWrapper":
        self.set_bg_color(bg_color)
        return self

    def bg_opa(self, bg_opa=lv.OPA.COVER) -> "StyleWrapper":
        self.set_bg_opa(bg_opa)
        return self

    def text_line_space(self, line_space) -> "StyleWrapper":
        self.set_text_line_space(line_space)
        return self

    def text_letter_space(self, letter_space) -> "StyleWrapper":
        self.set_text_letter_space(letter_space)
        return self

    def pad_all(self, pad) -> "StyleWrapper":
        self.set_pad_all(pad)
        return self

    def pad_hor(self, pad) -> "StyleWrapper":
        self.set_pad_hor(pad)
        return self

    def pad_ver(self, pad) -> "StyleWrapper":
        self.set_pad_ver(pad)
        return self

    def pad_gap(self, gap) -> "StyleWrapper":
        """pad row + pad column"""
        self.set_pad_gap(gap)
        return self

    def pad_row(self, pad) -> "StyleWrapper":
        self.set_pad_row(pad)
        return self

    def pad_column(self, pad) -> "StyleWrapper":
        self.set_pad_column(pad)
        return self

    def pad_top(self, pad) -> "StyleWrapper":
        self.set_pad_top(pad)
        return self

    def pad_bottom(self, pad) -> "StyleWrapper":
        self.set_pad_bottom(pad)
        return self

    def pad_left(self, pad) -> "StyleWrapper":
        self.set_pad_left(pad)
        return self

    def pad_right(self, pad) -> "StyleWrapper":
        self.set_pad_right(pad)
        return self

    def transform_height(self, height) -> "StyleWrapper":
        self.set_transform_height(height)
        return self

    def transform_width(self, width) -> "StyleWrapper":
        self.set_transform_width(width)
        return self

    def transform_zoom(self, zoom) -> "StyleWrapper":
        self.set_transform_zoom(zoom)
        return self

    def translate_y(self, y) -> "StyleWrapper":
        self.set_translate_y(y)
        return self

    def translate_x(self, x) -> "StyleWrapper":
        self.set_translate_x(x)
        return self

    def bg_img_src(self, src) -> "StyleWrapper":
        self.set_bg_img_src(src)
        return self

    def bg_img_opa(self, opa) -> "StyleWrapper":
        self.set_bg_img_opa(opa)
        return self

    def bg_img_recolor(self, color) -> "StyleWrapper":
        self.set_bg_img_recolor(color)
        return self

    def bg_img_recolor_opa(self, opa) -> "StyleWrapper":
        self.set_bg_img_recolor_opa(opa)
        return self

    def border_width(self, width) -> "StyleWrapper":
        self.set_border_width(width)
        return self

    def max_height(self, height) -> "StyleWrapper":
        self.set_max_height(height)
        return self

    def max_width(self, width) -> "StyleWrapper":
        self.set_max_width(width)
        return self

    def min_width(self, width) -> "StyleWrapper":
        self.set_min_width(width)
        return self

    def min_height(self, height) -> "StyleWrapper":
        self.set_min_height(height)
        return self

    def transition(self, transition) -> "StyleWrapper":
        self.set_transition(transition)
        return self

    def bg_grad_color(self, color) -> "StyleWrapper":
        self.set_bg_grad_color(color)
        return self

    def bg_grad_dir(self, dir) -> "StyleWrapper":
        self.set_bg_grad_dir(dir)
        return self

    def bg_main_stop(self, value) -> "StyleWrapper":
        self.set_bg_main_stop(value)
        return self

    def bg_grad_stop(self, value) -> "StyleWrapper":
        self.set_bg_grad_stop(value)
        return self

    def border_color(self, color) -> "StyleWrapper":
        self.set_border_color(color)
        return self

    def border_opa(self, opa=lv.OPA.COVER) -> "StyleWrapper":
        self.set_border_opa(opa)
        return self

    def width(self, width) -> "StyleWrapper":
        self.set_width(width)
        return self

    def height(self, height) -> "StyleWrapper":
        self.set_height(height)
        return self

    def grid_column_dsc_array(self, arr) -> "StyleWrapper":
        self.set_grid_column_dsc_array(arr)
        return self

    def grid_row_dsc_array(self, arr) -> "StyleWrapper":
        self.set_grid_row_dsc_array(arr)
        return self









ui_Screen1 = lv.obj(lv.scr_act())
ui_Screen1.set_size(480, 800)
ui_Screen1.set_style_bg_color(lv.color_hex(0x464B55),lv.PART.MAIN|lv.STATE.DEFAULT)
ui_Screen1.set_style_bg_grad_color(lv.color_hex(0x2D323C),lv.PART.MAIN|lv.STATE.DEFAULT)
ui_Screen1.set_style_bg_opa(255,lv.PART.MAIN|lv.STATE.DEFAULT)


ui_Ta_PWD = lv.textarea(ui_Screen1)
ui_Ta_PWD.align(lv.ALIGN.TOP_MID, 0, 150)
ui_Ta_PWD.add_style(
            StyleWrapper()
            .bg_color(lv.color_hex(0))
            .border_width(0)
            .width(lv.SIZE.CONTENT)
            .max_width(432)
            .text_color(lv.color_hex(0xffffff))
            .text_letter_space(12)
            .text_align_center(),
            0,
        )
ui_Ta_PWD.set_one_line(True)
ui_Ta_PWD.set_accepted_chars("0123456789")
ui_Ta_PWD.set_max_length(50)
ui_Ta_PWD.set_password_mode(True)
ui_Ta_PWD.clear_flag(lv.obj.FLAG.CLICKABLE)
ui_Ta_PWD.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)




ui_Arc_Group = lv.obj(ui_Screen1)
ui_Arc_Group.set_width(400)
ui_Arc_Group.set_height(400)
ui_Arc_Group.set_align(lv.ALIGN.CENTER)
ui_Arc_Group.clear_flag(lv.obj.FLAG.SCROLLABLE)
ui_Arc_Group.set_style_bg_color(lv.color_hex(0xFFFFFF),lv.PART.MAIN|lv.STATE.DEFAULT)
ui_Arc_Group.set_style_bg_opa(0,lv.PART.MAIN|lv.STATE.DEFAULT)
ui_Arc_Group.set_style_border_width(0,lv.PART.MAIN|lv.STATE.DEFAULT)


ui_Arc1 = lv.arc(ui_Arc_Group)
ui_Arc1.set_width(350)
ui_Arc1.set_height(350)
ui_Arc1.set_x(1)
ui_Arc1.set_y(0)
ui_Arc1.set_align(lv.ALIGN.CENTER)
ui_Arc1.set_range(0,9)
ui_Arc1.set_value(5)
ui_Arc1.set_style_radius(350,lv.PART.MAIN|lv.STATE.DEFAULT)
ui_Arc1.set_style_bg_color(lv.color_hex(0x1E232D),lv.PART.MAIN|lv.STATE.DEFAULT)
ui_Arc1.set_style_bg_opa(255,lv.PART.MAIN|lv.STATE.DEFAULT)
ui_Arc1.set_style_pad_left(10,lv.PART.MAIN|lv.STATE.DEFAULT)
ui_Arc1.set_style_pad_right(10,lv.PART.MAIN|lv.STATE.DEFAULT)
ui_Arc1.set_style_pad_top(10,lv.PART.MAIN|lv.STATE.DEFAULT)
ui_Arc1.set_style_pad_bottom(10,lv.PART.MAIN|lv.STATE.DEFAULT)
ui_Arc1.set_style_arc_color(lv.color_hex(0x0F1215),lv.PART.MAIN|lv.STATE.DEFAULT)
ui_Arc1.set_style_arc_opa(255,lv.PART.MAIN|lv.STATE.DEFAULT)
ui_Arc1.set_style_arc_width(15,lv.PART.MAIN|lv.STATE.DEFAULT)

ui_Arc1.set_style_arc_color(lv.color_hex(0x36B9F6),lv.PART.INDICATOR|lv.STATE.DEFAULT)
ui_Arc1.set_style_arc_opa(255,lv.PART.INDICATOR|lv.STATE.DEFAULT)
ui_Arc1.set_style_arc_width(15,lv.PART.INDICATOR|lv.STATE.DEFAULT)

ui_Arc1.set_style_arc_color(lv.color_hex(0xFFFFFF),lv.PART.KNOB|lv.STATE.DEFAULT)
ui_Arc1.set_style_arc_opa(0,lv.PART.KNOB|lv.STATE.DEFAULT)


ui_Temp_Bg = lv.obj(ui_Arc_Group)
ui_Temp_Bg.set_width(280)
ui_Temp_Bg.set_height(280)
ui_Temp_Bg.set_align(lv.ALIGN.CENTER)
ui_Temp_Bg.clear_flag(lv.obj.FLAG.CLICKABLE | lv.obj.FLAG.SCROLLABLE)
ui_Temp_Bg.set_style_radius(280,lv.PART.MAIN|lv.STATE.DEFAULT)
ui_Temp_Bg.set_style_bg_color(lv.color_hex(0x646464),lv.PART.MAIN|lv.STATE.DEFAULT)
ui_Temp_Bg.set_style_bg_opa(255,lv.PART.MAIN|lv.STATE.DEFAULT)
ui_Temp_Bg.set_style_bg_grad_color(lv.color_hex(0x3C414B),lv.PART.MAIN|lv.STATE.DEFAULT)
ui_Temp_Bg.set_style_bg_grad_dir(lv.GRAD_DIR.VER,lv.PART.MAIN|lv.STATE.DEFAULT)
ui_Temp_Bg.set_style_border_color(lv.color_hex(0x2D323C),lv.PART.MAIN|lv.STATE.DEFAULT)
ui_Temp_Bg.set_style_border_opa(255,lv.PART.MAIN|lv.STATE.DEFAULT)
ui_Temp_Bg.set_style_border_width(2,lv.PART.MAIN|lv.STATE.DEFAULT)
ui_Temp_Bg.set_style_shadow_color(lv.color_hex(0x050A0F),lv.PART.MAIN|lv.STATE.DEFAULT)
ui_Temp_Bg.set_style_shadow_opa(255,lv.PART.MAIN|lv.STATE.DEFAULT)
ui_Temp_Bg.set_style_shadow_width(80,lv.PART.MAIN|lv.STATE.DEFAULT)
ui_Temp_Bg.set_style_shadow_spread(0,lv.PART.MAIN|lv.STATE.DEFAULT)
ui_Temp_Bg.set_style_shadow_ofs_x(0,lv.PART.MAIN|lv.STATE.DEFAULT)
ui_Temp_Bg.set_style_shadow_ofs_y(30,lv.PART.MAIN|lv.STATE.DEFAULT)


ui_Temp_Num_Bg = lv.obj(ui_Temp_Bg)
ui_Temp_Num_Bg.set_width(200)
ui_Temp_Num_Bg.set_height(200)
ui_Temp_Num_Bg.set_align(lv.ALIGN.CENTER)
ui_Temp_Num_Bg.clear_flag(lv.obj.FLAG.CLICKABLE | lv.obj.FLAG.SCROLLABLE)
ui_Temp_Num_Bg.set_style_radius(200,lv.PART.MAIN|lv.STATE.DEFAULT)
ui_Temp_Num_Bg.set_style_bg_color(lv.color_hex(0x0C191E),lv.PART.MAIN|lv.STATE.DEFAULT)
ui_Temp_Num_Bg.set_style_bg_opa(255,lv.PART.MAIN|lv.STATE.DEFAULT)
ui_Temp_Num_Bg.set_style_bg_grad_color(lv.color_hex(0x191C26),lv.PART.MAIN|lv.STATE.DEFAULT)
ui_Temp_Num_Bg.set_style_bg_grad_dir(lv.GRAD_DIR.VER,lv.PART.MAIN|lv.STATE.DEFAULT)
ui_Temp_Num_Bg.set_style_border_color(lv.color_hex(0x5A646E),lv.PART.MAIN|lv.STATE.DEFAULT)
ui_Temp_Num_Bg.set_style_border_opa(255,lv.PART.MAIN|lv.STATE.DEFAULT)



ui_Label_Celsius = lv.label(ui_Temp_Num_Bg)
ui_Label_Celsius.set_width(lv.SIZE.CONTENT)
ui_Label_Celsius.set_height(lv.SIZE.CONTENT)
ui_Label_Celsius.set_align(lv.ALIGN.CENTER)
ui_Label_Celsius.set_text("5")
ui_Label_Celsius.set_style_text_color(lv.color_hex(0xFFFFFF),lv.PART.MAIN|lv.STATE.DEFAULT)
ui_Label_Celsius.set_style_text_opa(255,lv.PART.MAIN|lv.STATE.DEFAULT)


ui_btn_false = lv.btn(ui_Screen1)
ui_btn_false.align(lv.ALIGN.BOTTOM_LEFT, 0, 0)
ui_btn_false.set_size(200, 60)
ui_btn_false.set_style_radius(0, lv.PART.MAIN | lv.STATE.DEFAULT)
ui_btn_false.set_style_bg_color(lv.color_hex(0xFF1100), lv.PART.MAIN | lv.STATE.DEFAULT)
false_label=lv.label(ui_btn_false)
false_label.set_text(lv.SYMBOL.CLOSE)
false_label.center()


ui_btn_true= lv.btn(ui_Screen1)
ui_btn_true.align(lv.ALIGN.BOTTOM_RIGHT, 0, 0)
ui_btn_true.set_size(200, 60)
ui_btn_true.set_style_radius(0, lv.PART.MAIN | lv.STATE.DEFAULT)
ui_btn_true.set_style_bg_color(lv.color_hex(0x00FF33), lv.PART.MAIN | lv.STATE.DEFAULT)
ui_btn_true.add_state(lv.STATE.DISABLED)
true_label=lv.label(ui_btn_true)
true_label.set_text(lv.SYMBOL.OK)
true_label.center()



def event_handler(event):
    code = event.code
    if code == lv.EVENT.VALUE_CHANGED:
        ui_Label_Celsius.set_text(str(ui_Arc1.get_value()))
    if code == lv.EVENT.RELEASED:
        ui_Ta_PWD.set_text(ui_Ta_PWD.get_text() + str(ui_Arc1.get_value()))
        if len(ui_Ta_PWD.get_text()) >= 4:
            ui_btn_true.clear_state(lv.STATE.DISABLED)
        if len(ui_Ta_PWD.get_text()) < 4:
            ui_btn_true.add_state(lv.STATE.DISABLED)
        if len(ui_Ta_PWD.get_text()) >0:
            false_label.set_text(lv.SYMBOL.BACKSPACE)
        if len(ui_Ta_PWD.get_text()) == 0:
            false_label.set_text(lv.SYMBOL.CLOSE)


def false_event_handler(event):
    code = event.get_code()
    if codelv.EVENT.CLICKED:
        if len(ui_Ta_PWD.get_text()) > 0:
            ui_Ta_PWD.set_text(ui_Ta_PWD.get_text()[:-1])
            if len(ui_Ta_PWD.get_text()) == 0:
                false_label.set_text(lv.SYMBOL.CLOSE)
                
        if len(ui_Ta_PWD.get_text()) == 0:
            #self.channel.publish(0)
            pass
def true_event_handler(event):
    code = event.get_code()
    if codelv.EVENT.CLICKED:
        #self.channel.publish(input)
        pass

            

ui_Arc1.add_event_cb(event_handler, lv.EVENT.ALL, None)
ui_btn_false.add_event_cb(false_event_handler,lv.EVENT.CLICKED,None)
ui_btn_true.add_event_cb(true_event_handler,lv.EVENT.CLICKED,None)


        


while 1:
    pass
