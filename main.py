from datetime import datetime
from win10toast import ToastNotifier
import ctypes
import winsound


def Notify(_header: str, _body: str, _duration: int, _threaded: bool):
    toast = ToastNotifier()

    toast.show_toast(
        _header,
        _body,
        duration=_duration,
        # icon_path="icon.ico",
        threaded=_threaded,
    )


def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


def Beep(_times: int):
    i = 0
    while i < _times:
        winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
        i += 1


def main():
    print("Program Started at", datetime.now())

    while True:
        # current_hour = datetime.now().time().hour
        current_minute = datetime.now().time().minute

        if current_minute % 15 == 0:
            print("Vize Başvuru Vakti")
            Beep(5)
            Mbox('Randevu Vakti', 'Randevuya Başvurmayı Dene', 0)
            Notify("Vize Başvuru Vakti", "Koş vizeye başvur", 60, False)


if __name__ == "__main__":
    main()
