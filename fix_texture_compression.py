import unreal

COMPRESSION_MAPPING = {
    "_D": unreal.TextureCompressionSettings.TC_DEFAULT,      # Diffuse / Albedo
    "_N": unreal.TextureCompressionSettings.TC_NORMALMAP,    # Normal
    #"_M": unreal.TextureCompressionSettings.TC_DEFAULT,        # Metallic
    "_R": unreal.TextureCompressionSettings.TC_GRAYSCALE,        # Roughness
    "_E": unreal.TextureCompressionSettings.TC_DEFAULT,            #emissive
}

def validator_texture_compression(directory:str, apply_fix:bool=True):
    assets_path = unreal.EditorAssetLibrary.list_assets(directory)

    for asset in assets_path:
        texture = unreal.EditorAssetLibrary.load_asset(asset)

        if not isinstance(texture,unreal.Texture2D):
            continue

        name = str(texture.get_fname())
        name_match = False
        correct_compression = None
        for suffix in COMPRESSION_MAPPING.keys():
            if name.endswith(suffix):
                name_match = True
                correct_compression = COMPRESSION_MAPPING[suffix]
                break
        if not name_match:
            continue

        current_compression = texture.get_editor_property("compression_settings")
        if current_compression != correct_compression:
            print(f"=== Wrong compression setting on {texture.get_fname()}")

            if apply_fix:
                print(f"=== {str(texture.get_fname())}'s compression setting was set to {str(correct_compression)}")
                texture.set_editor_property("compression_settings", correct_compression)

                if name.endswith("_D"):
                    texture.set_editor_property("srgb", True)
                    print(f"=== sRGB was checked on {texture.get_fname()}")
            print("================================")

if __name__ == "__main__":
    """Create Undoable for 'Fix Texture Compression' """
    with unreal.ScopedEditorTransaction("Fix Texture Compression"):
        validator_texture_compression(directory="/Game/StarterContent/Textures", apply_fix=True)


