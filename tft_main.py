#!/usr/bin/env python
# -*- coding: utf-8 -*-

#tft.py


import kivy
kivy.require('1.8.0')

__version__ = "1"

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition, FadeTransition
from kivy.uix.relativelayout import RelativeLayout
from kivy.network.urlrequest import UrlRequest
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.progressbar import ProgressBar
from kivy.config import Config
from kivy.uix.scrollview import ScrollView
from kivy.uix.dropdown import DropDown
from kivy.base import runTouchApp
#from kivy.core.window import Window
#from kivy.uix.popup import Popup

#Config.set('graphics', 'width', '750')
#Config.set('graphics', 'height', '1334')
Config.set('graphics', 'width', '540')
Config.set('graphics', 'height', '960')

Builder.load_string("""

<CustomScreenManager>
	id: custom_screen_manager
	canvas.before:
        Color:
            rgba: 1,1,1,1
        Rectangle:
            pos: self.pos
            size: self.size

<LoginScreen>:
    id: login_screeen
    name: 'login_screen'
    canvas.before:
        Color:
            rgba: 1,1,1,1
        Rectangle:
            pos: self.pos
            size: self.size
    RelativeLayout:
        id: relative_layout
        Label:
            id: app_name
            text: "TFT"
            font_size: 60
            bold: True
            color: 0.77, 0.12, 0.23,1
            size_hint: .35, .075
            pos: 350, 1260
        Label:
            id: username_label
            text: "Username:"
            font_size: 30
            size_hint: 0.15, 0.005
            pos: 200, 1200
            color: 0.77, 0.12, 0.23,1
            bold: True
        TextInput:
            id: username
            multiline: False
            foucs: True
            size_hint: 0.5, 0.075
            pos: 225, 1050
        Label:
            id: password_label
            text: "Password:"
            font_size: 30
            size_hint: 0.15, 0.005
            pos: 200, 900
            color: 0.77, 0.12, 0.23,1
            bold: True
        TextInput:
            id: password
            multiline: False
            password: True
            foucs: True
            size_hint: 0.5, 0.075
            pos: 225, 750
        Button:
            id: newuser
            text: "New User?"
            font_size: 25
            size_hint: 0.15, 0.03
            color: 0,1,1,1
            pos:753,700
            on_release: root.register()
            color: 1,1,1,1
            background_color:2.07,0.12,0.23,1
            bold: True
        Label:
            id: incorrect_label
            text: ""
            font_size: 30
            size_hint: 0.15, 0.005
            pos: 400, 550
            color: 0.77, 0.12, 0.23,1
            bold: True
        Button:
            id: submit
            text: "Submit"
            font_size: 25
            size_hint: 0.15, 0.05
            color: 1,1,1,1
            pos: 750, 400
            on_release: root.sign_in()
            background_color:2.07,0.12,0.23,1
            bold: True


<HomeScreen>:
    id: home_screeen
    name: 'home_screen'
    canvas.before:
        Color:
            rgba: 1,1,1,1
        Rectangle:
            pos: self.pos
            size: self.size
    canvas:
        Color:
            rgba: 0.77,0.12,0.23,1.9
        Rectangle:
            pos: 0, 1295
            size: 1175, 45
    RelativeLayout:
        id: relative_layout
        Button:
            id: my_profile
            text: "My Profile"
            font_size: 30
            bold: True
            color: 1,1,1,1
            size_hint: .15, .025
            pos: 970, 1300
            on_release: root.my_profile()
            background_color: 1,1,1,0
        Button:
            id: buy
            text: "Buy Books"
            font_size: 50
            color: 1,1,1,1
            bold: True
            size_hint: 0.4, 0.15
            pos: 300, 800
            on_release: root.buy()
            background_color:2.07,0.12,0.23,1
        Button:
            id: sell
            text: "Sell Books"
            font_size: 50
            color: 1,1,1,1
            bold: True
            size_hint: 0.4, 0.15
            pos: 300, 400
            on_release: root.sell()
            background_color:2.07,0.12,0.23,1


<ProfileScreen>:
    id: profile_screeen
    name: 'profile_screen'
    canvas.before:
        Color:
            rgba: 1,1,1,1
        Rectangle:
            pos: self.pos
            size: self.size
    canvas:
        Color:
            rgba: 0.77,0.12,0.23,1
        Rectangle:
            pos: 0, 1295
            size: 1300, 45
    RelativeLayout:
        id: relative_layout
        Label:
            id: name
            text: "First Last"
            font_size: 50
            bold: True
            color:0.77,0.12,0.23,1
            size_hint: .15, .025
            pos: 480, 1150
        Label:
            id: email
            text: "firstlast@stanford.edu"
            font_size: 50
            bold: True
            color: 0.77,0.12,0.23,1
            size_hint: 0.15, 0.025
            pos: 480,1000
        Label:
            id: phone
            text: "My Number"
            font_size: 50
            bold: True
            color: 0.77,0.12,0.23,1
            size_hint: 0.15, 0.025
            pos:480,850
        Label:
            id: university
            text: "Amazing University"
            font_size: 50
            bold: True
            color: 0.77,0.12,0.23,1
            size_hint: 0.15, 0.025
            pos:480,700
        Button:
            id: back
            text: "Back"
            font_size: 50
            color: 1,1,1,1
            bold: True
            size_hint: 0.5, 0.2
            pos: 0,0
            on_release: root.back()
            background_color:2.07,0.12,0.23,1
        Button:
            id: Edit
            text: "Edit"
            font_size: 50
            color: 1,1,1,1
            bold: True
            size_hint: 0.5, 0.2
            pos: 538,0
            on_release: root.edit()
            background_color:2.07,0.12,0.23,1

<DepartmentScreen>:
    id: deparment_screen
    name: 'department_screen'
    canvas.before:
        Color:
            rgba: 1,1,1,1
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        id: boxlayout
        orientation:'vertical'
        Label:
            id: choose
            text: "Choose Department"
            size_hint: 1,0.1
            font_size:50
            color: 0.77,0.12,0.23,1
            bold: True
        ScrollView:
            id: ScrollView
            size_hint: 1, 0.8
            scroll_distance: 5
            scroll_timeout: 200
            GridLayout:
                id: grid_layout
                orientation: 'vertical'
                cols: 1
                rows:7
                height:500
                size_hint_x: 1
                size_hint_y: None
                Button:
                    id: math
                    text: "Math"
                    font_size: 50
                    color: 1,1,1,1
                    size_hint_x: 1
                    size_hint_y: None
                    height: 300
                    on_press: root.math()
                    on_release: root.specificDepartmentScreen()
                    background_color:2.07,0.12,0.23,1
                    bold: True
                Button:
                    id: biology
                    text: "Biology"
                    font_size: 50
                    color: 1,1,1,1
                    size_hint_x: 1
                    size_hint_y: None
                    height: 300
                    on_press: root.biology()
                    on_release: root.specificDepartmentScreen()
                    background_color:2.07,0.12,0.23,1
                    bold: True
                Button:
                    id: chemistry
                    text: "Chemistry"
                    font_size: 50
                    color: 1,1,1,1
                    size_hint_x: 1
                    size_hint_y: None
                    height: 300
                    on_press: root.chemistry()
                    on_release: root.specificDepartmentScreen()
                    background_color:2.07,0.12,0.23,1
                    bold: True
                Button:
                    id: computer science
                    text: "CS"
                    font_size: 50
                    color: 1,1,1,1
                    size_hint_x: 1
                    size_hint_y: None
                    height: 300
                    on_press: root.computerScience()
                    on_release: root.specificDepartmentScreen()
                    background_color:2.07,0.12,0.23,1
                    bold: True
                Button:
                    id: psychology
                    text: "Psych"
                    font_size: 50
                    color: 1,1,1,1
                    size_hint_x: 1
                    size_hint_y: None
                    height: 300
                    on_press: root.psychology()
                    background_color:2.07,0.12,0.23,1
                    on_release: root.specificDepartmentScreen()
                    bold: True
                Button:
                    id: history
                    text: "History"
                    font_size: 50
                    color: 1,1,1,1
                    size_hint_x: 1
                    size_hint_y: None
                    height: 300
                    on_press: root.history()
                    on_release: root.specificDepartmentScreen()
                    background_color:2.07,0.12,0.23,1
                    bold: True
                Button:
                    id: english
                    text: "English"
                    font_size: 50
                    color: 1,1,1,1
                    size_hint_x: 1
                    size_hint_y: None
                    height: 300
                    on_press: root.english()
                    on_release: root.specificDepartmentScreen()
                    background_color:2.07,0.12,0.23,1
                    bold: True
        Button:
            id: back
            text: "Back"
            font_size: 50
            size_hint: 1, 0.1
            color: 0.77,0.12,0.23,1
            on_release: root.back()
            bold: True
            background_color:1,1,1,0


<RegistrationScreen>:
    id: registration
    name: 'registration_screen'
    canvas.before:
        Color:
            rgba: 1,1,1,1
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        id: box_layout
        orientation: 'vertical'
        Label:
            id: top_label
            text: "Enter Data"
            halign: 'center'
            font_size: 70
            color: 1,1,1,1
            canvas.before:
                Color:
                    rgba: 0.77,0.12,0.23,1
                Rectangle:
                    pos: self.pos
                    size: self.size
            background_color:1,1,1,1
            bold: True
        BoxLayout:
            id: box1
            orientation: 'horizontal'
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    pos: self.pos
                    size: self.size
            Label:
                id: label1
                text: "Name"
                halign: 'center'
                font_size: 50
                size_hint: .3, 1
                color: 0.77,0.12,0.23,1
                bold: True
            TextInput:
                id: name
                halign: 'center'
                font_size: 50
                size_hint: .7, 1
                multiline: False
                focus: True
        BoxLayout:
            id: box2
            orientation: 'horizontal'
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    pos: self.pos
                    size: self.size
            Label:
                id: label2
                text: "Email"
                halign: 'center'
                font_size: 50
                size_hint: .3, 1
                color:0.77,0.12,0.23,1
                bold: True
            TextInput:
                id: email
                halign: 'center'
                font_size: 50
                size_hint: .7, 1
                multiline: False
                focus: True
        BoxLayout:
            id: box3
            orientation: 'horizontal'
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    pos: self.pos
                    size: self.size
            Label:
                id: label3
                text: "Phone"
                halign: 'center'
                font_size: 50
                size_hint: .3, 1
                color: 0.77,0.12,0.23,1
                bold: True
            TextInput:
                id: phone
                halign: 'center'
                font_size: 50
                size_hint: .7, 1
                multiline: False
                focus: True
        BoxLayout:
            id: box4
            orientation: 'horizontal'
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    pos: self.pos
                    size: self.size
            Label:
                id: label4
                text: "University"
                halign: 'center'
                font_size: 50
                size_hint: .3, 1
                color: 0.77,0.12,0.23,1
                bold: True
            TextInput:
                id: university
                halign: 'center'
                font_size: 50
                size_hint: .7, 1
                multiline: False
                focus: True
        BoxLayout:
            id: box5
            orientation: 'horizontal'
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    pos: self.pos
                    size: self.size
            Label:
                id: label5
                text: "Password"
                halign: 'center'
                font_size: 50
                size_hint: .3, 1
                color: 0.77,0.12,0.23,1
                bold: True
            TextInput:
                id: password
                halign: 'center'
                font_size: 50
                size_hint: .7, 1
                multiline: False
                focus: True
        BoxLayout:
            id: box6
            orientation: 'horizontal'
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    pos: self.pos
                    size: self.size
            Label:
                id: label6
                text: "Confirm"
                halign: 'center'
                font_size: 50
                size_hint: .3, 1
                color: 0.77,0.12,0.23,1
                bold: True
            TextInput:
                id: confirm
                halign: 'center'
                font_size: 50
                size_hint: .7, 1
                multiline: False
                focus: True
        BoxLayout:
            id: box_layout
            orientation: 'horizontal'
            Button:
                id: upload
                text: "Upload Pic"
                font_size: 50
                on_release: root.upload_pic()
                color: 1,1,1,1
                bold: True
                background_color:2.07,0.12,0.23,1
            Button:
                id: submit
                text: "Register"
                font_size:50
                on_release: root.submit()
                color: 1,1,1,1
                bold: True
                background_color:2.07,0.12,0.23,1

<SpecificDepartmentScreen>:
    id: specific_department_screen
    name: 'specific_department_screen'
    canvas.before:
        Color:
            rgba: 1,1,1,1
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        id: boxlayout
        orientation:'vertical'
        Label:
            id: choose
            text: "Choose Your Course"
            size_hint: 1,0.1
            font_size:50
            color: 0.77,0.12,0.23,1
            bold: True
        ScrollView:
            id: ScrollView
            size_hint: 1, 0.8
            scroll_distance: 5
            scroll_timeout: 200
            GridLayout:
                id: grid_layout
                orientation: 'vertical'
                cols: 2
                rows:15
                height:500
                size_hint_x: 1
                size_hint_y: None

        Button:
            id: back
            text: "Back"
            font_size: 50
            size_hint: 1, 0.1
            color: 0.77,0.12,0.23,1
            on_release: root.back()
            bold: True
            background_color: 1,1,1,0

<ListingsScreen>:
    id: listings_screen
    name: 'listings_screen'
    canvas.before:
        Color:
            rgba: 1,1,1,1
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        id: box_layout
        orientation:'vertical'
        Label:
            id: choose
            text: "Browse all the listings: "
            size_hint: 1,0.1
            font_size:50
            color: 0.77,0.12,0.23,1
            bold: True
        ScrollView:
            id: ScrollView
            size_hint: 1, 0.8
            scroll_distance: 5
            scroll_timeout: 200
            GridLayout:
                id: grid_layout
                orientation: 'vertical'
                cols: 2
                rows:15
                height:500
                size_hint_x: 1
                size_hint_y: None
        Button:
            id: back
            text: "Back"
            font_size: 50
            size_hint: 1, 0.1
            color: 0.77,0.12,0.23,1
            bold: True
            background_color:1,1,1,0

            on_release: root.back()


<SellScreen>:
    id: sell_screen
    name: 'sell_screen'
    canvas.before:
        Color:
            rgba: 1,1,1,1
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        id: box_layout
        orientation: 'vertical'
        Label:
            id: top_label
            text: "Upload Your Textbook"
            halign: 'center'
            font_size: 70
            color: 1,1,1,1
            canvas.before:
                Color:
                    rgba: 0.77,0.12,0.23,1
                Rectangle:
                    pos: self.pos
                    size: self.size
            background_color:1,1,1,1
            bold: True
        BoxLayout:
            id: box1
            orientation: 'horizontal'
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    pos: self.pos
                    size: self.size
            Label:
                id: label1
                text: "Title"
                halign: 'center'
                font_size: 40
                size_hint: .3, 1
                color: 0.77,0.12,0.23,1
                bold: True
            TextInput:
                id: textinput1
                multiline: False
                focus: True
                halign: 'center'
                font_size: 40
                size_hint: .7, 1
        BoxLayout:
            id: box2
            orientation: 'horizontal'
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    pos: self.pos
                    size: self.size
            Label:
                id: label2
                text: "Department"
                halign: 'center'
                font_size: 40
                size_hint: .3, 1
                color: 0.77,0.12,0.23,1
                bold: True
            BoxLayout:
                id: input2
                halign: 'center'
                size_hint: .7, 1
                Button:
                    id: select1
                    text: 'Select'
                    on_release: dropdown1.open(self)
                    size_hint_y: None
                    height: '73dp'
                    background_color:2.07,0.12,0.23,1
                    bold: True
                DropDown:
                    id: dropdown1
                    on_select: select1.text = '{}'.format(args[1])
                    Button:
                        text: 'Math'
                        size_hint_y: None
                        height: '73dp'
                        on_release: dropdown1.select('Math')
                        bold: True
                    Button:
                        text: 'Bio'
                        size_hint_y: None
                        height: '73dp'
                        on_release: dropdown1.select('Bio')
                        bold: True
                    Button:
                        text: 'Chem'
                        size_hint_y: None
                        height: '73dp'
                        on_release: dropdown1.select('Chem')
                        bold: True
                    Button:
                        text: 'CS'
                        size_hint_y: None
                        height: '73dp'
                        on_release: dropdown1.select('CS')
                        bold: True
                    Button:
                        text: 'English'
                        size_hint_y: None
                        height: '73dp'
                        on_release: dropdown1.select('English')
                        bold: True
                    Button:
                        text: 'History'
                        size_hint_y: None
                        height: '73dp'
                        on_release: dropdown1.select('History')
                        bold: True
                    Button:
                        text: 'Psych'
                        size_hint_y: None
                        height: '73dp'
                        on_release: dropdown1.select('Psych')
                        bold: True
        BoxLayout:
            id: box3
            orientation: 'horizontal'
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    pos: self.pos
                    size: self.size
            Label:
                id: label3
                text: "Class"
                halign: 'center'
                font_size: 40
                size_hint: .3, 1
                color: 0.77,0.12,0.23,1
                bold: True
            TextInput:
                id: textinput3
                halign: 'center'
                font_size: 40
                size_hint: .7, 1
        BoxLayout:
            id: box4
            orientation: 'horizontal'
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    pos: self.pos
                    size: self.size
            Label:
                id: label4
                text: "Price"
                halign: 'center'
                font_size: 40
                size_hint: .3, 1
                color: 0.77,0.12,0.23,1
                bold: True
            TextInput:
                id: textinput4
                halign: 'center'
                font_size: 40
                size_hint: .7, 1
        BoxLayout:
            id: box5
            orientation: 'horizontal'
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    pos: self.pos
                    size: self.size
            Label:
                id: label5
                text: "Sell/Rent"
                halign: 'center'
                font_size: 40
                size_hint: .3, 1
                color: 0.77,0.12,0.23,1
                bold: True
            BoxLayout:
                id: input5
                halign: 'center'
                size_hint: .7, 1
                Button:
                    id: select2
                    text: 'Select'
                    on_release: dropdown2.open(self)
                    size_hint_y: None
                    height: '73dp'
                    background_color:2.07,0.12,0.23,1
                    bold: True
                DropDown:
                    id: dropdown2
                    on_select: select2.text = '{}'.format(args[1])
                    Button:
                        text: 'Sell'
                        size_hint_y: None
                        height: '73dp'
                        on_release: dropdown2.select('Sell')
                        bold: True
                    Button:
                        text: 'Rent'
                        size_hint_y: None
                        height: '73dp'
                        on_release: dropdown2.select('Rent')
                        bold: True
        BoxLayout:
            id: box6
            orientation: 'horizontal'
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    pos: self.pos
                    size: self.size
            Label:
                id: label6
                text: "Condition"
                halign: 'center'
                font_size: 40
                size_hint: .3, 1
                color: 0.77,0.12,0.23,1
                bold: True
            BoxLayout:
                id: input6
                halign: 'center'
                size_hint: .7, 1
                Button:
                    id: select3
                    text: 'Select'
                    on_release: dropdown3.open(self)
                    size_hint_y: None
                    height: '73dp'
                    background_color:2.07,0.12,0.23,1
                    bold: True
                DropDown:
                    id: dropdown3
                    on_select: select3.text = '{}'.format(args[1])
                    Button:
                        text: 'New'
                        size_hint_y: None
                        height: '73dp'
                        on_release: dropdown3.select('New')
                        bold: True
                    Button:
                        text: 'Great'
                        size_hint_y: None
                        height: '73dp'
                        on_release: dropdown3.select('Great')
                        bold: True
                    Button:
                        text: 'Good'
                        size_hint_y: None
                        height: '73dp'
                        on_release: dropdown3.select('Good')
                        bold: True
                    Button:
                        text: 'Used'
                        size_hint_y: None
                        height: '73dp'
                        on_release: dropdown3.select('Used')
                        bold: True
        BoxLayout:
            id: box7
            orientation: 'horizontal'
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Rectangle:
                    pos: self.pos
                    size: self.size
            Label:
                id: label7
                text: "Description"
                halign: 'center'
                font_size: 40
                size_hint: .3, 1
                color: 0.77,0.12,0.23,1
                bold: True
            TextInput:
                id: textinput7
                halign: 'center'
                font_size: 40
                size_hint: .7, 1
        BoxLayout:
            id: box_layout
            orientation: 'horizontal'
            Button:
                id: back
                text: "Back"
                background_color:2.07,0.12,0.23,1
                bold: True
                on_release: root.back()
            Button:
                id: submit
                text: "Submit"
                on_release: root.submit()
                background_color:2.07,0.12,0.23,1
                bold: True


<CurrentListingScreen>:
    id: current_listing_screen
    name: 'current_listing_screen'
    canvas.before:
        Color:
            rgba: 1,1,1,1
        Rectangle:
            pos: self.pos
            size: self.size
    canvas:
        Color:
            rgba: 0.77,0.12,0.23,1
        Rectangle:
            pos: 0, 1295
            size: 1500, 45
    RelativeLayout:
        id: relative_layout
        Label:
            id: listing_department
            text: "Department"
            font_size: 50
            color: 0.77,0.12,0.23,1
            size_hint: .15, .025
            pos: 50, 1100
            bold: True
        	size_hint_y: None
            size_hint_x: .5
		    text_size: self.width, None
		    height: self.texture_size[1]
		    halign: 'center'
        Label:
            id: listing_class
            text: "Class"
            font_size: 50
            color: 0.77,0.12,0.23,1
            size_hint: 0.15, 0.025
            pos: 775, 1100
            bold: True
            size_hint_y: None
            size_hint_x: .5
		    text_size: self.width, None
		    height: self.texture_size[1]
		    halign: 'center'
        Label:
            id: listing_textbook
            text: "Textbook"
            font_size: 50
            color: 0.77,0.12,0.23,1
            pos: 50,900
            bold: True
            size_hint_y: None
            size_hint_x: .5
		    text_size: self.width, None
		    height: self.texture_size[1]
		    halign: 'center'
        Label:
            id: sale_method
            text: "Rent"
            font_size: 50
            color: 0.77,0.12,0.23,1
            size_hint: 0.15, 0.025
            pos: 775, 900
            bold: True
            size_hint_y: None
            size_hint_x: .5
		    text_size: self.width, None
		    height: self.texture_size[1]
		    halign: 'center'
        Label:
            id: price
            text: "Cost"
            font_size: 50
            color:0.77,0.12,0.23,1
            size_hint:0.15, 0.025
            pos: 775,700
            bold: True
            size_hint_y: None
            size_hint_x: .5
		    text_size: self.width, None
		    height: self.texture_size[1]
		    halign: 'center'
        Label:
            id: listing_condition
            text: "Condition"
            font_size: 50
            color: 0.77,0.12,0.23,1
            size_hint: 0.15, 0.025
            pos:50,700
            bold: True
            size_hint_y: None
            size_hint_x: .5
		    text_size: self.width, None
		    height: self.texture_size[1]
		    halign: 'center'
        Label:
            id: listing_description
            text: "Amazing Resource"
            font_size: 50
            color: 0.77,0.12,0.23,1
            size_hint: 0.15, 0.025
            pos:50,500
            bold: True
            size_hint_y: None
            size_hint_x: .5
		    text_size: self.width, None
		    height: self.texture_size[1]
		    halign: 'center'
        Label:
            id: listing_seller
            text: "Seller"
            font_size: 50
            color: 0.77,0.12,0.23,1
            size_hint: 0.15, 0.025
            pos: 775, 500
            bold: True
            size_hint_y: None
            size_hint_x: .5
		    text_size: self.width, None
		    height: self.texture_size[1]
		    halign: 'center'
        Button:
            id: back
            text: "Back"
            font_size: 50
            color: 1,1,1,1
            size_hint: 0.5, 0.2
            pos: 0,0
            on_release: root.back()
            bold: True
            background_color:2.07,0.12,0.23,1
        Button:
            id: home
            text: "Home"
            font_size: 50
            color: 1,1,1,1
            size_hint: 0.5, 0.2
            pos: 750,0
            on_release: root.home()
            bold: True
            background_color:2.07,0.12,0.23,1


""")


  



class LoginScreen(Screen): 

	def sign_in(self):
		global username

		#gets the user input from the text inputs
		input_username = self.ids.username.text.strip()
		input_password = self.ids.password.text.strip()

		def authenticate(input_username, input_password):

			#Downloads the Users spreadsheet
			download = UrlRequest("https://spreadsheets.google.com/feeds/list/1GaWe5tWQO_z3hzPbu_7iCgElQOKeojiGP0ki-ouW4vI/od6/public/values?alt=json-in-script&callback=x") 
			download.wait()
			#parses it into json
			users = eval(download.result[18:len(download.result)-2])
			#separates each row into a list called entries
			entries = users["feed"]["entry"]
			#Iterates through all the entries
			for x in entries:
				username = x['gsx$username']['$t']
				password = x['gsx$password']['$t']
				if(username == input_username):
					if(password == input_password):
						return True
					else:
						return False

			#If the username wasn't found
			return False

		if(authenticate(input_username, input_password)):

			username = input_username

			#create and switch to home screen
			sm.remove_widget(self)
			home_screen = HomeScreen()
			sm.add_widget(home_screen)
			sm.current = 'home_screen'
		else:
			self.ids.incorrect_label.text = "Incorrect username/password"

	def register(self):
		sm.remove_widget(self)
		registration_screen = RegistrationScreen()
		sm.add_widget(registration_screen)
		sm.current = 'registration_screen'


class RegistrationScreen(Screen):

	def upload_pic(self):
		pass

	def submit(self):
		global username
		username = self.ids.email.text.strip()
		name = self.ids.name.text
		email = self.ids.email.text
		phone = self.ids.phone.text
		university = self.ids.university.text
		password = self.ids.password.text
		confirm = self.ids.confirm.text
		print password, confirm
		if (password != confirm):
			self.ids.top_label.text = "Passwords don't match!"
		else:
			url = "https://script.google.com/macros/s/AKfycbw82sgTI3SzMT6WAYY9DIxaXIU70ZYdhcXRgashr0B0r5SLWyoW/exec"
			url += "?"
			url += "username=" + username.replace(" ", "+")
			url += "&" + "name=" + name.replace(" ", "+")
			url += "&" + "email=" + email.replace(" ", "+")
			url += "&" + "phone=" + phone
			url += "&" + "university=" + university.replace(" ", "+")
			url += "&" + "password=" + password.replace(" ", "+")
			url += "&" + "listings=" + "[]"
			url += "&" + "requests=" + "[]"

			print url
			upload = UrlRequest(url)
			upload.wait()
			print upload.result

			sm.remove_widget(self)
			login_screen = LoginScreen()
			sm.add_widget(login_screen)
			sm.current = 'login_screen'


class ProfileScreen(Screen):

	def back(self):
		sm.remove_widget(self)
		home_screen = HomeScreen()
		sm.add_widget(home_screen)
		sm.current = 'home_screen'

	def edit(self):
		print "Not Implemented!"


class HomeScreen(Screen):

	def my_profile(self):
		global username

		sm.remove_widget(self)
		profile_screen = ProfileScreen()

		#Gets the user info
		download = UrlRequest("https://spreadsheets.google.com/feeds/list/1GaWe5tWQO_z3hzPbu_7iCgElQOKeojiGP0ki-ouW4vI/od6/public/values?alt=json-in-script&callback=x") 
		download.wait()
		#parses it into json
		users = eval(download.result[18:len(download.result)-2])
		#separates each row into a list called entries
		entries = users["feed"]["entry"]
		#Iterates through all the entries
		for x in entries:
			if(username == x['gsx$username']['$t']):
				profile_screen.ids.email.text = x['gsx$email']['$t']
				profile_screen.ids.name.text = x['gsx$name']['$t']
				profile_screen.ids.phone.text = x['gsx$phone']['$t']
				profile_screen.ids.phone.text = x['gsx$phone']['$t']
				profile_screen.ids.university.text = x['gsx$university']['$t']


		sm.add_widget(profile_screen)
		sm.current = 'profile_screen'

	def my_listings(self):
		sm.remove_widget(self)
		my_listings_screen = MyListingsScreen()
		sm.add_widget(my_listings_screen)
		sm.current = 'my_listings_screen'

	def my_postings(self):
		sm.remove_widget(self)
		my_postings_screen = MyPostingsScreen()
		sm.add_widget(my_postings_screen)
		sm.current = 'my_postings_screen'

	def buy(self):
		sm.remove_widget(self)
		department_screen = DepartmentScreen()
		department_screen.ids.grid_layout.bind(minimum_height = department_screen.ids.grid_layout.setter('height'))
		sm.add_widget(department_screen)
		sm.current = 'department_screen'

	def sell(self):
		sm.remove_widget(self)
		sell_screen = SellScreen()
		sell_screen.ids.dropdown1.dismiss()
		sell_screen.ids.dropdown2.dismiss()
		sell_screen.ids.dropdown3.dismiss()
		sm.add_widget(sell_screen)
		sm.current = 'sell_screen'


class DepartmentScreen(Screen):

	def math(self):
		global department

		department = "Math"

	def biology(self):
		global department

		department = "Biology"

	def chemistry(self):
		global department

		department = "Chemistry"

	def computerScience(self):
		global department

		department = "Computer Science"

	def psychology(self):
		global department

		department = "Psych"

	def english(self):
		global department

		department = "English"

	def history(self):
		global department

		department = "History"

	def specificDepartmentScreen(self):
		global department

		sm.remove_widget(self)
		specific_department_screen = SpecificDepartmentScreen()

		classes = {
					"Biology" : ["Bio 60", "Bio 61", "Bio 62", "Bio 81", "Bio 82", "Bio 83", "Bio 84", "Bio 85", "Bio 86", "Bio 104", "Bio 107", "Bio 108", "Bio 110", "Bio 112", "Bio 113", "Bio 115", "Bio 116", "Bio 117", "Bio 118", "Bio 119", "Bio 120", "Bio 124"],
					"Math"    : ["Math 19", "Math 20", "Math 21", "Math 51", "Math 52", "Math 53", "Math 61", "Math 62", "Math 63", "Math 104", "Math 107", "Math 108", "Math 109", "Math 110", "Math 113", "Math 115", "Math 120", "Math 122"],
					"Chemistry": ["Chem 31A", "Chem 31B", "Chem 31X", "Chem 33", "Chem 35", "Chem 130", "Chem 131", "Chem 134", "Chem 137", "Chem 141", "Chem 143", "Chem 153", "Chem 155","Chem 171", "Chem 185", "Chem 225", "Chem 255","chem 275"],
					"Computer Science": ["CS 106A", "CS 106B", "CS 106X", "CS 103", "CS 107", "Cs 109", "CS 110", "CS 140", "CS 142", "CS 155", "CS 166", "CS 181", "CS 196", "CS 221", "CS 229", "CS 230", "CS 233", "CS 240"],
					"Psych": ["Psych 1", "Psych 10", "Psych 30", "Psych 35", "Psych 45", "Psych 50", "Psych 60", "Psych 70", "Psych 75","Psych 80", "Psych 85", "Psych 90", "Psych 95", "Psych 103", "Psych 146", "Psych 147", "Psych 150", "Psych 186"],
					"English": ["English 10A", "Englsih 10B", "English 11a", "Englsih 11B", "Egnlsih 12A", "English 12C", "English 160", "English 161", "English 101A", "English 103B", "English 112A", "English 115D", "English 163F", "English 201", "English 233", "English 240A"],
					"History": ["History 1B", "History 1C", "History 102", "History 103D", "History 103E", "History 103F", "History 104", "History 105A", "History 106A", "History 106B", "History 107D", "History 110B", "History 115D", "History 116", "History 120A", "History 125", "History 131G", "History 137"]
		}

		specific_department_screen.ids.grid_layout.bind(minimum_height=specific_department_screen.ids.grid_layout.setter('height'))

		def showListings(instance):
			global course

			course = instance.text

			specific_department_screen.showListings()

		for x in classes[department]:
			specific_department_screen.ids.grid_layout.add_widget(Button(text = x,size_hint_y=None, height = 300,valign = 'middle',halign = 'center', on_release = showListings, background_color= [2.07, 0.12, 0.23,1], bold= True))

		print department


		sm.add_widget(specific_department_screen)
		sm.current = 'specific_department_screen'

	def back(self):
		sm.remove_widget(self)
		home_screen = HomeScreen()
		sm.add_widget(home_screen)
		sm.current = 'home_screen'


class SpecificDepartmentScreen(Screen):

	def showListings(self):
		global course

		print course

		sm.remove_widget(self)
		listings_screen = ListingsScreen()

		listings_screen.ids.grid_layout.bind(minimum_height=listings_screen.ids.grid_layout.setter('height'))

		def showCurrentListing(instance):
			global currentListing

			currentListing = int(instance.text[0:6])
			print currentListing

			listings_screen.goToCurrentListing()


		download = UrlRequest("https://spreadsheets.google.com/feeds/list/1vaTFcxuDrsEn7yPVJCD3_m-tlu01W3m-IOVIv_eFfpQ/od6/public/values?alt=json-in-script&callback=x") 
		download.wait()
		#parses it into json
		listings = eval(download.result[18:len(download.result)-2])
		#separates each row into a list called entries
		entries = listings["feed"]["entry"]
		#Iterates through all the entries
		for x in entries:
			if(course == x['gsx$course']['$t']):
				text = x['gsx$listingid']['$t'] + " " + course + "\n " + x['gsx$title']['$t'] + " \n" + x['gsx$sellrent']['$t'] + " $" + x['gsx$price']['$t']
				listings_screen.ids.grid_layout.add_widget(Button(text = text, size_hint_y = None, height = 300,valign = 'middle',halign = 'center', on_release = showCurrentListing, background_color= [2.07,0.12,0.23,1], bold= True ))



		sm.add_widget(listings_screen)
		sm.current = 'listings_screen'

	def back(self):
		sm.remove_widget(self)
		department_screen = DepartmentScreen()
		department_screen.ids.grid_layout.bind(minimum_height = department_screen.ids.grid_layout.setter('height'))
		sm.add_widget(department_screen)
		sm.current = 'department_screen'


class ListingsScreen(Screen):

	def goToCurrentListing(self):
		global currentListing

		sm.remove_widget(self)
		current_listing_screen = CurrentListingScreen()

		download = UrlRequest("https://spreadsheets.google.com/feeds/list/1vaTFcxuDrsEn7yPVJCD3_m-tlu01W3m-IOVIv_eFfpQ/od6/public/values?alt=json-in-script&callback=x") 
		download.wait()
		#parses it into json
		listings = eval(download.result[18:len(download.result)-2])
		#separates each row into a list called entries
		entries = listings["feed"]["entry"]
		#Iterates through all the entries
		for x in entries:
			if(str(currentListing) == x['gsx$listingid']['$t']):
				print "-"*300
				print x, currentListing, x['gsx$listingid']['$t']
				print "-"*300

				current_listing_screen.ids.listing_class.text = x['gsx$course']['$t']
				current_listing_screen.ids.listing_department.text = x['gsx$department']['$t']
				current_listing_screen.ids.listing_textbook.text = x['gsx$title']['$t']
				current_listing_screen.ids.listing_condition.text = x['gsx$condition']['$t']
				current_listing_screen.ids.listing_description.text = x['gsx$description']['$t']
				current_listing_screen.ids.sale_method.text = x['gsx$sellrent']['$t']
				current_listing_screen.ids.price.text = x['gsx$price']['$t']
				current_listing_screen.ids.listing_seller.text = x['gsx$seller']['$t']

		sm.add_widget(current_listing_screen)
		sm.current = 'current_listing_screen'

				
		

	def back(self):
		sm.remove_widget(self)
		specific_department_screen = SpecificDepartmentScreen()

		classes = {
					"Biology" : ["Bio 60", "Bio 61", "Bio 62", "Bio 81", "Bio 82", "Bio 83", "Bio 84", "Bio 85", "Bio 86", "Bio 104", "Bio 107", "Bio 108", "Bio 110", "Bio 112", "Bio 113", "Bio 115", "Bio 116", "Bio 117", "Bio 118", "Bio 119", "Bio 120", "Bio 124"],
					"Math"    : ["Math 19", "Math 20", "Math 21", "Math 51", "Math 52", "Math 53", "Math 61", "Math 62", "Math 63", "Math 104", "Math 107", "Math 108", "Math 109", "Math 110", "Math 113", "Math 115", "Math 120", "Math 122"],
					"Chemistry": ["Chem 31A", "Chem 31B", "Chem 31X", "Chem 33", "Chem 35", "Chem 130", "Chem 131", "Chem 134", "Chem 137", "Chem 141", "Chem 143", "Chem 153", "Chem 155","Chem 171", "Chem 185", "Chem 225", "Chem 255","chem 275"],
					"Computer Science": ["CS 106A", "CS 106B", "CS 106X", "CS 103", "CS 107", "Cs 109", "CS 110", "CS 140", "CS 142", "CS 155", "CS 166", "CS 181", "CS 196", "CS 221", "CS 229", "CS 230", "CS 233", "CS 240"],
					"Psych": ["Psych 1", "Psych 10", "Psych 30", "Psych 35", "Psych 45", "Psych 50", "Psych 60", "Psych 70", "Psych 75","Psych 80", "Psych 85", "Psych 90", "Psych 95", "Psych 103", "Psych 146", "Psych 147", "Psych 150", "Psych 186"],
					"English": ["English 10A", "Englsih 10B", "English 11a", "Englsih 11B", "Egnlsih 12A", "English 12C", "English 160", "English 161", "English 101A", "English 103B", "English 112A", "English 115D", "English 163F", "English 201", "English 233", "English 240A"],
					"History": ["History 1B", "History 1C", "History 102", "History 103D", "History 103E", "History 103F", "History 104", "History 105A", "History 106A", "History 106B", "History 107D", "History 110B", "History 115D", "History 116", "History 120A", "History 125", "History 131G", "History 137"]
		}

		specific_department_screen.ids.grid_layout.bind(minimum_height=specific_department_screen.ids.grid_layout.setter('height'))

		def showListings(instance):
			global course

			course = instance.text

			specific_department_screen.showListings()

		for x in classes[department]:
			specific_department_screen.ids.grid_layout.add_widget(Button(text = x,size_hint_y=None, height = 300,valign = 'middle',halign = 'center', on_release = showListings, background_color=[2.07,0.12,0.23,1], bold=True))

		print department


		sm.add_widget(specific_department_screen)
		sm.current = 'specific_department_screen'


class CurrentListingScreen(Screen):

	def back(self):
		global course

		print course

		sm.remove_widget(self)
		listings_screen = ListingsScreen()

		listings_screen.ids.grid_layout.bind(minimum_height=listings_screen.ids.grid_layout.setter('height'))

		def showCurrentListing(instance):
			global currentListing

			currentListing = int(instance.text[0:6])
			print currentListing

			listings_screen.goToCurrentListing()


		download = UrlRequest("https://spreadsheets.google.com/feeds/list/1vaTFcxuDrsEn7yPVJCD3_m-tlu01W3m-IOVIv_eFfpQ/od6/public/values?alt=json-in-script&callback=x") 
		download.wait()
		#parses it into json
		listings = eval(download.result[18:len(download.result)-2])
		#separates each row into a list called entries
		entries = listings["feed"]["entry"]
		#Iterates through all the entries
		for x in entries:
			if(course == x['gsx$course']['$t']):
				text = x['gsx$listingid']['$t'] + " " + course + " \n" + x['gsx$title']['$t'] + " \n" + x['gsx$sellrent']['$t'] + " $" + x['gsx$price']['$t']
				listings_screen.ids.grid_layout.add_widget(Button(text = text,text_size =  self.size, size_hint_y=None, height = 300,valign = 'middle',halign = 'center', on_release = showCurrentListing, background_color=[2.07, 0.12,0.23,1], bold=True))



		sm.add_widget(listings_screen)
		sm.current = 'listings_screen'

	def home(self):
		sm.remove_widget(self)
		home_screen = HomeScreen()
		sm.add_widget(home_screen)
		sm.current = 'home_screen'

class SellScreen(Screen):

	def submit(self):
		title = self.ids.textinput1.text
		department = self.ids.select1.text
		course = self.ids.textinput3.text
		price = self.ids.textinput4.text
		sellrent = self.ids.select2.text
		condition = self.ids.select3.text
		description = self.ids.textinput7.text

		url = "https://script.google.com/macros/s/AKfycbwcmKL150oFHB6KK4ZMGrR4B61Jo_ACv1WMkW4fyTIadsY08vw/exec"
		url += "?"
		url += "title=" + title.replace(" ", "+")
		url += "&" + "department=" + department
		url += "&" + "course=" + course.replace(" ", "+")
		url += "&" + "price=" + price
		url += "&" + "sellrent=" + sellrent
		url += "&" + "condition=" + condition
		url += "&" + "description=" + description.replace(" ", "+")
		url += "&" + "seller=" + username
		url += "&" + "buyers=" + "[]"
		url += "&" + "acceptedbuyers=" + "[]"
		from random import randint
		randomNumber = str(randint(100000, 999999))
		print randomNumber
		url += "&" + "listing_id=" + randomNumber


		print url
		upload = UrlRequest(url)
		upload.wait()
		print upload.result

		sm.remove_widget(self)
		home_screen = HomeScreen()
		sm.add_widget(home_screen)
		sm.current = 'home_screen'

	def back(self):
		sm.remove_widget(self)
		home_screen = HomeScreen()
		sm.add_widget(home_screen)
		sm.current = 'home_screen'

class CustomScreenManager(ScreenManager):

	pass


class TFT(App):

		def build(self):
			global sm

			sm = CustomScreenManager(transition = FadeTransition())
			sm.add_widget(LoginScreen())
			return sm

if __name__=='__main__':
	TFT().run()




"""

Users spreadsheet:
	add to:
		https://script.google.com/macros/s/AKfycbw82sgTI3SzMT6WAYY9DIxaXIU70ZYdhcXRgashr0B0r5SLWyoW/exec
	download:
		https://spreadsheets.google.com/feeds/list/1GaWe5tWQO_z3hzPbu_7iCgElQOKeojiGP0ki-ouW4vI/od6/public/values?alt=json-in-script&callback=x

Stanford spreadsheet:
	add to:
		https://script.google.com/macros/s/AKfycbwcmKL150oFHB6KK4ZMGrR4B61Jo_ACv1WMkW4fyTIadsY08vw/exec
	download:
		https://spreadsheets.google.com/feeds/list/1vaTFcxuDrsEn7yPVJCD3_m-tlu01W3m-IOVIv_eFfpQ/od6/public/values?alt=json-in-script&callback=x



Download tutorial:
	https://coderwall.com/p/duapqq/use-a-google-spreadsheet-as-your-json-backend

Upload tutorial:
	https://mashe.hawksey.info/2014/07/google-sheets-as-a-database-insert-with-apps-script-using-postget-methods-with-ajax-example/


Need to check if all inputted data is valid or not
"""