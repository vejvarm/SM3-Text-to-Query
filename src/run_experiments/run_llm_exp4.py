from prompts.cypher_prompts_4 import *
from prompts.sql_prompts_4 import *
from prompts.sparql_prompts_4 import *
from prompts.mql_prompts_4 import *

cypher_prompttypes = {
    "prompt_schema_fewshots": cypher_prompt_schema_fewshots,
    "prompt_schema_oneshot": cypher_prompt_schema_oneshot,
    "prompt_0schema_fewshots": cypher_prompt_0schema_fewshots,
    "prompt_0schema_oneshot": cypher_prompt_0schema_oneshot,
}

sql_prompttypes = {
    "prompt_schema_fewshots": sql_prompt_schema_fewshots,
    "prompt_schema_oneshot": sql_prompt_schema_oneshot,
    "prompt_0schema_fewshots": sql_prompt_0schema_fewshots,
    "prompt_0schema_oneshot": sql_prompt_0schema_oneshot,
}

sparql_prompttypes = {
    "prompt_schema_fewshots": sparql_prompt_schema_fewshots,
    "prompt_schema_oneshot": sparql_prompt_schema_oneshot,
    "prompt_0schema_fewshots": sparql_prompt_0schema_fewshots,
    "prompt_0schema_oneshot": sparql_prompt_0schema_oneshot,
}

mql_prompttypes = {
    "prompt_schema_fewshots": mql_prompt_schema_fewshots,
    "prompt_schema_oneshot": mql_prompt_schema_oneshot,
    "prompt_0schema_fewshots": mql_prompt_0schema_fewshots,
    "prompt_0schema_oneshot": mql_prompt_0schema_oneshot,
}

from run_llm_common import *


if __name__ == "__main__":
    main(cypher_prompttypes, sql_prompttypes, sparql_prompttypes, mql_prompttypes, exp_name="EXP4")
