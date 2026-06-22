import unreal
import time

##################################################################################
def main():
    total_steps = 100
    dialog_name = "Slow task in progress"

    with unreal.ScopedSlowTask(total_steps, dialog_name) as slow_task:
        # Display the dialog window and enable the "Cancel" button
        slow_task.make_dialog(can_cancel=True)

        for i in range(total_steps):
            # Check if the user has requested to stop the process via UI
            if slow_task.should_cancel():
                break

            # Simulate heavy workload (replace this with your actual logic)
            time.sleep(0.1)

            # Advance the progress bar by 1 increment and refresh the UI
            slow_task.enter_progress_frame(1)

if __name__ == "__main__":
    main()

######################################################################################
"""EXAMPLE: Progress Bar with Asset Renaming"""

def rename_assets(folder_path):
    # 1. Get all asset paths
    assets = unreal.EditorAssetLibrary.list_assets(folder_path)
    total_steps = len(assets) # Set total steps dynamically

    with unreal.ScopedSlowTask(total_steps, "Renaming assets...") as slow_task:
        slow_task.make_dialog(can_cancel=True)

        for asset_path in assets:
            # Check if the user clicked cancel
            if slow_task.should_cancel():
                break

            # --- Replace time.sleep(0.1) with actual function ---
            new_path = asset_path + "_New"
            unreal.EditorAssetLibrary.rename_asset(asset_path, new_path)

            # Update progress bar
            slow_task.enter_progress_frame(1)
