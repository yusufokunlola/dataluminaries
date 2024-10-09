import io
from google.oauth2.service_account import Credentials
import gspread
import pgcredentials as pgc
import pandas as pd
import psycopg2
import os


# Use google-auth instead of oauth2client
creds = Credentials.from_service_account_file(
    r"C:\Users\DELL\Documents\extractionproject\key\projectdata-437811-e9bfdb8f2ef6.json",
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ],
)

client = gspread.authorize(creds)


# Now that that's done, pull data from the Google sheet.
def GetSpreadsheetData(sheetName, worksheetIndex):
    sheet = client.open_by_url(sheetName).get_worksheet(worksheetIndex)
    data = sheet.get_all_values()[1:]  # Exclude headers
    headers = sheet.row_values(1)  # Get headers
    df = pd.DataFrame(data, columns=headers)  # Convert to DataFrame
    # Ensure the directory exists
    directory = r"C:\Users\DELL\Documents\extractionproject\data"
    if not os.path.exists(directory):
        os.makedirs(directory)
    # Save the DataFrame to CSV
    student_file = df.to_csv(
        os.path.join(directory, "student_response.csv"), index=False, encoding="utf-8"
    )
    return df


def clean_student_data(df):
    """
    This function cleans the student data
    """
    # drop the @ column
    df = df.drop("@", axis=1)
    # replace the column names
    df = df.rename(
        columns={
            "Timestamp": "created_time",
            "Average Household Income": "average_household_income",
            "Educational qualification of parent/guardian": "parents_educational_qualification",
            "Marital status of parents": "marital_status_of_parents",
            "Type of Family": "Type_of_family",
            "No. of siblings": "no_of_siblings",
            "Do your parents/guardians support your academic work?": "parental_support",
            "Average number of days absent from school each month": "average_days_absent",
            "Distance between home and school": "distance_btwn_home_school",
            "How often do you use the library and study spaces?": "use_of_library_and_study_spaces",
            "How often do you use the internet to access learning materials": "use_of_internet",
            "What was your JAMB Score?": "jamb_score",
            "How often do you participate in Class?": "class_participation",
            "How often do you experience Stress?": "stress_levels",
            "How often do you study on a daily basis?": "daily_study",
            "How often do you engage do you engage in extracurricular activity?": "extracurricular_activities",
            "Are you happy studying this course?": "study_satasifaction",
            "Last academic performance": "last_academic_performance",
            "What challenges do you face in preparing for your exams? (Select all that apply)": "exam_prep_challenges",
            "What support do you think could improve your exam performance? (Select all that apply)": "recommendations",
        }
    )
    # replace the null values in the last 2 columns as the were selected as none but it saw it as Nan
    df[["exam_prep_challenges", "recommendations"]] = df[
        ["exam_prep_challenges", "recommendations"]
    ].where(df[["exam_prep_challenges", "recommendations"]].notna(), "None")

    # Save the cleaned DataFrame to CSV
    csv_file_path = r"C:\Users\DELL\Documents\dataluminaries\data\cleaned_data.csv"
    try:
        df.to_csv(csv_file_path, index=False, encoding="utf-8")
        return csv_file_path
    except Exception as e:
        print(f"Failed to save CSV: {e}")
        return None


def connect_to_postgres():
    try:
        # Connection credentials for PostgreSQL
        connection = psycopg2.connect(
            user=pgc.user,
            password=pgc.password,
            host=pgc.host,
            port=pgc.port,
            database=pgc.database,
        )
        return connection
    except (Exception, psycopg2.Error) as error:
        print("Error connecting to PostgreSQL", error)
        return None


def create_table_if_not_exists(conn):
    """
    Create the student_data table if it doesn't exist.
    """
    try:
        cursor = conn.cursor()
        create_table_query = """
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
        """
        cursor.execute(create_table_query)
        conn.commit()
        print("Table student_data created successfully (or already exists).")
    except Exception as e:
        print(f"Failed to create table: {e}")
    finally:
        cursor.close()


def copy_csv_to_postgres(csv_file_path):
    try:
        conn = connect_to_postgres()
        if conn is None:
            print("Failed to connect to PostgreSQL")
            return

        # Create the table if it doesn't exist
        create_table_if_not_exists(conn)

        cursor = conn.cursor()

        if csv_file_path:
            with open(csv_file_path, "r") as f:
                cursor.copy_expert("COPY student_data FROM STDIN WITH CSV HEADER", f)
            conn.commit()
            print("Data loaded into PostgreSQL successfully.")
        else:
            print("No valid CSV file to load.")

    except Exception as e:
        print(f"Failed to load data into PostgreSQL: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()


if __name__ == "__main__":

    # Step 1: Extract data from Google Sheets
    df = GetSpreadsheetData(pgc.url, 0)

    # Step 2: Clean and save the DataFrame as a CSV file
    csv_file_path = clean_student_data(df)

    # Step 3: Load data into PostgreSQL if CSV exists
    if csv_file_path:
        copy_csv_to_postgres(csv_file_path)
