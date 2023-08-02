from django.db import models

# class Frequency(models.Model):
#     # scan = models.ForeignKey("Scan", on_delete=models.CASCADE)
#     # window = models.PositiveIntegerField()
#     # channel = models.PositiveIntegerField()
#     frequency = models.FloatField()
#     # intensity = models.FloatField(help_text="Intensity in Jy")
# # Create your models here.
#     class Meta:
#         unique_together = ("scan", "channel", "frequency")

#     def __str__(self):
#         return f"{self.name}"
    

class Source(models.Model):
    name = models.TextField(db_index=True)

    def __str__(self):
        return f"{self.name}"

class Frontend(models.Model):
    name = models.TextField(unique=True, db_index=True)

    def __str__(self):
        
        return f"{self.name}"


class Polarization(models.Model):
    name = models.TextField(db_index=True)

    def __str__(self):
        return f"{self.name}"
    

class Project(models.Model):
    name = models.TextField(unique=False, db_index=True)

    def __str__(self):
        return f"{self.name}"

class File(models.Model):
    name = models.TextField(unique=True, db_index=True)
    path = models.TextField(unique=True, db_index=True)

    def __str__(self):
        return f"{self.name}"

class FrequencyType(models.Model):
    name = models.TextField(unique=True, db_index=True)

    def __str__(self):
        return f"{self.name}"

class Session(models.Model):
    name = models.TextField(unique=True, db_index=True)
    project = models.ForeignKey(
        "Project",
        on_delete=models.CASCADE,
        help_text="The Project this Session belongs to",
    )
    # NOTE: This might not turn out to be 1:1, but let's try
    file = models.OneToOneField(
        "File",
        on_delete=models.CASCADE,
        help_text="The FITS file this Session data was pulled from",
    )
    # From column 'counts' (unclear what this is)
    # NOTE: Seems unused
    # counts = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name}"

    class Meta:
        unique_together = ("project", "name")


class Scan(models.Model):
    session = models.ForeignKey("Session", on_delete=models.CASCADE)
    # feed = models.ForeignKey("Feed", on_delete=models.CASCADE)
    frontend = models.ForeignKey("Frontend", on_delete=models.CASCADE,null=True)
    # backend = models.ForeignKey("Backend", on_delete=models.CASCADE)
    # coordinates = models.ForeignKey(
    #     "Coordinates",
    #     on_delete=models.CASCADE,
    #     help_text="The averaged(?) location on the sky this scan took place",
    # )

    source = models.ForeignKey("Source", on_delete=models.CASCADE)
    frequency_type = models.ForeignKey("FrequencyType", on_delete=models.CASCADE)
    polarization = models.ForeignKey("Polarization", on_delete=models.CASCADE)

    # number = models.PositiveIntegerField()
    mjd = models.DecimalField(max_digits=8, decimal_places=3, db_index=True)
    datetime = models.DateTimeField(null=True, db_index=True)
    # lst = models.DecimalField(max_digits=9, decimal_places=7)
    # resolution = models.DecimalField(max_digits=11, decimal_places=10)
    # exposure = models.DecimalField(max_digits=8, decimal_places=5)
    # tsys = models.DecimalField(max_digits=6, decimal_places=4)
    # unit = models.TextField()

    def __str__(self):
        return f"{self.session.name}"

    class Meta:
        # unique_together = ("session", "number", "mjd")
        unique_together = ("session", "mjd")



class Frequency(models.Model):
    scan = models.ForeignKey("Scan", on_delete=models.CASCADE,null=True)
    # window = models.PositiveIntegerField()
    # channel = models.PositiveIntegerField()
    frequency = models.FloatField()
    intensity = models.FloatField(help_text="Intensity in Jy",null=True)

    class Meta:
        # unique_together = ("scan", "channel", "frequency")
        unique_together = ("scan","frequency")


    # def __str__(self):
    #     return (
    #         f"{self.scan.session.name}: Scan #{self.scan.number}: "
    #         f"Channel #{self.channel}: Frequency: {self.frequency} MHz "
    #         f" Intensity: {self.intensity} Jy"
    #     )