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

            [Q]: What is the start date of the procedure Urine protein test?
            [SQL]: SELECT start FROM procedures WHERE description='Urine protein test';

            [Q]: What is the start date of the condition Part-time employment (finding)?
            [SQL]: SELECT start FROM conditions WHERE description='Part-time employment (finding)';

            [Q]: What encounter is required during the use of the device with code 272265001?
            [SQL]: SELECT DISTINCT e.description FROM devices d LEFT JOIN encounters e ON d.encounter=e.id WHERE d.code='272265001';

            [Q]: How many immunizations are covered by the payer Dual Eligible?
            [SQL]: SELECT covered_immunizations FROM payers WHERE name='Dual Eligible';

            [Q]: Please provide me patients with the observation Tobacco smoking status.
            [SQL]: SELECT DISTINCT p.first, p.last FROM observations ob LEFT JOIN patients p ON ob.patient=p.id WHERE ob.description='Tobacco smoking status';


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

            [Q]: What is the start date of the procedure Urine protein test?
            [SQL]: SELECT start FROM procedures WHERE description='Urine protein test';


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

            [Q]: What is the start date of the procedure Urine protein test?
            [SQL]: SELECT start FROM procedures WHERE description='Urine protein test';

            [Q]: What is the start date of the condition Part-time employment (finding)?
            [SQL]: SELECT start FROM conditions WHERE description='Part-time employment (finding)';

            [Q]: What encounter is required during the use of the device with code 272265001?
            [SQL]: SELECT DISTINCT e.description FROM devices d LEFT JOIN encounters e ON d.encounter=e.id WHERE d.code='272265001';

            [Q]: How many immunizations are covered by the payer Dual Eligible?
            [SQL]: SELECT covered_immunizations FROM payers WHERE name='Dual Eligible';

            [Q]: Please provide me patients with the observation Tobacco smoking status.
            [SQL]: SELECT DISTINCT p.first, p.last FROM observations ob LEFT JOIN patients p ON ob.patient=p.id WHERE ob.description='Tobacco smoking status';


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

            [Q]: What is the start date of the procedure Urine protein test?
            [SQL]: SELECT start FROM procedures WHERE description='Urine protein test';


            With all the information given, provide a SQL query to the following question:

            [Q]: '{question}'
            [SQL]: 
            """