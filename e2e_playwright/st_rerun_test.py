# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022-2024)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from playwright.sync_api import Page, expect

from e2e_playwright.shared.app_utils import click_button


def test_st_rerun_restarts_the_session_when_invoked(app: Page):
    expect(app.get_by_test_id("stText")).to_have_text(
        "Being able to rerun a session is awesome!"
    )


def test_fragment_scoped_st_rerun(app: Page):
    expect(app.get_by_test_id("stText")).to_have_text(
        "Being able to rerun a session is awesome!"
    )

    click_button(app, "rerun fragment")
    expect(app.get_by_test_id("stMarkdown").first).to_have_text("fragment run count: 5")
    expect(app.get_by_test_id("stMarkdown").last).to_have_text("app run count: 4")

    click_button(app, "rerun fragment")
    expect(app.get_by_test_id("stMarkdown").first).to_have_text(
        "fragment run count: 10"
    )
    expect(app.get_by_test_id("stMarkdown").last).to_have_text("app run count: 4")
