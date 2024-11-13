###Prompts
mql_prompt_schema_fewshots = """ Given an input question, create a single syntactically correct MongoDB query leveraging the provided schema, notes, and examples. Only query for relevant fields given the question. Pay attention to using only the field names that you can see in the schema description. Be careful not to query for fields that do not exist.

            [Schema]:
            '{schema}'

            [Notes]:
            1) Use only the provided document collections in the schema.
            2) Use the collection fields that are explicitly mentioned in the question.
            3) Do not include any explanations or apologies in your responses. Provide the output in one line.
            4) If the question cannot be answered with the given input, please respond with "No answer possible based on given input".
            5) Pay attention to the group key that is used for the $group operator when needed.
            6) Pay attention to the fields that are used in the find() operator.
            7) Pay attention to add quotes where needed such as for strings.
            8) The "_id" field is only used as internal MomgoDB ObjectID and not as the domain specific ID of the objects in the collections. The objects are identified with a UUID in fields following a structure like PATIENT_ID, TRANSACTION_ID, CLAIM_ID...
            
            Please include the following examples for better understanding.

            [Examples]:

            [Q] = Question, [MongoDB] = Answer (correct query)

            [Q]: What is the city of residence of the patient named Eugene421 Fisher429?
            [MongoDB]: db.patients.find({ "FIRST": "Eugene421", "LAST": "Fisher429" }, { "_id": 0, "CITY": 1 })

            [Q]: What is the first name of the patient with the ID efa523f2-6ac2-641c-58f3-2ca1b97543f9?
            [MongoDB]: db.patients.find({ "PATIENT_ID": "efa523f2-6ac2-641c-58f3-2ca1b97543f9" }, { _id: 0, FIRST: 1 })

            [Q]: How many procedures are uncovered by the payer with the ID 26aab0cd-6aba-3e1b-ac5b-05c8867e762c?
            [MongoDB]: db.payers.find({ "PAYER_ID": "26aab0cd-6aba-3e1b-ac5b-05c8867e762c" }, { _id: 0, UNCOVERED_PROCEDURES: 1 })

            [Q]: Please provide me the encounters that are related to the condition with code 424393004.
            [MongoDB]: db.patients.aggregate([ {  $unwind:"ENCOUNTERS" }, {  $unwind:"ENCOUNTERS.CONDITIONS" }, { $match: { "ENCOUNTERS.CONDITIONS.CODE": 424393004 } }, { $project: { _id: 0, description: "$ENCOUNTERS.DESCRIPTION" } }, { $group: { _id: "$description" } }, { $project: { _id: 0, description: "$_id" } }]);
            
            [Q]: Please provide me the name of the provider associated with the encounter 76956a25-b2fe-4a8d-34b8-6baa62656a24.
            [MongoDB]: db.patients.aggregate([ { $match: { "ENCOUNTERS.ENCOUNTER_ID": "76956a25-b2fe-4a8d-34b8-6baa62656a24" } }, {  $unwind:"ENCOUNTERS" }, { $match: { "ENCOUNTERS.ENCOUNTER_ID": "76956a25-b2fe-4a8d-34b8-6baa62656a24" } }, { $lookup: { from: "providers", localField: "ENCOUNTERS.PROVIDER_REF", foreignField: "PROVIDER_ID", as: "provider_info" }}, {  $unwind:"provider_info" }, { $project: { _id: 0, provider_name: "$provider_info.NAME" } }])


            With all the information given, provide a MongoDB query to the following question:

            [Q]: '{question}'
            [MongoDB]: 
            """


mql_prompt_schema_oneshot = """ Given an input question, create a single syntactically correct MongoDB query leveraging the provided schema, notes, and examples. Only query for relevant fields given the question. Pay attention to using only the field names that you can see in the schema description. Be careful not to query for fields that do not exist.

            [Schema]:
            '{schema}'

            [Notes]:
            1) Use only the provided document collections in the schema.
            2) Use the collection fields that are explicitly mentioned in the question.
            3) Do not include any explanations or apologies in your responses. Provide the output in one line.
            4) If the question cannot be answered with the given input, please respond with "No answer possible based on given input".
            5) Pay attention to the group key that is used for the $group operator when needed.
            6) Pay attention to the fields that are used in the find() operator.
            7) Pay attention to add quotes where needed such as for strings.
            8) The "_id" field is only used as internal MomgoDB ObjectID and not as the domain specific ID of the objects in the collections. The objects are identified with a UUID in fields following a structure like PATIENT_ID, TRANSACTION_ID, CLAIM_ID...
            
            Please include the following examples for better understanding.

            [Examples]:

            [Q] = Question, [MongoDB] = Answer (correct query)

            [Q]: What is the city of residence of the patient named Eugene421 Fisher429?
            [MongoDB]: db.patients.find({ "FIRST": "Eugene421", "LAST": "Fisher429" }, { "_id": 0, "CITY": 1 })


            With all the information given, provide a MongoDB query to the following question:

            [Q]: '{question}'
            [MongoDB]: 
            """

mql_prompt_schema_0shot = """ Given an input question, create a single syntactically correct MongoDB query leveraging the provided schema and notes. Only query for relevant fields given the question. Pay attention to using only the field names that you can see in the schema description. Be careful not to query for fields that do not exist.

            [Schema]:
            '{schema}'

            [Notes]:
            1) Use only the provided document collections in the schema.
            2) Use the collection fields that are explicitly mentioned in the question.
            3) Do not include any explanations or apologies in your responses. Provide the output in one line.
            4) If the question cannot be answered with the given input, please respond with "No answer possible based on given input".
            5) Pay attention to the group key that is used for the $group operator when needed.
            6) Pay attention to the fields that are used in the find() operator.
            7) Pay attention to add quotes where needed such as for strings.
            8) The "_id" field is only used as internal MomgoDB ObjectID and not as the domain specific ID of the objects in the collections. The objects are identified with a UUID in fields following a structure like PATIENT_ID, TRANSACTION_ID, CLAIM_ID...
            

            [Q] = Question, [MongoDB] = Answer (correct query)


            With all the information given, provide a MongoDB query to the following question:

            [Q]: '{question}'
            [MongoDB]: 
            """


mql_prompt_0schema_fewshots = """ Given an input question, create a single syntactically correct MongoDB query leveraging the provided notes and examples. Only query for relevant fields given the question. Be careful not to query for fields that do not exist.

            [Notes]:
            1) Use the collection fields that are explicitly mentioned in the question.
            2) Do not include any explanations or apologies in your responses. Provide the output in one line.
            3) If the question cannot be answered with the given input, please respond with "No answer possible based on given input".
            4) Pay attention to the group key that is used for the $group operator when needed.
            5) Pay attention to the fields that are used in the find() operator.
            6) Pay attention to add quotes where needed such as for strings.
            7) The "_id" field is only used as internal MomgoDB ObjectID and not as the domain specific ID of the objects in the collections. The objects are identified with a UUID in fields following a structure like PATIENT_ID, TRANSACTION_ID, CLAIM_ID...

            Please include the following examples for better understanding.

            [Examples]:

            [Q] = Question, [MongoDB] = Answer (correct query)

            [Q]: What is the city of residence of the patient named Eugene421 Fisher429?
            [MongoDB]: db.patients.find({ "FIRST": "Eugene421", "LAST": "Fisher429" }, { "_id": 0, "CITY": 1 })

            [Q]: What is the first name of the patient with the ID efa523f2-6ac2-641c-58f3-2ca1b97543f9?
            [MongoDB]: db.patients.find({ "PATIENT_ID": "efa523f2-6ac2-641c-58f3-2ca1b97543f9" }, { _id: 0, FIRST: 1 })

            [Q]: How many procedures are uncovered by the payer with the ID 26aab0cd-6aba-3e1b-ac5b-05c8867e762c?
            [MongoDB]: db.payers.find({ "PAYER_ID": "26aab0cd-6aba-3e1b-ac5b-05c8867e762c" }, { _id: 0, UNCOVERED_PROCEDURES: 1 })

            [Q]: Please provide me the encounters that are related to the condition with code 424393004.
            [MongoDB]: db.patients.aggregate([ {  $unwind:"ENCOUNTERS" }, {  $unwind:"ENCOUNTERS.CONDITIONS" }, { $match: { "ENCOUNTERS.CONDITIONS.CODE": 424393004 } }, { $project: { _id: 0, description: "$ENCOUNTERS.DESCRIPTION" } }, { $group: { _id: "$description" } }, { $project: { _id: 0, description: "$_id" } }]);
            
            [Q]: Please provide me the name of the provider associated with the encounter 76956a25-b2fe-4a8d-34b8-6baa62656a24.
            [MongoDB]: db.patients.aggregate([ { $match: { "ENCOUNTERS.ENCOUNTER_ID": "76956a25-b2fe-4a8d-34b8-6baa62656a24" } }, {  $unwind:"ENCOUNTERS" }, { $match: { "ENCOUNTERS.ENCOUNTER_ID": "76956a25-b2fe-4a8d-34b8-6baa62656a24" } }, { $lookup: { from: "providers", localField: "ENCOUNTERS.PROVIDER_REF", foreignField: "PROVIDER_ID", as: "provider_info" }}, {  $unwind:"provider_info" }, { $project: { _id: 0, provider_name: "$provider_info.NAME" } }])


            With all the information given, provide a MongoDB query to the following question:

            [Q]: '{question}'
            [MongoDB]: 
            """

mql_prompt_0schema_oneshot = """ Given an input question, create a single syntactically correct MongoDB query leveraging the provided notes and examples. Only query for relevant fields given the question. Be careful not to query for fields that do not exist.

            [Notes]:
            1) Use the collection fields that are explicitly mentioned in the question.
            2) Do not include any explanations or apologies in your responses. Provide the output in one line.
            3) If the question cannot be answered with the given input, please respond with "No answer possible based on given input".
            4) Pay attention to the group key that is used for the $group operator when needed.
            5) Pay attention to the fields that are used in the find() operator.
            6) Pay attention to add quotes where needed such as for strings.
            7) The "_id" field is only used as internal MomgoDB ObjectID and not as the domain specific ID of the objects in the collections. The objects are identified with a UUID in fields following a structure like PATIENT_ID, TRANSACTION_ID, CLAIM_ID...
            
            Please include the following examples for better understanding.

            [Examples]:

            [Q] = Question, [MongoDB] = Answer (correct query)

            [Q]: What is the city of residence of the patient named Eugene421 Fisher429?
            [MongoDB]: db.patients.find({ "FIRST": "Eugene421", "LAST": "Fisher429" }, { "_id": 0, "CITY": 1 })


            With all the information given, provide a MongoDB query to the following question:

            [Q]: '{question}'
            [MongoDB]: 
            """

mql_prompt_0schema_bm25 = """ Given an input question, create a single syntactically correct MongoDB query leveraging the provided notes and examples. Only query for relevant fields given the question. Be careful not to query for fields that do not exist.

            [Notes]:
            1) Use the collection fields that are explicitly mentioned in the question.
            2) Do not include any explanations or apologies in your responses. Provide the output in one line.
            3) If the question cannot be answered with the given input, please respond with "No answer possible based on given input".
            4) Pay attention to the group key that is used for the $group operator when needed.
            5) Pay attention to the fields that are used in the find() operator.
            6) Pay attention to add quotes where needed such as for strings.
            7) The "_id" field is only used as internal MomgoDB ObjectID and not as the domain specific ID of the objects in the collections. The objects are identified with a UUID in fields following a structure like PATIENT_ID, TRANSACTION_ID, CLAIM_ID...
            
            
            Please include the following examples for better understanding.

            [Examples]:

            [Q] = Question, [MongoDB] = Answer (correct query)

            '{examples}'
            

            With all the information given, provide a MongoDB query to the following question:

            [Q]: '{question}'
            [MongoDB]: 
            """
            
mql_prompt_schema_bm25= """ Given an input question, create a single syntactically correct MongoDB query leveraging the provided schema, notes, and examples. Only query for relevant fields given the question. Pay attention to using only the field names that you can see in the schema description. Be careful not to query for fields that do not exist.

            [Schema]:
            '{schema}'

            [Notes]:
            1) Use only the provided document collections in the schema.
            2) Use the collection fields that are explicitly mentioned in the question.
            3) Do not include any explanations or apologies in your responses. Provide the output in one line.
            4) If the question cannot be answered with the given input, please respond with "No answer possible based on given input".
            5) Pay attention to the group key that is used for the $group operator when needed.
            6) Pay attention to the fields that are used in the find() operator.
            7) Pay attention to add quotes where needed such as for strings.
            8) The "_id" field is only used as internal MomgoDB ObjectID and not as the domain specific ID of the objects in the collections. The objects are identified with a UUID in fields following a structure like PATIENT_ID, TRANSACTION_ID, CLAIM_ID...
            
            
            Please include the following examples for better understanding.

            [Examples]:

            [Q] = Question, [MongoDB] = Answer (correct query)

            '{examples}'


            With all the information given, provide a MongoDB query to the following question:

            [Q]: '{question}'
            [MongoDB]: 
            """