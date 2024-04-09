# Recommend

1. python : 3.10


# 1. steps for deploying llm as server rest-api

1.  SFT/deployment framework LLaMA-Factory
```
cd LLaMAFactoryForSLLM
pip install -r requirements.txt
```

2. download base LLM
```
git lfs install
git clone https://huggingface.co/THUDM/chatglm3-6b-32k
```

3. copy api shell script
```
cp api_raw_llm.sh LLaMAFactoryForSLLM/.
```

4. start the server api
```
cd LLaMAFactoryForSLLM
bash api_raw_llm.sh
```


# 2. steps for RAG

1. download bge-m3 embedding model
```
git clone https://huggingface.co/BAAI/bge-m3
git clone https://huggingface.co/BAAI/bge-m3
```

2. install milvus (vector db)
```
wget https://raw.githubusercontent.com/milvus-io/milvus/master/scripts/standalone_embed.sh
bash standalone_embed.sh start
```

3. run the demo [sandboxllm_rag_workflow_demo.ipynb](sandboxllm_rag_workflow_demo.ipynb)


# 3. steps to run SFT

1. SFT framework
```
cd LLaMAFactoryForSLLM
```

2. download base LLM
```
git lfs install
git clone https://huggingface.co/THUDM/chatglm3-6b-32k
```

3. copy data and SFT shell script
```
cp sft_run.sh LLaMA-Factory/
cp data_xxx_train.json LLaMA-Factory/data/
cp data_xxx_test.json LLaMA-Factory/data/
cp dataset_info.json LLaMA-Factory/data/
```

4. run SFT
```
bash sft_run.sh
```

# 4. steps to start the SandboxLLM UI

```
cd LLaMAFactoryForSLLM
bash web_sandbox_llm.sh
```
