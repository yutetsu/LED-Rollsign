from PIL import Image, ImageFont, ImageDraw
from database import RollsignDatabase
from hardware import LedDriver

Framebuffer = []

class E233():
    def __init__(self, args):
        self.args = args
        self.data = RollsignDatabase().GetRollsignData(self.args['train'])

    def main(self):
        match self.args.mode:
            case "Special":
                self.sepcial_mode()
            case "TypeOnly":
                self.type_only_mode()
            case "DestOnly":
                self.dest_only_mode()
            case "LineOnly":
                self.line_only_mode()
            case "Normal":
                self.normal_mode()
            case "Line":
                self.line_mode()
            case "Line-TypeChange":
                self.line_type_change_mode()
            case "Next":
                self.next_mode()
            case "StopsAt":
                self.stops_at_mode()
            case _:
                return {'message': 'Mode not found', 'recived_mode': self.args.Mode,'mode_avalible': self.data['mode']}, 404
        return {'message': 'Rollsign set', 'args': self.args}, 200

    def sepcial_mode(self):
        img = Image.new("RGB", (self.data['width'], self.data['height']), (0, 0, 0))
        if self.args['type'] is not None : 
            SpecialFrame =  Image.open(f"trainroms/Images/{self.data['name']}/Special/{self.args['type']}.png")
            img.paste(SpecialFrame, (0, 0))
        Framebuffer.append(img.convert("P", palette=Image.ADAPTIVE, colors=self.data['colors']))
        MakeGif()

    def type_only_mode(self):
        img = Image.new("RGB", (self.data['width'], self.data['height']), (0, 0, 0))
        if self.args['type'] is not None : 
            TypeFrame =  Image.open(f"trainroms/Images/{self.data['name']}/TypeOnly/{self.args['type']}.png")
            img.paste(TypeFrame, (0, 0))
        Framebuffer.append(img.convert("P", palette=Image.ADAPTIVE, colors=self.data['colors']))
        MakeGif()

    def dest_only_mode(self):
        img = Image.new("RGB", (self.data['width'], self.data['height']), (0, 0, 0))
        if self.args['dest'] is not None : 
            DestFrame =  Image.open(f"trainroms/Images/{self.data['name']}/DestOnly/{self.args['dest']}.png")
            img.paste(DestFrame, (0, 0))
        Framebuffer.append(img.convert("P", palette=Image.ADAPTIVE, colors=self.data['colors']))
        MakeGif()

    def line_only_mode(self):
        img = Image.new("RGB", (self.data['width'], self.data['height']), (0, 0, 0))
        if self.args['line'] is not None : 
            LineFrame =  Image.open(f"trainroms/Images/{self.data['name']}/LineOnly/{self.args['line']}.png")
            img.paste(LineFrame, (0, 0))
        Framebuffer.append(img.convert("P", palette=Image.ADAPTIVE, colors=self.data['colors']))
        MakeGif()
        
    def normal_mode(self):
        img = Image.new("RGB", (self.data['width'], self.data['height']), (0, 0, 0))
        if self.args['type'] is not None : 
            TypeFrame =  Image.open(f"trainroms/Images/{self.data['name']}/Type/{self.args['type']}_JP.png")
            img.paste(TypeFrame, (0, 0))
        if self.args['dest'] is not None : 
            DestFrame =  Image.open(f"trainroms/Images/{self.data['name']}/Dest/{self.args['dest']}.png")
            img.paste(DestFrame, (48, 0))
        Framebuffer.append(img.convert("P", palette=Image.ADAPTIVE, colors=self.data['colors']))
        MakeGif()
    
    def line_mode(self):
        img = Image.new("RGB", (self.data['width'], self.data['height']), (0, 0, 0))
        if self.args['type'] is not None : 
            TypeFrame =  Image.open(f"trainroms/Images/{self.data['name']}/Type/{self.args['type']}_JP.png")
            img.paste(TypeFrame, (0, 0))
        if self.args['dest'] is not None : 
            DestFrame =  Image.open(f"trainroms/Images/{self.data['name']}/Dest/{self.args['dest']}.png")
            img.paste(DestFrame, (48, 0))
        Framebuffer.append(img.convert("P", palette=Image.ADAPTIVE, colors=self.data['colors']))
        img = Image.new("RGB", (self.data['width'], self.data['height']), (0, 0, 0))
        if self.args['type'] is not None : 
            TypeFrame =  Image.open(f"trainroms/Images/{self.data['name']}/Type/{self.args['type']}_JP.png")
            img.paste(TypeFrame, (0, 0))
        if self.args['line'] is not None : 
            LineFrame =  Image.open(f"trainroms/Images/{self.data['name']}/Line/{self.args['line']}.png")
            img.paste(LineFrame, (48, 0))
        Framebuffer.append(img.convert("P", palette=Image.ADAPTIVE, colors=self.data['colors']))
        MakeGif()

    def line_type_change_mode(self):
        img = Image.new("RGB", (self.data['width'], self.data['height']), (0, 0, 0))
        if self.args['type'] is not None : 
            TypeFrame =  Image.open(f"trainroms/Images/{self.data['name']}/Type/{self.args['type']}_JP.png")
            img.paste(TypeFrame, (0, 0))
        if self.args['dest'] is not None : 
            DestFrame =  Image.open(f"trainroms/Images/{self.data['name']}/Dest/{self.args['dest']}.png")
            img.paste(DestFrame, (48, 0))
        Framebuffer.append(img.convert("P", palette=Image.ADAPTIVE, colors=self.data['colors']))
        img = Image.new("RGB", (self.data['width'], self.data['height']), (0, 0, 0))
        if self.args['type'] is not None : 
            TypeFrame =  Image.open(f"trainroms/Images/{self.data['name']}/Type/{self.args['type']}_JP.png")
            img.paste(TypeFrame, (0, 0))
        if self.args['line'] is not None : 
            LineFrame =  Image.open(f"trainroms/Images/{self.data['name']}/Line/{self.args['line']}.png")
            img.paste(LineFrame, (48, 0))
        Framebuffer.append(img.convert("P", palette=Image.ADAPTIVE, colors=self.data['colors']))
        img = Image.new("RGB", (self.data['width'], self.data['height']), (0, 0, 0))
        if self.args['type'] is not None : 
            TypeFrame =  Image.open(f"trainroms/Images/{self.data['name']}/Type/{self.args['type']}_JP.png")
            img.paste(TypeFrame, (0, 0))
        if self.args['type_change'] is not None : 
            TypeChangeFrame =  Image.open(f"trainroms/Images/{self.data['name']}/TypeChange/{self.args['type_change']}.png")
            img.paste(TypeChangeFrame, (48, 0))
        Framebuffer.append(img.convert("P", palette=Image.ADAPTIVE, colors=self.data['colors']))
        MakeGif()

    def next_mode(self):
        img = Image.new("RGB", (self.data['width'], self.data['height']), (0, 0, 0))
        if self.args['type'] is not None : 
            TypeFrame =  Image.open(f"trainroms/Images/{self.data['name']}/Type/{self.args['type']}_JP.png")
            img.paste(TypeFrame, (0, 0))
        if self.args['dest'] is not None : 
            DestFrame =  Image.open(f"trainroms/Images/{self.data['name']}/DestNext/{self.args['dest']}_JP.png")
            img.paste(DestFrame, (48, 0))
        if self.args['next'] is not None : 
            NextFrame =  Image.open(f"trainroms/Images/{self.data['name']}/Next/{self.args['next']}_JP.png")
            img.paste(NextFrame, (48, 16))
        Framebuffer.append(img.convert("P", palette=Image.ADAPTIVE, colors=self.data['colors']))
        img = Image.new("RGB", (self.data['width'], self.data['height']), (0, 0, 0))
        if self.args['type'] is not None : 
            TypeFrame =  Image.open(f"trainroms/Images/{self.data['name']}/Type/{self.args['type']}_EN.png")
            img.paste(TypeFrame, (0, 0))
        if self.args['dest'] is not None : 
            DestFrame =  Image.open(f"trainroms/Images/{self.data['name']}/DestNext/{self.args['dest']}_EN.png")
            img.paste(DestFrame, (48, 0))
        if self.args['next'] is not None : 
            NextFrame =  Image.open(f"trainroms/Images/{self.data['name']}/Next/{self.args['next']}_EN.png")
            img.paste(NextFrame, (48, 16))
        Framebuffer.append(img.convert("P", palette=Image.ADAPTIVE, colors=self.data['colors']))
        MakeGif()

    def stops_at_mode(self):
        Text = f"この電車の停車駅は{self.args['stops_at']}駅に停車ります。"
        Font = ImageFont.truetype(f"trainroms/Fonts/{self.data['Font']}", 16)
        TextWidth = Font.getsize(Text)[0]

        i = 0
        count = 0
        while (TextWidth + 80) >= i:
            img = Image.new("RGB", (self.data['width'], self.data['height']), (0, 0, 0))
            draw = ImageDraw.Draw(img)
            draw.fontmode = "1"
            draw.text(((-abs(i) + self.data['width']), 16), Text, font=Font, fill=(255, 255, 0))

            if count <= 150:
                if self.args['type'] is not None : 
                    TypeFrame =  Image.open(f"trainroms/Images/{self.data['name']}/Type/{self.args['type']}_JP.png")
                    img.paste(TypeFrame, (0, 0))
                if self.args['dest'] is not None : 
                    DestFrame =  Image.open(f"trainroms/Images/{self.data['name']}/DestNext/{self.args['dest']}_JP.png")
                    img.paste(DestFrame, (48, 0))
            elif count <= 300:
                if self.args['type'] is not None : 
                    TypeFrame =  Image.open(f"trainroms/Images/{self.data['name']}/Type/{self.args['type']}_EN.png")
                    img.paste(TypeFrame, (0, 0))
                if self.args['dest'] is not None : 
                    DestFrame =  Image.open(f"trainroms/Images/{self.data['name']}/DestNext/{self.args['dest']}_EN.png")
                    img.paste(DestFrame, (48, 0))
            else:
                if self.args['type'] is not None : 
                    TypeFrame =  Image.open(f"trainroms/Images/{self.data['name']}/Type/{self.args['type']}_EN.png")
                    img.paste(TypeFrame, (0, 0))
                if self.args['dest'] is not None : 
                    DestFrame =  Image.open(f"trainroms/Images/{self.data['name']}/DestNext/{self.args['dest']}_EN.png")
                    img.paste(DestFrame, (48, 0))
                count = 0

            Framebuffer.append(img.convert("P", palette=Image.ADAPTIVE, colors=self.data['colors']))
            i = i + 1
            count = count + 1
        MakeGif(isScrolling=True)


def MakeGif(isScrolling: bool = False):
    duration = 3000
    if isScrolling: duration=20

    Framebuffer[0].save('output.gif', format='GIF', save_all=True, append_images=Framebuffer[1:], optimize=False, duration=duration, loop=0)
    Framebuffer.clear()
    LedDriver().clear()  
    LedDriver().show()