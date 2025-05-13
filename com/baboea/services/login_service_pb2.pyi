from com.baboea.models import curated_diet_pb2 as _curated_diet_pb2
from com.baboea.models import meal_pb2 as _meal_pb2
from com.baboea.models import recipes_pb2 as _recipes_pb2
from com.baboea.models import template_recipe_data_pb2 as _template_recipe_data_pb2
from com.baboea import concept_pb2 as _concept_pb2
from com.baboea.services import base_pb2 as _base_pb2
from com.baboea.models import users_pb2 as _users_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Gender(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    male: _ClassVar[Gender]
    female: _ClassVar[Gender]
    other: _ClassVar[Gender]

class MealSize(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    small: _ClassVar[MealSize]
    normal: _ClassVar[MealSize]
    big: _ClassVar[MealSize]

class MealStructurePreference(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ownRecipe: _ClassVar[MealStructurePreference]
    generated: _ClassVar[MealStructurePreference]
    disable: _ClassVar[MealStructurePreference]

class ActivityLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    sedentary: _ClassVar[ActivityLevel]
    lightlyActive: _ClassVar[ActivityLevel]
    moderatelyActive: _ClassVar[ActivityLevel]
    veryActive: _ClassVar[ActivityLevel]
    extraActive: _ClassVar[ActivityLevel]

class MacroStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    balanced: _ClassVar[MacroStrategy]
    keto: _ClassVar[MacroStrategy]
    low_carb: _ClassVar[MacroStrategy]
    high_carb: _ClassVar[MacroStrategy]

class ProteinStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    low_protein: _ClassVar[ProteinStrategy]
    high_protein: _ClassVar[ProteinStrategy]
    medium_protein: _ClassVar[ProteinStrategy]
    medium_high_protein: _ClassVar[ProteinStrategy]
    medium_low_protein: _ClassVar[ProteinStrategy]

class DesiredWeightLoss(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    gain_weight: _ClassVar[DesiredWeightLoss]
    maintain: _ClassVar[DesiredWeightLoss]
    lose_slowly: _ClassVar[DesiredWeightLoss]
    lose_rapid: _ClassVar[DesiredWeightLoss]

class DesiredSetup(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    advanced: _ClassVar[DesiredSetup]
    simplified: _ClassVar[DesiredSetup]
male: Gender
female: Gender
other: Gender
small: MealSize
normal: MealSize
big: MealSize
ownRecipe: MealStructurePreference
generated: MealStructurePreference
disable: MealStructurePreference
sedentary: ActivityLevel
lightlyActive: ActivityLevel
moderatelyActive: ActivityLevel
veryActive: ActivityLevel
extraActive: ActivityLevel
balanced: MacroStrategy
keto: MacroStrategy
low_carb: MacroStrategy
high_carb: MacroStrategy
low_protein: ProteinStrategy
high_protein: ProteinStrategy
medium_protein: ProteinStrategy
medium_high_protein: ProteinStrategy
medium_low_protein: ProteinStrategy
gain_weight: DesiredWeightLoss
maintain: DesiredWeightLoss
lose_slowly: DesiredWeightLoss
lose_rapid: DesiredWeightLoss
advanced: DesiredSetup
simplified: DesiredSetup

class MealInit(_message.Message):
    __slots__ = ("name", "mealKcalMin", "mealKcalMax", "maxSideFoods", "useKcal", "smart", "sideDishes", "mealSize", "mealPref", "ownRecipeIngredients", "templateRecipe")
    NAME_FIELD_NUMBER: _ClassVar[int]
    MEALKCALMIN_FIELD_NUMBER: _ClassVar[int]
    MEALKCALMAX_FIELD_NUMBER: _ClassVar[int]
    MAXSIDEFOODS_FIELD_NUMBER: _ClassVar[int]
    USEKCAL_FIELD_NUMBER: _ClassVar[int]
    SMART_FIELD_NUMBER: _ClassVar[int]
    SIDEDISHES_FIELD_NUMBER: _ClassVar[int]
    MEALSIZE_FIELD_NUMBER: _ClassVar[int]
    MEALPREF_FIELD_NUMBER: _ClassVar[int]
    OWNRECIPEINGREDIENTS_FIELD_NUMBER: _ClassVar[int]
    TEMPLATERECIPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    mealKcalMin: float
    mealKcalMax: float
    maxSideFoods: int
    useKcal: bool
    smart: _meal_pb2.SmartRecipePreferences
    sideDishes: _concept_pb2.BoolConceptValues
    mealSize: MealSize
    mealPref: MealStructurePreference
    ownRecipeIngredients: _containers.RepeatedCompositeFieldContainer[_recipes_pb2.QuantifiedRecipeIngredient]
    templateRecipe: _template_recipe_data_pb2.ImprovedTemplateRecipe
    def __init__(self, name: _Optional[str] = ..., mealKcalMin: _Optional[float] = ..., mealKcalMax: _Optional[float] = ..., maxSideFoods: _Optional[int] = ..., useKcal: bool = ..., smart: _Optional[_Union[_meal_pb2.SmartRecipePreferences, _Mapping]] = ..., sideDishes: _Optional[_Union[_concept_pb2.BoolConceptValues, _Mapping]] = ..., mealSize: _Optional[_Union[MealSize, str]] = ..., mealPref: _Optional[_Union[MealStructurePreference, str]] = ..., ownRecipeIngredients: _Optional[_Iterable[_Union[_recipes_pb2.QuantifiedRecipeIngredient, _Mapping]]] = ..., templateRecipe: _Optional[_Union[_template_recipe_data_pb2.ImprovedTemplateRecipe, _Mapping]] = ...) -> None: ...

class NutritionPrefs(_message.Message):
    __slots__ = ("kcal", "protein", "carbPercentage")
    KCAL_FIELD_NUMBER: _ClassVar[int]
    PROTEIN_FIELD_NUMBER: _ClassVar[int]
    CARBPERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    kcal: float
    protein: float
    carbPercentage: float
    def __init__(self, kcal: _Optional[float] = ..., protein: _Optional[float] = ..., carbPercentage: _Optional[float] = ...) -> None: ...

class PersonalData(_message.Message):
    __slots__ = ("gender", "age", "activityLevel", "weightKg", "heightCm", "name")
    GENDER_FIELD_NUMBER: _ClassVar[int]
    AGE_FIELD_NUMBER: _ClassVar[int]
    ACTIVITYLEVEL_FIELD_NUMBER: _ClassVar[int]
    WEIGHTKG_FIELD_NUMBER: _ClassVar[int]
    HEIGHTCM_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    gender: Gender
    age: int
    activityLevel: ActivityLevel
    weightKg: float
    heightCm: float
    name: str
    def __init__(self, gender: _Optional[_Union[Gender, str]] = ..., age: _Optional[int] = ..., activityLevel: _Optional[_Union[ActivityLevel, str]] = ..., weightKg: _Optional[float] = ..., heightCm: _Optional[float] = ..., name: _Optional[str] = ...) -> None: ...

class InitialLoginForm(_message.Message):
    __slots__ = ("personal", "manual", "diet", "macros", "meals", "remoteUserId", "weightLoss", "desiredSetup", "hatedFoods", "proteinStrategy")
    PERSONAL_FIELD_NUMBER: _ClassVar[int]
    MANUAL_FIELD_NUMBER: _ClassVar[int]
    DIET_FIELD_NUMBER: _ClassVar[int]
    MACROS_FIELD_NUMBER: _ClassVar[int]
    MEALS_FIELD_NUMBER: _ClassVar[int]
    REMOTEUSERID_FIELD_NUMBER: _ClassVar[int]
    WEIGHTLOSS_FIELD_NUMBER: _ClassVar[int]
    DESIREDSETUP_FIELD_NUMBER: _ClassVar[int]
    HATEDFOODS_FIELD_NUMBER: _ClassVar[int]
    PROTEINSTRATEGY_FIELD_NUMBER: _ClassVar[int]
    personal: PersonalData
    manual: NutritionPrefs
    diet: _curated_diet_pb2.CuratedDietRef
    macros: MacroStrategy
    meals: _containers.RepeatedCompositeFieldContainer[MealInit]
    remoteUserId: str
    weightLoss: DesiredWeightLoss
    desiredSetup: DesiredSetup
    hatedFoods: _concept_pb2.BoolConceptValues
    proteinStrategy: ProteinStrategy
    def __init__(self, personal: _Optional[_Union[PersonalData, _Mapping]] = ..., manual: _Optional[_Union[NutritionPrefs, _Mapping]] = ..., diet: _Optional[_Union[_curated_diet_pb2.CuratedDietRef, _Mapping]] = ..., macros: _Optional[_Union[MacroStrategy, str]] = ..., meals: _Optional[_Iterable[_Union[MealInit, _Mapping]]] = ..., remoteUserId: _Optional[str] = ..., weightLoss: _Optional[_Union[DesiredWeightLoss, str]] = ..., desiredSetup: _Optional[_Union[DesiredSetup, str]] = ..., hatedFoods: _Optional[_Union[_concept_pb2.BoolConceptValues, _Mapping]] = ..., proteinStrategy: _Optional[_Union[ProteinStrategy, str]] = ...) -> None: ...

class LoginRequest(_message.Message):
    __slots__ = ("remoteUserId",)
    REMOTEUSERID_FIELD_NUMBER: _ClassVar[int]
    remoteUserId: str
    def __init__(self, remoteUserId: _Optional[str] = ...) -> None: ...

class LoginResponse(_message.Message):
    __slots__ = ("user", "needsInit")
    USER_FIELD_NUMBER: _ClassVar[int]
    NEEDSINIT_FIELD_NUMBER: _ClassVar[int]
    user: _users_pb2.UserRef
    needsInit: bool
    def __init__(self, user: _Optional[_Union[_users_pb2.UserRef, _Mapping]] = ..., needsInit: bool = ...) -> None: ...

class TempTest(_message.Message):
    __slots__ = ("text",)
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str
    def __init__(self, text: _Optional[str] = ...) -> None: ...

class TempResponse(_message.Message):
    __slots__ = ("text",)
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str
    def __init__(self, text: _Optional[str] = ...) -> None: ...
