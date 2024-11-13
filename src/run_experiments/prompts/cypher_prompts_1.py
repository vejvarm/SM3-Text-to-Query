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

            [Q]: Which encounter is related to allergy Animal dander (substance)?
            [Cypher]: MATCH (e:Encounter)-[:HAS_DIAGNOSED]->(a:Allergy {{description: 'Animal dander (substance)'}}) RETURN DISTINCT e.description;

            [Q] :Provide the list of patients associated with the payer Dual Eligible.
            [Cypher] :MATCH (p:Patient)-[:INSURANCE_START]->(py:Payer {{name: 'Dual Eligible'}}) RETURN DISTINCT p.firstName, p.lastName;

            [Q]: Give me the organization affiliated with the provider with the ID beff794b-089c-3098-9bed-5cc458acbc05.
            [Cypher]: MATCH (o:Organization)-[:IS_PERFORMED_AT]->(p:Provider {{id: 'beff794b-089c-3098-9bed-5cc458acbc05'}}) RETURN o.name;

            [Q]: What is the base cost of medication with the code 205923.
            [Cypher]: MATCH (m:Medication {{code: '205923'}}) RETURN m.baseCost;

            [Q]: What is the procedure code of the claim transaction 210ae4cd-7ca0-7da4-66a7-ef20b4f5db4d?
            [Cypher]: MATCH (ct:ClaimTransaction {{id: '210ae4cd-7ca0-7da4-66a7-ef20b4f5db4d'}}) RETURN ct.procedureCode;
            
            
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

            [Example]:

            [Q] = Question, [Cypher] = Answer (correct query)

            [Q]: Which encounter is related to allergy Animal dander (substance)?
            [Cypher]: MATCH (e:Encounter)-[:HAS_DIAGNOSED]->(a:Allergy {{description: 'Animal dander (substance)'}}) RETURN DISTINCT e.description;


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

            [Q]: Which encounter is related to allergy Animal dander (substance)?
            [Cypher]: MATCH (e:Encounter)-[:HAS_DIAGNOSED]->(a:Allergy {{description: 'Animal dander (substance)'}}) RETURN DISTINCT e.description;

            [Q] :Provide the list of patients associated with the payer Dual Eligible.
            [Cypher] :MATCH (p:Patient)-[:INSURANCE_START]->(py:Payer {{name: 'Dual Eligible'}}) RETURN DISTINCT p.firstName, p.lastName;

            [Q]: Give me the organization affiliated with the provider with the ID beff794b-089c-3098-9bed-5cc458acbc05.
            [Cypher]: MATCH (o:Organization)-[:IS_PERFORMED_AT]->(p:Provider {{id: 'beff794b-089c-3098-9bed-5cc458acbc05'}}) RETURN o.name;

            [Q]: What is the base cost of medication with the code 205923.
            [Cypher]: MATCH (m:Medication {{code: '205923'}}) RETURN m.baseCost;

            [Q]: What is the procedure code of the claim transaction 210ae4cd-7ca0-7da4-66a7-ef20b4f5db4d?
            [Cypher]: MATCH (ct:ClaimTransaction {{id: '210ae4cd-7ca0-7da4-66a7-ef20b4f5db4d'}}) RETURN ct.procedureCode;


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

            [Q]: Which encounter is related to allergy Animal dander (substance)?
            [Cypher]: MATCH (e:Encounter)-[:HAS_DIAGNOSED]->(a:Allergy {{description: 'Animal dander (substance)'}}) RETURN DISTINCT e.description;


            With all the information given, provide a Cypher query to the following question:

            [Q]: '{question}'
            [Cypher]: 
            """