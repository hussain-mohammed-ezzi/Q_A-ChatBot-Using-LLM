import os
from dotenv import load_dotenv
from langchain.llms import HuggingFaceHub
from langchain.llms import GooglePalm
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain,SequentialChain
load_dotenv()
os.environ['HUGGINGFACEHUB_API_TOKEN'] = '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'
llm = HuggingFaceHub(repo_id='google/flan-t5-large',model_kwargs={"temperature": 0.5, "max_length": 64})
output = llm.predict('Can you tell me the capital of America')
#llm = GooglePalm(google_api_key=os.environ.get('GOOGLE_API_KEY'),temparature=0.5)

# intialize the Prompt template

prom_template = PromptTemplate(input_variables={'country'},
                               template='Tell me the top 5 best city in this {country}')



#multile chain
cap_template = PromptTemplate(input_variables=['country'],
                              template='Tell me the capital of {country}')

cap_chain = LLMChain(llm= llm,prompt=cap_template,output_key='capital')

famous_template = PromptTemplate(input_variables=['capital'],
                                 template='Suggest me place to visit {capital}')

famous_chain = LLMChain(llm=llm,prompt=famous_template,output_key='places')

#chain = SimpleSequentialChain(chains=[cap_chain,famous_chain])

chain = SequentialChain(chains=[cap_chain,famous_chain],
                        input_variables=['country'],
                        output_variables=['capital','places'])
#chain = LLMChain(llm=llm,prompt=prom_template)
output = chain({'country':'Australia'} )
print(output)
