
class Function:
    def execute_sql(self, *args):
        translate_args = []
        for arg in args :
            translate_args.append(arg)
        for i in range(len(translate_args)):
            print(f"translate_args[{i}] = {translate_args[i]}")

    def execute_sql2(self, **kwargs):
        print(kwargs)
        for key,value in kwargs.items():
            print(f"{key} = {value}")
fn = Function()
# fn.execute_sql(
#         "AIRFLOW", # p_process text, 
#         "start_time_str", # p_process_datetime text, 
#         "func", # p_fn_name text, 
#         ["billing_period"], # p_billing_period text, 
#         ["billing_period_start"], # p_billing_period_start text, 
#         ["billing_period_end"], # p_billing_period_end text, 
#         ["filter_date_start"], # p_filter_date_start text, 
#         ["filter_date_end"], # p_filter_date_end text, 
#         "country", # p_country text, 
#         "partners", # p_partner_id_list text
    # )

A =null
fn.execute_sql2(
            p_process = ("AIRFLOW"),
            p_process_datetime = "start_time_str",
            p_fn_name = "func",
            p_billing_period = "202311",
            p_billing_period_start = "20231101",
            p_billing_period_end = "20231130",
            p_filter_date_start = "p_filter_date_start",
            p_filter_date_end = "p_filter_date_end",
            p_country = "TH",
            p_partner_id_list = "null",
)

