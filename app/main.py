from kivy.uix.screenmanager import Screen

from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton

from model import *
from sqlalchemy import desc

class MainApp(MDApp):
    def build(self):
        screen = Screen()
        screen.add_widget(
            MDRectangleFlatButton(
                text="Hello, World " + self.getWorkoutName(),
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
        )
        return screen

    def getWorkoutName(self):
        session = getNewSession()
        newWorkout = Workout(name='5x5 Baby!')
        session.add(newWorkout)
        session.commit()
        w = session.query(Workout).order_by(desc(Workout.id)).first()
        return w.name + '-' + str(w.id)


MainApp().run()