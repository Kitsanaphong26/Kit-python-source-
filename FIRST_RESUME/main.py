from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.progressbar import ProgressBar
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, RoundedRectangle
from kivy.core.window import Window


# ==========================================
# ตั้งค่าหน้าจอ
# ==========================================

Window.size = (390, 844)
Window.clearcolor = (0.03, 0.05, 0.09, 1)


# ==========================================
# Custom Card
# ==========================================

class Card(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.padding = 15
        self.spacing = 5

        with self.canvas.before:
            Color(0.06, 0.10, 0.16, 1)
            self.bg = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[15]
            )

        self.bind(
            pos=self.update_background,
            size=self.update_background
        )

    def update_background(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size


# ==========================================
# Main Application
# ==========================================

class ResumeApp(App):

    def build(self):

        self.main = BoxLayout(
            orientation="vertical"
        )

        self.content = BoxLayout(
            orientation="vertical"
        )

        self.main.add_widget(self.content)

        self.show_home()

        return self.main


    # ======================================
    # ล้างหน้าเก่า
    # ======================================

    def clear_page(self):

        self.content.clear_widgets()


    # ======================================
    # HOME
    # ======================================

    def show_home(self):

        self.clear_page()

        scroll = ScrollView()

        layout = BoxLayout(
            orientation="vertical",
            spacing=15,
            padding=20,
            size_hint_y=None
        )

        layout.bind(
            minimum_height=layout.setter("height")
        )


        # -------------------------------
        # Profile
        # -------------------------------

        profile = Card(
            size_hint_y=None,
            height=150
        )

        name = Label(
            text="FIRST",
            font_size=30,
            bold=True,
            color=(0, 0.85, 1, 1)
        )

        role = Label(
            text="Digital Technology Student",
            font_size=14
        )

        level = Label(
            text="PLAYER LEVEL 20",
            font_size=13,
            color=(0, 0.85, 1, 1)
        )

        exp = ProgressBar(
            max=100,
            value=80
        )

        profile.add_widget(name)
        profile.add_widget(role)
        profile.add_widget(level)
        profile.add_widget(exp)

        layout.add_widget(profile)


        # -------------------------------
        # Introduction
        # -------------------------------

        intro = Card(
            size_hint_y=None,
            height=170
        )

        intro.add_widget(
            Label(
                text="HELLO, I'M FIRST 👋",
                font_size=13,
                color=(0, 0.85, 1, 1),
                halign="left"
            )
        )

        intro.add_widget(
            Label(
                text="I turn ideas into\ndigital experiences.",
                font_size=23,
                bold=True
            )
        )

        intro.add_widget(
            Label(
                text=(
                    "นักศึกษาด้านวิทยาการและเทคโนโลยีดิจิทัล\n"
                    "สนใจ Programming, AI และ UX/UI"
                ),
                font_size=12
            )
        )

        layout.add_widget(intro)


        # -------------------------------
        # Player Stats
        # -------------------------------

        title = Label(
            text="PLAYER STATS",
            font_size=16,
            bold=True,
            color=(0, 0.85, 1, 1),
            size_hint_y=None,
            height=35
        )

        layout.add_widget(title)


        skills = [
            ("💻 CODING", 75),
            ("🎨 CREATIVE", 90),
            ("🧠 PROBLEM SOLVING", 85),
            ("🤝 TEAMWORK", 80)
        ]


        for skill, value in skills:

            card = Card(
                size_hint_y=None,
                height=85
            )

            card.add_widget(
                Label(
                    text=f"{skill}     {value}/100",
                    font_size=13
                )
            )

            bar = ProgressBar(
                max=100,
                value=value
            )

            card.add_widget(bar)

            layout.add_widget(card)


        # -------------------------------
        # Featured Quest
        # -------------------------------

        quest_title = Label(
            text="FEATURED QUEST",
            font_size=16,
            bold=True,
            color=(0, 0.85, 1, 1),
            size_hint_y=None,
            height=35
        )

        layout.add_widget(quest_title)


        quest = Card(
            size_hint_y=None,
            height=180
        )

        quest.add_widget(
            Label(
                text="QUEST #01",
                font_size=11,
                color=(0, 0.85, 1, 1)
            )
        )

        quest.add_widget(
            Label(
                text="AI Tourism Platform",
                font_size=20,
                bold=True
            )
        )

        quest.add_widget(
            Label(
                text=(
                    "แพลตฟอร์มท่องเที่ยวที่ใช้ AI\n"
                    "ช่วยแนะนำสถานที่ให้เหมาะกับผู้ใช้"
                ),
                font_size=11
            )
        )

        quest_button = Button(
            text="VIEW QUEST →",
            size_hint_y=None,
            height=45,
            background_color=(0, 0.65, 0.85, 1)
        )

        quest_button.bind(
            on_press=lambda x: self.show_projects()
        )

        quest.add_widget(quest_button)

        layout.add_widget(quest)


        scroll.add_widget(layout)

        self.content.add_widget(scroll)

        self.add_navigation()


    # ======================================
    # ABOUT
    # ======================================

    def show_about(self):

        self.clear_page()

        layout = BoxLayout(
            orientation="vertical",
            spacing=15,
            padding=20
        )

        layout.add_widget(
            Label(
                text="PROFILE\nABOUT ME",
                font_size=28,
                bold=True,
                color=(0, 0.85, 1, 1)
            )
        )

        card = Card()

        card.add_widget(
            Label(
                text="FIRST",
                font_size=30,
                bold=True,
                color=(0, 0.85, 1, 1)
            )
        )

        card.add_widget(
            Label(
                text="Digital Technology Student"
            )
        )

        card.add_widget(
            Label(
                text=(
                    "\nผมสนใจด้านเทคโนโลยีดิจิทัล\n"
                    "Programming\n"
                    "Artificial Intelligence\n"
                    "UX/UI Design\n"
                    "Digital Product"
                ),
                font_size=14
            )
        )

        layout.add_widget(card)

        layout.add_widget(
            Label(
                text="MY JOURNEY",
                font_size=18,
                color=(0, 0.85, 1, 1)
            )
        )

        journey = [
            "2024  →  Start University",
            "2025  →  Programming",
            "2026  →  AI & Digital Projects"
        ]

        for item in journey:

            layout.add_widget(
                Label(
                    text=item,
                    font_size=14
                )
            )

        self.content.add_widget(layout)

        self.add_navigation()


    # ======================================
    # SKILLS
    # ======================================

    def show_skills(self):

        self.clear_page()

        scroll = ScrollView()

        layout = BoxLayout(
            orientation="vertical",
            spacing=15,
            padding=20,
            size_hint_y=None
        )

        layout.bind(
            minimum_height=layout.setter("height")
        )

        layout.add_widget(
            Label(
                text="ABILITY\nSKILLS",
                font_size=28,
                bold=True,
                color=(0, 0.85, 1, 1),
                size_hint_y=None,
                height=80
            )
        )


        skills = {
            "Python": 75,
            "C Programming": 70,
            "UI / UX": 75,
            "Creative Thinking": 90,
            "Problem Solving": 85,
            "Teamwork": 80
        }


        for name, value in skills.items():

            card = Card(
                size_hint_y=None,
                height=80
            )

            card.add_widget(
                Label(
                    text=f"{name}     {value}%",
                    font_size=14
                )
            )

            card.add_widget(
                ProgressBar(
                    max=100,
                    value=value
                )
            )

            layout.add_widget(card)


        scroll.add_widget(layout)

        self.content.add_widget(scroll)

        self.add_navigation()


    # ======================================
    # PROJECTS
    # ======================================

    def show_projects(self):

        self.clear_page()

        scroll = ScrollView()

        layout = BoxLayout(
            orientation="vertical",
            spacing=15,
            padding=20,
            size_hint_y=None
        )

        layout.bind(
            minimum_height=layout.setter("height")
        )

        layout.add_widget(
            Label(
                text="QUEST LOG\nPROJECTS",
                font_size=28,
                bold=True,
                color=(0, 0.85, 1, 1),
                size_hint_y=None,
                height=80
            )
        )


        projects = [
            (
                "QUEST #01",
                "AI Tourism",
                "AI + UX/UI + Tourism",
                "COMPLETED"
            ),

            (
                "QUEST #02",
                "Smart Campus",
                "Technology + UX/UI",
                "IN PROGRESS"
            ),

            (
                "QUEST #03",
                "Programming Projects",
                "Python + C",
                "COMPLETED"
            )
        ]


        for number, name, tech, status in projects:

            card = Card(
                size_hint_y=None,
                height=150
            )

            card.add_widget(
                Label(
                    text=number,
                    font_size=11,
                    color=(0, 0.85, 1, 1)
                )
            )

            card.add_widget(
                Label(
                    text=name,
                    font_size=20,
                    bold=True
                )
            )

            card.add_widget(
                Label(
                    text=tech
                )
            )

            card.add_widget(
                Label(
                    text=status,
                    color=(0.2, 1, 0.6, 1)
                )
            )

            layout.add_widget(card)


        scroll.add_widget(layout)

        self.content.add_widget(scroll)

        self.add_navigation()


    # ======================================
    # NAVIGATION
    # ======================================

    def add_navigation(self):

        nav = BoxLayout(
            size_hint_y=None,
            height=70,
            spacing=3
        )


        buttons = [
            ("⌂\nHOME", self.show_home),
            ("◉\nABOUT", self.show_about),
            ("◆\nSKILLS", self.show_skills),
            ("▣\nPROJECTS", self.show_projects)
        ]


        for text, function in buttons:

            button = Button(
                text=text,
                font_size=10,
                background_color=(0.04, 0.08, 0.14, 1)
            )

            button.bind(
                on_press=lambda instance,
                f=function: f()
            )

            nav.add_widget(button)


        self.main.add_widget(nav)


# ==========================================
# RUN APP
# ==========================================

if __name__ == "__main__":
    ResumeApp().run()