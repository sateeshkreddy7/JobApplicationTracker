from django import forms
from .models import JobApplication


class JobApplicationForm(forms.ModelForm):

    class Meta:
        model = JobApplication
        fields = [
            'company_name',
            'job_title',
            'job_type',
            'location',
            'application_date',
            'status',
            'job_link',
            'salary',
            'interview_date',
            'notes',
        ]

        widgets = {
            'application_date': forms.DateInput(
                attrs={'type': 'date'}
            ),
            'interview_date': forms.DateInput(
                attrs={'type': 'date'}
            ),
            'notes': forms.Textarea(
                attrs={'rows': 4}
            ),
        }