from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, Date
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

engine = create_engine('sqlite:///app/lifttracker.sqlite3', echo=False)
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()


def getNewSession():
    return Session()


class Exercise(Base):
    __tablename__ = 'exercise'

    id = Column(Integer, primary_key=True)
    name = Column(String(254))


class ExerciseRepsSetWorkoutPlan(Base):
    __tablename__ = 'exercise_reps_set_workout_plan'
    workout_plan_id = Column(ForeignKey('workout_plan.id'), primary_key=True)
    exercise_reps_set_id = Column(ForeignKey('exercise_reps_set.id'), primary_key=True)
    order = Column(Integer)
    exercise_reps_set = relationship('ExerciseRepsSet', back_populates='workout_plans')
    workout_plan = relationship('WorkoutPlan', back_populates='exercise_reps_sets')


class ExerciseRepsSet(Base):
    __tablename__ = 'exercise_reps_set'

    id = Column(Integer, primary_key=True)
    exercise_id = Column(Integer, ForeignKey('exercise.id'))  # fk to exercise
    exercise = relationship("Exercise")
    rep_count = Column(Integer)
    set_count = Column(Integer)
    workout_plans = relationship("ExerciseRepsSetWorkoutPlan", back_populates='exercise_reps_set')


class WorkoutPlan(Base):
    __tablename__ = 'workout_plan'
    id = Column(Integer, primary_key=True)
    name = Column(String(254))
    rest_min = Column(Integer)
    rest_max = Column(Integer)
    weight_increment = Column(Boolean)
    order = Column(Integer)
    exercise_reps_sets = relationship("ExerciseRepsSetWorkoutPlan", back_populates='workout_plan')
    workout_schedule_id = Column(Integer, ForeignKey('workout_schedule.id'))
    workout_schedule = relationship("WorkoutSchedule")


class Workout(Base):
    __tablename__ = 'workout'

    id = Column(Integer, primary_key=True)
    name = Column(String(254))
    workout_schedules = relationship("WorkoutSchedule")


class WorkoutSchedule(Base):
    __tablename__ = 'workout_schedule'

    id = Column(Integer, primary_key=True)
    workout_id = Column(Integer, ForeignKey('workout.id'))  # fk to workout
    order = Column(Integer)
    rest_between_plans = Column(Integer)
    workout_plans = relationship("WorkoutPlan", back_populates='workout_schedule')


class ExerciseSetInstance(Base):
    __tablename__ = 'exercide_set_instance'

    id = Column(Integer, primary_key=True)
    exercise_id = Column(Integer)  # fk to exercise
    reps_achieved = Column(Integer)
    set = Column(Integer)


class WorkoutInstance(Base):
    __tablename__ = 'workout_instance'

    id = Column(Integer, primary_key=True)
    workout_plan_id = Column(Integer)  # fk workoutplan
    date = Column(Date)
    exercise_set_instance_Id = Column(Integer)
