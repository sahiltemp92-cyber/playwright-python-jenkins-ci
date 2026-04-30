import os
import allure
import pytest


@pytest.fixture(autouse=True)
def attach_video_on_failure(request, page):
    yield

    # Attach video ONLY if test failed
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        video = page.video
        if video:
            video_path = video.path()
            page.context.close()  # 🔥 THIS IS CRITICAL

            if os.path.exists(video_path):
                with open(video_path, "rb") as f:
                    allure.attach(
                        f.read(),
                        name="Failure video",
                        attachment_type=allure.attachment_type.WEBM,
                    )


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
