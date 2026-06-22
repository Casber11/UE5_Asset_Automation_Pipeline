import unreal
from pathlib import Path
from typing import List

source_path = r"D:\UE_Automation\Batch_Import_FBX_Meshes"
destination_path  = "/Game/Enviro"
assets_to_import = list(Path(source_path).glob("*.fbx"))

static_mesh_import_data = unreal.FbxStaticMeshImportData()
static_mesh_import_data.combine_meshes = True
static_mesh_import_data.remove_degenerates = True

options = unreal.FbxImportUI()
options.import_mesh = True
options.import_materials = True
options.import_textures = False
options.automated_import_should_detect_type = True
options.static_mesh_import_data = static_mesh_import_data

tasks_list: List[unreal.AssetImportTask] = []

for input_file_path in assets_to_import:
    task = unreal.AssetImportTask()
    task.automated = True
    task.destination_path = destination_path
    task.destination_name = input_file_path.stem
    task.filename = str(input_file_path)
    task.replace_existing = True
    task.save = True
    task.options = options

    tasks_list.append(task)

unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks(tasks_list)

for task in tasks_list:
    for path in task.imported_object_paths:
        print(f"===Imported {path}")