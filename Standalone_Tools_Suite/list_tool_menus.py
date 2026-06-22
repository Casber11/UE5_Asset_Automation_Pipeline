import unreal

"""
PURPOSE: Unreal Engine Python Menu Customization Collection.

USAGE: 
- This script is for manual copying and pasting into the Unreal Engine Python Console/Scripting window.
- TO RUN AT STARTUP: If you want these menus to load automatically when Unreal starts, 
  add this code to your 'init_unreal.py' file.
"""
###############################################################################################################################################
""" Locate the "Edit" menu object and print its internal path for reference(This is useful for identifying the correct path when extending existing menus) """
menus = unreal.ToolMenus.get()
edit_menu = menus.find_menu("LevelEditor.MainMenu.Edit")
print(edit_menu)

###############################################################################################################################################
""" PURPOSE: List available Unreal Engine menu names."""
def list_menu(num=1000):
    menu_list = set()

    for i in range(num):
        obj = unreal.find_object(None, "/Engine/Transient.ToolMenus_0:RegisteredMenu_%s" % i)
        if not obj:
            obj = unreal.find_object(None, f"/Engine/Transient.ToolMenus_0:ToolMenu_{i}")
            if not obj:
                continue

        menu_name = str(obj.menu_name)
        if menu_name == "None":
            continue

        menu_list.add(menu_name)

    return list(menu_list)


for p in list_menu():
    print(p)

###############################################################################################################################################
""" Add a new sub-menu to the main menu bar """
menus = unreal.ToolMenus.get()
main_menu = menus.find_menu("LevelEditor.MainMenu")
custom_menu = main_menu.add_sub_menu("Custom Menu", "Python Automation", "Menu Name", "Menu Label")

""" Refresh all menu widgets to make the new menu visible on the UI """
unreal.ToolMenus.get().refresh_all_widgets()

###############################################################################################################################################

""" PURPOSE: Create a custom button in the UE5 Editor 'Edit' menu using Python. """

@unreal.uclass()
class MyScriptObject(unreal.ToolMenuEntryScript):
    """
    Define a custom script object that inherits from ToolMenuEntryScript.
    This allows the script to be integrated into the Unreal Editor menus.
    """
    @unreal.ufunction(override=True)
    def execute(self, context):
        """
        The code inside this function will run when the menu entry is clicked.
        """
        print("SCRIPT EXECUTED")

""" EXAMPLE 1 """
""" Get a reference to the 'Edit' menu in the Level Editor Main Menu """
edit_menu = unreal.ToolMenus.get().find_menu("LevelEditor.MainMenu.Edit")

""" Instantiate our custom script object """
script_object = MyScriptObject()

""" Initialize the menu entry settings """
script_object.init_entry(
    owner_name=edit_menu.menu_name,
    menu=edit_menu.menu_name,
    section="EditMain",
    name="Unreal Engine 5 Python Automation Course",
    label="Unreal Engine 5 Python Automation Course",
    tool_tip="Custom Script Entry"
)

""" Register the entry to the menu so it becomes visible """
script_object.register_menu_entry()

""" Set a custom icon for the menu entry"""
tool_menu_entry_script_data = script_object.data
script_icon = unreal.ScriptSlateIcon(style_set_name="UMGStyle",
                                     style_name="Palette.Icon",
                                     small_style_name="Palette.Icon.Small")
tool_menu_entry_script_data.icon = script_icon

unreal.ToolMenus.get().refresh_all_widgets()


""" EXAMPLE 2 """
""" Get a reference to the Static Mesh asset context menu """
""" This ensures the button only appears when right-clicking on a Static Mesh """
asset_context_menu = unreal.ToolMenus.get().find_menu("ContentBrowser.AssetContextMenu.StaticMesh")

""" Instantiate the custom script object """
script_object2 = MyScriptObject()

""" Initialize the menu entry settings """
script_object2.init_entry(
    owner_name=asset_context_menu.menu_name,
    menu=asset_context_menu.menu_name,
    section="GetAssetActions",
    name="Unreal Engine 5 Python Automation Course",
    label="Unreal Engine 5 Python Automation Course",
    tool_tip="Custom Script Entry"
)

""" Register the entry to the Static Mesh context menu """
script_object2.register_menu_entry()

""" Set a custom icon for the menu entry"""
tool_menu_entry_script_data = script_object2.data
script_icon = unreal.ScriptSlateIcon(style_set_name="UMGStyle",
                                     style_name="Palette.Icon",
                                     small_style_name="Palette.Icon.Small")
tool_menu_entry_script_data.icon = script_icon

unreal.ToolMenus.get().refresh_all_widgets()

""" EXAMPLE 3 """
"""Creating a Nested Menu Hierarchy to group custom tools under a sub-menu. """
asset_context_menu = unreal.ToolMenus.get().find_menu("ContentBrowser.AssetContextMenu.StaticMesh")
custom_menu_sub =  asset_context_menu.add_sub_menu("Custom.Menu","Custom Menu", "Label",
                                               "We added this menu our selves")

### SEPARATOR
separator_entry = unreal.ToolMenuEntry(name=unreal.Name("Custom Separator Entry"),type=unreal.MultiBlockType.SEPARATOR)
custom_menu_sub.add_menu_entry("", separator_entry)

script_object3 = MyScriptObject()
script_object3.init_entry(
    owner_name=custom_menu_sub.menu_name,
    menu=custom_menu_sub.menu_name,
    section="",
    name="Unreal Engine 5 Python Automation Course",
    label="Unreal Engine 5 Python Automation Course",
    tool_tip="Custom Script Entry"
)

script_object3.register_menu_entry()

""" Set a custom icon for the menu entry"""
tool_menu_entry_script_data = script_object3.data
script_icon = unreal.ScriptSlateIcon(style_set_name="UMGStyle",
                                     style_name="Palette.Icon",
                                     small_style_name="Palette.Icon.Small")
tool_menu_entry_script_data.icon = script_icon

unreal.ToolMenus.get().refresh_all_widgets()

###############################################################################################################################################
