from ImporterRules.Queries import QueryBase
from ImporterRules.Actions import ImportActionBase
from ImporterRules import importer_rules_manager , Rule

import unreal

mesh_type_to_directory = {
    "environment" : "Enviro",
    "weapon" : "Weapons"
}


class CheckContainMetaTag(QueryBase):

    def test(self, factory: unreal.Factory, created_object: unreal.Object) -> bool:
        print("=============================")
        if not created_object:
            return False

        asset_subsystem = unreal.get_editor_subsystem(unreal.EditorAssetSubsystem)
        if not asset_subsystem:
            return False

        all_keys = asset_subsystem.get_metadata_tag_values(created_object)

        for tag_key in all_keys:
            current_key = str(tag_key).lower()
            if "mesh_type" in current_key:
                target_value = asset_subsystem.get_metadata_tag(created_object, tag_key)
                if target_value in mesh_type_to_directory:
                    print(f"===SUCCESS: Asset '{created_object.get_fname()}' matched type '{target_value}' ===")
                    return True

        print(f"===ERROR {created_object.get_fname()} does not contain mesh_type")
        return False

class MoveMeshBaseOnType(ImportActionBase):

    def apply(self, factory: unreal.Factory, created_object: unreal.Object) -> bool:
        print("===MoveMeshBaseOnType is processing")

        if not created_object:
            return False
        asset_subsystem = unreal.get_editor_subsystem(unreal.EditorAssetSubsystem)
        if not asset_subsystem:
            return False

        mesh_type_value = None
        all_keys = asset_subsystem.get_metadata_tag_values(created_object)
        for tag_key in all_keys:
            current_key = str(tag_key).lower()
            if "mesh_type" in current_key:
                mesh_type_value = asset_subsystem.get_metadata_tag(created_object, tag_key)
                break

        if not mesh_type_value or mesh_type_value not in mesh_type_to_directory:
            unreal.log_warning(f"===SKIPPING: {created_object.get_name()} has no valid mesh_type tag.")
            return False

        destination_path = f"/Game/{mesh_type_to_directory.get(mesh_type_value)}/{created_object.get_fname()}"
        success = asset_subsystem.rename_asset(created_object.get_path_name(), destination_path)

        if success:
            unreal.log(f"===SUCCESS: Moved {created_object.get_fname()} to {destination_path}")
        else:
            unreal.log_error(f"===FAILED: Could not move {created_object.get_fname()} to {destination_path}")

        return success


######################################################################################################################################

importer_rules_manager.register_rules(
    class_type = unreal.StaticMesh,
    rules = [
        Rule(
            queries = [
                CheckContainMetaTag()
            ],
            actions = [
                MoveMeshBaseOnType()
            ]
        )
    ]
)

