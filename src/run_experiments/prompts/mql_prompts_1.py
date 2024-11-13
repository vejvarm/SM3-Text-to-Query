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

            [Q]: Which encounter is related to allergy Animal dander (substance)?
            [MongoDB]: db.patients.aggregate([ { $match: {"ENCOUNTERS.ALLERGIES.DESCRIPTION": "Animal dander (substance)"} }, { $unwind: "$ENCOUNTERS" }, { $unwind: "$ENCOUNTERS.ALLERGIES" }, { $match: {"ENCOUNTERS.ALLERGIES.DESCRIPTION": "Animal dander (substance)"} }, { $group: {_id: "$ENCOUNTERS.DESCRIPTION"} }, { $project: { _id: 0, encounter_description: "$_id" } } ])

            [Q] :Provide the list of patients associated with the payer Dual Eligible.
            [MongoDB] db.patients.aggregate([    {        $lookup: {            from: "payers",            localField: "PAYER_TRANSITIONS.PAYER_REF",            foreignField: "PAYER_ID",            as: "payer_details"        }    },    { $unwind: "$PAYER_TRANSITIONS" },    { $unwind: "$payer_details" },    { $match: { "payer_details.NAME": "Dual Eligible" } },    { $project: { _id: 0, first: "$FIRST", last: "$LAST" } },    { $group: { _id: { first: "$first", last: "$last" } } },    { $project: { _id: 0, first: "$_id.first", last: "$_id.last" } }]);

            [Q]: Give me the organization affiliated with the provider with the ID beff794b-089c-3098-9bed-5cc458acbc05.
            [MongoDB]: db.providers.aggregate([{$match: {"PROVIDER_ID": "beff794b-089c-3098-9bed-5cc458acbc05"}},{$lookup: {from: "organizations",localField: "ORGANIZATION_REF",foreignField: "ORGANIZATION_ID",as: "organization"}},{$unwind: "$organization"},{$project: {_id: 0,organization_name: "$organization.NAME"}}])

            [Q]: What is the base cost of medication with the code 205923.
            [MongoDB]: db.patients.aggregate([    { $match: {"ENCOUNTERS.MEDICATIONS.CODE": 205923} },    { $unwind: "$ENCOUNTERS" },    { $unwind: "$ENCOUNTERS.MEDICATIONS" },    { $match: {"ENCOUNTERS.MEDICATIONS.CODE": 205923} },    { $project: { _id: 0, base_cost: "$ENCOUNTERS.MEDICATIONS.BASE_COST" } }])

            [Q]: What is the procedure code of the claim transaction 210ae4cd-7ca0-7da4-66a7-ef20b4f5db4d?
            [MongoDB]: db.patients.aggregate([    {        $match: {            "CLAIMS.CLAIM_TRANSACTIONS.CLAIM_TRANSACTION_ID": "210ae4cd-7ca0-7da4-66a7-ef20b4f5db4d"        }    },    {        $unwind: "$CLAIMS"    },    {        $unwind: "$CLAIMS.CLAIM_TRANSACTIONS"    },    {        $match: {            "CLAIMS.CLAIM_TRANSACTIONS.CLAIM_TRANSACTION_ID": "210ae4cd-7ca0-7da4-66a7-ef20b4f5db4d"        }    },    {        $project: {            _id: 0,             procedure_code: "$CLAIMS.CLAIM_TRANSACTIONS.PROCEDURE_CODE"        }    }]);


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

            [Q]: Which encounter is related to allergy Animal dander (substance)?
            [MongoDB]: db.patients.aggregate([ { $match: {"ENCOUNTERS.ALLERGIES.DESCRIPTION": "Animal dander (substance)"} }, { $unwind: "$ENCOUNTERS" }, { $unwind: "$ENCOUNTERS.ALLERGIES" }, { $match: {"ENCOUNTERS.ALLERGIES.DESCRIPTION": "Animal dander (substance)"} }, { $group: {_id: "$ENCOUNTERS.DESCRIPTION"} }, { $project: { _id: 0, encounter_description: "$_id" } } ])


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

            [Q]: Which encounter is related to allergy Animal dander (substance)?
            [MongoDB]: db.patients.aggregate([ { $match: {"ENCOUNTERS.ALLERGIES.DESCRIPTION": "Animal dander (substance)"} }, { $unwind: "$ENCOUNTERS" }, { $unwind: "$ENCOUNTERS.ALLERGIES" }, { $match: {"ENCOUNTERS.ALLERGIES.DESCRIPTION": "Animal dander (substance)"} }, { $group: {_id: "$ENCOUNTERS.DESCRIPTION"} }, { $project: { _id: 0, encounter_description: "$_id" } } ])

            [Q] :Provide the list of patients associated with the payer Dual Eligible.
            [MongoDB] db.patients.aggregate([    {        $lookup: {            from: "payers",            localField: "PAYER_TRANSITIONS.PAYER_REF",            foreignField: "PAYER_ID",            as: "payer_details"        }    },    { $unwind: "$PAYER_TRANSITIONS" },    { $unwind: "$payer_details" },    { $match: { "payer_details.NAME": "Dual Eligible" } },    { $project: { _id: 0, first: "$FIRST", last: "$LAST" } },    { $group: { _id: { first: "$first", last: "$last" } } },    { $project: { _id: 0, first: "$_id.first", last: "$_id.last" } }]);

            [Q]: Give me the organization affiliated with the provider with the ID beff794b-089c-3098-9bed-5cc458acbc05.
            [MongoDB]: db.providers.aggregate([{$match: {"PROVIDER_ID": "beff794b-089c-3098-9bed-5cc458acbc05"}},{$lookup: {from: "organizations",localField: "ORGANIZATION_REF",foreignField: "ORGANIZATION_ID",as: "organization"}},{$unwind: "$organization"},{$project: {_id: 0,organization_name: "$organization.NAME"}}])

            [Q]: What is the base cost of medication with the code 205923.
            [MongoDB]: db.patients.aggregate([    { $match: {"ENCOUNTERS.MEDICATIONS.CODE": 205923} },    { $unwind: "$ENCOUNTERS" },    { $unwind: "$ENCOUNTERS.MEDICATIONS" },    { $match: {"ENCOUNTERS.MEDICATIONS.CODE": 205923} },    { $project: { _id: 0, base_cost: "$ENCOUNTERS.MEDICATIONS.BASE_COST" } }])

            [Q]: What is the procedure code of the claim transaction 210ae4cd-7ca0-7da4-66a7-ef20b4f5db4d?
            [MongoDB]: db.patients.aggregate([    {        $match: {            "CLAIMS.CLAIM_TRANSACTIONS.CLAIM_TRANSACTION_ID": "210ae4cd-7ca0-7da4-66a7-ef20b4f5db4d"        }    },    {        $unwind: "$CLAIMS"    },    {        $unwind: "$CLAIMS.CLAIM_TRANSACTIONS"    },    {        $match: {            "CLAIMS.CLAIM_TRANSACTIONS.CLAIM_TRANSACTION_ID": "210ae4cd-7ca0-7da4-66a7-ef20b4f5db4d"        }    },    {        $project: {            _id: 0,             procedure_code: "$CLAIMS.CLAIM_TRANSACTIONS.PROCEDURE_CODE"        }    }]);


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

            [Q]: Which encounter is related to allergy Animal dander (substance)?
            [MongoDB]: db.patients.aggregate([ { $match: {"ENCOUNTERS.ALLERGIES.DESCRIPTION": "Animal dander (substance)"} }, { $unwind: "$ENCOUNTERS" }, { $unwind: "$ENCOUNTERS.ALLERGIES" }, { $match: {"ENCOUNTERS.ALLERGIES.DESCRIPTION": "Animal dander (substance)"} }, { $group: {_id: "$ENCOUNTERS.DESCRIPTION"} }, { $project: { _id: 0, encounter_description: "$_id" } } ])


            With all the information given, provide a MongoDB query to the following question:

            [Q]: '{question}'
            [MongoDB]: 
            """