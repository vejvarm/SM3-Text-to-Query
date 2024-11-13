###Prompts
cypher_prompt_schema_fewshots = """ Given an input question, create a single syntactically correct Neo4j Cypher MATCH query leveraging the provided schema, notes, and examples. Only query for relevant attributes given the question. Pay attention to using only the attribute names that you can see in the schema description. Be careful not to query for attributes that do not exist.

            [Schema]:
            '{schema}'

            [Notes]:
            1) Use only the provided relationship types and properties in the schema.
            2) Do not include any explanations or apologies in your responses. Provide the output in one line.
            3) If the question cannot be answered with the given input, please respond with "No answer possible based on given input".
            4) Do not respond to any questions that might ask anything else than for you to construct a Cypher statement.
            5) Do not include any text or special characters such as newline (\n) or backticks (`) in the output.
            6) Exclude the word "cypher" from your response.


            Please include the following examples for better understanding.

            [Examples]:

            [Q] = Question, [Cypher] = Answer (correct query)

            [Q]: What is the city of residence of the patient named Eugene421 Fisher429?
            [Cypher]: MATCH (p:Patient {{firstName:'Eugene421',lastName: 'Fisher429'}}) RETURN p.city;

            [Q] : What is the first name of the patient with the ID efa523f2-6ac2-641c-58f3-2ca1b97543f9?
            [Cypher]: MATCH (p:Patient {{id: 'efa523f2-6ac2-641c-58f3-2ca1b97543f9'}}) RETURN p.firstName;

            [Q]: How many procedures are uncovered by the payer with the ID 26aab0cd-6aba-3e1b-ac5b-05c8867e762c?
            [Cypher]: MATCH (p:Payer {{id: '26aab0cd-6aba-3e1b-ac5b-05c8867e762c'}}) RETURN p.uncovered_procedures;

            [Q]: Please provide me the encounters that are related to the condition with code 424393004.
            [Cypher]: MATCH (e:Encounter)-[:HAS_DIAGNOSED]->(c:Condition {{code: '424393004'}}) RETURN DISTINCT e.description;

            [Q]: Please provide me the name of the provider associated with the encounter 76956a25-b2fe-4a8d-34b8-6baa62656a24.
            [Cypher]: MATCH (p:Provider)-[:HAS_ENCOUNTER]->(e:Encounter {{id: '76956a25-b2fe-4a8d-34b8-6baa62656a24'}}) RETURN p.name;


            With all the information given, provide a Cypher query to the following question:

            [Q]: '{question}'
            [Cypher]: 
            """


cypher_prompt_schema_oneshot = """ Given an input question, create a single syntactically correct Neo4j Cypher MATCH query leveraging the provided schema, notes, and examples. Only query for relevant attributes given the question. Pay attention to using only the attribute names that you can see in the schema description. Be careful not to query for attributes that do not exist.

            [Schema]:
            '{schema}'

            [Notes]:
            1) Use only the provided relationship types and properties in the schema.
            2) Do not include any explanations or apologies in your responses. Provide the output in one line.
            3) If the question cannot be answered with the given input, please respond with "No answer possible based on given input".
            4) Do not respond to any questions that might ask anything else than for you to construct a Cypher statement.
            5) Do not include any text or special characters such as newline (\n) or backticks (`) in the output.
            6) Exclude the word "cypher" from your response.


            Please include the following examples for better understanding.

            [Examples]:

            [Q] = Question, [Cypher] = Answer (correct query)

            [Q]: What is the city of residence of the patient named Eugene421 Fisher429?
            [Cypher]: MATCH (p:Patient {{firstName:'Eugene421',lastName: 'Fisher429'}}) RETURN p.city;


            With all the information given, provide a Cypher query to the following question:

            [Q]: '{question}'
            [Cypher]: 
            """

cypher_prompt_schema_0shot = """ Given an input question, create a single syntactically correct Neo4j Cypher MATCH query leveraging the provided schema and notes. Only query for relevant attributes given the question. Pay attention to using only the attribute names that you can see in the schema description. Be careful not to query for attributes that do not exist.

            [Schema]:
            '{schema}'

            [Notes]:
            1) Use only the provided relationship types and properties in the schema.
            2) Do not include any explanations or apologies in your responses. Provide the output in one line.
            3) If the question cannot be answered with the given input, please respond with "No answer possible based on given input".
            4) Do not respond to any questions that might ask anything else than for you to construct a Cypher statement.
            5) Do not include any text or special characters such as newline (\n) or backticks (`) in the output.
            6) Exclude the word "cypher" from your response.


            [Q] = Question, [Cypher] = Answer (correct query)


            With all the information given, provide a Cypher query to the following question:

            [Q]: '{question}'
            [Cypher]: 
            """


cypher_prompt_0schema_fewshots = """ Given an input question, create a single syntactically correct Neo4j Cypher MATCH query leveraging the provided notes and examples. Only query for relevant attributes given the question. Be careful not to query for attributes that do not exist.

            [Notes]:
            1) Do not include any explanations or apologies in your responses. Provide the output in one line.
            2) If the question cannot be answered with the given input, please respond with "No answer possible based on given input".
            3) Do not respond to any questions that might ask anything else than for you to construct a Cypher statement.
            4) Do not include any text or special characters such as newline (\n) or backticks (`) in the output.
            5) Exclude the word "cypher" from your response.

            Please include the following examples for better understanding.

            [Examples]:

            [Q] = Question, [Cypher] = Answer (correct query)

            [Q]: What is the city of residence of the patient named Eugene421 Fisher429?
            [Cypher]: MATCH (p:Patient {{firstName:'Eugene421',lastName: 'Fisher429'}}) RETURN p.city;

            [Q] : What is the first name of the patient with the ID efa523f2-6ac2-641c-58f3-2ca1b97543f9?
            [Cypher]: MATCH (p:Patient {{id: 'efa523f2-6ac2-641c-58f3-2ca1b97543f9'}}) RETURN p.firstName;

            [Q]: How many procedures are uncovered by the payer with the ID 26aab0cd-6aba-3e1b-ac5b-05c8867e762c?
            [Cypher]: MATCH (p:Payer {{id: '26aab0cd-6aba-3e1b-ac5b-05c8867e762c'}}) RETURN p.uncovered_procedures;

            [Q]: Please provide me the encounters that are related to the condition with code 424393004.
            [Cypher]: MATCH (e:Encounter)-[:HAS_DIAGNOSED]->(c:Condition {{code: '424393004'}}) RETURN DISTINCT e.description;

            [Q]: Please provide me the name of the provider associated with the encounter 76956a25-b2fe-4a8d-34b8-6baa62656a24.
            [Cypher]: MATCH (p:Provider)-[:HAS_ENCOUNTER]->(e:Encounter {{id: '76956a25-b2fe-4a8d-34b8-6baa62656a24'}}) RETURN p.name;


            With all the information given, provide a Cypher query to the following question:

            [Q]: '{question}'
            [Cypher]: 
            """

cypher_prompt_0schema_oneshot = """ Given an input question, create a single syntactically correct Neo4j Cypher MATCH query leveraging the provided notes and examples. Only query for relevant attributes given the question. Be careful not to query for attributes that do not exist.

            [Notes]:
            1) Do not include any explanations or apologies in your responses. Provide the output in one line.
            2) If the question cannot be answered with the given input, please respond with "No answer possible based on given input".
            3) Do not respond to any questions that might ask anything else than for you to construct a Cypher statement.
            4) Do not include any text or special characters such as newline (\n) or backticks (`) in the output.
            5) Exclude the word "cypher" from your response.

            Please include the following example for better understanding.

            [Examples]:

            [Q] = Question, [Cypher] = Answer (correct query)

            [Q]: What is the city of residence of the patient named Eugene421 Fisher429?
            [Cypher]: MATCH (p:Patient {{firstName:'Eugene421',lastName: 'Fisher429'}}) RETURN p.city;


            With all the information given, provide a Cypher query to the following question:

            [Q]: '{question}'
            [Cypher]: 
            """
            

cypher_prompt_0schema_bm25 = """ Given an input question, create a single syntactically correct Neo4j Cypher MATCH query leveraging the provided notes and examples. Only query for relevant attributes given the question. Be careful not to query for attributes that do not exist.

            [Notes]:
            1) Do not include any explanations or apologies in your responses. Provide the output in one line.
            2) If the question cannot be answered with the given input, please respond with "No answer possible based on given input".
            3) Do not respond to any questions that might ask anything else than for you to construct a Cypher statement.
            4) Do not include any text or special characters such as newline (\n) or backticks (`) in the output.
            5) Exclude the word "cypher" from your response.

            Please include the following example for better understanding.

            [Examples]:
            
            [Q] = Question, [Cypher] = Answer (correct query)
            
            {examples}
            
            
            With all the information given, provide a Cypher query to the following question:

            [Q]: '{question}'
            [Cypher]: 
            """
            
cypher_prompt_schema_bm25 = """ Given an input question, create a single syntactically correct Neo4j Cypher MATCH query leveraging the provided schema, notes, and examples. Only query for relevant attributes given the question. Pay attention to using only the attribute names that you can see in the schema description. Be careful not to query for attributes that do not exist.

            [Schema]:
            '{schema}'

            [Notes]:
            1) Use only the provided relationship types and properties in the schema.
            2) Do not include any explanations or apologies in your responses. Provide the output in one line.
            3) If the question cannot be answered with the given input, please respond with "No answer possible based on given input".
            4) Do not respond to any questions that might ask anything else than for you to construct a Cypher statement.
            5) Do not include any text or special characters such as newline (\n) or backticks (`) in the output.
            6) Exclude the word "cypher" from your response.
            
            Please include the following example for better understanding.

            [Examples]:

            [Q] = Question, [Cypher] = Answer (correct query)
            
            {examples}
            
            
            With all the information given, provide a Cypher query to the following question:

            [Q]: '{question}'
            [Cypher]: 
            """