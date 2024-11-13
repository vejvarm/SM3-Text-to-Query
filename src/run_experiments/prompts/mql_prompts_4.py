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

            [Q]: What is the start date of the procedure Urine protein test?
            [MongoDB]: db.patients.aggregate( [{ $match: {"ENCOUNTERS.PROCEDURES.DESCRIPTION": "Urine protein test"} }, { $unwind:"ENCOUNTERS" }, { $unwind:"ENCOUNTERS.PROCEDURES" }, { $match: {"ENCOUNTERS.PROCEDURES.DESCRIPTION": "Urine protein test"} }, { $group: { _id: "$ENCOUNTERS.PROCEDURES.START" } }, { $project: { _id: 0, start: "$_id" } }, ] )

            [Q]: What is the start date of the condition Part-time employment (finding)?
            [MongoDB]: db.patients.aggregate([ { $unwind:"ENCOUNTERS" }, { $unwind:"ENCOUNTERS.CONDITIONS" }, { $match: { "ENCOUNTERS.CONDITIONS.DESCRIPTION": "Part-time employment (finding)" } }, { $project: { _id: 0, start: "$ENCOUNTERS.CONDITIONS.START" } }]);

            [Q]: What encounter is required during the use of the device with code 272265001?
            [MongoDB]: db.patients.aggregate([{$unwind:"ENCOUNTERS"},{$unwind:"ENCOUNTERS.DEVICES"},{$match: {"ENCOUNTERS.DEVICES.CODE": 272265001}},{$group: {_id: "$ENCOUNTERS.DESCRIPTION"}},{$project: {_id: 0,encounter_description: "$_id"}}])

            [Q]: How many immunizations are covered by the payer Dual Eligible?
            [MongoDB]: db.payers.aggregate([ { $match: { "NAME": "Dual Eligible" } }, { $project: { _id: 0, covered_immunizations: "$COVERED_IMMUNIZATIONS" } }])
            
            [Q]: Please provide me patients with the observation Tobacco smoking status.
            [MongoDB]: db.patients.aggregate([ { $match: {"ENCOUNTERS.OBSERVATIONS.DESCRIPTION": "Tobacco smoking status"} }, { $unwind:"ENCOUNTERS" }, { $unwind:"ENCOUNTERS.OBSERVATIONS" }, { $match: { "ENCOUNTERS.OBSERVATIONS.DESCRIPTION": "Tobacco smoking status"} }, {$group: {_id: {first: "$FIRST",last: "$LAST"}}},{$project: {_id: 0,first: "$_id.first",last: "$_id.last"}}])


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

            [Q]: What is the start date of the procedure Urine protein test?
            [MongoDB]: db.patients.aggregate( [{ $match: {"ENCOUNTERS.PROCEDURES.DESCRIPTION": "Urine protein test"} }, { $unwind:"ENCOUNTERS" }, { $unwind:"ENCOUNTERS.PROCEDURES" }, { $match: {"ENCOUNTERS.PROCEDURES.DESCRIPTION": "Urine protein test"} }, { $group: { _id: "$ENCOUNTERS.PROCEDURES.START" } }, { $project: { _id: 0, start: "$_id" } }, ] )


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

            [Q]: What is the start date of the procedure Urine protein test?
            [MongoDB]: db.patients.aggregate( [{ $match: {"ENCOUNTERS.PROCEDURES.DESCRIPTION": "Urine protein test"} }, { $unwind:"ENCOUNTERS" }, { $unwind:"ENCOUNTERS.PROCEDURES" }, { $match: {"ENCOUNTERS.PROCEDURES.DESCRIPTION": "Urine protein test"} }, { $group: { _id: "$ENCOUNTERS.PROCEDURES.START" } }, { $project: { _id: 0, start: "$_id" } }, ] )

            [Q]: What is the start date of the condition Part-time employment (finding)?
            [MongoDB]: db.patients.aggregate([ { $unwind:"ENCOUNTERS" }, { $unwind:"ENCOUNTERS.CONDITIONS" }, { $match: { "ENCOUNTERS.CONDITIONS.DESCRIPTION": "Part-time employment (finding)" } }, { $project: { _id: 0, start: "$ENCOUNTERS.CONDITIONS.START" } }]);

            [Q]: What encounter is required during the use of the device with code 272265001?
            [MongoDB]: db.patients.aggregate([{$unwind:"ENCOUNTERS"},{$unwind:"ENCOUNTERS.DEVICES"},{$match: {"ENCOUNTERS.DEVICES.CODE": 272265001}},{$group: {_id: "$ENCOUNTERS.DESCRIPTION"}},{$project: {_id: 0,encounter_description: "$_id"}}])

            [Q]: How many immunizations are covered by the payer Dual Eligible?
            [MongoDB]: db.payers.aggregate([ { $match: { "NAME": "Dual Eligible" } }, { $project: { _id: 0, covered_immunizations: "$COVERED_IMMUNIZATIONS" } }])
            
            [Q]: Please provide me patients with the observation Tobacco smoking status.
            [MongoDB]: db.patients.aggregate([ { $match: {"ENCOUNTERS.OBSERVATIONS.DESCRIPTION": "Tobacco smoking status"} }, { $unwind:"ENCOUNTERS" }, { $unwind:"ENCOUNTERS.OBSERVATIONS" }, { $match: { "ENCOUNTERS.OBSERVATIONS.DESCRIPTION": "Tobacco smoking status"} }, {$group: {_id: {first: "$FIRST",last: "$LAST"}}},{$project: {_id: 0,first: "$_id.first",last: "$_id.last"}}])


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

            [Q]: What is the start date of the procedure Urine protein test?
            [MongoDB]: db.patients.aggregate( [{ $match: {"ENCOUNTERS.PROCEDURES.DESCRIPTION": "Urine protein test"} }, { $unwind:"ENCOUNTERS" }, { $unwind:"ENCOUNTERS.PROCEDURES" }, { $match: {"ENCOUNTERS.PROCEDURES.DESCRIPTION": "Urine protein test"} }, { $group: { _id: "$ENCOUNTERS.PROCEDURES.START" } }, { $project: { _id: 0, start: "$_id" } }, ] )


            With all the information given, provide a MongoDB query to the following question:

            [Q]: '{question}'
            [MongoDB]: 
            """