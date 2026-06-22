import unreal
from unreal import Object

LIMITED_TRIANGLE = 3000

@unreal.uclass()
class TriangleCountValidator(unreal.EditorValidatorBase):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg,**kwargs)

    @unreal.ufunction(override=True)
    def k2_can_validate_asset(self, asset:Object) -> bool:
        return isinstance(asset,unreal.StaticMesh)

    @unreal.ufunction(override=True)
    def k2_validate_loaded_asset(self, asset:Object) -> unreal.DataValidationResult:
        correct_path = ".".join(str(asset.get_path_name()).split(".")[:-1])
        tag_values = unreal.EditorAssetLibrary.get_tag_values(correct_path)
        print(tag_values)
        if 'Triangles' not in tag_values:
            self.asset_warning(asset,unreal.Text("Could not validate asset triangle count. "
                                                 "'Triangles' tag is not available"))
            return unreal.DataValidationResult.NOT_VALIDATED

        triangle_count = int(tag_values[unreal.Name('Triangles')])
        if triangle_count > LIMITED_TRIANGLE:
            self.asset_fails(asset,unreal.Text(f'Asset has too many triangles: {triangle_count}. '
                                               f'Limit is {LIMITED_TRIANGLE}'))
            return unreal.DataValidationResult.INVALID

        return unreal.DataValidationResult.VALID

def register_triangle_count_validator():
    editor_validate_subsystem = unreal.get_editor_subsystem(unreal.EditorValidatorSubsystem)
    triangle_count_validator = TriangleCountValidator()
    editor_validate_subsystem.add_validator(triangle_count_validator)