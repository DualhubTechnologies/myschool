from django import template
from schoolprofile.models import ClassSubject

register = template.Library()

@register.filter
def get_subject(class_subjects, subject_id):
    try:
        return class_subjects.get(subject_id=subject_id)
    except ClassSubject.DoesNotExist:
        return None
