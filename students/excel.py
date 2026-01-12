import pandas as pd
from django.db import IntegrityError
from schoolprofile.models import SchoolClass, Stream
from students.models import  Student
from students.models import Student

def import_students_from_excel(excel_file):
    """
    Read an uploaded Excel/CSV file and import into Student.
    Builds detailed error messages per row, listing ALL issues.
    """
    # Load DataFrame
    if excel_file.name.lower().endswith(('.xls', '.xlsx')):
        df = pd.read_excel(excel_file)
    else:
        df = pd.read_csv(excel_file)

    total = len(df)
    imported = 0
    errors = []

    # Valid choice sets
    valid_genders = {k for k, _ in Student.GENDER_CHOICES}
    valid_status = {k for k, _ in Student.STATUS_CHOICES}
    valid_section = {k for k, _ in Student.SECTION_CHOICES}

    for idx, row in df.iterrows():
        row_num = idx + 2  # Excel row number (header assumed at row 1)
        row_issues = []

        # ✅ Safely extract admission_number
        raw_adm = row.get('admission_number')
        if pd.isna(raw_adm) or str(raw_adm).strip().lower() in ("", "nan", "none"):
            errors.append(f"Row {row_num}: admission_number is missing — cannot import this row.")
            continue
        adm = str(raw_adm).strip()

        # ✅ Safely extract and check schoolpay_code uniqueness
        raw_code = row.get('schoolpay_code')
        schoolpay_code = None
        if not pd.isna(raw_code):
            schoolpay_code = str(raw_code).strip()
            if schoolpay_code.lower() not in ("", "nan", "none"):
                exists = Student.objects.exclude(admission_number=adm).filter(schoolpay_code=schoolpay_code).exists()
                if exists:
                    row_issues.append(f"SchoolPay Code '{schoolpay_code}' is already used by another student.")
            else:
                schoolpay_code = None

        # first_name
        raw_first = row.get('first_name')
        fn = str(raw_first).strip() if not pd.isna(raw_first) else ''
        if not fn:
            row_issues.append("first_name is missing")

        # other_names (optional)
        other_names = str(row.get('other_names')).strip() if not pd.isna(row.get('other_names')) else None

        # date_of_birth
        try:
            dob = pd.to_datetime(row['date_of_birth']).date()
        except Exception:
            row_issues.append("date_of_birth is missing or invalid")

        # gender
        raw_gender = row.get('gender')
        gender = str(raw_gender).strip().lower() if not pd.isna(raw_gender) else ''
        if gender not in valid_genders:
            row_issues.append(f"gender '{gender}' is invalid")

        # school_class
        class_name = str(row.get('school_class')).strip() if not pd.isna(row.get('school_class')) else ''
        if not class_name:
            row_issues.append("school_class is missing")

        # stream
        stream_name = str(row.get('stream')).strip() if not pd.isna(row.get('stream')) else ''
        if not stream_name:
            row_issues.append("stream is missing")

        # enrollment_date
        try:
            enroll = pd.to_datetime(row['enrollment_date']).date()
        except Exception:
            row_issues.append("enrollment_date is missing or invalid")

        # status
        raw_status = row.get('status')
        status = str(raw_status).strip().lower() if not pd.isna(raw_status) else 'active'
        if status not in valid_status:
            row_issues.append(f"status '{status}' is invalid")

        # section
        raw_section = row.get('section')
        section = str(raw_section).strip().lower() if not pd.isna(raw_section) else 'day'
        if section not in valid_section:
            row_issues.append(f"section '{section}' is invalid")

        # address (optional)
        address = str(row.get('address')).strip() if not pd.isna(row.get('address')) else None

        # Skip saving if any validation issues
        if row_issues:
            errors.append(f"Row {row_num}: " + "; ".join(row_issues))
            continue

        # Resolve foreign key objects
        school_class, _ = SchoolClass.objects.get_or_create(name=class_name)
        stream, _ = Stream.objects.get_or_create(name=stream_name, school_class=school_class)

        # Prepare data
        data = {
            'schoolpay_code':   schoolpay_code,
            'first_name':       fn,
            'other_names':      other_names,
            'date_of_birth':    dob,
            'gender':           gender,
            'school_class':     school_class,
            'stream':           stream,
            'enrollment_date':  enroll,
            'address':          address,
            'status':           status,
            'section':          section,
        }

        try:
            Student.objects.update_or_create(
                admission_number=adm,
                defaults=data
            )
            imported += 1
        except IntegrityError as e:
            errors.append(f"Row {row_num}: Database error: {str(e)}")

    if errors:
        error_message = "; ".join(errors)
        raise Exception(f"{error_message} | The system only Imported {imported}/{total} students successfully.")

    return f"Imported {imported}/{total} students successfully."