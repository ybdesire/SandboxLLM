# 1. steps for deploying llm as server rest-api

1. download SFT/deployment framework
```
git clone https://github.com/hiyouga/LLaMA-Factory.git`
```

2. download base LLM
```
git lfs install
git clone https://huggingface.co/THUDM/chatglm3-6b-32k
```

3. copy api shell script
```
cp api_raw_llm.sh LLaMA-Factory/.
```

4. start the server api
```
cd LLaMA-Factory
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


# 3. steps to run SFT

1. download SFT framework
```
git clone https://github.com/hiyouga/LLaMA-Factory.git`
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
