from prompts.cypher_prompts_5 import *
from prompts.sql_prompts_5 import *
from prompts.sparql_prompts_5 import *
from prompts.mql_prompts_5 import *

cypher_prompttypes = {
    "prompt_0schema_bm25": cypher_prompt_0schema_bm25,
    "prompt_schema_bm25": cypher_prompt_schema_bm25,
}

sql_prompttypes = {
    "prompt_0schema_bm25": sql_prompt_0schema_bm25,
    "prompt_schema_bm25": sql_prompt_schema_bm25,
}

sparql_prompttypes = {
    "prompt_0schema_bm25": sparql_prompt_0schema_bm25,
    "prompt_schema_bm25": sparql_prompt_schema_bm25,
}

mql_prompttypes = {
    "prompt_0schema_bm25": mql_prompt_0schema_bm25,
    "prompt_schema_bm25": mql_prompt_schema_bm25,
}

from run_llm_common import *


if __name__ == "__main__":
    main(cypher_prompttypes, sql_prompttypes, sparql_prompttypes, mql_prompttypes,  exp_name="EXP6")
