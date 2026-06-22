from pathlib import Path
from typing import Set
import unreal


source_path = r"D:\PlasticProject\OnyxProject\FlintArt\Assets\Beech_Tree"
destination_path = "/Game/MyTexture"

def batch_import_textures(destination_path_in: str, source_folder:str)-> Set[unreal.Object]:
    asset_to_import = Path(source_folder).glob("*.tga")
    asset_to_import = list(map(lambda path:str(path),asset_to_import))

    asset_import_data = unreal.AutomatedAssetImportData()
    asset_import_data.destination_path = destination_path_in
    asset_import_data.filenames = asset_to_import
    asset_import_data.replace_existing = True

    imported = set(unreal.AssetToolsHelpers.get_asset_tools().import_assets_automated(asset_import_data))
    return imported

if __name__ == "__main__":
    imported_result = batch_import_textures(destination_path,source_path)
    print(f"==={imported_result}")


