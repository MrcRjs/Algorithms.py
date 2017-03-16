import dbus

def set_backlight(newLightValue):
    bus = dbus.SystemBus()
    kbd_backlight_proxy = bus.get_object(
        'org.freedesktop.UPower', '/org/freedesktop/UPower/KbdBacklight')
    kbd_backlight = dbus.Interface(
        kbd_backlight_proxy, 'org.freedesktop.UPower.KbdBacklight')
    maximum = kbd_backlight.GetMaxBrightness()
    if newLightValue >= 0 and newLightValue <= maximum:
      kbd_backlight.SetBrightness(newLightValue)