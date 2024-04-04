CUDA_VISIBLE_DEVICES=0 python /data/LLaMA-Factory/src/train_bash.py \
    --stage sft \
    --model_name_or_path /data/chatglm3-6b-32k \
    --do_train \
    --dataset xxx_train \
    --template chatglm3 \
    --finetuning_type lora \
    --lora_target query_key_value \
    --output_dir output/chatglm3_32k_sft/  \
    --overwrite_cache \
    --per_device_train_batch_size 4 \
    --gradient_accumulation_steps 4 \
    --lr_scheduler_type cosine \
    --logging_steps 10 \
    --save_steps 2000 \
    --learning_rate 5e-5 \
    --num_train_epochs 300 \
    --plot_loss \
    --fp16

