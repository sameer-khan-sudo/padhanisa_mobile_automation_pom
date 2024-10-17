from pages.base_class import BaseClass


class PassiveVideoPlayerActions(BaseClass):
    PLAY_BUTTON_LOCATOR = '//android.view.View[@content-desc="Play"]'
    PAUSE_BUTTON_LOCATOR = '//android.view.View[@content-desc="Pause"]'
    SETTING_BUTTON_LOCATOR = '//android.widget.ImageView[@content-desc="Settings"]'
    CROSS_BUTTON_LOCATOR = '//android.view.View[contains(@content-desc,"0")]/android.view.View[1]'
    SEEK_BUTTON_LOCATOR = '//android.widget.SeekBar[contains(@content-desc,"%")]'