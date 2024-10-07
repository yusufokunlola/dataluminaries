
GRANT ALL PRIVILEGES ON DATABASE STUDENT_DATA TO data_luminaries;
-- Create schema
CREATE SCHEMA IF NOT EXISTS RESPONSES;


-- create and populate tables
create table if not exists RESPONSES.STUDENT_DATA
(
    created_time varchar,
    Age varchar,
    Gender varchar,
    average_household_income varchar,
    parents_educational_qualification varchar,
    marital_status_of_parents varchar,
    Residence varchar,
    Type_of_family varchar,
    no_of_siblings int,
    parental_support int,
    average_days_absent int,
    home_school_dist varchar,
    use_of_library_and_study_spaces int,
    use_of_internet int,
    jamb_score int,
    class_participation varchar,
    stress_levels int,
    daily_study  int,
    extracurricular_activities int,
    study_satasifaction int,
    last_academic_performance int,
    exam_prep_challenges varchar,
    recommendations varchar
);


COPY RESPONSES.STUDENT_DATA(created_time, Age, Gender, average_household_income,parents_educational_qualification,
marital_status_of_parents, Residence,Type_of_family, no_of_siblings,parental_support,
average_days_absent, home_school_dist,use_of_library_and_study_spaces,
use_of_internet, jamb_score,class_participation, stress_levels, daily_study,
extracurricular_activities, study_satasifaction, last_academic_performance, exam_prep_challenges, recommendations)
FROM '/data/cleaned_data.csv' DELIMITER ',' CSV HEADER;








