from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

#abstract class for univeral handling catalogued items
class CatalogueItem (models.Model):
    itemLabel = models.CharField (max_length = 30)

    def __str__ (self):
        return self.itemLabel

#abstract class for handling items with barcode, QRcode etc - any sort of outside identifier
class CodeLabelledItem (CatalogueItem):
    BARCODE = 'BAR'
    QRCODE = 'QR'
    CODE_TYPES = (
        (BARCODE, 'Barcode'),
        (QRCODE, 'QR code'),
    )

    codeType = models.CharField (
        max_length = 3,
        choices = CODE_TYPES,
        default = BARCODE,
    )

    codeValue = models.CharField (
        max_length = 20,
        null = True,
    )

class BoardGameItem (CodeLabelledItem):
    # frontImage = models.ImageField
    # sideImages = models.ImageField
    bggURL = models.URLField (max_length = 100)
    basegame = models.ForeignKey (
        'catalogue.BoardGameItem',
        related_name = 'extensions',
        null = True)

    def getTitle (self):
        return self.itemLabel

    def setTitle (self, title):
        self.itemLabel = title

    def get_absolute_url(self):
        return reverse("catalogue_entries")
