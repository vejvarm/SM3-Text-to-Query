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

            [Q]: In what type of allergy does the description House dust mite (organism) fall?
            [Cypher]: MATCH (a:Allergy {{description: 'House dust mite (organism)'}})RETURN DISTINCT a.type; 	

            [Q] : Please provide me the patients with the claim ID 56a60caf-14fc-db17-e331-65b4e8dcf942.
            [Cypher]: MATCH (p:Patient)-[:HAS_CLAIM]->(c:Claim {{id: '56a60caf-14fc-db17-e331-65b4e8dcf942'}}) RETURN DISTINCT p.firstName,p.lastName;

            [Q]: What encounter is associated with the supply named Disposable air-purifying respirator (physical object)?
            [Cypher]: MATCH (e:Encounter)-[:HAS_ORDERED]->(s:Supply {{description: 'Disposable air-purifying respirator (physical object)'}}) RETURN DISTINCT e.description;

            [Q]: What is the description of encounter 2377dc28-54be-b1a0-407f-2fcd515cf588?
            [Cypher]: MATCH (e:Encounter {{id: '2377dc28-54be-b1a0-407f-2fcd515cf588'}}) RETURN e.description; 	

            [Q]: Who are the patients associated with the device Home continuous positive airway pressure unit (physical object)?
            [Cypher]: MATCH (p:Patient)-[:IS_MEASURED_BY]->(d:Device {{description: 'Home continuous positive airway pressure unit (physical object)'}}) RETURN DISTINCT p.firstName, p.lastName; 	


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

            [Q]: In what type of allergy does the description House dust mite (organism) fall?
            [Cypher]: MATCH (a:Allergy {{description: 'House dust mite (organism)'}})RETURN DISTINCT a.type; 	


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

            [Q]: In what type of allergy does the description House dust mite (organism) fall?
            [Cypher]: MATCH (a:Allergy {{description: 'House dust mite (organism)'}})RETURN DISTINCT a.type; 	

            [Q] : Please provide me the patients with the claim ID 56a60caf-14fc-db17-e331-65b4e8dcf942.
            [Cypher]: MATCH (p:Patient)-[:HAS_CLAIM]->(c:Claim {{id: '56a60caf-14fc-db17-e331-65b4e8dcf942'}}) RETURN DISTINCT p.firstName,p.lastName;

            [Q]: What encounter is associated with the supply named Disposable air-purifying respirator (physical object)?
            [Cypher]: MATCH (e:Encounter)-[:HAS_ORDERED]->(s:Supply {{description: 'Disposable air-purifying respirator (physical object)'}}) RETURN DISTINCT e.description;

            [Q]: What is the description of encounter 2377dc28-54be-b1a0-407f-2fcd515cf588?
            [Cypher]: MATCH (e:Encounter {{id: '2377dc28-54be-b1a0-407f-2fcd515cf588'}}) RETURN e.description; 	

            [Q]: Who are the patients associated with the device Home continuous positive airway pressure unit (physical object)?
            [Cypher]: MATCH (p:Patient)-[:IS_MEASURED_BY]->(d:Device {{description: 'Home continuous positive airway pressure unit (physical object)'}}) RETURN DISTINCT p.firstName, p.lastName; 	


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

            [Q]: In what type of allergy does the description House dust mite (organism) fall?
            [Cypher]: MATCH (a:Allergy {{description: 'House dust mite (organism)'}})RETURN DISTINCT a.type; 	


            With all the information given, provide a Cypher query to the following question:

            [Q]: '{question}'
            [Cypher]: 
            """