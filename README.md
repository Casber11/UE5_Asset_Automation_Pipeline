# UE5_Asset_Automation_Pipeline

A collection of modular, config-driven Python tools built to automate asset workflows, enforce studio conventions, and profile technical budgets in Unreal Engine 5.

> 💡 **Developer Background:** Built with **2.5 years of AAA production experience as a 3D Vegetation & Environment Artist (Shipped Title: *South of Midnight*)**. Driven by real-world art production pain points, I spent the last **2 years in intensive, self-directed R&D** to master the Unreal Python API, delivering this framework to eliminate repetitive workflow friction and optimize engine performance.

---

## 🚀 Core Toolset Breakdown

### 1. Ingestion & Workflow Automation
*   `batch_import_FBX_Meshes.py`: Automates bulk FBX ingestion into Unreal Engine 5 using optimized standard import tasks and automatic mesh combining.
*   `batch_import_textures.py`: A highly optimized scripting task utilizing automated factory data to bulk-import TGA textures directly into UE5 target directories asynchronously.
*   `pipeline_event_callback.py`: A zero-friction subsystem listener that hooks into UE5's `ImportSubsystem` to automatically audit, metadata-tag, and dynamically route assets based on dictionary rules upon import.
*   `remote_importer.py`: A cross-DCC pipeline bridge utilizing the UE5 HTTP Remote Control API to allow external software (like Blender) to trigger background asset ingestion tasks silently.

### 2. Automated Quality Assurance (QA Pipeline)
*   `validate_asset_prefix.py`: An automated QA validation gate inheriting from `EditorValidatorBase` to enforce naming conventions via Python `match-case` pattern matching upon asset saving.
*   `validate_texture.py`: An automated VRAM validation gate inheriting from `EditorValidatorBase` to enforce strict square and Power-of-Two (POT) texture constraints upon save.
*   `validate_triangle_count.py`: An automated poly-count budget gate inheriting from `EditorValidatorBase` that extracts asset triangle metadata to block over-budget static meshes upon save.
*   `test_api_health_check.py`: An automated CI/CD pipeline sanity checker that leverages CDO class path reflection to execute defensive API health checks and prevent breaking path regressions.

### 3. Scene Diagnostics & Optimization
*   `find_overlapping_meshes.py`: A performance profiling utility that detects and auto-destroys spatially redundant overlapping actors to optimize draw calls and eliminate Z-fighting.
*   `remove_unused_assets.py`: A high-performance cleanup utility using Python generators (`yield`) and `AssetRegistry` to securely scan, audit, and purge zero-reference orphaned assets while maintaining a constant O(1) memory footprint.

### 4. Materials & Viewport Utilities
*   `editing_material_properties.py`: A pipeline utility that utilizes Editor and Material Editing libraries to batch-modify Vector properties inside Material Instances with built-in validation.
*   `list_tool_menus.py` / `init_unreal.py`: Extends the Unreal Engine 5 editor UI via the `ToolMenus` API to integrate custom automation tools seamlessly into native main menus on engine startup.
*   `slow_task_progress.py`: A UX optimization tool leveraging `ScopedSlowTask` to provide responsive progress bar dialogs and safe Ctrl+C style cancel feedback during heavy asset processing routines.

---

## 🛠️ Technical Stack
*   **Engine Target:** Unreal Engine 5.0+
*   **Language:** Python 3.x (Unreal Editor Python API)
*   **Core Concepts:** Data Validation Subsystem, Asset Registry, Event Callbacks, Generators (`yield`), Remote Control API, UX/UI Progress Feedback.

---

## 📬 Contact & Professional Links
*   **Role:** Technical Artist (Pipeline & Tools)
*   **Location:** Malaysia (Open to Local & Remote Roles)
*   **Email:** casberdesign@gmail.com
*   **ArtStation (Foliage Art Portfolio):** https://www.artstation.com/casberwong
