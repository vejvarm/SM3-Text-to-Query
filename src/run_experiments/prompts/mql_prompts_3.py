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

            [Q]: In what type of allergy does the description House dust mite (organism) fall?
            [MongoDB]: db.patients.aggregate([    { $match: {"ENCOUNTERS.ALLERGIES.DESCRIPTION": "House dust mite (organism)"} },    { $unwind: "$ENCOUNTERS" },    { $unwind: "$ENCOUNTERS.ALLERGIES" },    { $match: {"ENCOUNTERS.ALLERGIES.DESCRIPTION": "House dust mite (organism)"} },    { $group: { _id: "$ENCOUNTERS.ALLERGIES.TYPE" } },    { $project: { _id: 0, type: "$_id" } }])

            [Q]: Please provide me the patients with the claim ID 56a60caf-14fc-db17-e331-65b4e8dcf942.
            [MongoDB]: db.patients.aggregate([    {        $match: {            "CLAIMS.CLAIM_ID": "56a60caf-14fc-db17-e331-65b4e8dcf942"        }    },    {        $unwind: "$CLAIMS"    },    {        $unwind: "$CLAIMS.CLAIM_TRANSACTIONS"    },    {        $project: {            _id: 0,             FIRST: 1,            LAST: 1        }    },    {        $group: {            _id: {                FIRST: "$FIRST",                LAST: "$LAST"            }        }    },    {        $project: {            _id: 0,            FIRST: "$_id.FIRST",            LAST: "$_id.LAST"        }    }]);

            [Q]: What encounter is associated with the supply named Disposable air-purifying respirator (physical object)?
            [MongoDB]: db.patients.aggregate([    {        $match: {"ENCOUNTERS.SUPPLIES.DESCRIPTION": "Disposable air-purifying respirator (physical object)"}    },    {        $unwind: "$ENCOUNTERS"    },    {        $unwind: "$ENCOUNTERS.SUPPLIES"    },    {        $match: {"ENCOUNTERS.SUPPLIES.DESCRIPTION": "Disposable air-purifying respirator (physical object)"}    },    {        $group: {            _id: {            desc: "$ENCOUNTERS.DESCRIPTION"            }        }    },    {        $project: {            _id: 0,            ENCOUNTER_DESCRIPTION: "$_id.desc"        }    }])

            [Q]: What is the description of encounter 2377dc28-54be-b1a0-407f-2fcd515cf588?
            [MongoDB]: db.patients.aggregate([    { $match: { "ENCOUNTERS.ENCOUNTER_ID": "2377dc28-54be-b1a0-407f-2fcd515cf588" } },    { $unwind: "$ENCOUNTERS" },    { $match: { "ENCOUNTERS.ENCOUNTER_ID": "2377dc28-54be-b1a0-407f-2fcd515cf588" } },    { $project: { _id: 0, description: "$ENCOUNTERS.DESCRIPTION" } }])
            
            [Q]: Who are the patients associated with the device Home continuous positive airway pressure unit (physical object)?
            [MongoDB]: db.patients.aggregate([{$unwind: "$ENCOUNTERS"},{$unwind: "$ENCOUNTERS.DEVICES"},{$match: {"ENCOUNTERS.DEVICES.DESCRIPTION": "Home continuous positive airway pressure unit (physical object)"}},{$group: {_id: {first: "$FIRST",last: "$LAST"}}},{$project: {_id: 0,first: "$_id.first",last: "$_id.last"}}])


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

            [Q]: In what type of allergy does the description House dust mite (organism) fall?
            [MongoDB]: db.patients.aggregate([    { $match: {"ENCOUNTERS.ALLERGIES.DESCRIPTION": "House dust mite (organism)"} },    { $unwind: "$ENCOUNTERS" },    { $unwind: "$ENCOUNTERS.ALLERGIES" },    { $match: {"ENCOUNTERS.ALLERGIES.DESCRIPTION": "House dust mite (organism)"} },    { $group: { _id: "$ENCOUNTERS.ALLERGIES.TYPE" } },    { $project: { _id: 0, type: "$_id" } }])


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

            [Q]: In what type of allergy does the description House dust mite (organism) fall?
            [MongoDB]: db.patients.aggregate([    { $match: {"ENCOUNTERS.ALLERGIES.DESCRIPTION": "House dust mite (organism)"} },    { $unwind: "$ENCOUNTERS" },    { $unwind: "$ENCOUNTERS.ALLERGIES" },    { $match: {"ENCOUNTERS.ALLERGIES.DESCRIPTION": "House dust mite (organism)"} },    { $group: { _id: "$ENCOUNTERS.ALLERGIES.TYPE" } },    { $project: { _id: 0, type: "$_id" } }])

            [Q]: Please provide me the patients with the claim ID 56a60caf-14fc-db17-e331-65b4e8dcf942.
            [MongoDB]: db.patients.aggregate([    {        $match: {            "CLAIMS.CLAIM_ID": "56a60caf-14fc-db17-e331-65b4e8dcf942"        }    },    {        $unwind: "$CLAIMS"    },    {        $unwind: "$CLAIMS.CLAIM_TRANSACTIONS"    },    {        $project: {            _id: 0,             FIRST: 1,            LAST: 1        }    },    {        $group: {            _id: {                FIRST: "$FIRST",                LAST: "$LAST"            }        }    },    {        $project: {            _id: 0,            FIRST: "$_id.FIRST",            LAST: "$_id.LAST"        }    }]);

            [Q]: What encounter is associated with the supply named Disposable air-purifying respirator (physical object)?
            [MongoDB]: db.patients.aggregate([    {        $match: {"ENCOUNTERS.SUPPLIES.DESCRIPTION": "Disposable air-purifying respirator (physical object)"}    },    {        $unwind: "$ENCOUNTERS"    },    {        $unwind: "$ENCOUNTERS.SUPPLIES"    },    {        $match: {"ENCOUNTERS.SUPPLIES.DESCRIPTION": "Disposable air-purifying respirator (physical object)"}    },    {        $group: {            _id: {            desc: "$ENCOUNTERS.DESCRIPTION"            }        }    },    {        $project: {            _id: 0,            ENCOUNTER_DESCRIPTION: "$_id.desc"        }    }])

            [Q]: What is the description of encounter 2377dc28-54be-b1a0-407f-2fcd515cf588?
            [MongoDB]: db.patients.aggregate([    { $match: { "ENCOUNTERS.ENCOUNTER_ID": "2377dc28-54be-b1a0-407f-2fcd515cf588" } },    { $unwind: "$ENCOUNTERS" },    { $match: { "ENCOUNTERS.ENCOUNTER_ID": "2377dc28-54be-b1a0-407f-2fcd515cf588" } },    { $project: { _id: 0, description: "$ENCOUNTERS.DESCRIPTION" } }])
            
            [Q]: Who are the patients associated with the device Home continuous positive airway pressure unit (physical object)?
            [MongoDB]: db.patients.aggregate([{$unwind: "$ENCOUNTERS"},{$unwind: "$ENCOUNTERS.DEVICES"},{$match: {"ENCOUNTERS.DEVICES.DESCRIPTION": "Home continuous positive airway pressure unit (physical object)"}},{$group: {_id: {first: "$FIRST",last: "$LAST"}}},{$project: {_id: 0,first: "$_id.first",last: "$_id.last"}}])


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

            [Q]: In what type of allergy does the description House dust mite (organism) fall?
            [MongoDB]: db.patients.aggregate([    { $match: {"ENCOUNTERS.ALLERGIES.DESCRIPTION": "House dust mite (organism)"} },    { $unwind: "$ENCOUNTERS" },    { $unwind: "$ENCOUNTERS.ALLERGIES" },    { $match: {"ENCOUNTERS.ALLERGIES.DESCRIPTION": "House dust mite (organism)"} },    { $group: { _id: "$ENCOUNTERS.ALLERGIES.TYPE" } },    { $project: { _id: 0, type: "$_id" } }])


            With all the information given, provide a MongoDB query to the following question:

            [Q]: '{question}'
            [MongoDB]: 
            """