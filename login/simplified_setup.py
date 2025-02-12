from abc import abstractmethod
from typing import Protocol, Iterable, Tuple

from com.baboea.models.days_pb2 import MealPlanDayRef
from com.baboea.models.diet_pb2 import ClientMealSize
from com.baboea.models.meal_pb2 import MealRef
from com.baboea.models.objectivegroup_pb2 import ObjectiveGroupRef
from com.baboea.models.users_pb2 import UserRef
from com.baboea.services.login_service_pb2 import InitialLoginForm


class ObjectiveGroupCreator(Protocol):

    @abstractmethod
    def create_user(self, user: UserRef, login: InitialLoginForm) -> Iterable[ObjectiveGroupRef]:
        pass


class MealCreator(Protocol):
    @abstractmethod
    def create_meals(self, user: UserRef, login: InitialLoginForm) -> Iterable[ClientMealSize]:
        pass


class DayCreator(Protocol):
    @abstractmethod
    def create_meals(self, user: UserRef, login: InitialLoginForm, meals: Iterable[MealRef]) -> Iterable[
        MealPlanDayRef]:
        pass


def setup_simplified(form: InitialLoginForm):
    # Fetch admin diet
    # Fetch admin meals
    # Add admin meals as our meals, when meal is generated
    # If disabled, disable
    # If My own then save template recipe and add ref to meal
    # Add constraints
    pass
