# Project Student_data
This is a project aiming to help students' perform better in upcoming examinations. 

## Tools used
- Google Forms
- Python 3.12.x
- Postgres Docker database

## Data Collection
Data was collected through survey with a google form. It was then extracted via google api to a postgres database.
## Schema Definition
The structure of the database was defined as follows

```
 CREATE TABLE IF NOT EXISTS student_data (
            created_time TIMESTAMP,
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
            distance_btwn_home_school varchar,
            use_of_library_and_study_spaces int,
            use_of_internet float,
            jamb_score int,
            class_participation varchar,
            stress_levels int,
            daily_study int,
            extracurricular_activities int,
            study_satasifaction int,
            last_academic_performance int,
            exam_prep_challenges varchar,
            recommendations varchar
        );
        
```    

        
The Schema defines the columns 'created_time', 'Age', 'Gender', 'average_household_income',
       'parents_educational_qualification', 'marital_status_of_parents',
       'Residence', 'Type_of_family', 'no_of_siblings', 'parental_support',
       'average_days_absent', 'home_school_dist',
       'use_of_library_and_study_spaces', 'use_of_internet', 'jamb_score',
       'class_participation', 'stress_levels', 'daily_study',
       'extracurricular_activities', 'study_satasifaction',
       'last_academic_performance', 'exam_prep_challenges', 'recommendations'

