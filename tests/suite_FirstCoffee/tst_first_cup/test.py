# -*- coding: utf-8 -*-

import names

def main():
    startApplication("coffee")
    test.startVideoCapture()
    mouseClick(waitForObject(names.sideBar_cappuccinoButton_CoffeeButton), 151, 158, Qt.LeftButton)
    mouseClick(waitForObject(names.coffee_image_Image), 48, 34, Qt.LeftButton)
    mouseDrag(waitForObject(names.coffee_handleRect_Rectangle), 6, 6, -84, 10, Qt.NoModifier, Qt.LeftButton)
    mouseDrag(waitForObject(names.coffee_handleRect_Rectangle_2), 6, 3, 60, 14, Qt.NoModifier, Qt.LeftButton)
    test.compare(waitForObjectExists(names.coffee_sugarSlider_Slider).value, 5)
    mouseClick(waitForObject(names.coffee_image_Image), 29, 48, Qt.LeftButton)
    mouseClick(waitForObject(names.coffee_image_Image_2), 33, 45, Qt.LeftButton)
    test.vp("VP1")
    mouseClick(waitForObject(names.coffee_image_Image_3), 39, 41, Qt.LeftButton)
    test.stopVideoCapture()