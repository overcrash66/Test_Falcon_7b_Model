from torch import cuda, bfloat16 
import transformers
from transformers import AutoTokenizer, AutoModelForCausalLM 
device = f'cuda:{cuda.current_device()}' if cuda.is_available() else 'cpu'  

#creating a model 
fmodel = AutoModelForCausalLM.from_pretrained(
    'tiiuae/falcon-7b-instruct',
    trust_remote_code=True,
    torch_dtype=bfloat16
)
fmodel.eval() 
fmodel.to(device) 
print(f'Model loaded on {device}') 
tokenizer = AutoTokenizer.from_pretrained('tiiuae/falcon-7b-instruct')
gen_text = transformers.pipeline(
    model=fmodel, 
    tokenizer=tokenizer, 
    task='text-generation', 
    return_full_text=True, 
    device=device, 
    max_length=10000, 
    temperature=0.1, 
    top_p=0.15, #select from top tokens whose probability adds up to 15%
    top_k=0, #selecting from top 0 tokens 
    repetition_penalty=1.1, #without a penalty, output starts to repeat 
    do_sample=True, 
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id,
)