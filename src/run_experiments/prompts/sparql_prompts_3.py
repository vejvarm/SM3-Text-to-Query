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

            [Q]: In what type of allergy does the description House dust mite (organism) fall?
            [SPARQL]: PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX syn: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> PREFIX pl: <http://www.w3.org/1999/02/22-rdf-syntax-ns#PlainLiteral> SELECT DISTINCT ?type WHERE {{ ?allergy a syn:Allergy ; syn:description 'House dust mite (organism)'^^pl:; syn:type ?type; }}

            [Q]: Please provide me the patients with the claim ID 56a60caf-14fc-db17-e331-65b4e8dcf942.
            [SPARQL]: PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX syn: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> PREFIX uuid: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#urn:uuid> SELECT DISTINCT ?first ?last WHERE {{ ?claim a syn:Claim;syn:id '56a60caf-14fc-db17-e331-65b4e8dcf942'^^uuid:; syn:patientId ?patientId. ?patient a syn:Patient; syn:id ?patientId; syn:first ?first; syn:last ?last.}}

            [Q]: What encounter is associated with the supply named Disposable air-purifying respirator (physical object)?
            [SPARQL]: PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX syn: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> PREFIX pl: <http://www.w3.org/1999/02/22-rdf-syntax-ns#PlainLiteral> SELECT DISTINCT ?description WHERE {{ ?supply a syn:Supply; syn:description 'Disposable air-purifying respirator (physical object)'^^pl:; syn:encounterId ?encounterid. ?encounter a syn:Encounter; syn:id ?encounterid; syn:description ?description.}}

            [Q]: What is the description of encounter 2377dc28-54be-b1a0-407f-2fcd515cf588?
            [SPARQL]: PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX syn: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> PREFIX uuid: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#urn:uuid> SELECT ?description WHERE {{ ?encounter a syn:Encounter; syn:id '2377dc28-54be-b1a0-407f-2fcd515cf588'^^uuid:; syn:description ?description. }}

            [Q]: Who are the patients associated with the device Home continuous positive airway pressure unit (physical object)?
            [SPARQL]: PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX syn: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> PREFIX pl: <http://www.w3.org/1999/02/22-rdf-syntax-ns#PlainLiteral> SELECT DISTINCT ?first ?last WHERE {{ ?device a syn:Device; syn:description 'Home continuous positive airway pressure unit (physical object)'^^pl:; syn:patientId ?patientid. ?patient a syn:Patient; syn:id ?patientid; syn:first ?first; syn:last ?last. }}


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

            [Q]: In what type of allergy does the description House dust mite (organism) fall?
            [SPARQL]: PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX syn: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> PREFIX pl: <http://www.w3.org/1999/02/22-rdf-syntax-ns#PlainLiteral> SELECT DISTINCT ?type WHERE {{ ?allergy a syn:Allergy ; syn:description 'House dust mite (organism)'^^pl:; syn:type ?type; }}


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

            [Q]: In what type of allergy does the description House dust mite (organism) fall?
            [SPARQL]: PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX syn: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> PREFIX pl: <http://www.w3.org/1999/02/22-rdf-syntax-ns#PlainLiteral> SELECT DISTINCT ?type WHERE {{ ?allergy a syn:Allergy ; syn:description 'House dust mite (organism)'^^pl:; syn:type ?type; }}

            [Q]: Please provide me the patients with the claim ID 56a60caf-14fc-db17-e331-65b4e8dcf942.
            [SPARQL]: PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX syn: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> PREFIX uuid: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#urn:uuid> SELECT DISTINCT ?first ?last WHERE {{ ?claim a syn:Claim;syn:id '56a60caf-14fc-db17-e331-65b4e8dcf942'^^uuid:; syn:patientId ?patientId. ?patient a syn:Patient; syn:id ?patientId; syn:first ?first; syn:last ?last.}}

            [Q]: What encounter is associated with the supply named Disposable air-purifying respirator (physical object)?
            [SPARQL]: PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX syn: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> PREFIX pl: <http://www.w3.org/1999/02/22-rdf-syntax-ns#PlainLiteral> SELECT DISTINCT ?description WHERE {{ ?supply a syn:Supply; syn:description 'Disposable air-purifying respirator (physical object)'^^pl:; syn:encounterId ?encounterid. ?encounter a syn:Encounter; syn:id ?encounterid; syn:description ?description.}}

            [Q]: What is the description of encounter 2377dc28-54be-b1a0-407f-2fcd515cf588?
            [SPARQL]: PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX syn: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> PREFIX uuid: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#urn:uuid> SELECT ?description WHERE {{ ?encounter a syn:Encounter; syn:id '2377dc28-54be-b1a0-407f-2fcd515cf588'^^uuid:; syn:description ?description. }}

            [Q]: Who are the patients associated with the device Home continuous positive airway pressure unit (physical object)?
            [SPARQL]: PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX syn: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> PREFIX pl: <http://www.w3.org/1999/02/22-rdf-syntax-ns#PlainLiteral> SELECT DISTINCT ?first ?last WHERE {{ ?device a syn:Device; syn:description 'Home continuous positive airway pressure unit (physical object)'^^pl:; syn:patientId ?patientid. ?patient a syn:Patient; syn:id ?patientid; syn:first ?first; syn:last ?last. }}


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

            [Q]: In what type of allergy does the description House dust mite (organism) fall?
            [SPARQL]: PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX syn: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> PREFIX pl: <http://www.w3.org/1999/02/22-rdf-syntax-ns#PlainLiteral> SELECT DISTINCT ?type WHERE {{ ?allergy a syn:Allergy ; syn:description 'House dust mite (organism)'^^pl:; syn:type ?type; }}


            With all the information given, provide a SPARQL query to the following question:

            [Q]: '{question}'
            [SPARQL]: 
            """