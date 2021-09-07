# https://dev.to/tim_tr/advanced-python-oop-polymorphism-5a80

class Image:
    EXTENSION = "jpg"

    def __init__(self, filename: str):
        if not filename.endswith(self.EXTENSION):
            raise ValueError("Invalid Extension")
        self.filename = filename

    def show(self):
        print(f"You are displaying image : {self.filename} Using <{self.__class__.__name__}> ")


class PNGImage(Image):
    EXTENSION = "png"


class JPGImage(Image):
    EXTENSION = "jpg"


class GIFImage(Image):
    EXTENSION = "gif"


class EPSImage(Image):
    EXTENSION = "eps"


if __name__ == '__main__':
    profile = PNGImage("Profile.png")
    trip = JPGImage("Trip.jpg")
    shared = GIFImage("Shared.gif")
    wallpaper = EPSImage("Wallpaper.eps")
    images = [trip, profile, shared, wallpaper]
    for image in images:
        image.show()
