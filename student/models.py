from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator,RegexValidator
from django.urls import reverse

class Student(models.Model):
    YEAR=[('I', 'First'),
    ('II', 'Second'),
    ('III', 'Third'),
    ('IV', 'Fourth')]
    BRANCH_SEC = [
    ('ECE-A', 'ECE-A'),
    ('ECE-B', 'ECE-B'),
    ('CSE-A', 'CSE-A'),
    ('CSE-B', 'CSE-B'),
    ('EEE-A', 'EEE-A')]
    roll_no=models.PositiveBigIntegerField(help_text="Enter your roll number (length-12) : <em>(318126xxxxxx)</em> format",verbose_name="Roll number",default=318126512000
    ,validators=[MinValueValidator(1),MaxValueValidator(318126512999),RegexValidator(r"^\d{1,12}")],unique=True)
    name=models.CharField(max_length=50)
    class_signature=models.CharField(
        max_length=5,
        choices=BRANCH_SEC,
        default="ECE-A",
        verbose_name="Branch and Section"
    )
    cgpa=models.DecimalField(decimal_places=2,max_digits=4,validators=[RegexValidator(r"^\d{1}\.\d{1,2}$")],help_text="format: <em>x.xx</em> Eg:8.85",error_messages={"invalid":"Enter according to the format x.xx"})
    year=models.CharField(max_length=4,choices=YEAR,default="I")

    def __str__(self) -> str:
        return f"{self.name} {self.roll_no}"

    def get_absolute_url(self):
        return reverse("record-detail",kwargs={"pk":self.pk})
