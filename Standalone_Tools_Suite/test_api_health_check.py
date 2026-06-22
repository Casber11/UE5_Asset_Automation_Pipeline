import unreal
from remote_control_demo_functions import RemoteControlDemo


def test_api_health_check():
    remote_control_expected_path = r"/Game/Python/remote_control_demo_functions_PY.Default__RemoteControlDemo"
    remote_control_demo_path = (
        RemoteControlDemo.get_default_object().get_path_name()
    )

    if remote_control_expected_path != remote_control_demo_path:
        unreal.log_error(
            "RemoteControlDemo class path has changed, Remote Control API call may no longer work. "
            f"Expected: {remote_control_expected_path} Current: {remote_control_demo_path}"
        )


if __name__ == "__main__":
    test_api_health_check()
