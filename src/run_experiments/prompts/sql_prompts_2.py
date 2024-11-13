sql_prompt_schema_0shot = """ Given an input question create a syntactically correct Postgres SQL query leveraging the provided schema and notes. Only query for relevant columns given the question. Pay attention to using only the column names that you can see in the schema description. Be careful not to query for columns that do not exist. Also, pay attention to which column is in which table. If more than one table participates, use a JOIN. Only provide the SQL query, without any further explanations.


            [Schema]:
            '{schema}'

            [Notes]:
            1) Use the database values that are explicitly mentioned in the question.
            2) Pay attention to the columns that are used for the JOIN by using the Foreign_keys.
            3) Use DESC and DISTINCT when needed.
            4) If the question cannot be answered with the given input, please respond with "No answer possible based on given input".
            5) Pay attention to the columns that are used for the GROUP BY statement.
            6) Pay attention to the columns that are used for the SELECT statement.


            [Q] = Question, [SQL] = Answer (correct query)


            With all the information given, provide a SQL query to the following question:

            [Q]: '{question}'
            [SQL]: 
            """
sql_prompt_0schema_fewshots = """ Given an input question create a syntactically correct Postgres SQL query leveraging the provided notes and examples. Only query for relevant columns given the question. If more than one table participates, use a JOIN.

            [Notes]:
            1) Use the database values that are explicitly mentioned in the question.
            2) Pay attention to the columns that are used for the JOIN by using the Foreign_keys.
            3) Use DESC and DISTINCT when needed.
            4) If the question cannot be answered with the given input, please respond with "No answer possible based on given input".
            5) Pay attention to the columns that are used for the GROUP BY statement.
            6) Pay attention to the columns that are used for the SELECT statement.

            Please include the following examples for better understanding.

            [Examples]:

            [Q] = Question, [SQL] = Answer (correct query)

            [Q]: Please provide me the patients with the claim ID 25382c93-4b35-d58c-d519-2f50343b3626.
            [SQL]: SELECT DISTINCT p.first, p.last FROM claims cl LEFT JOIN patients p ON cl.patientid= p.id WHERE cl.id='25382c93-4b35-d58c-d519-2f50343b3626';

            [Q]: Please provide me a reason for the use of the care plan with code 734163000.
            [SQL]: SELECT reasondescription FROM careplans WHERE code='734163000'; 	

            [Q]: Please provide me the quality for the supply with the code 1137596000.
            [SQL]: SELECT DISTINCT quantity FROM supplies s WHERE code='1137596000'; 	

            [Q]: What is the SNOMED code for the allergy described as Eggs (edible) (substance)?
            [SQL]: SELECT DISTINCT code FROM allergies WHERE description='Eggs (edible) (substance)'; 	

            [Q]: What is the department id of the claim with the ID 2bfc5ac8-bf25-4845-f673-c6f6bc344034?
            [SQL]: SELECT departmentid FROM claims WHERE id='2bfc5ac8-bf25-4845-f673-c6f6bc344034';


            With all the information given, provide a SQL query to the following question:

            [Q]: '{question}'
            [SQL]: 
            """
sql_prompt_0schema_oneshot = """ Given an input question create a syntactically correct Postgres SQL query leveraging the provided notes and examples. Only query for relevant columns given the question. If more than one table participates, use a JOIN.

            [Notes]:
            1) Use the database values that are explicitly mentioned in the question.
            2) Pay attention to the columns that are used for the JOIN by using the Foreign_keys.
            3) Use DESC and DISTINCT when needed.
            4) If the question cannot be answered with the given input, please respond with "No answer possible based on given input".
            5) Pay attention to the columns that are used for the GROUP BY statement.
            6) Pay attention to the columns that are used for the SELECT statement.

            Please include the following example for better understanding.

            [Examples]:

            [Q] = Question, [SQL] = Answer (correct query)

            [Q]: Please provide me the patients with the claim ID 25382c93-4b35-d58c-d519-2f50343b3626.
            [SQL]: SELECT DISTINCT p.first, p.last FROM claims cl LEFT JOIN patients p ON cl.patientid= p.id WHERE cl.id='25382c93-4b35-d58c-d519-2f50343b3626';


            With all the information given, provide a SQL query to the following question:

            [Q]: '{question}'
            [SQL]: 
            """
sql_prompt_schema_fewshots = """ Given an input question create a syntactically correct Postgres SQL query leveraging the provided schema, notes, and examples. Only query for relevant columns given the question. Pay attention to using only the column names that you can see in the schema description. Be careful not to query for columns that do not exist. Also, pay attention to which column is in which table. If more than one table participates, use a JOIN.

            [Schema]:
            '{schema}'

            [Notes]:
            1) Use the database values that are explicitly mentioned in the question.
            2) Pay attention to the columns that are used for the JOIN by using the Foreign_keys.
            3) Use DESC and DISTINCT when needed.
            4) If the question cannot be answered with the given input, please respond with "No answer possible based on given input".
            5) Pay attention to the columns that are used for the GROUP BY statement.
            6) Pay attention to the columns that are used for the SELECT statement.

            Please include the following examples for better understanding.

            [Examples]:

            [Q] = Question, [SQL] = Answer (correct query)

            [Q]: Please provide me the patients with the claim ID 25382c93-4b35-d58c-d519-2f50343b3626.
            [SQL]: SELECT DISTINCT p.first, p.last FROM claims cl LEFT JOIN patients p ON cl.patientid= p.id WHERE cl.id='25382c93-4b35-d58c-d519-2f50343b3626';

            [Q]: Please provide me a reason for the use of the care plan with code 734163000.
            [SQL]: SELECT reasondescription FROM careplans WHERE code='734163000'; 	

            [Q]: Please provide me the quality for the supply with the code 1137596000.
            [SQL]: SELECT DISTINCT quantity FROM supplies s WHERE code='1137596000'; 	

            [Q]: What is the SNOMED code for the allergy described as Eggs (edible) (substance)?
            [SQL]: SELECT DISTINCT code FROM allergies WHERE description='Eggs (edible) (substance)'; 	

            [Q]: What is the department id of the claim with the ID 2bfc5ac8-bf25-4845-f673-c6f6bc344034?
            [SQL]: SELECT departmentid FROM claims WHERE id='2bfc5ac8-bf25-4845-f673-c6f6bc344034';


            With all the information given, provide a SQL query to the following question:

            [Q]: '{question}'
            [SQL]: 
            """
sql_prompt_schema_oneshot = """ Given an input question create a syntactically correct Postgres SQL query leveraging the provided schema, notes, and examples. Only query for relevant columns given the question. Pay attention to using only the column names that you can see in the schema description. Be careful not to query for columns that do not exist. Also, pay attention to which column is in which table. If more than one table participates, use a JOIN.

            [Schema]:
            '{schema}'

            [Notes]:
            1) Use the database values that are explicitly mentioned in the question.
            2) Pay attention to the columns that are used for the JOIN by using the Foreign_keys.
            3) Use DESC and DISTINCT when needed.
            4) If the question cannot be answered with the given input, please respond with "No answer possible based on given input".
            5) Pay attention to the columns that are used for the GROUP BY statement.
            6) Pay attention to the columns that are used for the SELECT statement.


            Please include the following examples for better understanding.

            [Examples]:

            [Q] = Question, [SQL] = Answer (correct query)

            [Q]: Please provide me the patients with the claim ID 25382c93-4b35-d58c-d519-2f50343b3626.
            [SQL]: SELECT DISTINCT p.first, p.last FROM claims cl LEFT JOIN patients p ON cl.patientid= p.id WHERE cl.id='25382c93-4b35-d58c-d519-2f50343b3626';


            With all the information given, provide a SQL query to the following question:

            [Q]: '{question}'
            [SQL]: 
            """
