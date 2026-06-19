# UE5_Asset_Automation_Pipeline

Production-ready Python automation tools for Unreal Engine 5 pipeline.

> 💡 **Developer Profile:** Designed with **2.5 years of 3A production experience (Shipped Title: *South of Midnight*)** to bridge the gap between foliage/environment art pipelines and engine technical performance.

---

## 🚀 Core Toolset Breakdown

### 1. Ingestion & Workflow Automation
*   `batch_import_FBX_Meshes.py`: Automates bulk FBX ingestion into Unreal Engine 5 using optimized standard import tasks and automatic mesh combining.
*   `batch_import_textures.py`: A highly optimized scripting task utilizing automated factory data to bulk-import TGA textures directly into UE5 target directories asynchronously.
*   `pipeline_event_callback.py`: A zero-friction subsystem listener that hooks into UE5's ImportSubsystem to automatically audit, metadata-tag, and dynamically route assets based on dictionary rules upon import.
*   `remote_importer.py`: A cross-DCC pipeline bridge utilizing the UE5 HTTP Remote Control API to allow external software (like Blender) to trigger background asset ingestion tasks silently.

### 2. Automated Quality Assurance (QA Pipeline)
*   `validate_asset_prefix.py`: An automated QA validation gate inheriting from EditorValidatorBase to enforce naming conventions via Python match-case pattern matching upon asset saving.
*   `validate_texture.py`: An automated VRAM validation gate inheriting from EditorValidatorBase to enforce strict square and Power-of-Two (POT) texture constraints upon save.
*   `validate_triangle_count.py`: An automated poly-count budget gate inheriting from EditorValidatorBase that extracts asset triangle metadata to block over-budget static meshes upon save.
*   `test_api_health_check.py`: A automated CI/CD pipeline sanity checker that leverages CDO class path reflection to execute defensive API health checks and prevent breaking path regressions.

### 3. Scene Diagnostics & Optimization
*   `find_overlapping_meshes.py`: A performance profiling utility that detects and auto-destroys spatially redundant overlapping actors to optimize draw calls and eliminate Z-fighting.
*   `remove_unused_assets.py`: A high-performance cleanup utility using Python generators (yield) and AssetRegistry to securely scan, audit, and purge zero-reference orphaned assets while maintaining a constant O(1) memory footprint.

### 4. Materials & Viewport Utilities
*   `editing_material_properties.py`: A pipeline utility that utilizes Editor and Material Editing libraries to batch-modify Vector properties inside Material Instances with built-in validation.
*   `list_tool_menus.py`: Extends the Unreal Engine 5 editor UI via the ToolMenus API to integrate custom automation tools seamlessly into native main menus and right-click asset context menus.
*   `slow_task_progress.py`: A UX optimization tool leveraging ScopedSlowTask to provide responsive progress bar dialogs and safe Ctrl+C style cancel feedback during heavy asset processing routines.

---

## 🛠️ Technical Stack
*   **Engine Target:** Unreal Engine 5.0+
*   **Language:** Python 3.x (Unreal Editor Python API)

---

## 📬 Contact & Professional Links
*   **Role:** Technical Artist (Pipeline & Tools)
*   **Location:** Malaysia (Open to Local & Remote Roles)
*   **Email:** cas
*   **Portfolio / ArtStation:** [你的作品集/渲染图链接]
