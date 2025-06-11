from com.baboea.models.meal_pb2 import MealRef
from com.baboea.services.objective_group_service_pb2_grpc import ObjectiveGroupServiceStub
from login.simplified_setup import ObjectiveGroupCreator

from injector import inject
from typing import Optional, Iterable, List
from com.baboea.concept_pb2 import BoolConceptValues
from com.baboea.models.concepts_pb2 import ConceptRef
from com.baboea.models.objectivegroup_pb2 import SpecializedRequirement, MealSelection, RequirementConcepts, \
    ObjectiveGroup, ObjectiveGroupRef
from com.baboea.models.property_pb2 import PropertyRef
from com.baboea.models.users_pb2 import UserRef
from com.baboea.services.login_service_pb2 import InitialLoginForm
from login.bmr import UserReqs, BmrUseCase
from login.dependencies import Concepts, InitProperties, ApplicationLevels, PropertyByHandleResolver
from login.nutrients import VitaminsAndMinerals
from typing import Optional, Iterable

from injector import inject

from com.baboea.concept_pb2 import BoolConceptValues
from com.baboea.models.concepts_pb2 import ConceptRef
from com.baboea.models.objectivegroup_pb2 import SpecializedRequirement, MealSelection, RequirementConcepts, \
    ObjectiveGroup, ObjectiveGroupRef
from com.baboea.models.property_pb2 import PropertyRef
from com.baboea.models.users_pb2 import UserRef
from com.baboea.services.login_service_pb2 import InitialLoginForm
from login.bmr import UserReqs
from login.dependencies import Concepts, InitProperties, ApplicationLevels, PropertyByHandleResolver
from login.nutrients import VitaminsAndMinerals
from login.simplified_setup import ObjectiveGroupCreator


class BaseObjectiveGroupCreator(ObjectiveGroupCreator):

    @inject
    def __init__(self,
                 objective_group_service: ObjectiveGroupServiceStub,
                 use_case: BmrUseCase,
                 concepts: Concepts,
                 application_levels: ApplicationLevels,
                 properties: InitProperties,
                 property_resolver: PropertyByHandleResolver,
                 vitamins: VitaminsAndMinerals
                 ):
        super().__init__()
        self.objective_group_service = objective_group_service
        self.use_case = use_case
        self.vitamins = vitamins
        self.concepts = concepts
        self.application_levels = application_levels
        self.properties = properties
        self.property_resolver = property_resolver

    def create_user(self, user: UserRef, login: InitialLoginForm) -> Iterable[ObjectiveGroupRef]:
        return [
            ObjectiveGroupRef(id=self.objective_group_service.Add(x).id)
            for x in BaseObjectiveGroupCreator.create_all_objective_groups(
                reqs=self.use_case.calculate(login),
                properties=self.properties,
                application_levels=self.application_levels,
                user=user,
                concepts=self.concepts,
                resolver=self.property_resolver,
                vitamins=self.vitamins)
        ]

    @staticmethod
    def create_all_objective_groups(
            concepts: Concepts,
            reqs: UserReqs,
            properties: InitProperties,
            application_levels: ApplicationLevels,
            user: UserRef,
            resolver: PropertyByHandleResolver,
            vitamins: VitaminsAndMinerals
    ) -> List[ObjectiveGroup]:
        macros = ObjectiveGroup(
            name="Macros",
            description="Applies your desired macros to every day",
            owner=user,
            reward=5.0,
            objectives=[
                BaseObjectiveGroupCreator.create_fat_requirement(reqs, properties, application_levels),
                BaseObjectiveGroupCreator.create_fiber_requirement(reqs, properties, application_levels),
                BaseObjectiveGroupCreator.create_kcal_requirement(reqs, properties, application_levels),
                BaseObjectiveGroupCreator.create_protein_requirement(reqs, properties, application_levels),
                BaseObjectiveGroupCreator.create_carb_requirement(reqs, properties, application_levels),
            ]
        )
        objective_groups = [
            macros,
            BaseObjectiveGroupCreator.create_fruit_and_veg_objective(properties=properties, concepts=concepts,
                                                                     application_levels=application_levels, user=user),
            BaseObjectiveGroupCreator.create_nutrient_targets(vitamins, resolver, application_levels, user),
            BaseObjectiveGroupCreator.create_recipe_preferences_objective(properties, application_levels, user)
        ]
        return objective_groups

    @staticmethod
    def create_fruit_and_veg_objective(properties: InitProperties, concepts: Concepts,
                                       application_levels: ApplicationLevels, user: UserRef) -> ObjectiveGroup:
        return ObjectiveGroup(
            name="Fruit and vegetables intake",
            description="We have established recommended minimum and generous maximum intake levels for fruits and "
                        "vegetables to promote a balanced diet without requiring you to consume excessive amounts, "
                        "such as 2kg of vegetables daily. Feel free to adjust these limits to suit your individual "
                        "preferences and nutritional needs.",
            owner=user,
            reward=1.0,
            objectives=[
                BaseObjectiveGroupCreator.create_absolute_requirement_for_concept(
                    min_value=150,
                    max_value=600,
                    concepts=concepts,
                    concept=concepts.fruit,
                    selected_property=properties.food_weight,
                    application_levels=application_levels
                ),
                BaseObjectiveGroupCreator.create_absolute_requirement_for_concept(
                    min_value=250,
                    max_value=750,
                    concepts=concepts,
                    concept=concepts.vegetable,
                    selected_property=properties.food_weight,
                    application_levels=application_levels
                ),
            ]
        )

    @staticmethod
    def create_recipe_preferences_objective(properties: InitProperties,
                                            application_levels: ApplicationLevels, user: UserRef) -> ObjectiveGroup:
        return ObjectiveGroup(
            name="Recipe preferences",
            description="We have set the maximum number of recipes you have to make per meal to 1. Feel free to adjust",
            owner=user,
            reward=1.0,
            objectives=[BaseObjectiveGroupCreator.create_recipe_count_requirement(properties, application_levels)]
        )

    @staticmethod
    def create_recipe_count_requirement(properties: InitProperties,
                                        application_levels: ApplicationLevels) -> SpecializedRequirement:
        return SpecializedRequirement(
            applicationLevel=application_levels.meal,
            numerator=properties.recipe_count,
            useRatio=False,
            useMax=True,
            useMin=True,
            min=0,
            max=1,
            numeratorMeals=MealSelection(
                useAllMeals=True,
                useAllDays=True,
                useAllComponents=True,
            ),
            scaleNumerator=1,
            numeratorConcepts=RequirementConcepts(useAllConcepts=True),
            reward=1.0
        )

    @staticmethod
    def create_kcal_requirement(targets: UserReqs, properties: InitProperties,
                                application_levels: ApplicationLevels) -> SpecializedRequirement:
        return BaseObjectiveGroupCreator.create_absolute_requirement(min_value=targets.minKcal,
                                                                     max_value=targets.maxKcal,
                                                                     selected_property=properties.kcal,
                                                                     application_levels=application_levels)

    @staticmethod
    def create_fiber_requirement(targets: UserReqs, properties: InitProperties,
                                 application_levels: ApplicationLevels) -> SpecializedRequirement:
        return BaseObjectiveGroupCreator.create_absolute_requirement(min_value=targets.minFiber,
                                                                     max_value=targets.maxFiber,
                                                                     selected_property=properties.fiber,
                                                                     application_levels=application_levels)

    @staticmethod
    def create_protein_requirement(targets: UserReqs, properties: InitProperties,
                                   application_levels: ApplicationLevels) -> SpecializedRequirement:
        return BaseObjectiveGroupCreator.create_absolute_req_with_kcal_ratio_fallback(min_value=targets.minProtein,
                                                                                      max_value=targets.maxProtein,
                                                                                      selected_property=properties.protein,
                                                                                      kcal_per_unit=4.0,
                                                                                      properties=properties,
                                                                                      application_levels=application_levels)

    @staticmethod
    def create_absolute_requirement_for_concept(min_value: Optional[float], max_value: Optional[float],
                                                selected_property: PropertyRef, concept: ConceptRef,
                                                concepts: Concepts,
                                                application_levels: ApplicationLevels) -> SpecializedRequirement:
        return SpecializedRequirement(
            applicationLevel=application_levels.day,
            numerator=selected_property,
            denominator=selected_property,
            useRatio=False,
            useMax=max_value is not None,
            useMin=min_value is not None,
            min=min_value or 0,
            max=max_value or 10000,
            numeratorMeals=MealSelection(
                useAllMeals=True,
                useAllDays=True,
                useAllComponents=True,
            ),
            scaleNumerator=1,
            reward=1.0,
            numeratorConcepts=RequirementConcepts(concepts=BoolConceptValues(
                conceptValues={concepts.root.id: False, concept.id: True}
            )),
        )

    @staticmethod
    def create_absolute_requirement(min_value: Optional[float], max_value: Optional[float],
                                    selected_property: PropertyRef,
                                    application_levels: ApplicationLevels) -> SpecializedRequirement:
        return SpecializedRequirement(
            applicationLevel=application_levels.day,
            numerator=selected_property,
            denominator=selected_property,
            useRatio=False,
            useMax=max_value is not None,
            useMin=min_value is not None,
            min=min_value or 0,
            max=max_value or 10000,
            numeratorMeals=MealSelection(
                useAllMeals=True,
                useAllDays=True,
                useAllComponents=True,
            ),
            reward=1.0,
            scaleNumerator=1,
            numeratorConcepts=RequirementConcepts(useAllConcepts=True),
        )

    @staticmethod
    def create_kcal_ratio_requirement(min_percentage: float, max_percentage: float, selected_property: PropertyRef,
                                      kcal_per_unit: float,
                                      properties: InitProperties,
                                      application_levels: ApplicationLevels) -> SpecializedRequirement:
        return SpecializedRequirement(
            applicationLevel=application_levels.day,
            numerator=selected_property,
            denominator=properties.kcal,
            useRatio=True,
            useMax=True,
            useMin=True,
            min=min_percentage,
            max=max_percentage,
            numeratorMeals=MealSelection(
                useAllMeals=True,
                useAllDays=True,
                useAllComponents=True,
            ),
            denominatorMeals=MealSelection(
                useAllMeals=True,
                useAllDays=True,
                useAllComponents=True,
            ),
            scaleNumerator=kcal_per_unit,
            scaleDenominator=1,
            reward=1.0,
            numeratorConcepts=RequirementConcepts(useAllConcepts=True),
            denominatorConcepts=RequirementConcepts(useAllConcepts=True)
        )

    @staticmethod
    def create_absolute_req_with_kcal_ratio_fallback(min_value: float, max_value: float, selected_property: PropertyRef,
                                                     kcal_per_unit: float,
                                                     properties: InitProperties,
                                                     application_levels: ApplicationLevels) -> SpecializedRequirement:
        return SpecializedRequirement(
            applicationLevel=application_levels.day,
            numerator=selected_property,
            denominator=properties.kcal,
            useRatio=False,
            useMax=True,
            useMin=True,
            min=min_value,
            max=max_value,
            numeratorMeals=MealSelection(
                useAllMeals=True,
                useAllDays=True,
                useAllComponents=True,
            ),
            denominatorMeals=MealSelection(
                useAllMeals=True,
                useAllDays=True,
                useAllComponents=True,
            ),
            scaleNumerator=kcal_per_unit,
            scaleDenominator=1,
            reward=1.0,
            numeratorConcepts=RequirementConcepts(useAllConcepts=True),
            denominatorConcepts=RequirementConcepts(useAllConcepts=True)
        )

    @staticmethod
    def create_fat_requirement(targets: UserReqs, properties: InitProperties,
                               application_levels: ApplicationLevels) -> SpecializedRequirement:
        return BaseObjectiveGroupCreator.create_kcal_ratio_requirement(min_percentage=targets.minFatPercentage,
                                                                       max_percentage=targets.maxFatPercentage,
                                                                       selected_property=properties.fat,
                                                                       kcal_per_unit=9,
                                                                       properties=properties,
                                                                       application_levels=application_levels)

    @staticmethod
    def create_carb_requirement(targets: UserReqs, properties: InitProperties,
                                application_levels: ApplicationLevels) -> SpecializedRequirement:
        return BaseObjectiveGroupCreator.create_kcal_ratio_requirement(min_percentage=targets.minCarbPercentage,
                                                                       max_percentage=targets.maxCarbPercentage,
                                                                       selected_property=properties.net_carbs,
                                                                       kcal_per_unit=4,
                                                                       properties=properties,
                                                                       application_levels=application_levels)

    @staticmethod
    def create_nutrient_targets(data: VitaminsAndMinerals, property_resolver: PropertyByHandleResolver,
                                application_levels: ApplicationLevels, owner: UserRef) -> ObjectiveGroup:
        nutrient_targets = [
            BaseObjectiveGroupCreator.create_absolute_requirement(
                min_value=x.min,
                max_value=x.max,
                selected_property=property_resolver.resolve(x.nutrient1),
                application_levels=application_levels
            ) for x in data.objectives
        ]
        return ObjectiveGroup(name=data.name, description=data.description, objectives=nutrient_targets,
                              owner=owner, reward=1.0)
