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

            [Q]: What is the city of residence of the patient named Eugene421 Fisher429?
            [SQL]: SELECT city FROM patients WHERE first='Eugene421' AND last='Fisher429';

            [Q]: What is the first name of the patient with the ID efa523f2-6ac2-641c-58f3-2ca1b97543f9?
            [SQL]: SELECT first FROM patients WHERE id ='efa523f2-6ac2-641c-58f3-2ca1b97543f9';

            [Q]: How many procedures are uncovered by the payer with the ID 26aab0cd-6aba-3e1b-ac5b-05c8867e762c?
            [SQL]: SELECT uncovered_procedures FROM payers WHERE id='26aab0cd-6aba-3e1b-ac5b-05c8867e762c';

            [Q]: Please provide me the encounters that are related to the condition with code 424393004.
            [SQL]: SELECT DISTINCT e.description FROM conditions c LEFT JOIN encounters e ON c.encounter=e.id WHERE c.code='424393004';

            [Q]: Please provide me the name of the provider associated with the encounter 76956a25-b2fe-4a8d-34b8-6baa62656a24.
            [SQL]: SELECT provider FROM encounters WHERE id='76956a25-b2fe-4a8d-34b8-6baa62656a24';


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

            [Q]: What is the city of residence of the patient named Eugene421 Fisher429?
            [SQL]: SELECT city FROM patients WHERE first='Eugene421' AND last='Fisher429';


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

            [Q]: What is the city of residence of the patient named Eugene421 Fisher429?
            [SQL]: SELECT city FROM patients WHERE first='Eugene421' AND last='Fisher429';

            [Q]: What is the first name of the patient with the ID efa523f2-6ac2-641c-58f3-2ca1b97543f9?
            [SQL]: SELECT first FROM patients WHERE id ='efa523f2-6ac2-641c-58f3-2ca1b97543f9';

            [Q]: How many procedures are uncovered by the payer with the ID 26aab0cd-6aba-3e1b-ac5b-05c8867e762c?
            [SQL]: SELECT uncovered_procedures FROM payers WHERE id='26aab0cd-6aba-3e1b-ac5b-05c8867e762c';

            [Q]: Please provide me the encounters that are related to the condition with code 424393004.
            [SQL]: SELECT DISTINCT e.description FROM conditions c LEFT JOIN encounters e ON c.encounter=e.id WHERE c.code='424393004';

            [Q]: Please provide me the name of the provider associated with the encounter 76956a25-b2fe-4a8d-34b8-6baa62656a24.
            [SQL]: SELECT provider FROM encounters WHERE id='76956a25-b2fe-4a8d-34b8-6baa62656a24';


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

            [Q]: What is the city of residence of the patient named Eugene421 Fisher429?
            [SQL]: SELECT city FROM patients WHERE first='Eugene421' AND last='Fisher429';


            With all the information given, provide a SQL query to the following question:

            [Q]: '{question}'
            [SQL]: 
            """
sql_prompt_0schema_bm25 = """ Given an input question create a syntactically correct Postgres SQL query leveraging the provided notes and examples. Only query for relevant columns given the question. If more than one table participates, use a JOIN.

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

            {examples}


            With all the information given, provide a SQL query to the following question:

            [Q]: '{question}'
            [SQL]: 
            """
sql_prompt_schema_bm25 = """ Given an input question create a syntactically correct Postgres SQL query leveraging the provided schema and notes. Only query for relevant columns given the question. Pay attention to using only the column names that you can see in the schema description. Be careful not to query for columns that do not exist. Also, pay attention to which column is in which table. If more than one table participates, use a JOIN. Only provide the SQL query, without any further explanations.


            [Schema]:
            '{schema}'

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
            
            {examples}


            With all the information given, provide a SQL query to the following question:

            [Q]: '{question}'
            [SQL]: 
            """