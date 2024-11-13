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
sql_prompt_0schema_fewshots = """ Given an input question create a syntactically correct Postgres SQL query leveraging the provided notes and examples. Only query for relevant columns given the question. If more than one table participates, use a JOIN. Only provide the SQL query, without any further explanations.

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

            [Q]: Which encounter is related to allergy Animal dander (substance)?
            [SQL]: SELECT DISTINCT e.description FROM encounters e LEFT JOIN allergies a ON a.encounter = e.id WHERE a.description=' Animal dander (substance)';

            [Q]: Provide the list of patients associated with the payer Dual Eligible.
            [SQL]: SELECT DISTINCT p.first, p.last FROM payers py LEFT JOIN payer_transitions pt ON py.id=pt.payer LEFT JOIN patients p ON pt.patient=p.id WHERE py.id='Dual Eligible';

            [Q]: Give me the organization affiliated with the provider with the ID beff794b-089c-3098-9bed-5cc458acbc05.
            [SQL]: SELECT org.name FROM providers pr LEFT JOIN organizations org ON pr.organization=org.id WHERE id='beff794b-089c-3098-9bed-5cc458acbc05';

            [Q]: What is the base cost of medication with the code 205923.
            [SQL]: SELECT DISTINCT base_cost FROM medications WHERE code='205923';

            [Q]: What is the procedure code of the claim transaction 210ae4cd-7ca0-7da4-66a7-ef20b4f5db4d?
            [SQL]: SELECT procedurecode FROM claims_transactions WHERE id='210ae4cd-7ca0-7da4-66a7-ef20b4f5db4d';


            With all the information given, provide a SQL query to the following question:

            [Q]: '{question}'
            [SQL]: 
            """
sql_prompt_0schema_oneshot = """ Given an input question create a syntactically correct Postgres SQL query leveraging the provided notes and examples. Only query for relevant columns given the question. If more than one table participates, use a JOIN. Only provide the SQL query, without any further explanations.

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

            [Q]: Which encounter is related to allergy Animal dander (substance)?
            [SQL]: SELECT DISTINCT e.description FROM encounters e LEFT JOIN allergies a ON a.encounter = e.id WHERE a.description=' Animal dander (substance)';


            With all the information given, provide a SQL query to the following question:

            [Q]: '{question}'
            [SQL]: 
            """
sql_prompt_schema_fewshots = """ Given an input question create a syntactically correct Postgres SQL query leveraging the provided schema, notes, and examples. Only query for relevant columns given the question. Pay attention to using only the column names that you can see in the schema description. Be careful not to query for columns that do not exist. Also, pay attention to which column is in which table. If more than one table participates, use a JOIN. Only provide the SQL query, without any further explanations.

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

            [Q]: Which encounter is related to allergy Animal dander (substance)?
            [SQL]: SELECT DISTINCT e.description FROM encounters e LEFT JOIN allergies a ON a.encounter = e.id WHERE a.description=' Animal dander (substance)';

            [Q]: Provide the list of patients associated with the payer Dual Eligible.
            [SQL]: SELECT DISTINCT p.first, p.last FROM payers py LEFT JOIN payer_transitions pt ON py.id=pt.payer LEFT JOIN patients p ON pt.patient=p.id WHERE py.id='Dual Eligible';

            [Q]: Give me the organization affiliated with the provider with the ID beff794b-089c-3098-9bed-5cc458acbc05.
            [SQL]: SELECT org.name FROM providers pr LEFT JOIN organizations org ON pr.organization=org.id WHERE id='beff794b-089c-3098-9bed-5cc458acbc05';

            [Q]: What is the base cost of medication with the code 205923.
            [SQL]: SELECT DISTINCT base_cost FROM medications WHERE code='205923';

            [Q]: What is the procedure code of the claim transaction 210ae4cd-7ca0-7da4-66a7-ef20b4f5db4d?
            [SQL]: SELECT procedurecode FROM claims_transactions WHERE id='210ae4cd-7ca0-7da4-66a7-ef20b4f5db4d';


            With all the information given, provide a SQL query to the following question:

            [Q]: '{question}'
            [SQL]: 
            """
sql_prompt_schema_oneshot = """ Given an input question create a syntactically correct Postgres SQL query leveraging the provided schema, notes, and examples. Only query for relevant columns given the question. Pay attention to using only the column names that you can see in the schema description. Be careful not to query for columns that do not exist. Also, pay attention to which column is in which table. If more than one table participates, use a JOIN. Only provide the SQL query, without any further explanations.

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

            [Q]: Which encounter is related to allergy Animal dander (substance)?
            [SQL]: SELECT DISTINCT e.description FROM encounters e LEFT JOIN allergies a ON a.encounter = e.id WHERE a.description=' Animal dander (substance)';


            With all the information given, provide a SQL query to the following question:

            [Q]: '{question}'
            [SQL]: 
            """