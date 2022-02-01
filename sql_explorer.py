import re
import pandas as pd

class SQL(object):
    def __init__(self, sql_text):
        self.sql: str = sql_text
        self.sql_list: list = None
        self.sql_tables: list = None
        self.raw_sql_tables: list = None
        self.table_vars: list = None
        
    def clean_whitespaces(self):
        """ Remove extra whitespaces in SQL script """
        self.sql = re.sub(' +', ' ', self.sql)


    def lowercase_text(self):
        """ Lower case the entire SQL script """
        self.sql = self.sql.lower()


    def replace_commas_w_newline(self):
        """ Replace commas with newline """
        self.sql = self.sql.replace(",", "\n")


    def split_sql_text_by_newlines(self):
        """ Split SQL text (str) in a list by \n """ 
        self.sql_list = [i.strip() for i in self.sql.split("\n")]

    
    def rm_comments(self):
        self.sql_list = [i for i in self.sql_list if '--' not in i]


    def rm_empty_strings(self):
       self.sql_list = [i for i in self.sql_list if i != ''] 

    
    # Table Variable methods
    def extract_table_variables(self):
        select_from_index = [i for i, x in enumerate(self.sql_list) if "select" in x or "from" in x]
        table_start_stop = [(i,j) for i,j in zip(select_from_index[::2], select_from_index[1::2])]

        table_vars = list()
        for i in table_start_stop:
            tmp_var = [i.split(" as ")[0].replace(",", "") for i in self.sql_list[i[0]+1:i[1]]]
            table_vars.append(tmp_var)

        self.table_vars = table_vars


    def clean_up_case_when_vars(self):
        """ Rm CASE WHEN, and THEN, END variables."""
        final_tmp = list()
        for table_var_list in self.table_vars:
            tmp = [re.findall("case when (\w+)", i)[0] if "case when" in i else i for i in table_var_list]
            tmp = [i for i in tmp if 'when' not in i if 'end' not in i]
            final_tmp.append(tmp)
        
        self.table_vars = final_tmp

    
    def clean_date_timestamp_vars(self):
        """ Rm date() and timestamp() operators in variables"""
        final_tmp = list()
        for table_var_list in self.table_vars:
            
            tmp = [re.findall(r'\((.*?)\)', i)[0] if 'date(' in i else i for i in table_var_list]
            
            tmp = [re.findall(r'\((.*?)\)', i)[0] if 'timestamp(' in i else i for i in table_var_list]
            
            final_tmp.append(tmp)
        
        self.table_vars = final_tmp

    # Table level methods
    def extract_tables(self):
        """ Extract all tables from SQL list """
        tmp = [i for i in self.sql_list if 'from' in i or 'join' in i]
        tmp = [i.replace("from", "").replace("`", "").strip() for i in tmp]
        self.sql_tables = " | ".join([i.split("join ")[-1].split(" ")[0] for i in tmp])


    def extract_primary_tables(self):
        """ Keep on primary tables from the database"""
        self.raw_sql_tables = " | ".join([i for i in self.sql_tables.split(" | ") if '.' in i])
