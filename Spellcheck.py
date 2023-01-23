from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.core.spelling import Spelling
Window.size=(375,550)
Builder.load_string(''' 
<SpellWidget>
    BoxLayout:
        orientation:"vertical"
        size: root.width,root.height
        Label:
            id:suggestwords
            text:"Enter Word Below"
            font_size:25
            size_hint:(1,9)
            background_color:(0.051,0.239,0.239,1)
            canvas.before:
                Color:
                    rgba:self.background_color
                Rectangle:
                    size:self.size
                    pos: self.pos
        GridLayout:
            cols:2
            rows:1
            TextInput:
                id:userword
                text:""
                multiline:True
                font_size:25
                size_hint:(0.8,1)
            Button:
                id:checkword
                text:"Suggest"
                font_size:19
                size_hint:(0.2,1)
                background_color:(0,0.6,0.059,1.0)
                background_normal:''
                on_press:root.checkword()   
                    
                    ''')
class SpellWidget(Widget):
    def checkword(self):
        spell=Spelling()
        spell.select_language("en-US")
        word=self.ids.userword.text
        suggestions=spell.suggest(word)
        prevword=''
        for suggestion in suggestions:
            prevword=f'{prevword}\n{suggestion}'
        self.ids.suggestwords.text=prevword
class Spellcheck(App):
    def build(self):
        return SpellWidget()
Spellcheck().run()