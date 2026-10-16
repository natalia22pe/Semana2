from django.db import models

class Programa(models.Model):
    nombre = models.CharField(max_length=23)
    ficha = models.IntegerField()
    programa = models.CharField(max_length=50)
    lugar = models.CharField(max_length=30)
    duracion = models.IntegerField()
    modalidad = models.CharField(max_length=20)
    nivel_profesional = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=40)

    def __str__(self):      
        return f"{self.nombre} {self.ficha} - programa: {self.programa} lugar: {self.lugar} {self.duracion} {self.modalidad} {self.nivel_profesional} {self.descripcion}"


class instructores(models.Model):
    nombre = models.CharField(max_length=23)
    apellido = models.CharField(max_length=23)
    documento = models.IntegerField(unique=True)
    especialidad = models.CharField(max_length=30)
    ficha_asignada = models.IntegerField()
    correo = models.EmailField(unique=True)
    telefono = models.IntegerField(unique=True)

    def __str__(self):      
        return f"{self.nombre} {self.apellido} {self.documento} {self.especialidad} {self.ficha_asignada} {self.correo} {self.telefono}"


class Aprendiz(models.Model):
    nombre = models.CharField(max_length=23)
    apellido = models.CharField(max_length=23)
    documento = models.IntegerField(unique=True)
    correo = models.EmailField(unique=True)
    telefono = models.IntegerField(unique=True)
    ficha = models.IntegerField()
    programa = models.CharField(max_length=50)

    # Cardinalidad corregida (nombre de atributo en minúscula)
    programa_rel = models.ForeignKey(
        Programa,
        on_delete=models.CASCADE,
        related_name="aprendices",
        null=True,
        blank=True
    )

    def __str__(self):      
        return f"{self.nombre} {self.apellido} Doc: {self.documento} {self.correo} {self.telefono} - Ficha: {self.ficha} {self.programa}"


class Competencias(models.Model):
    nombre = models.CharField(max_length=23)
    ficha = models.IntegerField()
    instructor = models.CharField(max_length=23)

    programa_rel = models.ForeignKey(
        Programa,
        on_delete=models.CASCADE,
        related_name="competencias_programa",
        null=True,
        blank=True
    )

    instructores_rel = models.ForeignKey(
        instructores,
        on_delete=models.CASCADE,                        
        related_name="competencias_instructores",
        null=True,
        blank=True                                     
    )

    def __str__(self):      
        return f"{self.nombre} {self.ficha} {self.instructor}"
