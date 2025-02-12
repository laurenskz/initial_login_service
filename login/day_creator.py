from typing import Iterable

from injector import inject

from com.baboea.models.days_pb2 import MealPlanDayRef, MealPlanDay
from com.baboea.models.meal_pb2 import MealRef
from com.baboea.models.users_pb2 import UserRef
from com.baboea.services.base_pb2 import AddResponse
from com.baboea.services.login_service_pb2 import InitialLoginForm
from com.baboea.services.meal_plan_day_service_pb2_grpc import MealPlanDayServiceStub
from login.simplified_setup import DayCreator


class BaseDayCreator(DayCreator):

    @inject
    def __init__(self, service: MealPlanDayServiceStub):
        super().__init__()
        self.service = service

    def create_meals(self, user: UserRef, login: InitialLoginForm, meals: Iterable[MealRef]) -> Iterable[
        MealPlanDayRef]:
        response: AddResponse = self.service.Add(MealPlanDay(
            meals=meals, owner=user, name="Standard day",
            description="Your basic meal plan for the average day, you can create another specialized day for "
                        "different requirements(heavy training etc.)"
        ))
        return [MealPlanDayRef(id=response.id)]
