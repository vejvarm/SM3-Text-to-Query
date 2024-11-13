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

            [Q]: Please provide me the patients with the claim ID 25382c93-4b35-d58c-d519-2f50343b3626.
            [Cypher]: MATCH (p:Patient)-[:HAS_CLAIM]->(c:Claim {{id: '25382c93-4b35-d58c-d519-2f50343b3626'}}) RETURN DISTINCT p.firstName,p.lastName;

            [Q]: Please provide me a reason for the use of the care plan with code 734163000.
            [Cypher]: MATCH (c:CarePlan {{code: '734163000'}}) RETURN c.reasondescription;

            [Q]: Please provide me the quality for the supply with the code 1137596000.
            [Cypher]: MATCH (s:Supply {{code: '1137596000'}}) RETURN DISTINCT s.quantity; 	

            [Q]: What is the SNOMED code for the allergy described as Eggs (edible) (substance)?
            [Cypher]: MATCH (a:Allergy {{description: 'Eggs (edible) (substance)'}})RETURN DISTINCT a.code;

            [Q]: What is the department id of the claim with the ID 2bfc5ac8-bf25-4845-f673-c6f6bc344034?
            [Cypher]: MATCH (c:Claim {{id: '2bfc5ac8-bf25-4845-f673-c6f6bc344034'}}) RETURN c.departmentId; 	


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

            [Q]: Please provide me the patients with the claim ID 25382c93-4b35-d58c-d519-2f50343b3626.
            [Cypher]: MATCH (p:Patient)-[:HAS_CLAIM]->(c:Claim {{id: '25382c93-4b35-d58c-d519-2f50343b3626'}}) RETURN DISTINCT p.firstName,p.lastName;


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

            [Q]: Please provide me the patients with the claim ID 25382c93-4b35-d58c-d519-2f50343b3626.
            [Cypher]: MATCH (p:Patient)-[:HAS_CLAIM]->(c:Claim {{id: '25382c93-4b35-d58c-d519-2f50343b3626'}}) RETURN DISTINCT p.firstName,p.lastName;

            [Q]: Please provide me a reason for the use of the care plan with code 734163000.
            [Cypher]: MATCH (c:CarePlan {{code: '734163000'}}) RETURN c.reasondescription;

            [Q]: Please provide me the quality for the supply with the code 1137596000.
            [Cypher]: MATCH (s:Supply {{code: '1137596000'}}) RETURN DISTINCT s.quantity; 	

            [Q]: What is the SNOMED code for the allergy described as Eggs (edible) (substance)?
            [Cypher]: MATCH (a:Allergy {{description: 'Eggs (edible) (substance)'}})RETURN DISTINCT a.code;

            [Q]: What is the department id of the claim with the ID 2bfc5ac8-bf25-4845-f673-c6f6bc344034?
            [Cypher]: MATCH (c:Claim {{id: '2bfc5ac8-bf25-4845-f673-c6f6bc344034'}}) RETURN c.departmentId; 


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

            [Q]: Please provide me the patients with the claim ID 25382c93-4b35-d58c-d519-2f50343b3626.
            [Cypher]: MATCH (p:Patient)-[:HAS_CLAIM]->(c:Claim {{id: '25382c93-4b35-d58c-d519-2f50343b3626'}}) RETURN DISTINCT p.firstName,p.lastName;


            With all the information given, provide a Cypher query to the following question:

            [Q]: '{question}'
            [Cypher]: 
            """