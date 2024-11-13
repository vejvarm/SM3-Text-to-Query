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

            [Q]: In what type of allergy does the description House dust mite (organism) fall?
            [SQL]: SELECT DISTINCT type FROM allergies WHERE description='House dust mite (organism)';

            [Q]: Please provide me the patients with the claim ID 56a60caf-14fc-db17-e331-65b4e8dcf942.
            [SQL]: SELECT DISTINCT p.first, p.last FROM claims cl LEFT JOIN patients p ON cl.patientid= p.id WHERE cl.id='56a60caf-14fc-db17-e331-65b4e8dcf942';

            [Q]: What encounter is associated with the supply named Disposable air-purifying respirator (physical object)?
            [SQL]: SELECT DISTINCT e.description FROM supplies s LEFT JOIN encounters e ON s.encounter=e.id WHERE s.code='409534002';

            [Q]: What is the description of encounter 2377dc28-54be-b1a0-407f-2fcd515cf588?
            [SQL]: SELECT description FROM encounters WHERE id='2377dc28-54be-b1a0-407f-2fcd515cf588';

            [Q]: Who are the patients associated with the device Home continuous positive airway pressure unit (physical object)?
            [SQL]: SELECT DISTINCT p.first, p.last FROM devices d LEFT JOIN patients p ON d.patient=p.id WHERE d.description='Home continuous positive airway pressure unit (physical object)';


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

            [Q]: In what type of allergy does the description House dust mite (organism) fall?
            [SQL]: SELECT DISTINCT type FROM allergies WHERE description='House dust mite (organism)';


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

            [Q]: In what type of allergy does the description House dust mite (organism) fall?
            [SQL]: SELECT DISTINCT type FROM allergies WHERE description='House dust mite (organism)';

            [Q]: Please provide me the patients with the claim ID 56a60caf-14fc-db17-e331-65b4e8dcf942.
            [SQL]: SELECT DISTINCT p.first, p.last FROM claims cl LEFT JOIN patients p ON cl.patientid= p.id WHERE cl.id='56a60caf-14fc-db17-e331-65b4e8dcf942';

            [Q]: What encounter is associated with the supply named Disposable air-purifying respirator (physical object)?
            [SQL]: SELECT DISTINCT e.description FROM supplies s LEFT JOIN encounters e ON s.encounter=e.id WHERE s.code='409534002';

            [Q]: What is the description of encounter 2377dc28-54be-b1a0-407f-2fcd515cf588?
            [SQL]: SELECT description FROM encounters WHERE id='2377dc28-54be-b1a0-407f-2fcd515cf588';

            [Q]: Who are the patients associated with the device Home continuous positive airway pressure unit (physical object)?
            [SQL]: SELECT DISTINCT p.first, p.last FROM devices d LEFT JOIN patients p ON d.patient=p.id WHERE d.description='Home continuous positive airway pressure unit (physical object)';


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

            [Q]: In what type of allergy does the description House dust mite (organism) fall?
            [SQL]: SELECT DISTINCT type FROM allergies WHERE description='House dust mite (organism)';


            With all the information given, provide a SQL query to the following question:

            [Q]: '{question}'
            [SQL]: 
            """