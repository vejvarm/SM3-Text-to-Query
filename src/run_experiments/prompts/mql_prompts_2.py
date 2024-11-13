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

            [Q]: Please provide me the patients with the claim ID 25382c93-4b35-d58c-d519-2f50343b3626.
            [MongoDB]: db.patients.aggregate([    {        $match: {            "CLAIMS.CLAIM_ID": "25382c93-4b35-d58c-d519-2f50343b3626"        }    },    {        $unwind: "$CLAIMS"    },    {        $unwind: "$CLAIMS.CLAIM_TRANSACTIONS"    },    {        $project: {            _id: 0,             FIRST: 1,            LAST: 1        }    },    {        $group: {            _id: {                FIRST: "$FIRST",                LAST: "$LAST"            }        }    },    {        $project: {            _id: 0,            FIRST: "$_id.FIRST",            LAST: "$_id.LAST"        }    }]);   

            [Q]: Please provide me a reason for the use of the care plan with code 734163000.
            [MongoDB] db.patients.aggregate([    { $match: {"ENCOUNTERS.CAREPLANS.CODE": 734163000} },    { $unwind: "$ENCOUNTERS" },    { $unwind: "$ENCOUNTERS.CAREPLANS" },    { $match: {"ENCOUNTERS.CAREPLANS.CODE": 734163000} },    { $project: { _id: 0, reason_description: "$ENCOUNTERS.CAREPLANS.REASON_DESCRIPTION" } }])

            [Q]: Please provide me the quality for the supply with the code 1137596000.
            [MongoDB]: db.patients.aggregate([    {        $match: {"ENCOUNTERS.SUPPLIES.CODE": 1137596000}    },    {        $unwind: "$ENCOUNTERS"    },    {        $unwind: "$ENCOUNTERS.SUPPLIES"    },    {        $match: {"ENCOUNTERS.SUPPLIES.CODE": 1137596000}    },    {        $group: {            _id: {            quantity: "$ENCOUNTERS.SUPPLIES.QUANTITY"            }        }    },    {        $project: {            _id: 0,            QUANTITY: "$_id.quantity"        }    }])

            [Q]: What is the SNOMED code for the allergy described as Eggs (edible) (substance)?
            [MongoDB]: db.patients.aggregate([    { $match: {"ENCOUNTERS.ALLERGIES.DESCRIPTION": "Eggs (edible) (substance)"} },    { $unwind: "$ENCOUNTERS" },    { $unwind: "$ENCOUNTERS.ALLERGIES" },    { $match: {"ENCOUNTERS.ALLERGIES.DESCRIPTION": "Eggs (edible) (substance)"} },    { $group: { _id: "$ENCOUNTERS.ALLERGIES.CODE" } },    { $project: { _id: 0, code: "$_id" } }])
            
            [Q]: What is the department id of the claim with the ID 2bfc5ac8-bf25-4845-f673-c6f6bc344034?
            [MongoDB]: db.patients.aggregate(    [{        $match: {"CLAIMS.CLAIM_ID": "2bfc5ac8-bf25-4845-f673-c6f6bc344034"},    },    {        $unwind: "$CLAIMS"    },    {        $match: {"CLAIMS.CLAIM_ID": "2bfc5ac8-bf25-4845-f673-c6f6bc344034"},    },    {        $project: {             "_id": 0,             department_id: "$CLAIMS.DEPARTMENT_ID"}    }    ]);


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

            [Q]: Please provide me the patients with the claim ID 25382c93-4b35-d58c-d519-2f50343b3626.
            [MongoDB]: db.patients.aggregate([    {        $match: {            "CLAIMS.CLAIM_ID": "25382c93-4b35-d58c-d519-2f50343b3626"        }    },    {        $unwind: "$CLAIMS"    },    {        $unwind: "$CLAIMS.CLAIM_TRANSACTIONS"    },    {        $project: {            _id: 0,             FIRST: 1,            LAST: 1        }    },    {        $group: {            _id: {                FIRST: "$FIRST",                LAST: "$LAST"            }        }    },    {        $project: {            _id: 0,            FIRST: "$_id.FIRST",            LAST: "$_id.LAST"        }    }]);   


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

            [Q]: Please provide me the patients with the claim ID 25382c93-4b35-d58c-d519-2f50343b3626.
            [MongoDB]: db.patients.aggregate([    {        $match: {            "CLAIMS.CLAIM_ID": "25382c93-4b35-d58c-d519-2f50343b3626"        }    },    {        $unwind: "$CLAIMS"    },    {        $unwind: "$CLAIMS.CLAIM_TRANSACTIONS"    },    {        $project: {            _id: 0,             FIRST: 1,            LAST: 1        }    },    {        $group: {            _id: {                FIRST: "$FIRST",                LAST: "$LAST"            }        }    },    {        $project: {            _id: 0,            FIRST: "$_id.FIRST",            LAST: "$_id.LAST"        }    }]);   

            [Q]: Please provide me a reason for the use of the care plan with code 734163000.
            [MongoDB] db.patients.aggregate([    { $match: {"ENCOUNTERS.CAREPLANS.CODE": 734163000} },    { $unwind: "$ENCOUNTERS" },    { $unwind: "$ENCOUNTERS.CAREPLANS" },    { $match: {"ENCOUNTERS.CAREPLANS.CODE": 734163000} },    { $project: { _id: 0, reason_description: "$ENCOUNTERS.CAREPLANS.REASON_DESCRIPTION" } }])

            [Q]: Please provide me the quality for the supply with the code 1137596000.
            [MongoDB]: db.patients.aggregate([    {        $match: {"ENCOUNTERS.SUPPLIES.CODE": 1137596000}    },    {        $unwind: "$ENCOUNTERS"    },    {        $unwind: "$ENCOUNTERS.SUPPLIES"    },    {        $match: {"ENCOUNTERS.SUPPLIES.CODE": 1137596000}    },    {        $group: {            _id: {            quantity: "$ENCOUNTERS.SUPPLIES.QUANTITY"            }        }    },    {        $project: {            _id: 0,            QUANTITY: "$_id.quantity"        }    }])

            [Q]: What is the SNOMED code for the allergy described as Eggs (edible) (substance)?
            [MongoDB]: db.patients.aggregate([    { $match: {"ENCOUNTERS.ALLERGIES.DESCRIPTION": "Eggs (edible) (substance)"} },    { $unwind: "$ENCOUNTERS" },    { $unwind: "$ENCOUNTERS.ALLERGIES" },    { $match: {"ENCOUNTERS.ALLERGIES.DESCRIPTION": "Eggs (edible) (substance)"} },    { $group: { _id: "$ENCOUNTERS.ALLERGIES.CODE" } },    { $project: { _id: 0, code: "$_id" } }])
            
            [Q]: What is the department id of the claim with the ID 2bfc5ac8-bf25-4845-f673-c6f6bc344034?
            [MongoDB]: db.patients.aggregate(    [{        $match: {"CLAIMS.CLAIM_ID": "2bfc5ac8-bf25-4845-f673-c6f6bc344034"},    },    {        $unwind: "$CLAIMS"    },    {        $match: {"CLAIMS.CLAIM_ID": "2bfc5ac8-bf25-4845-f673-c6f6bc344034"},    },    {        $project: {             "_id": 0,             department_id: "$CLAIMS.DEPARTMENT_ID"}    }    ]);


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

            [Q]: Please provide me the patients with the claim ID 25382c93-4b35-d58c-d519-2f50343b3626.
            [MongoDB]: db.patients.aggregate([    {        $match: {            "CLAIMS.CLAIM_ID": "25382c93-4b35-d58c-d519-2f50343b3626"        }    },    {        $unwind: "$CLAIMS"    },    {        $unwind: "$CLAIMS.CLAIM_TRANSACTIONS"    },    {        $project: {            _id: 0,             FIRST: 1,            LAST: 1        }    },    {        $group: {            _id: {                FIRST: "$FIRST",                LAST: "$LAST"            }        }    },    {        $project: {            _id: 0,            FIRST: "$_id.FIRST",            LAST: "$_id.LAST"        }    }]);   


            With all the information given, provide a MongoDB query to the following question:

            [Q]: '{question}'
            [MongoDB]: 
            """