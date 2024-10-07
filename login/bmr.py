import abc
from abc import abstractmethod
from dataclasses import dataclass

from com.baboea.services.login_service_pb2 import InitialLoginForm, ActivityLevel, Gender, MacroStrategy, \
    DesiredWeightLoss


@dataclass
class UserReqs:
    minKcal: float
    maxKcal: float
    minProtein: float
    maxProtein: float
    minFiber: float
    maxFiber: float
    minCarbPercentage: float
    maxCarbPercentage: float


class BmrUseCase(abc.ABC):
    @abstractmethod
    def calculate(self, form: InitialLoginForm) -> UserReqs:
        pass


class BaseBmrUseCase(BmrUseCase):

    def calculate(self, form: InitialLoginForm) -> UserReqs:
        kcal = calculate_bmr(form.personal.heightCm, form.personal.weightKg, form.personal.activityLevel,
                             form.personal.gender, form.personal.age, form.weightLoss)
        protein = form.personal.weightKg
        carb_percentages = {
            MacroStrategy.low_carb: (0.1, 0.3),
            MacroStrategy.balanced: (0.4, 0.65),
            MacroStrategy.keto: (0.0, 0.1),
            MacroStrategy.high_protein: (0.2, 0.65),

        }
        if form.macros == MacroStrategy.high_protein:
            protein *= 2.0
        if form.macros == MacroStrategy.low_carb:
            protein *= 1.25

        fiber = {
            Gender.male: (35, 65),
            Gender.other: (35, 65),
            Gender.female: (23, 50)
        }
        minFiber, maxFiber = fiber[form.personal.gender]
        minCarb, maxCarb = carb_percentages[form.macros]
        return UserReqs(
            minKcal=kcal * 0.99,
            maxKcal=kcal * 1.01,
            minProtein=protein * 0.9,
            maxProtein=protein * 1.1,
            minCarbPercentage=minCarb,
            maxCarbPercentage=maxCarb,
            minFiber=minFiber,
            maxFiber=maxFiber
        )


def calculate_bmr(height_cm: float, weight_kg: float, activity_level: ActivityLevel, gender: Gender, age: int,
                  desired_weight_loss: DesiredWeightLoss) -> float:
    """
    Calculate Basal Metabolic Rate (BMR) and adjust it based on activity level.

    :param desired_weight_loss:
    :param height_cm: Height in centimeters
    :param weight_kg: Weight in kilograms
    :param activity_level: Activity level (options: 'sedentary', 'lightly_active', 'moderately_active', 'very_active', 'extra_active')
    :param gender: Gender ('male' or 'female')
    :param age: Age in years
    :return: Adjusted BMR
    """

    # Harris-Benedict Equation for BMR
    if gender == Gender.male:
        bmr = 5 + (10 * weight_kg) + (6.25 * height_cm) - (5.0 * age)
    elif gender == Gender.female:
        bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) - 161
    else:
        bmr = 88.362 + (13.397 * weight_kg) + (4.799 * height_cm) - (5.677 * age)

    # Adjust BMR based on activity level
    activity_multipliers = {
        ActivityLevel.sedentary: 1.2,
        ActivityLevel.lightlyActive: 1.375,
        ActivityLevel.moderatelyActive: 1.55,
        ActivityLevel.veryActive: 1.725,
        ActivityLevel.extraActive: 1.9
    }
    if activity_level not in activity_multipliers:
        raise ValueError(
            "Invalid activity level. Must be one of: 'sedentary', 'lightly_active', 'moderately_active', 'very_active', 'extra_active'.")

    weight_loss_kcal_offset = {
        DesiredWeightLoss.gain_weight: 350,
        DesiredWeightLoss.maintain: 0,
        DesiredWeightLoss.lose_slowly: -300,
        DesiredWeightLoss.lose_rapid: -500
    }
    adjusted_bmr = bmr * activity_multipliers[activity_level]
    adjusted_bmr = adjusted_bmr + weight_loss_kcal_offset[desired_weight_loss]
    return adjusted_bmr


if __name__ == '__main__':
    print(calculate_bmr(193, 93, ActivityLevel.extraActive, Gender.male, 28,DesiredWeightLoss.maintain))
