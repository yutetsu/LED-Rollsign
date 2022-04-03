from PIL import Image
from database import RollsignDatabase
from hardware import LedDriver

Framebuffer = []

class Laview():
    def __init__(self, args):
        self.args = args
        self.data = RollsignDatabase().GetRollsignData(self.args['train'])

    def main(self):
        match self.args.mode:
            case "Special":
                self.special_mode()
            case "TypeOnly":
                self.type_only_mode()
            case "Normal":
                self.normal_mode()
            case _:
                return {'message': 'Mode not found', 'recived_mode': self.args.Mode,'mode_avalible': self.data['mode']}, 404
        return {'message': 'Rollsign set', 'args': self.args}, 200

    def special_mode(self):
        img = Image.new("RGB", (self.data['width'], self.data['height']), (0, 0, 0))
        if self.args['type'] is not None : 
            SpecialFrame =  Image.open(f"trainroms/Images/{self.data['name']}/Special/{self.args['type']}.png")
            img.paste(SpecialFrame, (0, 0))
        Framebuffer.append(img.convert("P", palette=Image.ADAPTIVE, colors=self.data['colors']))
        MakeGif()
    
    def type_only_mode(self):
        img = Image.new("RGB", (self.data['width'], self.data['height']), (0, 0, 0))
        if self.args['type'] is not None : 
            TypeFrame =  Image.open(f"trainroms/Images/{self.data['name']}/TypeOnly/{self.args['type']}_JP.png")
            img.paste(TypeFrame, (0, 0))
        Framebuffer.append(img.convert("P", palette=Image.ADAPTIVE, colors=self.data['colors']))
        img = Image.new("RGB", (self.data['width'], self.data['height']), (0, 0, 0))
        if self.args['type'] is not None : 
            TypeFrame =  Image.open(f"trainroms/Images/{self.data['name']}/TypeOnly/{self.args['type']}_EN.png")
            img.paste(TypeFrame, (0, 0))
        Framebuffer.append(img.convert("P", palette=Image.ADAPTIVE, colors=self.data['colors']))
        MakeGif()


    def normal_mode(self):
        img = Image.new("RGB", (self.data['width'], self.data['height']), (0, 0, 0))
        if self.args['type'] is not None : 
            TypeFrame =  Image.open(f"trainroms/Images/{self.data['name']}/Type/{self.args['type']}_JP.png")
            img.paste(TypeFrame, (0, 0))
        if self.args['dest'] is not None : 
            DestFrame =  Image.open(f"trainroms/Images/{self.data['name']}/Dest/{self.args['dest']}_JP.png")
            img.paste(DestFrame, (39, 0))
        Framebuffer.append(img.convert("P", palette=Image.ADAPTIVE, colors=self.data['colors']))
        img = Image.new("RGB", (self.data['width'], self.data['height']), (0, 0, 0))
        if self.args['type'] is not None : 
            TypeFrame =  Image.open(f"trainroms/Images/{self.data['name']}/Type/{self.args['type']}_EN.png")
            img.paste(TypeFrame, (0, 0))
        if self.args['dest'] is not None : 
            DestFrame =  Image.open(f"trainroms/Images/{self.data['name']}/Dest/{self.args['dest']}_EN.png")
            img.paste(DestFrame, (39, 0))
        Framebuffer.append(img.convert("P", palette=Image.ADAPTIVE, colors=self.data['colors']))
        MakeGif()
   

def MakeGif():
    Framebuffer[0].save('output.gif', format='GIF', save_all=True, append_images=Framebuffer[1:], optimize=False, duration=3000, loop=0)
    Framebuffer.clear()
    LedDriver().clear()  
    LedDriver().show()