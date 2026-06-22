import unreal
from unreal import Object

@unreal.uclass()
class AssetPrefixValidator(unreal.EditorValidatorBase):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg,**kwargs)

    @unreal.ufunction(override=True)
    def k2_can_validate_asset(self, asset:Object) -> bool:
        return isinstance(asset,(unreal.Texture2D,unreal.Material,unreal.Blueprint,unreal.MaterialInstance))

    @unreal.ufunction(override=True)
    def k2_validate_loaded_asset(self, asset:Object) -> unreal.DataValidationResult:
        name = str(asset.get_fname())
        message = "===Name should start with "

        match asset.__class__:
            case unreal.Texture2D:
                if name.startswith("T_"):
                    return unreal.DataValidationResult.VALID
                message += "T_"
            case unreal.Blueprint:
                if name.startswith("BP_"):
                    return unreal.DataValidationResult.VALID
                message += "BP_"
            case unreal.Material:
                if name.startswith("M_"):
                    return unreal.DataValidationResult.VALID
                message += "M_"
            case unreal.MaterialInstance:
                if name.startswith("MI_"):
                    return unreal.DataValidationResult.VALID
                message += "MI_"

        self.asset_warning(asset,unreal.Text(message))
        return unreal.DataValidationResult.VALID

def register_validate_asset_prefix():
    editor_validate_subsystem = unreal.get_editor_subsystem(unreal.EditorValidatorSubsystem)
    validator = AssetPrefixValidator()
    editor_validate_subsystem.add_validator(validator)
