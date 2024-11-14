from appium.webdriver.common.appiumby import AppiumBy

from pages.base_class import BaseClass

class PracticeModePage(BaseClass):
    PRACTICE_MODE_TAB_LOCATOR = '//android.view.View[contains(@content-desc,"Sing A Song")]'
    SING_BOTTOM_TAB_LOCATOR = '//android.widget.ImageView[@content-desc="Sing"]'

    SONG_LIST_LOCATOR = (AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[6]/android.view.View/android.view.View')
    SEARCH_BAR_ICON_LOCATOR = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().className("android.widget.ImageView").instance(0)')
    GLOBAL_SEARCH_SONG_LIST_LOCATOR = (AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View')

    # Select 'Sing A Song' tab
    def select_practice_mode(self):
        self.wait_and_click(AppiumBy.XPATH,self.SING_BOTTOM_TAB_LOCATOR)
