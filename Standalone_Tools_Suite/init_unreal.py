from post_import_callback import register_import_callback
from validate_asset_prefix import register_validate_asset_prefix
from validate_texture import register_validate_texture
from validate_triangle_count import register_triangle_count_validator
import remote_import_fbx



print(50 * "=")
print("===Init Unreal is processed")

register_import_callback()
register_validate_asset_prefix()
register_validate_texture()
register_triangle_count_validator()

# Create RemoteImporter instance , RemoteImporter is a class. We MUST instantiate it to load it into memory.
remote_import_fbx_service = remote_import_fbx.RemoteImporter()

