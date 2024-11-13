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

            [Q]:Which encounter is related to allergy Animal dander (substance)?
            [SPARQL]:PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX syn: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> PREFIX pl: <http://www.w3.org/1999/02/22-rdf-syntax-ns#PlainLiteral> SELECT DISTINCT ?description WHERE {{ ?allergy a syn:Allergy ; syn:description 'Animal dander (substance)'^^pl:; syn:encounterId ?encounterId. ?encounter a syn:Encounter; syn:id ?encounterId; syn:description ?description. }}

            [Q]:Provide the list of patients associated with the payer Dual Eligible.
            [SPARQL]:PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX syn: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> PREFIX pl: <http://www.w3.org/1999/02/22-rdf-syntax-ns#PlainLiteral> SELECT DISTINCT ?first ?last WHERE {{ ?payer a syn:Payer; syn:name 'Dual Eligible'^^pl:; syn:id ?id. ?payerTransition a syn:PayerTransition; syn:patientId ?patientid. ?patient a syn:Patient; syn:id ?patientid; syn:first ?first; syn:last ?last. }}

            [Q]:Give me the organization affiliated with the provider with the ID beff794b-089c-3098-9bed-5cc458acbc05.
            [SPARQL]:PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX syn: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> PREFIX uuid: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#urn:uuid> SELECT  ?name WHERE {{ ?provider a syn:Provider; syn:id 'beff794b-089c-3098-9bed-5cc458acbc05'^^uuid:; syn:organizationId ?organizationId. ?organization a syn:Organization; syn:id ?organization_id; syn:name ?name; }}

            [Q]:What is the base cost of medication with the code 205923.
            [SPARQL]:PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX syn: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> PREFIX ct:<https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#umls:RxNorm> SELECT DISTINCT ?baseCost WHERE {{ ?medication a syn:Medication; syn:code '205923'^^ct:; syn:baseCost ?baseCost; }}

            [Q]:What is the procedure code of the claim transaction 210ae4cd-7ca0-7da4-66a7-ef20b4f5db4d?
            [SPARQL]:PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX syn: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> PREFIX uuid: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#urn:uuid> SELECT  ?procedureCode WHERE {{ ?claimtransaction a syn:ClaimTransaction;syn:id '210ae4cd-7ca0-7da4-66a7-ef20b4f5db4d'^^uuid:; syn:procedureCode ?procedureCode.}}


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

            [Q]:Which encounter is related to allergy Animal dander (substance)?
            [SPARQL]:PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX syn: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> PREFIX pl: <http://www.w3.org/1999/02/22-rdf-syntax-ns#PlainLiteral> SELECT DISTINCT ?description WHERE {{ ?allergy a syn:Allergy ; syn:description 'Animal dander (substance)'^^pl:; syn:encounterId ?encounterId. ?encounter a syn:Encounter; syn:id ?encounterId; syn:description ?description. }}


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

            [Q]:Which encounter is related to allergy Animal dander (substance)?
            [SPARQL]:PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX syn: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> PREFIX pl: <http://www.w3.org/1999/02/22-rdf-syntax-ns#PlainLiteral> SELECT DISTINCT ?description WHERE {{ ?allergy a syn:Allergy ; syn:description 'Animal dander (substance)'^^pl:; syn:encounterId ?encounterId. ?encounter a syn:Encounter; syn:id ?encounterId; syn:description ?description. }}

            [Q]:Provide the list of patients associated with the payer Dual Eligible.
            [SPARQL]:PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX syn: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> PREFIX pl: <http://www.w3.org/1999/02/22-rdf-syntax-ns#PlainLiteral> SELECT DISTINCT ?first ?last WHERE {{ ?payer a syn:Payer; syn:name 'Dual Eligible'^^pl:; syn:id ?id. ?payerTransition a syn:PayerTransition; syn:patientId ?patientid. ?patient a syn:Patient; syn:id ?patientid; syn:first ?first; syn:last ?last. }}

            [Q]:Give me the organization affiliated with the provider with the ID beff794b-089c-3098-9bed-5cc458acbc05.
            [SPARQL]:PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX syn: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> PREFIX uuid: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#urn:uuid> SELECT  ?name WHERE {{ ?provider a syn:Provider; syn:id 'beff794b-089c-3098-9bed-5cc458acbc05'^^uuid:; syn:organizationId ?organizationId. ?organization a syn:Organization; syn:id ?organization_id; syn:name ?name; }}

            [Q]:What is the base cost of medication with the code 205923.
            [SPARQL]:PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX syn: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> PREFIX ct:<https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#umls:RxNorm> SELECT DISTINCT ?baseCost WHERE {{ ?medication a syn:Medication; syn:code '205923'^^ct:; syn:baseCost ?baseCost; }}

            [Q]:What is the procedure code of the claim transaction 210ae4cd-7ca0-7da4-66a7-ef20b4f5db4d?
            [SPARQL]:PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX syn: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> PREFIX uuid: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#urn:uuid> SELECT  ?procedureCode WHERE {{ ?claimtransaction a syn:ClaimTransaction;syn:id '210ae4cd-7ca0-7da4-66a7-ef20b4f5db4d'^^uuid:; syn:procedureCode ?procedureCode.}}


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

            [Q]:Which encounter is related to allergy Animal dander (substance)?
            [SPARQL]:PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX syn: <https://knacc.umbc.edu/dae-young/kim/ontologies/synthea#> PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> PREFIX pl: <http://www.w3.org/1999/02/22-rdf-syntax-ns#PlainLiteral> SELECT DISTINCT ?description WHERE {{ ?allergy a syn:Allergy ; syn:description 'Animal dander (substance)'^^pl:; syn:encounterId ?encounterId. ?encounter a syn:Encounter; syn:id ?encounterId; syn:description ?description. }}


            With all the information given, provide a SPARQL query to the following question:

            [Q]: '{question}'
            [SPARQL]: 
            """