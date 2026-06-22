import unreal

mesh_type_to_directory = {
    "environment" : "Enviro",
    "weapon" : "Weapons"
}

import_subsystem = None
registered_once = False

def my_post_import_callback(_factory: unreal.Factory, created_object: unreal.Object):
    if created_object is None:
        return

    editor_subsystem = unreal.get_editor_subsystem(unreal.EditorAssetSubsystem)

    if not editor_subsystem:
        return

    is_reimport = "True" == editor_subsystem.get_metadata_tag(created_object,"importer_rules_applied")
    print(f"{f'===REIMPORTING : {created_object.get_fname()}' if is_reimport else f'===FIRST TIME IMPORT : {created_object.get_fname()}'}")
    if is_reimport:
        return

    editor_subsystem.set_metadata_tag(created_object, unreal.Name("importer_rules_applied"), "True")

    all_tag_keys = editor_subsystem.get_metadata_tag_values(created_object)

    mesh_type_value = None
    for tag, value in all_tag_keys.items():
        current_tag = str(tag).lower()
        if "mesh_type" in current_tag:
            if value in mesh_type_to_directory:
                mesh_type_value = mesh_type_to_directory[value]
                break

    if not mesh_type_value:
        return

    destination_path = f"/Game/{mesh_type_value}/{created_object.get_fname()}"
    success = editor_subsystem.rename_asset(created_object.get_path_name(),destination_path)

    if success:
        unreal.log(f"===SUCCESS: Moved {created_object.get_fname()} to {destination_path}")
        print(50 * "=")
    else:
        unreal.log_error(f"===FAILED: Could not move {created_object.get_fname()} to {destination_path}")
        print(50 * "=")



def register_import_callback():
    global import_subsystem , registered_once

    if registered_once:
        return

    registered_once = True

    import_subsystem = unreal.get_editor_subsystem(unreal.ImportSubsystem)
    import_subsystem.on_asset_post_import.add_callable(my_post_import_callback)