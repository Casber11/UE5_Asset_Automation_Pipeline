import unreal
# from typing import List
EditorUtilityLibrary = unreal.EditorUtilityLibrary
EditorAssetLibrary = unreal.EditorAssetLibrary

########## This function is process by list for the asset paths ##########
# def get_selected_asset_path() -> str:
#     selected_assets = EditorUtilityLibrary.get_selected_assets()
#
#     asset_path_list = []
#     for asset in selected_assets:
#         asset_path_list.append(EditorAssetLibrary.get_path_name_for_loaded_asset(asset))
#
#     return asset_path_list
#
# def remove_unused_asset(asset_path_list: List[str]):
#
#     for asset_path in asset_path_list:
#         reference = EditorAssetLibrary.find_package_referencers_for_asset(asset_path)
#
#         if len(reference) == 0:
#             delete_success = EditorAssetLibrary.delete_asset(asset_path)
#
#             if not delete_success:
#                 unreal.log_warning(f"Could not delete {asset_path}")



########## This function is process by "yield" for the asset paths ##########
def get_selected_asset_path():
    selected_assets = EditorUtilityLibrary.get_selected_assets()

    for asset in selected_assets:
        yield EditorAssetLibrary.get_path_name_for_loaded_asset(asset)

def remove_unused_asset(asset_path):
    reference = EditorAssetLibrary.find_package_referencers_for_asset(asset_path)

    if len(reference) == 0:
        delete_success = EditorAssetLibrary.delete_asset(asset_path)
        if not delete_success:
            unreal.log_warning(f"Could not delete {asset_path}")

if __name__ == "__main__":
    for path in get_selected_asset_path():
        remove_unused_asset(path)

############################# 方法 三 ####################################################
# ==============================================================================
# 主题：读取指定文件夹下的所有资产 (Read All Assets in Folder)
# 功能：连接 Asset Registry，通过路径递归检索文件夹内的所有资产信息
# ==============================================================================
# 1. 获取资产注册表对象 (连接数据库)
asset_registry = unreal.AssetRegistryHelpers.get_asset_registry()

# 2. 检索特定文件夹路径下的资产清单 (包含子文件夹)
assets = asset_registry.get_assets_by_path(unreal.Name('/Game/YourFolderPath/'), True)


