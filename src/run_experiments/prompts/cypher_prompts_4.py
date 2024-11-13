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

            [Q]: What is the start date of the procedure Urine protein test?
            [Cypher]: MATCH (p:Procedure {{description: 'Urine protein test'}}) RETURN p.start;

            [Q] : What is the start date of the condition Part-time employment (finding)?
            [Cypher]: MATCH (c:Condition {{description: 'Part-time employment (finding)'}}) RETURN c.start;

            [Q]: What encounter is required during the use of the device with code 272265001?
            [Cypher]: MATCH (e:Encounter)-[:HAS_ORDERED]->(d:Device {{code: '272265001'}}) RETURN DISTINCT e.description;

            [Q]: How many immunizations are covered by the payer Dual Eligible?
            [Cypher]: MATCH (p:Payer {{name: 'Dual Eligible'}}) RETURN p.covered_immunizations;

            [Q]: Please provide me patients with the observation Tobacco smoking status.
            [Cypher]: MATCH (p:Patient)-[:HAS_HISTORY_OF]->(o:Observation {{description: 'Tobacco smoking status'}}) RETURN DISTINCT p.firstName, p.lastName;


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

            [Q]: What is the start date of the procedure Urine protein test?
            [Cypher]: MATCH (p:Procedure {{description: 'Urine protein test'}}) RETURN p.start;	


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

            [Q]: What is the start date of the procedure Urine protein test?
            [Cypher]: MATCH (p:Procedure {{description: 'Urine protein test'}}) RETURN p.start;

            [Q] : What is the start date of the condition Part-time employment (finding)?
            [Cypher]: MATCH (c:Condition {{description: 'Part-time employment (finding)'}}) RETURN c.start;

            [Q]: What encounter is required during the use of the device with code 272265001?
            [Cypher]: MATCH (e:Encounter)-[:HAS_ORDERED]->(d:Device {{code: '272265001'}}) RETURN DISTINCT e.description;

            [Q]: How many immunizations are covered by the payer Dual Eligible?
            [Cypher]: MATCH (p:Payer {{name: 'Dual Eligible'}}) RETURN p.covered_immunizations;

            [Q]: Please provide me patients with the observation Tobacco smoking status.
            [Cypher]: MATCH (p:Patient)-[:HAS_HISTORY_OF]->(o:Observation {{description: 'Tobacco smoking status'}}) RETURN DISTINCT p.firstName, p.lastName;


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

            [Q]: What is the start date of the procedure Urine protein test?
            [Cypher]: MATCH (p:Procedure {{description: 'Urine protein test'}}) RETURN p.start;	


            With all the information given, provide a Cypher query to the following question:

            [Q]: '{question}'
            [Cypher]: 
            """