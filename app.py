from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        funded_amnt_inv=float(request.form['funded_amnt_inv'])
        int_rate=float(request.form['int_rate'])
        emp_length=float(request.form['emp_length'])
        annual_inc=float(request.form['annual_inc'])
        pymnt_plan=float(request.form['pymnt_plan'])
        dti=float(request.form['dti'])
        delinq_2yrs=float(request.form['delinq_2yrs'])
        fico_range_low=float(request.form['fico_range_low'])
        inq_last_6mths=float(request.form['inq_last_6mths'])
        open_acc=float(request.form['open_acc'])
        pub_rec=float(request.form['pub_rec'])
        revol_bal=float(request.form['revol_bal'])
        revol_util=float(request.form['revol_util'])
        total_acc=float(request.form['total_acc'])
        initial_list_status=float(request.form['initial_list_status'])
        total_rec_late_fee=float(request.form['total_rec_late_fee'])
        last_pymnt_amnt=float(request.form['last_pymnt_amnt'])
        last_fico_range_high=float(request.form['last_fico_range_high'])
        last_fico_range_low=float(request.form['last_fico_range_low'])
        collections_12_mths_ex_med=float(request.form['collections_12_mths_ex_med'])
        policy_code=float(request.form['policy_code'])
        application_type=float(request.form['application_type'])
        acc_now_delinq=float(request.form['acc_now_delinq'])
        tot_coll_amt=float(request.form['tot_coll_amt'])
        tot_cur_bal=float(request.form['tot_cur_bal'])
        total_bal_il=float(request.form['total_bal_il'])
        max_bal_bc=float(request.form['max_bal_bc'])
        TARGET=float(request.form['TARGET'])
        issue_d_month=float(request.form['issue_d_month'])
        earliest_cr_line_month=float(request.form['earliest_cr_line_month'])
        earliest_cr_line_year=float(request.form['earliest_cr_line_year'])
        last_pymnt_d_month=float(request.form['last_pymnt_d_month'])
        last_credit_pull_d_month=float(request.form['last_credit_pull_d_month'])
        last_credit_pull_d_year=float(request.form['last_credit_pull_d_year'])

        
            
        prediction=model.predict([[funded_amnt_inv, int_rate, emp_length, annual_inc,pymnt_plan, dti, delinq_2yrs, fico_range_low, inq_last_6mths,open_acc, pub_rec, revol_bal, revol_util, total_acc,initial_list_status, total_rec_late_fee, last_pymnt_amnt,last_fico_range_high, last_fico_range_low,collections_12_mths_ex_med, policy_code, application_type,acc_now_delinq, tot_coll_amt, tot_cur_bal, total_bal_il,max_bal_bc, TARGET, issue_d_month, earliest_cr_line_month,earliest_cr_line_year, last_pymnt_d_month,last_credit_pull_d_month, last_credit_pull_d_year]])
        output=round(prediction[0],2)
        
        return render_template('index.html',prediction_text="loan prediction is {}".format(output))
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
