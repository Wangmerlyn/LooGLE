# !/bin/bash
# python Prediction/pred_opensource_models.py --model_path /mnt/longcontext/models/nishang --model_name phi-3-1-mini-l-m-5-3-128k-cd33-mono-ntk-left-multi-scale-init-pg19-needle-128k --max_length 130572 --task longdep_qa
python Prediction/pred_opensource_models.py --model_path /mnt/longcontext/models/siyuan/llama3 --model_name LLaMA-2-7B-32K  --max_length 32268 --task longdep_qa 
python Evaluation/automatic_eval.py --model_name LLaMA-2-7B-32K --task longdep_qa --eval_metric automatic_sim