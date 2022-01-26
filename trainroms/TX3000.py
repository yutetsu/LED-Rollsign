from PIL import Image
from database.RollsignData import RollsignDatabase
from hardware.LED import LED_Driver

Framebuffer = []

class TX3000():
    def __init__(self, args):
        self.args = args
        self.data = RollsignDatabase().GetRollsignData(self.args['Train'])

    def Main(self):
        match self.args.Mode:
            case "Special":
                self.SpecialMode()
            case "Normal":
                self.NormalMode()
            case "Next":
                self.NextMode()
            case _:
                return {'Message': 'Mode not found', 'RecivedMode': self.args.Mode,'ModeAvalible': self.data['ROM_Mode']}, 404
        return {'Message': 'Rollsign set', 'Args': self.args}, 200

    def SpecialMode(self):
        img = Image.new("RGB", (self.data['Width'], self.data['Height']), (0, 0, 0))
        if self.args['Type'] is not None : 
            SpecialFrame =  Image.open(f"trainroms/data/{self.data['Name']}/Special/{self.args['Type']}.png")
            img.paste(SpecialFrame, (0, 0))
        Framebuffer.append(img.convert("P", palette=Image.ADAPTIVE, colors=self.data['Colors']))
        MakeGif()

    def NormalMode(self):
        img = Image.new("RGB", (self.data['Width'], self.data['Height']), (0, 0, 0))
        if self.args['Type'] is not None : 
            TypeFrame =  Image.open(f"trainroms/data/{self.data['Name']}/Type/{self.args['Type']}.png")
            img.paste(TypeFrame, (0, 0))
        if self.args['Dest'] is not None : 
            DestFrame =  Image.open(f"trainroms/data/{self.data['Name']}/Dest/{self.args['Dest']}.png")
            img.paste(DestFrame, (48, 0))
        Framebuffer.append(img.convert("P", palette=Image.ADAPTIVE, colors=self.data['Colors']))
        MakeGif()

    def NextMode(self):  
        img = Image.new("RGB", (self.data['Width'], self.data['Height']), (0, 0, 0))
        if self.args['Type'] is not None : 
            TypeFrame =  Image.open(f"trainroms/data/{self.data['Name']}/Type/{self.args['Type']}.png")
            img.paste(TypeFrame, (0, 0))
        if self.args['Dest'] is not None : 
            DestFrame =  Image.open(f"trainroms/data/{self.data['Name']}/NextDest/{self.args['Dest']}_JP.png")
            img.paste(DestFrame, (48, 0))
        if self.args['Next'] is not None : 
            NextFrame =  Image.open(f"trainroms/data/{self.data['Name']}/Next/{self.args['Next']}_JP.png")
            img.paste(NextFrame, (48, 16))
        Framebuffer.append(img.convert("P", palette=Image.ADAPTIVE, colors=self.data['Colors']))
        img = Image.new("RGB", (self.data['Width'], self.data['Height']), (0, 0, 0))
        if self.args['Type'] is not None : 
            TypeFrame =  Image.open(f"trainroms/data/{self.data['Name']}/Type/{self.args['Type']}.png")
            img.paste(TypeFrame, (0, 0))
        if self.args['Dest'] is not None : 
            DestFrame =  Image.open(f"trainroms/data/{self.data['Name']}/NextDest/{self.args['Dest']}_EN.png")
            img.paste(DestFrame, (48, 0))
        if self.args['Next'] is not None : 
            NextFrame =  Image.open(f"trainroms/data/{self.data['Name']}/Next/{self.args['Next']}_EN.png")
            img.paste(NextFrame, (48, 16))
        Framebuffer.append(img.convert("P", palette=Image.ADAPTIVE, colors=self.data['Colors']))
        MakeGif()


def MakeGif(isStopsAt: bool = False):
    duration = 3000
    if isStopsAt: duration=30

    Framebuffer[0].save('output.gif', format='GIF', save_all=True, append_images=Framebuffer[1:], optimize=False, duration=duration, loop=0)
    Framebuffer.clear()
    LED_Driver().Clear()  
    LED_Driver().Show()