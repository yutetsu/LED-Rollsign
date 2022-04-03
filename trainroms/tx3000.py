from PIL import Image
from database import RollsignDatabase
from hardware import LedDriver

Framebuffer = []

class Tx3000():
    def __init__(self, args):
        self.args = args
        self.data = RollsignDatabase().GetRollsignData(self.args['Train'])

    def main(self):
        match self.args.Mode:
            case "Special":
                self.special_mode()
            case "Normal":
                self.normal_mode()
            case "next_mode":
                self.NextMode()
            case _:
                return {'Message': 'Mode not found', 'RecivedMode': self.args.Mode,'ModeAvalible': self.data['Mode']}, 404
        return {'Message': 'Rollsign set', 'Args': self.args}, 200

    def special_mode(self):
        img = Image.new("RGB", (self.data['Width'], self.data['Height']), (0, 0, 0))
        if self.args['Type'] is not None : 
            SpecialFrame =  Image.open(f"trainroms/Images/{self.data['Name']}/Special/{self.args['Type']}.png")
            img.paste(SpecialFrame, (0, 0))
        Framebuffer.append(img.convert("P", palette=Image.ADAPTIVE, colors=self.data['Colors']))
        MakeGif()

    def normal_mode(self):
        img = Image.new("RGB", (self.data['Width'], self.data['Height']), (0, 0, 0))
        if self.args['Type'] is not None : 
            TypeFrame =  Image.open(f"trainroms/Images/{self.data['Name']}/Type/{self.args['Type']}.png")
            img.paste(TypeFrame, (0, 0))
        if self.args['Dest'] is not None : 
            DestFrame =  Image.open(f"trainroms/Images/{self.data['Name']}/Dest/{self.args['Dest']}.png")
            img.paste(DestFrame, (48, 0))
        Framebuffer.append(img.convert("P", palette=Image.ADAPTIVE, colors=self.data['Colors']))
        MakeGif()

    def next_mode(self):  
        img = Image.new("RGB", (self.data['Width'], self.data['Height']), (0, 0, 0))
        if self.args['Type'] is not None : 
            TypeFrame =  Image.open(f"trainroms/Images/{self.data['Name']}/Type/{self.args['Type']}.png")
            img.paste(TypeFrame, (0, 0))
        if self.args['Dest'] is not None : 
            DestFrame =  Image.open(f"trainroms/Images/{self.data['Name']}/NextDest/{self.args['Dest']}_JP.png")
            img.paste(DestFrame, (48, 0))
        if self.args['Next'] is not None : 
            NextFrame =  Image.open(f"trainroms/Images/{self.data['Name']}/Next/{self.args['Next']}_JP.png")
            img.paste(NextFrame, (48, 16))
        Framebuffer.append(img.convert("P", palette=Image.ADAPTIVE, colors=self.data['Colors']))
        img = Image.new("RGB", (self.data['Width'], self.data['Height']), (0, 0, 0))
        if self.args['Type'] is not None : 
            TypeFrame =  Image.open(f"trainroms/Images/{self.data['Name']}/Type/{self.args['Type']}.png")
            img.paste(TypeFrame, (0, 0))
        if self.args['Dest'] is not None : 
            DestFrame =  Image.open(f"trainroms/Images/{self.data['Name']}/NextDest/{self.args['Dest']}_EN.png")
            img.paste(DestFrame, (48, 0))
        if self.args['Next'] is not None : 
            NextFrame =  Image.open(f"trainroms/Images/{self.data['Name']}/Next/{self.args['Next']}_EN.png")
            img.paste(NextFrame, (48, 16))
        Framebuffer.append(img.convert("P", palette=Image.ADAPTIVE, colors=self.data['Colors']))
        MakeGif()


def MakeGif():
    Framebuffer[0].save('output.gif', format='GIF', save_all=True, append_images=Framebuffer[1:], optimize=False, duration=3000, loop=0)
    Framebuffer.clear()
    LedDriver().clear()  
    LedDriver().show()