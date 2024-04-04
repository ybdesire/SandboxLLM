
# steps for RAG



# steps to run SFT

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
```

4. run SFT
```
bash sft_run.sh
```
