from typing import override

from lib.PluginHelper import PluginHelper
from lib.PluginSettingDefinitions import (
    PluginSettings, SettingsGrid, SelectOption, TextAreaSetting, TextSetting, SelectSetting, NumericalSetting, ToggleSetting, ParagraphSetting
)
from lib.Logger import log
from lib.PluginBase import PluginBase, PluginManifest


# Main plugin class
# This is the class that will be loaded by the PluginManager.
class {{cookiecutter.project_slug}}(PluginBase):
    def __init__(self, plugin_manifest: PluginManifest):
        super().__init__(plugin_manifest) # If you use event classes, add them to a second parameter here, named event_classes. This is needed for deserialization from covas.db.

        # Define the plugin settings
        # This is the settings that will be shown in the UI for this plugin.
        self.settings_config: PluginSettings | None = PluginSettings(
            key="{{cookiecutter.project_slug}}Plugin",
            label="{{cookiecutter.project_name}}",
            icon="waving_hand", # Uses Material Icons, like the built-in settings-tabs.
            grids=[
                SettingsGrid(
                    key="general",
                    label="General",
                    fields=[
                        ToggleSetting(
                            key="bool_setting",
                            label="Boolean Setting",
                            type="toggle",
                            readonly = False,
                            placeholder = None,
                            default_value = False
                        ),
                    ]
                ),
            ]
        )
    
    # The following overrides are optional. Remove them if you don't need them.
    @override
    def on_chat_start(self, helper: PluginHelper):
        # Register actions
        helper.register_action('{{cookiecutter.project_slug_lower}}_get_version', "Returns the current version of the {{cookiecutter.project_name}} plugin.", {
            "type": "object",
            "properties": {}
        }, self.{{cookiecutter.project_slug_lower}}_get_version, 'global')

        log('debug', f"Actions registered for {self.plugin_manifest.name}")
        
        pass
    
    @override
    def on_chat_stop(self, helper: PluginHelper):
        # Executed when the chat is stopped
        pass

    # Actions
    def {{cookiecutter.project_slug_lower}}_get_version(self, args, projected_states) -> str:
        log('info', 'Hello World from {{cookiecutter.project_name}}!')
            
        return f"Currently running {{cookiecutter.project_name}} version {self.plugin_manifest.version}."