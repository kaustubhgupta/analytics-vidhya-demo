from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
from pywebio.exceptions import SessionClosedException
import pandas  as pd
import pickle
import warnings
import argparse

warnings.filterwarnings("ignore")

with open('./pickledFiles/random_forest_model.pkl', 'rb') as f:
   random_forest_model = pickle.load(f)

with open('./pickledFiles/columns.pkl', 'rb') as f:
   model_columns = pickle.load(f)

def prediction(prediction_df):
    query_ = pd.get_dummies(pd.DataFrame(prediction_df, index = [0]), prefix=['Sector','job_sim'], columns=['Sector','job_sim'])
    query = query_.reindex(columns = model_columns, fill_value= 0)
    result = list(random_forest_model.predict(query))
    final_result = round(result[0], 3)

    return final_result

def main():
    put_markdown(
        '''
        # Salary Prediction Web App (`Using PyWebIO`)
        '''
        , lstrip=True
    )

    model_inputs = input_group(
        "Enter the following information",
        [
            input("Rating of the Job", name='rating', type=FLOAT),
            select("Job Sector", name='job_sec', options=[(i,i) for i in ['Information Technology', 'Business Services', 'Education', 'Finance', 'Government', 'Travel & Tourism', 'Health Care']]),
            select("Job Role", name='job_role', options=[('Data Scientist', 'data scientist'), ('Data Engineer', 'data engineer'), ('Analyst', 'analyst'), ('Machine Learning Engineer', 'mle'), ('Director', 'director'), ('Manager', 'manager')]),
            radio("Are you familiar with Python?", name='py_choice', options=[('Yes', 1), ('No', 0)]),
            radio("Are you familiar with R?", name='r_choice', options=[('Yes', 1), ('No', 0)]),
            radio("Are you familiar with Tableau?", name='t_choice', options=[('Yes', 1), ('No', 0)]),
            radio("Are you familiar with Power Bi?", name='pi_choice', options=[('Yes', 1), ('No', 0)]),
            radio("Are you familiar with Machine Learning?", name='ml_choice', options=[('Yes', 1), ('No', 0)]),
            radio("Are you familiar with Deep Learning?", name='dl_choice', options=[('Yes', 1), ('No', 0)]),
        ]
    )

    prediction_df = pd.DataFrame(data = [[model_inputs[i] for i in ['job_sec', 'job_role', 'py_choice', 'r_choice', 't_choice','pi_choice','ml_choice', 'dl_choice', 'rating']]], 
                           columns = ['Sector','job_sim','python_yn','R_yn','tableau','power bi','ml','dl', 'Rating'])

    expectedSalary = prediction(prediction_df)
    put_markdown("### Predicted Salary: {}k Dollars".format(expectedSalary))



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()

    start_server(main, port=args.port)