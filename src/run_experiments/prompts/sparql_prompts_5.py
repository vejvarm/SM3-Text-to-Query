sparql_prompt_schema_0shot = """ Given an input question create a syntactically correct SPARQL query leveraging the provided ontology and notes. Only query relevant attributes given the question. Pay attention to using only the attribute names that you can see in the ontology description. Be careful not to query for attributes that do not exist.

            [Ontology]:
            '{schema}'

            [Notes]:
            1) Use only the classes and properties provided in the ontology to construct the SPARQL query.
            2) Do not include any explanations or apologies in your responses.
            3) Do not include any text or special characters such as newline (\n) or backticks (`) or (*) in the output.
            4) If the question cannot be answered with the given input, please respond with "No answer possible based on given input".
            5) Include all necessary prefixes. 
            6) There are some newly added prefixes that are not in the ontology. Use these shortcuts instead of the full links:
                PREFIX pl: <http://www.w3.org/1999/02/22-rdf-syntax-ns#PlainLiteral>
                PREFIX snomed: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#snomed:SNOMED-CT>
                PREFIX uuid: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#urn:uuid>
                PREFIX cvx: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#hl7:CVX>
                PREFIX udi: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#fda:UDI>
                PREFIX ct:<https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#umls:RxNorm>
                PREFIX loinc: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#loinc:LOINC>
            The defined prefixes are used to shorten long URI links in SPARQL queries and improve the readability of the query. 
            Instead of using the full URI links in the query, you can use the defined prefixes to express the same meaning. For example, snomed: is used as a prefix for https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#snomed:SNOMED-CT to avoid using the full link.

            [Q] = Question, [SPARQL] = Answer (correct query)


            With all the information given, provide a SPARQL query to the following question:

            [Q]: '{question}'
            [SPARQL]: 
            """
sparql_prompt_0schema_fewshots = """ Given an input question create a syntactically correct SPARQL query leveraging the provided notes and examples. Only query relevant attributes given the question. Be careful not to query for attributes that do not exist.

            [Notes]:
            1) Do not include any explanations or apologies in your responses.
            2) Do not include any text or special characters such as newline (\n) or backticks (`) or (*) in the output.
            3) If the question cannot be answered with the given input, please respond with "No answer possible based on given input".
            4) Include all necessary prefixes. 
            5) Use these shortcuts instead of the full links:
                PREFIX pl: <http://www.w3.org/1999/02/22-rdf-syntax-ns#PlainLiteral>
                PREFIX snomed: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#snomed:SNOMED-CT>
                PREFIX uuid: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#urn:uuid>
                PREFIX cvx: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#hl7:CVX>
                PREFIX udi: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#fda:UDI>
                PREFIX ct:<https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#umls:RxNorm>
                PREFIX loinc: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#loinc:LOINC>
            The defined prefixes are used to shorten long URI links in SPARQL queries and improve the readability of the query. 
            Instead of using the full URI links in the query, you can use the defined prefixes to express the same meaning. For example, snomed: is used as a prefix for https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#snomed:SNOMED-CT to avoid using the full link.

            Please include the following examples for better understanding.

            [Examples]:

            [Q] = Question, [SPARQL] = Answer (correct query)

            [Q]: What is the city of residence of the patient named Eugene421 Fisher429?
            [SPARQL]: PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX syn: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> PREFIX pl: <http://www.w3.org/1999/02/22-rdf-syntax-ns#PlainLiteral> SELECT ?city WHERE {{ ?patient a syn:Patient ; syn:first 'Eugene421'^^pl:; syn:last 'Fisher429'^^pl:; syn:city ?city }}

            [Q]: What is the first name of the patient with the ID efa523f2-6ac2-641c-58f3-2ca1b97543f9?
            [SPARQL]: PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX syn: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> PREFIX uuid: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#urn:uuid> SELECT ?first WHERE {{ ?patient a syn:Patient ; syn:id 'efa523f2-6ac2-641c-58f3-2ca1b97543f9'^^uuid:; syn:first ?first }}

            [Q]: How many procedures are uncovered by the payer with the ID 26aab0cd-6aba-3e1b-ac5b-05c8867e762c?
            [SPARQL]: PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX syn: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> PREFIX uuid: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#urn:uuid> SELECT ?uncoveredProcedures WHERE {{ ?payer a syn:Payer; syn:id '26aab0cd-6aba-3e1b-ac5b-05c8867e762c'^^uuid:; syn:uncoveredProcedures ?uncoveredProcedures. }}

            [Q]: Please provide me the encounters that are related to the condition with code 424393004.
            [SPARQL]: PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX syn: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> PREFIX snomed: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#snomed:SNOMED-CT> SELECT DISTINCT ?description WHERE {{ ?condition a syn:Condition; syn:code '424393004'^^snomed:; syn:encounterId ?encounterid. ?encounter a syn:Encounter; syn:id ?encounterid; syn:description ?description }}

            [Q]: Please provide me the name of the provider associated with the encounter 76956a25-b2fe-4a8d-34b8-6baa62656a24.
            [SPARQL]: PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX syn: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> PREFIX uuid: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#urn:uuid> SELECT ?payername WHERE {{ ?Encounter a syn:Encounter; syn:id '76956a25-b2fe-4a8d-34b8-6baa62656a24'^^uuid:; syn:payerId ?payerId. ?Provider a syn:Provider; syn:id ?payerId; syn:name ?payername. }}


            With all the information given, provide a SPARQL query to the following question:

            [Q]: '{question}'
            [SPARQL]: 
            """
sparql_prompt_0schema_oneshot = """ Given an input question create a syntactically correct SPARQL query leveraging the provided notes and examples. Only query relevant attributes given the question. Be careful not to query for attributes that do not exist.

            [Notes]:
            1) Do not include any explanations or apologies in your responses.
            2) Do not include any text or special characters such as newline (\n) or backticks (`) or (*) in the output.
            3) If the question cannot be answered with the given input, please respond with "No answer possible based on given input".
            4) Include all necessary prefixes. 
            5) Use these shortcuts instead of the full links:
                PREFIX pl: <http://www.w3.org/1999/02/22-rdf-syntax-ns#PlainLiteral>
                PREFIX snomed: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#snomed:SNOMED-CT>
                PREFIX uuid: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#urn:uuid>
                PREFIX cvx: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#hl7:CVX>
                PREFIX udi: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#fda:UDI>
                PREFIX ct:<https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#umls:RxNorm>
                PREFIX loinc: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#loinc:LOINC>
            The defined prefixes are used to shorten long URI links in SPARQL queries and improve the readability of the query. 
            Instead of using the full URI links in the query, you can use the defined prefixes to express the same meaning. For example, snomed: is used as a prefix for https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#snomed:SNOMED-CT to avoid using the full link.

            Please include the following examples for better understanding.

            [Examples]:

            [Q] = Question, [SPARQL] = Answer (correct query)

            [Q]: What is the city of residence of the patient named Eugene421 Fisher429?
            [SPARQL]: PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX syn: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> PREFIX pl: <http://www.w3.org/1999/02/22-rdf-syntax-ns#PlainLiteral> SELECT ?city WHERE {{ ?patient a syn:Patient ; syn:first 'Eugene421'^^pl:; syn:last 'Fisher429'^^pl:; syn:city ?city }}


            With all the information given, provide a SPARQL query to the following question:

            [Q]: '{question}'
            [SPARQL]: 
            """
sparql_prompt_schema_fewshots = """ Given an input question create a syntactically correct SPARQL query leveraging the provided ontology, notes, and examples. Only query relevant attributes given the question. Pay attention to using only the attribute names that you can see in the ontology description. Be careful not to query for attributes that do not exist.

            [Ontology]:
            '{schema}'

            [Notes]:
            1) Use only the classes and properties provided in the ontology to construct the SPARQL query.
            2) Do not include any explanations or apologies in your responses.
            3) Do not include any text or special characters such as newline (\n) or backticks (`) or (*) in the output.
            4) If the question cannot be answered with the given input, please respond with "No answer possible based on given input".
            5) Include all necessary prefixes. 
            6) There are some newly added prefixes that are not in the ontology. Use these shortcuts instead of the full links:
                PREFIX pl: <http://www.w3.org/1999/02/22-rdf-syntax-ns#PlainLiteral>
                PREFIX snomed: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#snomed:SNOMED-CT>
                PREFIX uuid: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#urn:uuid>
                PREFIX cvx: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#hl7:CVX>
                PREFIX udi: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#fda:UDI>
                PREFIX ct:<https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#umls:RxNorm>
                PREFIX loinc: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#loinc:LOINC>
            The defined prefixes are used to shorten long URI links in SPARQL queries and improve the readability of the query. 
            Instead of using the full URI links in the query, you can use the defined prefixes to express the same meaning. For example, snomed: is used as a prefix for https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#snomed:SNOMED-CT to avoid using the full link.


            Please include the following examples for better understanding.

            [Examples]:

            [Q] = Question, [SPARQL] = Answer (correct query)

            [Q]: What is the city of residence of the patient named Eugene421 Fisher429?
            [SPARQL]: PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX syn: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> PREFIX pl: <http://www.w3.org/1999/02/22-rdf-syntax-ns#PlainLiteral> SELECT ?city WHERE {{ ?patient a syn:Patient ; syn:first 'Eugene421'^^pl:; syn:last 'Fisher429'^^pl:; syn:city ?city }}

            [Q]: What is the first name of the patient with the ID efa523f2-6ac2-641c-58f3-2ca1b97543f9?
            [SPARQL]: PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX syn: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> PREFIX uuid: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#urn:uuid> SELECT ?first WHERE {{ ?patient a syn:Patient ; syn:id 'efa523f2-6ac2-641c-58f3-2ca1b97543f9'^^uuid:; syn:first ?first }}

            [Q]: How many procedures are uncovered by the payer with the ID 26aab0cd-6aba-3e1b-ac5b-05c8867e762c?
            [SPARQL]: PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX syn: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> PREFIX uuid: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#urn:uuid> SELECT ?uncoveredProcedures WHERE {{ ?payer a syn:Payer; syn:id '26aab0cd-6aba-3e1b-ac5b-05c8867e762c'^^uuid:; syn:uncoveredProcedures ?uncoveredProcedures. }}

            [Q]: Please provide me the encounters that are related to the condition with code 424393004.
            [SPARQL]: PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX syn: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> PREFIX snomed: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#snomed:SNOMED-CT> SELECT DISTINCT ?description WHERE {{ ?condition a syn:Condition; syn:code '424393004'^^snomed:; syn:encounterId ?encounterid. ?encounter a syn:Encounter; syn:id ?encounterid; syn:description ?description }}

            [Q]: Please provide me the name of the provider associated with the encounter 76956a25-b2fe-4a8d-34b8-6baa62656a24.
            [SPARQL]: PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX syn: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> PREFIX uuid: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#urn:uuid> SELECT ?payername WHERE {{ ?Encounter a syn:Encounter; syn:id '76956a25-b2fe-4a8d-34b8-6baa62656a24'^^uuid:; syn:payerId ?payerId. ?Provider a syn:Provider; syn:id ?payerId; syn:name ?payername. }}


            With all the information given, provide a SPARQL query to the following question:

            [Q]: '{question}'
            [SPARQL]: 
            """
sparql_prompt_schema_oneshot = """ Given an input question create a syntactically correct SPARQL query leveraging the provided ontology, notes, and examples. Only query relevant attributes given the question. Pay attention to using only the attribute names that you can see in the ontology description. Be careful not to query for attributes that do not exist.

            [Ontology]:
            '{schema}'

            [Notes]:
            1) Use only the classes and properties provided in the ontology to construct the SPARQL query.
            2) Do not include any explanations or apologies in your responses.
            3) Do not include any text or special characters such as newline (\n) or backticks (`) or (*) in the output.
            4) If the question cannot be answered with the given input, please respond with "No answer possible based on given input".
            5) Include all necessary prefixes. 
            6) There are some newly added prefixes that are not in the ontology. Use these shortcuts instead of the full links:
                PREFIX pl: <http://www.w3.org/1999/02/22-rdf-syntax-ns#PlainLiteral>
                PREFIX snomed: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#snomed:SNOMED-CT>
                PREFIX uuid: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#urn:uuid>
                PREFIX cvx: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#hl7:CVX>
                PREFIX udi: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#fda:UDI>
                PREFIX ct:<https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#umls:RxNorm>
                PREFIX loinc: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#loinc:LOINC>
            The defined prefixes are used to shorten long URI links in SPARQL queries and improve the readability of the query. 
            Instead of using the full URI links in the query, you can use the defined prefixes to express the same meaning. For example, snomed: is used as a prefix for https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#snomed:SNOMED-CT to avoid using the full link.


            Please include the following examples for better understanding.

            [Examples]:

            [Q] = Question, [SPARQL] = Answer (correct query)

            [Q]: What is the city of residence of the patient named Eugene421 Fisher429?
            [SPARQL]: PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX syn: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> PREFIX pl: <http://www.w3.org/1999/02/22-rdf-syntax-ns#PlainLiteral> SELECT ?city WHERE {{ ?patient a syn:Patient ; syn:first 'Eugene421'^^pl:; syn:last 'Fisher429'^^pl:; syn:city ?city }}


            With all the information given, provide a SPARQL query to the following question:

            [Q]: '{question}'
            [SPARQL]: 
            """

sparql_prompt_0schema_bm25 = """ Given an input question create a syntactically correct SPARQL query leveraging the provided notes and examples. Only query relevant attributes given the question. Be careful not to query for attributes that do not exist.

            [Notes]:
            1) Do not include any explanations or apologies in your responses.
            2) Do not include any text or special characters such as newline (\n) or backticks (`) or (*) in the output.
            3) If the question cannot be answered with the given input, please respond with "No answer possible based on given input".
            4) Include all necessary prefixes. 
            5) Use these shortcuts instead of the full links:
                PREFIX pl: <http://www.w3.org/1999/02/22-rdf-syntax-ns#PlainLiteral>
                PREFIX snomed: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#snomed:SNOMED-CT>
                PREFIX uuid: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#urn:uuid>
                PREFIX cvx: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#hl7:CVX>
                PREFIX udi: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#fda:UDI>
                PREFIX ct:<https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#umls:RxNorm>
                PREFIX loinc: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#loinc:LOINC>
            The defined prefixes are used to shorten long URI links in SPARQL queries and improve the readability of the query. 
            Instead of using the full URI links in the query, you can use the defined prefixes to express the same meaning. For example, snomed: is used as a prefix for https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#snomed:SNOMED-CT to avoid using the full link.


            Please include the following examples for better understanding.

            [Examples]:

            [Q] = Question, [SPARQL] = Answer (correct query)

            {examples}


            With all the information given, provide a SPARQL query to the following question:

            [Q]: '{question}'
            [SPARQL]: 
            """

sparql_prompt_schema_bm25 = """ Given an input question create a syntactically correct SPARQL query leveraging the provided ontology, notes, and examples. Only query relevant attributes given the question. Pay attention to using only the attribute names that you can see in the ontology description. Be careful not to query for attributes that do not exist.

            [Ontology]:
            '{schema}'

            [Notes]:
            1) Use only the classes and properties provided in the ontology to construct the SPARQL query.
            2) Do not include any explanations or apologies in your responses.
            3) Do not include any text or special characters such as newline (\n) or backticks (`) or (*) in the output.
            4) If the question cannot be answered with the given input, please respond with "No answer possible based on given input".
            5) Include all necessary prefixes. 
            6) There are some newly added prefixes that are not in the ontology. Use these shortcuts instead of the full links:
                PREFIX pl: <http://www.w3.org/1999/02/22-rdf-syntax-ns#PlainLiteral>
                PREFIX snomed: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#snomed:SNOMED-CT>
                PREFIX uuid: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#urn:uuid>
                PREFIX cvx: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#hl7:CVX>
                PREFIX udi: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#fda:UDI>
                PREFIX ct:<https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#umls:RxNorm>
                PREFIX loinc: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#loinc:LOINC>
            The defined prefixes are used to shorten long URI links in SPARQL queries and improve the readability of the query. 
            Instead of using the full URI links in the query, you can use the defined prefixes to express the same meaning. For example, snomed: is used as a prefix for https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#snomed:SNOMED-CT to avoid using the full link.


            Please include the following examples for better understanding.

            [Examples]:

            [Q] = Question, [SPARQL] = Answer (correct query)

            {examples}


            With all the information given, provide a SPARQL query to the following question:

            [Q]: '{question}'
            [SPARQL]: 
            """