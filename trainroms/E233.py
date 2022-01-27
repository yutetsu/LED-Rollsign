from PIL import Image, ImageFont, ImageDraw
from database.RollsignData import RollsignDatabase
from hardware.LED import LED_Driver

Framebuffer = []

class E233():
    def __init__(self, args):
        self.args = args
        self.data = RollsignDatabase().GetRollsignData(self.args['Train'])

    def Main(self):
        match self.args.Mode:
            case "Special":
                self.SpecialMode()
            case "TypeOnly":
                self.TypeOnlyMode()
            case "DestOnly":
                self.DestOnlyMode()
            case "LineOnly":
                self.LineOnlyMode()
            case "Normal":
                self.NormalMode()
            case "Line":
                self.LineMode()
            case "Line-TypeChange":
                self.LineTypeChangeMode()
            case "Next":
                self.NextMode()
            case "StopsAt":
                self.StopsAtMode()
            case _:
                return {'Message': 'Mode not found', 'RecivedMode': self.args.Mode,'ModeAvalible': self.data['Mode']}, 404
        return {'Message': 'Rollsign set', 'Args': self.args}, 200

    def SpecialMode(self):
        img = Image.new("RGB", (self.data['Width'], self.data['Height']), (0, 0, 0))
        if self.args['Type'] is not None : 
            SpecialFrame =  Image.open(f"trainroms/Images/{self.data['Name']}/Special/{self.args['Type']}.png")
            img.paste(SpecialFrame, (0, 0))
        Framebuffer.append(img.convert("P", palette=Image.ADAPTIVE, colors=self.data['Colors']))
        MakeGif()

    def TypeOnlyMode(self):
        img = Image.new("RGB", (self.data['Width'], self.data['Height']), (0, 0, 0))
        if self.args['Type'] is not None : 
            TypeFrame =  Image.open(f"trainroms/Images/{self.data['Name']}/TypeOnly/{self.args['Type']}.png")
            img.paste(TypeFrame, (0, 0))
        Framebuffer.append(img.convert("P", palette=Image.ADAPTIVE, colors=self.data['Colors']))
        MakeGif()

    def DestOnlyMode(self):
        img = Image.new("RGB", (self.data['Width'], self.data['Height']), (0, 0, 0))
        if self.args['Dest'] is not None : 
            DestFrame =  Image.open(f"trainroms/Images/{self.data['Name']}/DestOnly/{self.args['Dest']}.png")
            img.paste(DestFrame, (0, 0))
        Framebuffer.append(img.convert("P", palette=Image.ADAPTIVE, colors=self.data['Colors']))
        MakeGif()

    def LineOnlyMode(self):
        img = Image.new("RGB", (self.data['Width'], self.data['Height']), (0, 0, 0))
        if self.args['Line'] is not None : 
            LineFrame =  Image.open(f"trainroms/Images/{self.data['Name']}/LineOnly/{self.args['Line']}.png")
            img.paste(LineFrame, (0, 0))
        Framebuffer.append(img.convert("P", palette=Image.ADAPTIVE, colors=self.data['Colors']))
        MakeGif()
        
    def NormalMode(self):
        img = Image.new("RGB", (self.data['Width'], self.data['Height']), (0, 0, 0))
        if self.args['Type'] is not None : 
            TypeFrame =  Image.open(f"trainroms/Images/{self.data['Name']}/Type/{self.args['Type']}_JP.png")
            img.paste(TypeFrame, (0, 0))
        if self.args['Dest'] is not None : 
            DestFrame =  Image.open(f"trainroms/Images/{self.data['Name']}/Dest/{self.args['Dest']}.png")
            img.paste(DestFrame, (48, 0))
        Framebuffer.append(img.convert("P", palette=Image.ADAPTIVE, colors=self.data['Colors']))
        MakeGif()
    
    def LineMode(self):
        img = Image.new("RGB", (self.data['Width'], self.data['Height']), (0, 0, 0))
        if self.args['Type'] is not None : 
            TypeFrame =  Image.open(f"trainroms/Images/{self.data['Name']}/Type/{self.args['Type']}_JP.png")
            img.paste(TypeFrame, (0, 0))
        if self.args['Dest'] is not None : 
            DestFrame =  Image.open(f"trainroms/Images/{self.data['Name']}/Dest/{self.args['Dest']}.png")
            img.paste(DestFrame, (48, 0))
        Framebuffer.append(img.convert("P", palette=Image.ADAPTIVE, colors=self.data['Colors']))
        img = Image.new("RGB", (self.data['Width'], self.data['Height']), (0, 0, 0))
        if self.args['Type'] is not None : 
            TypeFrame =  Image.open(f"trainroms/Images/{self.data['Name']}/Type/{self.args['Type']}_JP.png")
            img.paste(TypeFrame, (0, 0))
        if self.args['Line'] is not None : 
            LineFrame =  Image.open(f"trainroms/Images/{self.data['Name']}/Line/{self.args['Line']}.png")
            img.paste(LineFrame, (48, 0))
        Framebuffer.append(img.convert("P", palette=Image.ADAPTIVE, colors=self.data['Colors']))
        MakeGif()

    def LineTypeChangeMode(self):
        img = Image.new("RGB", (self.data['Width'], self.data['Height']), (0, 0, 0))
        if self.args['Type'] is not None : 
            TypeFrame =  Image.open(f"trainroms/Images/{self.data['Name']}/Type/{self.args['Type']}_JP.png")
            img.paste(TypeFrame, (0, 0))
        if self.args['Dest'] is not None : 
            DestFrame =  Image.open(f"trainroms/Images/{self.data['Name']}/Dest/{self.args['Dest']}.png")
            img.paste(DestFrame, (48, 0))
        Framebuffer.append(img.convert("P", palette=Image.ADAPTIVE, colors=self.data['Colors']))
        img = Image.new("RGB", (self.data['Width'], self.data['Height']), (0, 0, 0))
        if self.args['Type'] is not None : 
            TypeFrame =  Image.open(f"trainroms/Images/{self.data['Name']}/Type/{self.args['Type']}_JP.png")
            img.paste(TypeFrame, (0, 0))
        if self.args['Line'] is not None : 
            LineFrame =  Image.open(f"trainroms/Images/{self.data['Name']}/Line/{self.args['Line']}.png")
            img.paste(LineFrame, (48, 0))
        Framebuffer.append(img.convert("P", palette=Image.ADAPTIVE, colors=self.data['Colors']))
        img = Image.new("RGB", (self.data['Width'], self.data['Height']), (0, 0, 0))
        if self.args['Type'] is not None : 
            TypeFrame =  Image.open(f"trainroms/Images/{self.data['Name']}/Type/{self.args['Type']}_JP.png")
            img.paste(TypeFrame, (0, 0))
        if self.args['TypeChange'] is not None : 
            TypeChangeFrame =  Image.open(f"trainroms/Images/{self.data['Name']}/TypeChange/{self.args['TypeChange']}.png")
            img.paste(TypeChangeFrame, (48, 0))
        Framebuffer.append(img.convert("P", palette=Image.ADAPTIVE, colors=self.data['Colors']))
        MakeGif()

    def NextMode(self):
        img = Image.new("RGB", (self.data['Width'], self.data['Height']), (0, 0, 0))
        if self.args['Type'] is not None : 
            TypeFrame =  Image.open(f"trainroms/Images/{self.data['Name']}/Type/{self.args['Type']}_JP.png")
            img.paste(TypeFrame, (0, 0))
        if self.args['Dest'] is not None : 
            DestFrame =  Image.open(f"trainroms/Images/{self.data['Name']}/DestNext/{self.args['Dest']}_JP.png")
            img.paste(DestFrame, (48, 0))
        if self.args['Next'] is not None : 
            NextFrame =  Image.open(f"trainroms/Images/{self.data['Name']}/Next/{self.args['Next']}_JP.png")
            img.paste(NextFrame, (48, 16))
        Framebuffer.append(img.convert("P", palette=Image.ADAPTIVE, colors=self.data['Colors']))
        img = Image.new("RGB", (self.data['Width'], self.data['Height']), (0, 0, 0))
        if self.args['Type'] is not None : 
            TypeFrame =  Image.open(f"trainroms/Images/{self.data['Name']}/Type/{self.args['Type']}_EN.png")
            img.paste(TypeFrame, (0, 0))
        if self.args['Dest'] is not None : 
            DestFrame =  Image.open(f"trainroms/Images/{self.data['Name']}/DestNext/{self.args['Dest']}_EN.png")
            img.paste(DestFrame, (48, 0))
        if self.args['Next'] is not None : 
            NextFrame =  Image.open(f"trainroms/Images/{self.data['Name']}/Next/{self.args['Next']}_EN.png")
            img.paste(NextFrame, (48, 16))
        Framebuffer.append(img.convert("P", palette=Image.ADAPTIVE, colors=self.data['Colors']))
        MakeGif()

    def StopsAtMode(self):
        Text = f"この電車の停車駅は{self.args['StopsAt']}駅に停車ります。"
        Font = ImageFont.truetype(f"trainroms/Fonts/{self.data['Font']}", 16)
        TextWidth = Font.getsize(Text)[0]

        i = 0
        count = 0
        while (TextWidth + 80) >= i:
            img = Image.new("RGB", (self.data['Width'], self.data['Height']), (0, 0, 0))
            draw = ImageDraw.Draw(img)
            draw.fontmode = "1"
            draw.text(((-abs(i) + self.data['Width']), 16), Text, font=Font, fill=(255, 255, 0))

            if count <= 150:
                if self.args['Type'] is not None : 
                    TypeFrame =  Image.open(f"trainroms/Images/{self.data['Name']}/Type/{self.args['Type']}_JP.png")
                    img.paste(TypeFrame, (0, 0))
                if self.args['Dest'] is not None : 
                    DestFrame =  Image.open(f"trainroms/Images/{self.data['Name']}/DestNext/{self.args['Dest']}_JP.png")
                    img.paste(DestFrame, (48, 0))
            elif count <= 300:
                if self.args['Type'] is not None : 
                    TypeFrame =  Image.open(f"trainroms/Images/{self.data['Name']}/Type/{self.args['Type']}_EN.png")
                    img.paste(TypeFrame, (0, 0))
                if self.args['Dest'] is not None : 
                    DestFrame =  Image.open(f"trainroms/Images/{self.data['Name']}/DestNext/{self.args['Dest']}_EN.png")
                    img.paste(DestFrame, (48, 0))
            else:
                if self.args['Type'] is not None : 
                    TypeFrame =  Image.open(f"trainroms/Images/{self.data['Name']}/Type/{self.args['Type']}_EN.png")
                    img.paste(TypeFrame, (0, 0))
                if self.args['Dest'] is not None : 
                    DestFrame =  Image.open(f"trainroms/Images/{self.data['Name']}/DestNext/{self.args['Dest']}_EN.png")
                    img.paste(DestFrame, (48, 0))
                count = 0

            Framebuffer.append(img.convert("P", palette=Image.ADAPTIVE, colors=self.data['Colors']))
            i = i + 1
            count = count + 1
        MakeGif(isScrolling=True)


def MakeGif(isScrolling: bool = False):
    duration = 3000
    if isScrolling: duration=20

    Framebuffer[0].save('output.gif', format='GIF', save_all=True, append_images=Framebuffer[1:], optimize=False, duration=duration, loop=0)
    Framebuffer.clear()
    LED_Driver().Clear()  
    LED_Driver().Show()