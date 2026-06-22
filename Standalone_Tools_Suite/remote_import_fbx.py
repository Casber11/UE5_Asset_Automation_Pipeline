import unreal
from pathlib import Path

@unreal.uclass()
class RemoteImporter(unreal.Object):
    @unreal.ufunction(ret=bool, params=[str,str], meta=dict(Category="TechArtCorner"))
    def import_fbx(self, source_path, destination_path):
        static_mesh_import_data = unreal.FbxStaticMeshImportData()
        static_mesh_import_data.combine_meshes = True
        static_mesh_import_data.remove_degenerates = True

        options = unreal.FbxImportUI()
        options.import_mesh = True
        options.import_materials = False
        options.import_textures = False
        options.automated_import_should_detect_type = True
        options.static_mesh_import_data = static_mesh_import_data

        task = unreal.AssetImportTask()
        task.automated = True
        task.destination_name = Path(source_path).stem
        task.destination_path = destination_path
        task.filename = source_path
        task.replace_existing = True
        task.save = False
        task.options = options

        unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([task])

        return True

""" Option 1 """
""" following is ObjectPath for Blender API (Transient) """
""" "/Engine/Transient.RemoteImporter_0" """
""" paste below this code to init_unreal.py for auto execute ('class': RemoteImporter) and then you may execute API from Blender"""
#remote_import_fbx_service = remote_import_fbx.RemoteImporter()

""" Option 2 """
""" following is ObjectPath for Blender API (Default) """
""" "/Engine/PythonTypes.Default__RemoteImporter" """
""" This option is manually copy these remote_import_fbx.py code to the unreal's python console and then you may execute API from Blender"""

""" Test in Insomnia"""
""" json body"""
"""  
{
  "objectPath": "/Engine/Transient.RemoteImporter_0",
  "functionName": "import_fbx",
  "parameters": {
    "source_path": "D:\\UE_Automation\\Batch_Import_FBX_Meshes\\rock_A.fbx",
    "destination_path": "/Game/Enviro"
  }
}
"""
